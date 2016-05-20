#!/usr/bin/env python

import pytest
import requests

def test_resourcenotfound():
    """A py.test for returning status code 404 on a GET request.
    
    """

    URL_STR = "http://52.40.72.9:5000/api/fibonacci/foo"
    response = requests.get( URL_STR )
    data = response.json()
    assert response.status_code == 404
    
if __name__ == "__main__":
    print test_resourcenotfound()
    
