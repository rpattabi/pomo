# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('pomo')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('pomo')

from pomo_lib import Window
from pomo.AboutPomoDialog import AboutPomoDialog
from pomo.PreferencesPomoDialog import PreferencesPomoDialog

# See pomo_lib.Window.py for more details about how this class works
class PomoWindow(Window):
    __gtype_name__ = "PomoWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(PomoWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutPomoDialog
        self.PreferencesDialog = PreferencesPomoDialog

        # Code for other initialization actions should be added here.

