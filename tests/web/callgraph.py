import sys
import re
import networkx as nx
import collections

def read_file_content(filename):
    content = ''
    with open(filename, 'r') as f:
        content = f.read()
    if len(content) == 0:
        print "Something went wrong :("
        exit(0)
    return content


def get_members_in_function(lines):

    # search for all occurences of 'self'
    pattern = r'self\.\w*[^\w]'

    functions = set()
    variables = set()
    lists = set()

    for line in lines:
        findings = re.findall(pattern, line)
        for finding in findings:
            if finding[-1] == '(':
                finding = re.sub('self\.', '', finding)
                finding = finding + ')'
                functions.add(finding)
            elif finding[-1] == '[':
                lists.add(finding[:-1])
            elif re.match(r':', finding[-1]) is None:
                variables.add(finding[:-1])
            else:
                variables.add(finding[:-1])
    return functions, variables, lists


def get_members_of_class(segment, functions_only=True):

    member_functions = dict()
    function_segments = segment.split('def ')

    for segment in function_segments:

        lines = segment.split('\n')
        function_name = lines.pop(0)
        function_name = function_name.lstrip(' ')
        function_name = re.sub(r'\(.*', '()', function_name)
        member_functions[function_name] = dict()

        if functions_only: continue

        # search for all occurences of 'self'
        functions, variables, lists = get_members_in_function(lines)

        member_functions[function_name] = dict()
        if functions:
            member_functions[function_name]['functions'] = functions
        if variables:
            member_functions[function_name]['variables'] = variables
        if lists:
            member_functions[function_name]['lists'] = lists
    return member_functions


def parse_file_for_class_members(filecontent, functions_only=True):

    classes = dict()
    class_segments = filecontent.split('\nclass ')

    for segment in class_segments:

        lines = segment.split('\n')
        class_name = 'class ' + lines[0]
        classes[class_name] = get_members_of_class('\n'.join(lines[1:]), functions_only=functions_only)

    return classes



def print_call_dependencies(py_file):

    content = read_file_content(py_file)
    classes = parse_file_for_class_members(content, functions_only=False)

    for class_name in classes:
        print '\n' + '_' * 10 + class_name + '_' * 10
        member_functions = classes[class_name]

        graph = nx.Graph()
        for fun1 in member_functions:
            if fun1 not in graph.nodes():
                graph.add_node(fun1)
#            graph.add_edge(fun1, fun1)
            if 'functions' not in member_functions[fun1]:
                continue
            for fun2 in member_functions[fun1]['functions']:
                if fun2 not in graph.nodes():
                    graph.add_node(fun2)
                graph.add_edge(fun1, fun2)
        counter = collections.Counter([e[1] for e in graph.edges()])
        counter = [(k, counter[k]) for k in graph.nodes()]
        for fun, degree in sorted(counter, key=lambda x:x[1] ):
            classes[class_name][fun]['degree'] = degree




if __name__ == '__main__':

    if len(sys.argv) == 1:
        print 'no arguments provided.\nprvideone argument for printing dependencies within one class (assumes there is only one class in the file!),\nprovide two arguments to compare all functions in two files (used for refactoring)'
    elif len(sys.argv) == 2:
        print_call_dependencies(sys.argv[1])
    elif len(sys.argv) > 3:
        print 'please provide either one or wto arguments!'
        exit(0)
        
