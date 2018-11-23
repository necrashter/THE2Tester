#!/usr/bin/env python
import unittest
from the2 import is_firmus

class ExamplesInPDF(unittest.TestCase):
    """This is a test case containing the example figures and their provided outputs in the PDF"""
    def assertTHE2(self,r1,r2,answer):
        """Takes the parameters of is_firmus function (r1,r2) and compares them to the expected result (answer)
        In case of "ADDENDUM", the order of coordinates does not matter."""
        out = is_firmus(r1,r2)
        self.assertEqual(answer[0], out[0])
        if answer[0] == "ADDENDUM":
            outAddendum = [min(out[1][0],out[1][2]),min(out[1][1],out[1][3]),max(out[1][0],out[1][2]),max(out[1][1],out[1][3])]
            for i in xrange(4):
                self.assertAlmostEqual(answer[1][i], outAddendum[i])
        else:
            self.assertAlmostEqual(answer[1], out[1])
            
    def test_figure1(self):
        self.assertTHE2([-0.5,10,-6,13],[-7,0,3,10], ['FIRMUS', 116.5])
    def test_figure2(self):
        self.assertTHE2([0.5,19,9.5,9],[3.8,9,5.5,0], ['FIRMUS', 105.3])
    def test_figure3(self):
        self.assertTHE2([-8,11,2,5],[1,0,-2,5], ['ADDENDUM', [2, 5, 4, 11]])
    def test_figure4(self):
        self.assertTHE2([-7,5,7,10],[9.5,12.6,-1,10], ['DAMNARE', 97.3])
    def test_figure5(self):
        self.assertTHE2([-3,7,5,15],[-7,0,7,5], ['DAMNARE', 134.0])
    def test_figure6(self):
        self.assertTHE2([6,4,3.9,-1],[0.5,14.2,9.5,4], ['DAMNARE', 102.3])
    def test_figure7(self):
        self.assertTHE2([0,0,2.4,5.2],[-8.7,10,0,0], ['DAMNARE', 99.48])
    def test_figure8(self):
        self.assertTHE2([0,10,-8.7,0],[-4,9,-1,14], ['DAMNARE', 99.0])
        

if __name__ == '__main__':
    unittest.main()
