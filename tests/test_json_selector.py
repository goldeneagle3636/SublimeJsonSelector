import sublime
import sys
from unittest import TestCase

version = sublime.version()

class TestJsonSelector(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        # make sure we have a window to work with
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def test_copypath(self):
        self.setText("new ")
        self.view.run_command("copypath")
        first_row = self.getRow(0)
        self.assertEqual(first_row, "new hello world")
