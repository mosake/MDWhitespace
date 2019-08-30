"""
A simple whitespace converter script.
Attempts to use the most efficient whitespacing characters in terms of markdown
formatting.

Author: Kelly Mo
Date: Aug 29, 2019
"""

# can be run in cmd line
def main():
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
    
    """
    import sys

if __name__ == '__main__':
    main()