#!/usr/bin/env python

import pytest
import requests

def test_methodnotsupported():
    """A py.test for returning status code 405 on a POST request.
    
    """

    URL_STR = "http://52.24.157.193:5000/api/fib/2"
    response = requests.post( URL_STR )
    data = response.json()
    assert response.status_code == 405
    
if __name__ == "__main__":
    print test_methodnotsupported()
    
