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
from htmllib import HTML

from tools import compare_html, compare_soup
from classes import GeneratorTester


def test_escape_attribute():
    html = GeneratorTester()
    original = ["Test & \"alles\" <sowas von> klar!",\
                HTML("Ich bin <ein html> mit <div> tags </div>"),\
                5, 0.31415926, HTML]
    expected = ["Test &amp; &quot;alles&quot; &lt;sowas von&gt; klar!",\
                "Ich bin <ein html> mit <div> tags </div>",\
                "5", "0.31415926", str(HTML) ]
    for (orig, expt) in zip(original, expected):
        assert html._escape_attribute(orig) == expt


def test_escape_text():
   html = GeneratorTester()
   plain = [ "<div> Beispiel </br> Text </div>",\
               "",\
              ]
   expect = ["&lt;div&gt; Beispiel </br> Text &lt;/div&gt;",\
               "",\
               ]
#   text = re.sub(r'&lt;(/?)(h2|b|tt|i|br(?: /)?|pre|a|sup|p|li|ul|ol)&gt;', r'<\1\2>', text)
#   text = re.sub(r'&lt;a href=&quot;(.*?)&quot;&gt;', r'<a href="\1">', text)
   for p, e in zip(plain, expect):
       assert compare_html(html._escape_text(p), e)


def test_render_attribute():
    html = GeneratorTester()
    assert ''.join(html._render_attributes(class_="example")) == " class=\"example\""

    plain     = "<div class=\"\"></div>"
    generated1 = html.render_div('', class_="")
    generated2 = html.render_div('', class_=[])
    generated3 = html.render_div('', class_=None)
    compare_soup(plain, generated1)
    compare_soup(plain, generated2)
    compare_soup("<div></div>", generated3)

    plain     = "<div class=\"example\"></div>"
    generated1 = html.render_div('', class_="example")
    generated2 = html.render_div('', class_=["example"])
    compare_soup(plain, generated1)
    compare_soup(plain, generated2)

    plain     = "<div class=\"example1 example2\"></div>"
    generated1 = html.render_div('', class_=["example1", "example2"])
    generated2 = html.render_div('', class_=["example1   ", "    example2", " "])
    compare_soup(plain, generated1)
    compare_soup(plain, generated2)

    plain     = "<div class=\"1 2 0\"></div>"
    generated1 = html.render_div('', class_=["1", 2, 0, ''])
    generated2 = html.render_div('', class_=["1", 2, 0, None])
    compare_soup(plain, generated1)
    compare_soup(plain, generated2)

    plain     = "<div style=\"height:12px; width:20px;\"></div>"
    generated1 = html.render_div('', style=["height:12px", "width:20px"])
    generated2 = html.render_div('', style=["height:12px", "width:20px", ''])
    compare_soup(plain, generated1)
    compare_soup(plain, generated2)

    plain     = "<div onclick=\"if(true) alert(\'Hallo Welt!\');\"></div>"
    generated1 = html.render_div('', onclick="if(true) alert(\'Hallo Welt!\');")
    generated2 = html.render_div('', onclick="if(true) alert(\'Hallo Welt!\');")
    generated3 = html.render_div('', onclick=["if(true) alert(\'Hallo Welt!\')"])
    compare_soup(plain, generated1)
    compare_soup(plain, generated2)
    compare_soup(plain, generated3)

    plain     = "<div id=\"height_width_0\"></div>"
    generated1 = html.render_div('', id_=["height", "width", 0])
    generated2 = html.render_div('', id_=["height", "width", 0, None])
    compare_soup(plain, generated1)
    compare_soup(plain, generated2)

    plain     = "<div src=\"one_two.html\"></div>"
    generated1 = html.render_div('', src=["one", "two.html"])
    generated2 = html.render_div('', src=["one", "two.html", None])
    compare_soup(plain, generated1)
    compare_soup(plain, generated2)




