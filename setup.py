# -*- coding: utf-8 -*-
# Copyright (c) 2021, 2024, 2026 Rocky Bernstein
# Copyright (c) 2016 rsmenon
# Licensed under the MIT License (https://opensource.org/licenses/MIT)

r"""This is a lexer and highlighter for Mathematica/Wolfram Language source code \
using the pygments engine.

It currently supports:

 - All builtin functions in the ``System`` context including unicode symbols except those that use characters from the private unicode space (e.g. ``\[FormalA]``).
 - User defined symbols, including those in a context.
 - All operators including unicode operators like \u03C0.
 - Comments, including multi line and nested.
 - Strings, including multi line and escaped quotes.
 - Patterns, slots (including named slots ``#name`` introduced in version 10) and slot sequences.
 - Message names (e.g. the ivar in ``General::ivar``)
 - Numbers including base notation (e.g. ``8 ^^ 23 == 19``) and scientific notation (e.g. ``1 *^ 3 == 1000``).
 - Local variables in ``Block``, ``With`` and ``Module``.

A Sass file containing the styles can be obtained from the package repository for use in static \
website generators such as Jekyll, Octopress, Pelican, etc.

Copyright 2021, 2024, 2026 Rocky Bernstein
(C) 2016 rsmenon
"""

import os
import os.path as osp
from setuptools import setup
from setuptools.command.build_py import build_py as setuptools_build_py

def get_srcdir():
    """Return the directory of the location if this code"""
    filename = osp.normcase(osp.dirname(osp.abspath(__file__)))
    return osp.realpath(filename)


class build_py(setuptools_build_py):
    """
    The "run" method below of class gets invoked when setup.py is run through
    setuptools.

    Here, we just invoke ./admin-tools/make-JSON-tables.sh.
    """

    def run(self):
        """
        If you need to debug this, just extract this method, remove "self" above
        and save it in a standalone Python file without the setuptools_build_py.run(self)
        call below.
        """
        srcdir = get_srcdir()
        cmd = f"bash {osp.join(srcdir, 'admin-tools', 'make-JSON-tables.sh')}"
        print(cmd)
        os.system(cmd)
        setuptools_build_py.run(self)


CMDCLASS = {"build_py": build_py}


if __name__ == "__main__":
    setup(
        cmdclass=CMDCLASS,  # Set up to run build_py.run()
        # don't pack Mathics3 an in egg because of media files, etc.
        zip_safe=False,
    )
