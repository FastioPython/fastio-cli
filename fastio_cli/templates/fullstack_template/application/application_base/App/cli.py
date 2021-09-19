import os
import re
import json
import pprint
import click
import six
from PyInquirer import (
    Token, 
    ValidationError, 
    Validator, 
    print_json, 
    prompt,
    style_from_dict
)
from pyfiglet import figlet_format

# Init CLI style
try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None

# Get configuration
# try:
#     conf = ConfigStore("projects")
# except Exception as e:
#     print(e)
#     raise Exception(e)


style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})


def log(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)

@click.command()
def main():
    """
    PyWorks Code Generator
    """
    log("Fast Generator", color="blue", figlet=True)
    log("A Simple Code Generator CLI", "green")
    log("---------------------------------------------", "green")
    log("Step 1: Generate project dirs structure", "yellow")
    log("Step 2: Create input template", "yellow")
    log("Step 3: Generate output php file from template use default generator", "yellow")
    log("Step 4: Finish", "yellow")
    log("---------------------------------------------", "green")
    log("Load config:", "green")

    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(configs)

if __name__ == '__main__':
    main()