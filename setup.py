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

from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        packages=find_packages(),
        include_package_data=True,
    )
