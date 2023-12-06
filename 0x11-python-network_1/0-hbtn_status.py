#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request
    fetch = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(fetch) as response:
        the_page = response.read()
        print('Body response:')
        print(f"\t- type: {type(the_page)}")
        print(f"\t- content: {the_page}")
        print(f"\t- utf8 content: {the_page.decode('utf-8')}")
