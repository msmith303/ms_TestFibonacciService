#!/usr/bin/env python

import pytest
import requests

def test_servererror():
    """A py.test for returning status code 500 on a GET request.
    
    """

    URL_STR = "http://52.24.157.193:5000/api/fibonacci/^m"
    response = requests.post( URL_STR )
    data = response.json()
    assert response.status_code == 500
    
if __name__ == "__main__":
    print test_servererror()
    
