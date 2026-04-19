#!/usr/bin/env python
# This scripts reads the data from named-characters and converts it to the
# format used by the library internally

import json
import os.path as osp
import sys
from pathlib import Path
from typing import Any, Dict, Set

import click
import mathics_scanner
import yaml

try:
    from mathics_scanner.version import __version__
except ImportError:
    # When using build isolation
    __version__ = "unknown"

OPERATOR_FIELDS = [
    "ascii-operators",
    "unicode-operators",
]

DEFAULT_DATA_DIR = Path(osp.join(osp.dirname(mathics_scanner.__file__), "data"))


def get_srcdir() -> str:
    filename = osp.normcase(osp.dirname(osp.abspath(__file__)))
    return osp.realpath(filename)


def read(*rnames) -> str:
    return open(osp.join(get_srcdir(), *rnames)).read()


def compile_tables(
    operator_data: Dict[str, dict], character_data: Dict[str, dict]
) -> Dict[str, Any]:
    """
    Compiles the general table into the tables used internally by the library.
    This facilitates fast access of this information by clients needing this
    information.
    """
    ascii_operators: Set[str] = set()
    unicode_operators: Dict[str, str] = {}

    operator_names = {operator_name for operator_name in operator_data.keys()}
    for name, character_info in character_data.items():
        operator_name = character_info.get("operator-name")
        if name in operator_names or operator_name:
            if operator_name:
                name = operator_name
            if "unicode-equivalent" in character_info.keys():
                unicode_operators[character_info["unicode-equivalent"]] = name
            if "ascii" in character_info.keys():
                ascii_operators.add(character_info["ascii"])

    return {
        "ascii-operators": sorted(ascii_operators),
        "unicode-operators": unicode_operators,
    }


@click.command()
@click.version_option(version=__version__)  # NOQA
@click.option(
    "--output",
    "-o",
    show_default=True,
    type=click.Path(writable=True),
    default=DEFAULT_DATA_DIR / "operators.json",
)
@click.argument(
    "data_dir", type=click.Path(readable=True), default=DEFAULT_DATA_DIR, required=False
)
def main(output, data_dir):
    with (
        open(data_dir / "operators.yml", "r", encoding="utf8") as operator_f,
        open(data_dir / "named-characters.yml", "r", encoding="utf8") as character_f,
        open(output, "w") as o,
    ):
        # Load the YAML data.
        operator_data = yaml.load(operator_f, Loader=yaml.FullLoader)
        character_data = yaml.load(character_f, Loader=yaml.FullLoader)

        # Precompile the tables.
        data = compile_tables(operator_data, character_data)

        # Dump the preprocessed dictionaries to disk as JSON.
        json.dump(data, o)


if __name__ == "__main__":
    main(sys.argv[1:])
