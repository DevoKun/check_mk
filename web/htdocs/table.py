#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.


from lib import num_split


# TODO: This try block is only for testing and should be removed after refactoring!
try:
    from config.user import load_file, save_file
except:
    load_user_file = lambda x, y: {}
    save_user_file = lambda x, y: None


# These methods are a singleton pattern wrapping the table class
# Using these methods, globally for the whole program, there will be
# only one instance of the Table class!

def check_instance():
    if not Table.instance:
        Table(html)


def begin(table_id=None, title=None, **kwargs):
    check_instance()
    Table.instance.begin(table_id=table_id, title=title, **kwargs)


def finish_previous():
    Table.instance.finish_previous()


def row(*posargs, **kwargs):
    Table.instance.row(*posargs, **kwargs)


def add_row(css=None, state=0, collect_headers=True, fixed=False):
    Table.instance.add_row(css=css, state=state, collect_headers=collect_headers, fixed=fixed)


def groupheader(title):
    Table.instance.groupheader(title)


def cell(*posargs, **kwargs):
    Table.instance.cell(*posargs, **kwargs)


def add_cell(title="", text="", css=None, help=None, colspan=None, sortable=True):
    Table.instance.add_cell(title=title, text=text, css=css, help=help, colspan=colspan, sortable=sortable)

def render_headers(self, do_csv, table_id, actions_enabled, actions_visible):
    Table.instance.render_headers(do_csv=do_csv, 
                                  table_id=table_id, 
                                  actions_enabled=actions_enabled, 
                                  actions_visible=actions_visible)
    
def end():
    Table.instance.end()
    Table.instance = None



# TODO: GETTER UND SETTER FUER INSTANCE!




