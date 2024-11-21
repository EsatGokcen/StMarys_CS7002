from bold_template import BoldTemplate
from italic_template import ItalicTemplate 
from underline_template import UnderlineTemplate
from client import *

def main():
    
    bold = BoldTemplate("This is a bold message!")
    italic = ItalicTemplate("This is an italic message.")
    underline = UnderlineTemplate("This is an underline message.")

    add_template("Bold", bold.clone())
    add_template("Italic", italic.clone())

    retrieved_bold_template = get_template("Bold")
    retrieved_italic_template = get_template("Italic")

    if retrieved_bold_template:
        print(retrieved_bold_template.apply_formatting())  # Output: This is a bold message

    if retrieved_italic_template:
        print(retrieved_italic_template.apply_formatting())  # Output: This is an italic message

if __name__ == '__main__':
    main()