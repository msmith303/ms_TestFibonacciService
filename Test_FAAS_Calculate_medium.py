#!/usr/bin/env python

import pytest
import requests

def test_get():
    """A py.test for testing the GET verb
    
    """
    ival = 1
    assert ival == 1

    URL_STR = "https://api.github.com"
    response = requests.get( URL_STR )
    data = response.json()
    print(data['current_user_url'])
    
if __name__ == "__main__":
    print test_get()
    
