"""
A simple whitespace converter script.
Attempts to use the most efficient whitespacing characters in terms of markdown
formatting.

Author: Kelly Mo
Date: Aug 29, 2019
"""

# can be run in cmd line
def main(input):
    """
    Spaces        Format
    1             &nbsp;
    2             &ensp;
    4             &emsp;
    
    Additionally normal whitespaces can be used once, if precided by a
    char (excluding newline)
    
    i.e. 
    &nbsp;[SPACE]&nbsp; returns three spaces
    hi[SPACE]&nbsp;[SPACE]&nbsp;[SPACE] returns "hi     " (5 spaces)
    
    Test case/cat
     ^---^
    ( . _.) < Hello World
    |v   |
     v--v
     
    Input: file
    
    """
    
    print("Cat! \nI'm a kitty cat. \nAnd I dance dance dance,"
    + "\nand I dance dance dance")
    print(input)
    return("success")

if __name__ == '__main__':
    """
    Handles file I/O.
    Input: txt file from args
    Output: txt file named "output.txt"
    """
    import sys
    input = open(sys.argv[1], "r")
    text = input.readlines()
    output = open("output.txt", "w")
    output.write(main(text))
    input.close()
    output.close()