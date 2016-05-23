#!/usr/bin/env python

import pytest
import urllib

def test_frontend_calculate_large():
    """A py.test front end test for calculating a large number in a fibonacci sequence.
    
    """

    URL_STR = "http://53.24.157.193"
    values = {'number': 100,
                 'submit': 'Compute'}
    html = urllib.urlopen(URL_STR, urllib.urlencode(values)).read()
    assert html == 100
    
if __name__ == "__main__":
    print test_frontend_calculate_large()
    
