#!/usr/bin/python3

# Create a small text file with a few lines in it. Write a function that accepts
# two file names where the first is the source file and the second is the
# name of a destination file for a copy. Call it file_copy.

import os

#def file_copy():
    #scratch = open('./editme.txt')
    ##scratch = os.read('./editme.txt')
    #os.write('./newfile', scratch)
    ##f.write(newfile.txt)

#file_copy()

def file_copy(s, t):
    fs = open(s,'r')
    st1 = fs.read()
    ft = open(t, 'w')
    ft.write(st1)
    fs.close()
    ft.close()

file_copy()
