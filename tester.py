#!/usr/bin/env python
import unittest, sys
from time import clock
from the2 import is_firmus

SEPERATOR = ';'

def isWrong(r1,r2,answer):
    """Takes the parameters of is_firmus function (r1,r2) and compares them to the expected result (answer)
    Returns the output of the function if the test fails. Returns false otherwise."""
    out = is_firmus(r1,r2)
    if answer[0] != out[0]:
        return out
    if answer[0] == "ADDENDUM":
        outAddendum = [min(out[1][0],out[1][2]),min(out[1][1],out[1][3]),max(out[1][0],out[1][2]),max(out[1][1],out[1][3])]
        for i in xrange(4):
            if abs(answer[1][i]- outAddendum[i]) > 0.001:
                return out
        return False
    else:
        return out if abs(answer[1]- out[1]) > 0.001 else False
    
def test(filename):
    """Test every case in filename, printing failures and statistics.
    filename must be a file with every line containing one test case. 
    Each test case contains three lists, seperated by SEPERATOR global: First two are parameters for is_firmus function and last one is the expected output.
    Prints failures along the way and"""
    with open(filename) as f:
        lines = f.readlines()
    print "File '%s' has been read successfully. Testing starts..."%filename
    testno = 0
    fails = 0
    startTime = clock()
    for l in lines:
        testCase=[eval(a) for a in l.split(SEPERATOR)]
        out = isWrong(*testCase)
        if out:
            print "====== FAILURE ======"
            print "Test %i"%testno
            print "Rectangles:"
            print "%s, %s"%(str(testCase[0]),str(testCase[1]))
            print "Expected: %s"%str(testCase[2])
            print "Obtained: %s\n"%str(out)
            fails += 1
        testno+=1
    elapsedTime = clock() - startTime
    print
    print "====== DONE ======"
    print "%i tests done."%(testno)
    print "%i failures."%fails
    print "%s seconds elapsed."%elapsedTime
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        test(sys.argv.pop())
    else:
        test(raw_input("Please enter the filename of the dataset: "))
