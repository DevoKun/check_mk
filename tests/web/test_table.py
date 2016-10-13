#!/usr/bin/python
# call using
# > py.test -s -k test_html_generator.py

# enable imports from web directory
from testlib import cmk_path
import sys
sys.path.insert(0, "%s/web/htdocs" % cmk_path())

# external imports
import re
from bs4 import BeautifulSoup as bs

# internal imports
from htmllib import html
from htmllib import HTMLGenerator, HTMLCheck_MK
from tools import compare_html , gentest, compare_and_empty
from classes import DeprecatedRenderer
from table import Table

import traceback

class TableTest(html):

    written_text = ''
    tag_counter  = 0

    def lowlevel_write(self, text):

        if re.match(r'.*\.close_\w+[(][)]', '\n'.join(traceback.format_stack()), re.DOTALL):
            self.tag_counter -= 1 if self.tag_counter > 0 else 0
            self.written_text += " " * 4 * self.tag_counter + text
        elif re.match(r'.*\.open_\w+[(]', '\n'.join(traceback.format_stack()), re.DOTALL):
            self.written_text += " " * 4 * self.tag_counter + text
            self.tag_counter += 1
        else:
            self.written_text += " " * 4 * self.tag_counter + text + '\n'


def read_out_table(text):
    # Get the contents of the table as a list of lists
    data = []
    for row in bs(text, 'html5lib').findAll('tr'):
        columns = row.findAll('th')
        if not columns:
            columns = row.findAll('td')
        data.append([re.sub(r'\s', '', re.sub(r'<[^<]*>', '', cell.text)) for cell in columns])
    return data


def read_out_csv(text, separator):
    # Get the contents of the table as a list of lists
    data = []
    for row in text.split('\n'):
        columns = row.split(separator)
        data.append([re.sub(r'\s', '', re.sub(r'<[^<]*>', '', cell)) for cell in columns])
    data = [row for row in data if not all(cell == '' for cell in row)]
    return data


def table_test_cubical(sortable, searchable, limit, output_format):

    html = TableTest()

    table_id = 0
    title = " TEST "
    separator = ';'

    html.add_var('_%s_sort'   % table_id, "1,0")

    rows = [ (i, i**3) for i in range(10) ]
    header = ["Number", "Cubical"]

    table = Table(html)
    table.begin(table_id      = table_id,
                title         = title,
                sortable      = sortable,
                searchable    = searchable,
                limit         = limit,
                output_format = output_format)

    for row in rows:
        table.row()
        for i in range(len(header)):
            table.cell(_(header[i]), row[i])
    table.end()

    # write to file: This is part of the test! Look at the generated HTML!
    filename = "./web/data/testtable_%s_%s_%s.html" % ("sortable" * sortable, "searchable" * searchable, limit)
    text = html.written_text
    with open(filename, "w") as html_file:
        html_file.write(text)

    # Data assertions
    assert output_format in ['html', 'csv'], 'Fetch is not yet implemented'
    if output_format == 'html':
        data = read_out_table(text)
        assert data.pop(0) == header
    elif output_format == 'csv':
        data = read_out_csv(text, separator)
        assert data.pop(0) == header, header
    else:
        assert False, 'Not yet implemented!'

    data = [ tuple(map(int, row)) for row in data ]
    if limit is None:
        limit = len(rows)

    assert len(data) == limit
    assert data == rows[:limit]


def test_table():
    table_test_cubical(False, False, None, 'html')


def test_limit():
    table_test_cubical(False, False, 2, 'html')


def test_sortable():
    table_test_cubical(True, False, None, 'html')


def test_searchable():
    table_test_cubical(False, True, None, 'html')


def test_csv():
    table_test_cubical(False, False, None, 'csv')


