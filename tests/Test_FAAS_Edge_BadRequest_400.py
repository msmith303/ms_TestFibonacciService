#!/usr/bin/env python

import pytest
import requests

def test_badrequest():
    """A py.test for returning status code 400 on a GET request.
    
    """

    URL_STR = "http://52.24.157.193:5000/api/fibonacci/5/foo"
    response = requests.get( URL_STR )
    data = response.json()
    assert response.status_code == 400
    
if __name__ == "__main__":
    print test_badrequest()
    
