from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror
from Bypass import BASE_URL, PORT

if PORT is not None:
    while 1:
        try:
            rget(BASE_URL).status_code
            sleep(600)
        except Exception as e:
            logerror(f"alive.py: {e}")
            sleep(600)
            continue
