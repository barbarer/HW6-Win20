# SI 206
# HW6 - Regular Expressions
# Name: 
# Who did you work with: 


import re
import os
import unittest


def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines


            
def find_coordinates(string_list):
    """ Return a list of valid coordinates from the list of strings. 
    
        string_list -- list of strings to read from
        return -- the list of all coordinates from a list of strings
    """
    pass




def find_emails(string_list):
    """ Return a list of valid emails in the list of strings """
    pass




def find_dates(string_list):
    """ Return a list of dates in the list of strings """
    pass




## Extra credit
def count_char(string_list, char):
    """  return a count of the number of times a specified character appears in a list of strings. 
         It should match the character when it starts or ends a word, and ignore capitalization 
         (e.g., char = 'a' should match 'Apple' and 'apple')
         (It should not match any characters in the middle of a word)
    
        string_list -- the list of strings to count the char in
        char -- the character to look for
        return -- a count of the number of words that begins or ends with inputted char
    """
    pass
        




# Implement your own tests.    
class TestAllMethods(unittest.TestCase):


    def test_find_coordinates(self):
        pass




    def test_find_emails(self):
        pass




    def test_find_dates(self):
        pass




def main():
    # Use main to test your function. 
    # Run unit tests, but feel free to run any additional functions you need
        unittest.main(verbosity = 2)


if __name__ == "__main__":
        main()