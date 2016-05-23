#!/usr/bin/env python

import pytest
import requests

def test_frontend_calculate_medium():
    """A py.test front end test for calculating a typical number in a fibonacci sequence.
    
    """

    URL_STR = "http://53.24.157.193"
    response = requests.get( URL_STR, headers={"content-type":"text"} )
    assert response.status_code == 200
    data = response.json()
    
if __name__ == "__main__":
    print test_frontend_calculate_medium()
    
