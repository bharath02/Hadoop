#! /usr/bin/python


import sys

#------ line in stand input
for word in sys.stdin:
    word=word.strip()
    words=word.split()
    
    for values in words:
       print("%s\t%s"% (values,"1"))

