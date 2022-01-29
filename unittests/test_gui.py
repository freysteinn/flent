# -*- coding: utf-8 -*-
#
# test_gui.py
#
# Author:   Toke Høiland-Jørgensen (toke@toke.dk)
# Date:      4 July 2019
# Copyright (c) 2019, Toke Høiland-Jørgensen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest
import os
import sys

from .test_helpers import prefork

from flent.settings import parser, Settings, DEFAULT_SETTINGS
settings = parser.parse_args(args=[], namespace=Settings(DEFAULT_SETTINGS))

DEBUG_TEST = os.getenv("PYQT") == "PyQt5" and sys.version_info[:2] == (3, 7) and os.getenv("MATPLOTLIB_VERSION") == "3.5"

def debug_print(msg):
    if DEBUG_TEST:
        sys.stderr.write(msg + "\n")

class TestGui(unittest.TestCase):

    @prefork
    def test_start_gui(self):
        try:
            from qtpy import QtCore
        except ImportError:
            self.skipTest("No usable Qt module found")

        debug_print("start_gui")
        from flent import gui
        debug_print("imported gui")
        gui.run_gui(settings, test_mode=True)
        debug_print("exited from gui")


test_suite = unittest.TestSuite(
    [unittest.TestLoader().loadTestsFromTestCase(TestGui)])
