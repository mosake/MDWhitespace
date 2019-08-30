"""
A simple whitespace converter script.
Attempts to use the most efficient whitespacing characters in terms of markdown
formatting.

Author: Kelly Mo
Date: Aug 29, 2019
"""

SPC = [" ","&nbsp;","&ensp;","&ensp;[SPACE]","&emsp;","&emsp;[SPACE]"]
# Note: 5 is the largest combination of "&[en/em/np]sp;" and [SPACE] without
# using another "&[en/em/np]sp;"


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
     
    Input: string list
    Output: string
    
    """
    
    #print("Cat! \nI'm a kitty cat. \nAnd I dance dance dance,"
    #+ "\nand I dance dance dance")
    output = ""
    for line in input:    
        #print(line)
        output += optMd(line)
    #print(output)
    return(output)

def txtToMd(input):
    output = input.replace("    ", SPC[4])
    output = output.replace("  ", SPC[2])
    # only needed if following newline
    if output[0] == " ":
        output = output.replace(" ", SPC[1], 1)
    return(output)

def mdToTxt(input):
    output = input.replace("&emsp;", SPC[4])
    output = output.replace("&ensp;", SPC[2])
    output = output.replace("&nbsp;", SPC[1])
    return(output)

def optMd(line):
    """optimizes spacing to use the least amount of charecters possible
    Using a simple algorithm following these rules:
    [SPACE] after a character takes up one char
        - use as frequently as possible when useful
    &emsp;/&ensp;/&nbsp; are all the same string length
        - sometimes using [SPACE] as often as possible, leads to issues
        - i.e. '&emsp;' == '&ensp; &nbsp' == '&nbsp; &nbsp; '
    """
    # Count number of consecutive spaces when exceeding more than one
    # Or at a newline
    output = line;
    if line[0] == ' ':
        output = output.replace(" ", SPC[1], 1)
    count = 0
    for char in line:
        if (char != " "):
            if (count > 1):
                index = 5
                while index != 0:
                    div = count//index
                    rem = count%index
                    output = output.replace(" "*index, SPC[index], div)
                    if rem == 0: 
                        index = 0
                    else: 
                        index -= 1
            count = 0
        else:
            count += 1
    # replace placeholder spaces with actual space
    output = output.replace("[SPACE]", SPC[0])
    # TEST
    # print(mdToTxt(output))
    return(output)

if __name__ == '__main__':
    """
    Handles file I/O.
    Input: txt file from args
    Output: txt file named "output.txt"
    
    Note, strips trailing whitespaces
    """
    import sys
    input = open(sys.argv[1], "r")
    textIn = input.readlines()
    # print(textIn)
    input.close()
    output = open("output.txt", "w")
    output.write(main(textIn))
    output.close()
    