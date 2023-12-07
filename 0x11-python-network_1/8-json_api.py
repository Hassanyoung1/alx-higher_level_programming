#!/usr/bin/python3
"""
A Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    # Check if the letter is provided as a command line argument
    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    params = {'q': letter}

    response = requests.post(url, params=params)

    # Check the HTTP status code
    if response.status_code == 200:
        try:
            # Attempt to parse the JSON response
            json_data = response.json()

            if isinstance(json_data, list) and json_data:
                # Display the first result
                user = json_data[0]
                user_id = user.get('id', '')
                user_name = user.get('name', '')
                print(f"[{user_id}] {user_name}")
            else:
                print("No result")

        except ValueError:
            print("Not a valid JSON")
    else:
        print(f"Error: {response.status_code}")

