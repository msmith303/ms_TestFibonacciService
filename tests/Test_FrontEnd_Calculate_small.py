#!/usr/bin/env python

import pytest
import urllib

def test_frontend_calculate_small():
    """A py.test front end test for calculating a small number in a fibonacci sequence.
    
    """

    URL_STR = "http://53.24.157.193"
    values = {'number': 1,
                 'submit': 'SUBMIT'}
    html = urllib.urlopen(URL_STR, urllib.urlencode(values)).read()
    assert html == 200
    
if __name__ == "__main__":
    print test_frontend_calculate_small()
    
