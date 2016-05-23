#!/usr/bin/env python

import pytest
import requests

def test_calculate_large():
    """A py.test for calculating a typical number in a fibonacci sequence.
    
    """

    URL_STR = "http://52.24.157.193:5000/api/fibonacci/100"
    response = requests.get( URL_STR )
    data = response.json()
    assert response.status_code == 200
    
if __name__ == "__main__":
    print test_calculate_large()
    
