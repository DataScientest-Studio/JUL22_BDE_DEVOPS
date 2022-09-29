import pytest 
import requests

def test_hello():
    r = requests.get("http://localhost:8000/hello")
    assert r.json() == "Hello"

def test_status():
    r = requests.get("http://localhost:8000/status")
    assert int(r.json()) == 1

def test_data(): 
    r = requests.get("http://localhost:8000/data")
    r.status_code == 200

