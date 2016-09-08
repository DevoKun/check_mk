#!/usr/bin/python
# call using
# > py.test -s -k test_html_generator.py

# enable imports from web directory
from testlib import cmk_path
import sys
sys.path.insert(0, "%s/web/htdocs" % cmk_path())

# external imports
import re

# internal imports
from htmllib import html, DeprecatedRenderer
from htmllib import HTMLGenerator, HTMLCheck_MK

#
class HTMLTester(object):
# A Class which can be used to simulate HTML generation in varios tests in tests/web/

    def __init__(self):
        super(HTMLTester, self).__init__()
        self.plugged_text = ''


    def write(self, text):
        self.plugged_text += text


    def plug(self):
        self.plugged_text = ''


    def drain(self):
            t = self.plugged_text
            self.plugged_text = ''
            return t


class GeneratorTester(HTMLTester, HTMLGenerator):
    def __init__(self):
        super(GeneratorTester, self).__init__()
        HTMLTester.__init__(self)
        HTMLGenerator.__init__(self)


class HTMLCheck_MKTester(HTMLTester, HTMLCheck_MK):

    def __init__(self):
        super(HTMLCheck_MKTester, self).__init__()


    def add_custom_style_sheet(self):
        #raise NotImplementedError()
        pass


    def css_filename_for_browser(self, css):
        #raise NotImplementedError()
        return "file/name/css_%s" % css


    def javascript_filename_for_browser(self, jsname):
        #raise NotImplementedError()
        return "file/name/js_%s" % jsname 


    def top_heading(self, title):
        self.top_heading_left(title)
        self.top_heading_right()


    def detect_icon_path(self, icon_name):
        return "test/%s.jpg" % icon_name


class HTMLOrigTester(HTMLTester, DeprecatedRenderer):


    def add_custom_style_sheet(self):
        #raise NotImplementedError()
        pass


    def css_filename_for_browser(self, css):
        #raise NotImplementedError()
        return "file/name/css_%s" % css


    def javascript_filename_for_browser(self, jsname):
        #raise NotImplementedError()
        return "file/name/js_%s" % jsname 


    def top_heading(self, title):
        self.top_heading_left(title)
        self.top_heading_right()


    def detect_icon_path(self, icon_name):
        return "test/%s.jpg" % icon_name


