#!/usr/bin/python3
import urllib


"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
"""
fet = urllib.request.urlopen('https://alx-intranet.hbtn.io/status/')
with urllib.request.urlopen(fet) as response:
    the_page = response.read()


