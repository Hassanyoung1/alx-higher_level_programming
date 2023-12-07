#!/usr/bin/python3
"""
 a Python script that takes in a URL and an email address, sends
 a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    mail = argv[2]
    data = {'email': mail}
    response = requests.post(url, data=data)
    print(response.text)
