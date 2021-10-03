"""Script to remove soln environments in a homework."""
from textwrap import dedent
import argparse
import re
import sys

from TexSoup import TexSoup


SOLUTION_ENVIRONMENT_NAME = 'soln'


# what to replace the solution environment with
REPLACE_WITH = dedent(
        r"""
        \begin{soln}
            % write solution below

        \end{soln}
        """)


def get_leading_whitespace(s):
    """Return the whitespace at the beginning of a string."""
    return re.search(r'^(\s*)\S', s).groups()[0]


def make_blank_solution_node(leading_whitespace, remove_completely=False):
    """Create a blank solution node with nice indentation."""
    if not remove_completely:
        lines = REPLACE_WITH.split('\n')
    else:
        return ''

    for i in range(1, len(lines)):
        lines[i] = leading_whitespace + lines[i]
    return TexSoup('\n'.join(lines)).find(SOLUTION_ENVIRONMENT_NAME)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('--remove-completely', action='store_true')
    args = parser.parse_args()

    with open(args.input) as fileobj:
        contents = fileobj.read()

    document = TexSoup(contents)

    for node in document.find_all(SOLUTION_ENVIRONMENT_NAME):
        lines = str(node).split('\n')
        leading_whitespace = get_leading_whitespace(lines[-1])
        blank_node = make_blank_solution_node(leading_whitespace, args.remove_completely)
        node.replace_with(blank_node)

    print(document)


if __name__ == '__main__':
    main()
