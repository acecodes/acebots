"""
Import.io Scaffold

This is a barebones setup that can be used to start a project that utilizes 
the import.io web scraping API. You will need to create a file called importio_login.py
and create the variables GUID and API_key which, predictably, hold your official
import.io GUID and API key. I've kept mine out of this repository for obvious reasons.

"""

from importio_login import GUID, API_key
import logging, json, importio, latch

client = importio.importio(user_id=GUID, api_key=API_key)
client.connect()