def test_render_opening_tag():
    html = GeneratorTester()

    # test correct nes of attribute generation
    tag = html._render_opening_tag("div", id_="0", class_="example_class", type_="test", name="example")
    assert compare_html(tag, '<div id="0" type="test" name="example" class="example_class"\n>'), tag

    # test against possible injection
    tag = html._render_opening_tag("div", id_="0\" class=\"example\"")
    assert compare_html(tag, '<div id="0&quot; class=&quot;example&quot;">\n'), tag
    assert len(re.findall(r'\w+\s*=\s*[\"|\']', tag)) == 1, \
                "ERROR: POSSIBLE INJECTION!!" + '\n' + tag


def test_render_closing_tag():
    html = GeneratorTester()
    assert html._render_closing_tag('h2') == "</h2>\n"


def test_render_javascript():
    html = GeneratorTester()
    html.plug()

    html.open_html()
    html.open_body()

    html.heading("My First JavaScript")

    html.open_button(type_='button', onclick="if(true && true) {document.getElementById('demo').innerHTML = Date()}")
    html.write_text("Click me to display Date and Time.")
    html.close_button()

    html.p("", id_="demo")

    html.close_body()
    html.close_html()
    expected_html = '\
            <html>\
                <body>\
                    <h2>My First JavaScript</h2>\
                    <button type=\"button\" onclick=\"if(true && true) {document.getElementById(\'demo\').innerHTML = Date()}\">\
                    Click me to display Date and Time.</button>\
                    <p id="demo"></p>\
                </body>\
            </html>'
    assert compare_html(html.plugged_text, expected_html), '%s\nshould look like\n%s' % (prettify(html.plugged_text), prettify(expected_html))



def test_element_generation_basic():
    html = GeneratorTester()
    html.plug()

    html.open_html()

    html.open_head()
    html.close_head()

    html.open_body()
    html.close_body()

    html.close_html()

    expected_html = '\
        <html>\
            <head>\
            </head>\
            <body>\
            </body>\
        </html>'
    assert compare_html(html.plugged_text, expected_html), '%s\nshould look like\n%s' % (prettify(html.plugged_text), prettify(expected_html))


def test_element_generation_form():
    html = GeneratorTester()
    html.plug()

    html.open_html()

    html.open_head()
    html.close_head()

    html.open_body()
    html.open_form()
    html.label('test_input', 'Test')
    html.input('test_input', type_='radio')
    html.label('test_input_2', 'Hallo Welt')
    html.input('test_input_2', type_='radio')
    html.close_form()
    html.close_body()

    html.close_html()

    expected_html = '\
        <html>\
            <head>\
            </head>\
            <body>\
                <form>\
                    <label for="test_input">Test</label>\
                    <input type="radio" name="test_input">\
                    <label for="test_input_2">Hallo Welt</label>\
                    <input type="radio" name="test_input_2">\
                </form>\
            </body>\
        </html>'
    assert compare_html(html.plugged_text, expected_html), '%s\nshould look like\n%s' % (prettify(html.plugged_text), prettify(expected_html))


def test_element_generation_table():
    html = GeneratorTester()
    html.plug()

    html.open_html()

    html.open_head()
    html.close_head()

    html.open_body()
    html.open_table()

    list_of_lists = [ ["Col1", "Col2", "Col3"], [1,2,3], [4,5,6], [7,8,9] ]
    for row in list_of_lists:
        html.open_tr()
        for entry in row:
            html.td(entry)
        html.close_tr()

    html.close_table()
    html.close_body()

    html.close_html()

    expected_html = '\
        <html>\
            <head>\
            </head>\
            <body>\
                <table>\
                    <tr>\n<td>Col1</td>\n<td>Col2</td>\n<td>Col3</td>\n</tr>\
                    <tr>\n<td>1</td>\n<td>2</td>\n<td>3</td>\n</tr>\
                    <tr>\n<td>4</td>\n<td>5</td>\n<td>6</td>\n</tr>\
                    <tr>\n<td>7</td>\n<td>8</td>\n<td>9</td>\n</tr>\
                </table>\
            </body>\
        </html>'
    assert compare_html(html.plugged_text, expected_html), '%s\nshould look like\n%s' % (prettify(html.plugged_text), prettify(expected_html))