class Table(object):

    instance = None


    def __init__(self, html):

        self.html = html
        Table.instance = self


    def begin(self, table_id=None, title=None, **kwargs):

        # Use our pagename as table id if none is specified
        if table_id == None:
            table_id = self.html.myfile

        try:
            from config import table_row_limit
            limit = table_row_limit
        except:
            limit = None
        finally:
            limit = kwargs.get('limit', limit)
            if self.html.var('limit') == 'none' or kwargs.get("output_format", "html") != "html":
                limit = None

        self.id              = table_id
        self.title           = title
        self.rows            = []
        self.headers         = []
        self.collect_headers = False # also: True, "finished"
        self.limit           = limit

        self.omit_if_empty   = kwargs.get("omit_if_empty", False)
        self.omit_headers    = kwargs.get("omit_headers", False)
        self.searchable      = kwargs.get("searchable", True)
        self.sortable        = kwargs.get("sortable", True)
        self.output_format   = kwargs.get("output_format", "html") # possible: html, csv, fetch
        self.empty_text      = kwargs.get("empty_text", _("No entries."))
        self.help            = kwargs.get("help", None)
        self.css             = kwargs.get("css", None)

        self.mode            = 'row'
        self.next_func       = None
        self.next_header     = None
        self.is_closed       = False

        self.html.plug()


    def finish_previous(self):

        if self.next_func:
            self.next_func(*self.next_args[0], **self.next_args[1])
            self.next_func = None


    def row(self, *posargs, **kwargs):

        self.finish_previous()
        self.next_func = self.add_row
        self.next_args = posargs, kwargs


    def add_row(self, css=None, state=0, collect_headers=True, fixed=False):

        if self.next_header:
            self.rows.append((self.next_header, None, "header", True))
            self.next_header = None
        self.rows.append(([], css, state, fixed))
        if collect_headers:
            if self.collect_headers == False:
                self.collect_headers = True
            elif self.collect_headers == True:
                self.collect_headers = "finished"
        elif not collect_headers and self.collect_headers:
            self.collect_headers = False

    # Intermediate title, shown as soon as there is a following row.
    # We store the group headers in the list of rows, with css None
    # and state set to "header"
    def groupheader(self, title):
        self.next_header = title


    def cell(self, *posargs, **kwargs):
        self.finish_previous()
        self.next_func = self.add_cell
        self.next_args = posargs, kwargs


    def add_cell(self, title="", text="", css=None, help=None, colspan=None, sortable=True):

        #TODO:
        help_text = help

        if type(text) != unicode:
            text = str(text)
        htmlcode = text + self.html.drain()
        if self.collect_headers == True:
            # small helper to make sorting introducion easier. Cells which contain
            # buttons are never sortable
            if css and ('buttons' in css) and sortable:
                sortable = False
            self.headers.append((title, help_text, sortable))
        self.rows[-1][0].append((htmlcode, css, colspan))


    def render_headers(self, do_csv, table_id, actions_enabled, actions_visible):

        if self.omit_headers:
            return

        if do_csv:
            header_row = [self.html.strip_tags(header) or "" for (header, help_text, sortable) in self.headers]
            self.html.write(csv_separator.join(header_row) + "\n")
            return

        else:
            self._render_headers(table_id, actions_enabled, actions_visible)


    def _render_headers(self, table_id, actions_enabled, actions_visible):

        if self.omit_headers:
            return

        self.html.open_tr()

        first_col = True
        for nr, (header, help_text, sortable) in enumerate(self.headers):
            text = header

            if help_text:
                header = '<span title="%s">%s</span>' % (self.html.attrencode(help), header)

            if self.sortable and sortable:
                reverse = 0
                sort = self.html.var('_%s_sort' % table_id)
                if sort:
                    sort_col, sort_reverse = map(int, sort.split(',', 1))
                    if sort_col == nr:
                        reverse = sort_reverse == 0 and 1 or 0
                location_href = self.html.makeactionuri([('_%s_sort' % table_id, '%d,%d' % (nr, reverse))])
                self.html.open_th(class_="sort", title=_("Sort by %s") % text, onclick = "location.href='%s'" % location_href)
            else:
                self.html.open_th()

            # Add the table action link
            if first_col and actions_enabled:
                first_col = False
                if not header:
                    header = "&nbsp;" # Fixes layout problem with white triangle

                if actions_visible:
                    state      = '0'
                    help_text  = _('Hide table actions')
                    img        = 'table_actions_on'
                else:
                    state      = '1'
                    help_text  = _('Display table actions')
                    img        = 'table_actions_off'

                self.html.open_div(class_="toggle_actions")
                self.html.icon_button(self.html.makeuri([('_%s_actions' % table_id, state)]),
                    help_text, img, cssclass = 'toggle_actions')
                self.html.open_span()
                self.html.write(header)
                self.html.close_span()
                self.html.close_div()
            else:
                self.html.write(header)

            self.html.close_th()
        self.html.close_tr()


    # Does not do any filtering or sorting!
    def _write_csv(self, csv_separator):

        table_id = self.id
        rows = self.rows

        # Controls wether or not actions are available for a table
        search_term = None
        actions_enabled = False # False for csv

        num_rows_unlimited = len(rows)
        num_cols = len(self.headers)

        # Apply limit after search / sorting etc.
        limit = self.limit
        if limit is not None:
            rows = rows[:limit]

        # If we have no group headers then paint the headers now
        if not self.omit_headers and self.rows and self.rows[0][2] != "header":
            header_row = [self.html.strip_tags(header) or "" for (header, help_text, sortable) in self.headers]
            self.html.write(csv_separator.join(header_row) + "\n")

        for nr, (row, css, state, fixed) in enumerate(rows):
            self.html.write(csv_separator.join([self.html.strip_tags(cell_content) for cell_content, css_classes, colspan in row ]))
            self.html.write("\n")


    def _filter_rows(self, rows, search_term):

        filtered_rows = []
        for row, css, state, fixed in rows:
            if state == "header" or fixed:
                continue # skip filtering of headers or fixed rows
            for cell_content, css_classes, colspan in row:
                if fixed or search_term in cell_content.lower():
                    filtered_rows.append((row, css, state, fixed))
                    break # skip other cells when matched
        return filtered_rows

    def _sort_rows(self, rows, sort_col, sort_reverse):
        # remove and remind fixed rows, add to separate list
        fixed_rows = []
        for index, row in enumerate(rows[:]):
            if row[3] == True:
                rows.remove(row)
                fixed_rows.append((index, row))

        # Then use natural sorting to sort the list. Note: due to a
        # change in the number of columns of a table in different software
        # versions the cmp-function might fail. This is because the sorting
        # column is persisted in a user file. So we ignore exceptions during
        # sorting. This gives the user the chance to change the sorting and
        # see the table in the first place.
        try:
            rows.sort(cmp=lambda a, b: cmp(num_split(a[0][sort_col][0]),
                                           num_split(b[0][sort_col][0])),
                      reverse=sort_reverse==1)
        except IndexError:
            pass

        # Now re-add the removed "fixed" rows to the list again
        if fixed_rows:
            for index, row in fixed_rows:
                rows.insert(index, row)
        return rows


    def end(self):

        self.finish_previous()
        self.html.unplug()

        if self.is_closed:
            return

        # Output-Format "fetch" simply means that all data is being
        # returned as Python-values to be rendered somewhere else.
        if self.output_format == "fetch":
            return self.headers, self.rows

        if not self.rows and self.omit_if_empty:
            self.is_closed = True
            return

        if self.output_format == "csv":
            if self.rows:
                csv_separator = self.html.var("csv_separator", ";")
                self._write_csv(csv_separator)
            self.is_closed = True
            return

        if self.title:
            self.html.h3(self.title)

        if self.help:
            self.html.help(self.help)

        if not self.rows:
            self.html.open_div(class_="info")
            self.html.write(self.empty_text)
            self.html.close_div()
            self.is_closed = True
            return

        table_id = self.id
        rows = self.rows

        # Controls wether or not actions are available for a table
        search_term = None
        actions_enabled = (self.searchable or self.sortable)
        actions_visible = False

        if actions_enabled:
            user_opts = load_user_file("tableoptions", {})
            user_opts.setdefault(table_id, {})
            table_opts = user_opts[table_id]

            # Handle the initial visibility of the actions
            actions_visible = user_opts[table_id].get('actions_visible', False)
            if self.html.var('_%s_actions' % table_id):
                actions_visible = self.html.var('_%s_actions' % table_id) == '1'

                user_opts[table_id]['actions_visible'] = actions_visible

            if self.html.var('_%s_reset' % table_id):
                self.html.del_var('_%s_search' % table_id)
                if 'search' in table_opts:
                    del table_opts['search'] # persist

            if self.searchable:
                # Search is always lower case -> case insensitive
                search_term = self.html.get_unicode_input('_%s_search' % table_id, table_opts.get('search', '')).lower()
                if search_term:
                    self.html.set_var('_%s_search' % table_id, search_term)
                    table_opts['search'] = search_term # persist
                    rows = self._filter_rows(rows, search_term)

            if self.html.var('_%s_reset_sorting' % table_id):
                self.html.del_var('_%s_sort' % table_id)
                if 'sort' in table_opts:
                    del table_opts['sort'] # persist

            if self.sortable:
                # Now apply eventual sorting settings
                sort = self.html.var('_%s_sort' % table_id, table_opts.get('sort'))
                if sort is not None:
                    self.html.set_var('_%s_sort' % table_id, sort)
                    table_opts['sort'] = sort # persist
                    sort_col, sort_reverse = map(int, sort.split(',', 1))
                    rows = self._sort_rows(rows, sort_col, sort_reverse)

        num_rows_unlimited = len(rows)
        num_cols = len(self.headers)

        # Apply limit after search / sorting etc.
        limit = self.limit
        if limit is not None:
            rows = rows[:limit]

        self.html.open_table(class_=["data", "oddeven"] if not self.css else ["data", "oddeven", self.css])

        # If we have no group headers then paint the headers now
        if self.rows and self.rows[0][2] != "header":
            self._render_headers(table_id, actions_enabled, actions_visible)

        if actions_enabled and actions_visible:

            self.html.open_tr(class_=["data", "even0", "actions"])
            self.html.open_td(colspan=num_cols)

            if not self.html.in_form():
                self.html.begin_form("%s_actions" % table_id)

            if self.searchable:
                self.html.open_div(class_="search")
                self.html.text_input("_%s_search" % table_id)
                self.html.button("_%s_submit" % table_id, _("Search"))
                self.html.button("_%s_reset" % table_id, _("Reset search"))
                self.html.set_focus("_%s_search" % table_id)
                self.html.close_div()

            if self.html.has_var('_%s_sort' % table_id):
                self.html.open_div(class_="sort")
                self.html.button("_%s_reset_sorting" % table_id, _("Reset sorting"))
                self.html.close_div()

            if not self.html.in_form():
                self.html.begin_form("%s_actions" % table_id)

            self.html.hidden_fields()
            self.html.end_form()
            self.html.close_tr()

        odd = "even"
        for nr, (row, css, state, fixed) in enumerate(rows):

            # Intermediate header
            if state == "header":
                # Show the header only, if at least one (non-header) row follows
                if nr < len(rows) - 1 and rows[nr+1][2] != "header":
                    self.html.open_tr(class_="groupheader")
                    self.html.open_td(colspan=num_cols)
                    self.html.br()
                    self.html.write(row)
                    self.html.close_td()
                    self.html.close_tr()

                    odd = "even"
                    self._render_headers(table_id, actions_enabled, actions_visible)
                continue

            odd = "odd" if (odd == "even") else "even"

            self.html.open_tr(class_=["data", odd, state] + ([css] if css else []))
            for cell_content, css_classes, colspan in row:
                self.html.open_td(class_=css_classes, colspan=colspan)
                self.html.write(cell_content)
                self.html.close_td()
            self.html.close_tr()

        if self.searchable and search_term and not rows:
            self.html.open_tr(class_=["data", "odd0", "no_match"])
            self.html.open_td(colspan=num_cols)
            self.html.write(_('Found no matching rows. Please try another search term.'))
            self.html.close_td()
            self.html.close_tr()

        self.html.close_table()

        if limit is not None and num_rows_unlimited > limit:
            self.html.message(_('This table is limited to show only %d of %d rows. '
                           'Click <a href="%s">here</a> to disable the limitation.') %
                               (limit, num_rows_unlimited, self.html.makeuri([('limit', 'none')])))

        if actions_enabled:
            save_file("tableoptions", user_opts)

        self.is_closed = True


