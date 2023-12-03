# Project Title: 0x10. Python - Network #0

## Overview
This project focuses on enhancing your understanding of networking concepts and skills in both Bash and Python. The objectives cover a wide range of topics related to HTTP, URLs, HTTP requests and responses, headers, cookies, cURL usage, and more.

## Learning Objectives
Upon completing this project, you should be able to explain the following concepts without external assistance:

### General
- What a URL is
- What HTTP is
- How to read a URL
- The scheme for an HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Copyright - Plagiarism
- You are responsible for generating solutions to meet the learning objectives.
- Copying and pasting someone else’s work is not permitted.
- Publishing any content from this project is strictly forbidden.
- Plagiarism will result in removal from the program.

## Requirements
### General
- **Allowed editors:** vi, vim, emacs
- A `README.md` file at the root of the project folder is mandatory.
- All Bash scripts must be exactly 3 lines long (`wc -l file` should print 3).
- All files must end with a new line.
- All files must be executable.
- The first line of all Bash files should be exactly `#!/bin/bash`.
- The second line of all Bash scripts should be a comment explaining the script's purpose.
- All curl commands must have the option `-s` (silent mode).
- All Python scripts will be tested on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- The first line of all Python files should be exactly `#!/usr/bin/python3`.
- Code should adhere to PEP 8 standards (use `pycodestyle` version 2.8.*).
- All modules, classes, and functions should be documented appropriately.

## Project Structure
The project is organized with the following structure:
- `bash/`: Directory containing Bash scripts.
- `python/`: Directory containing Python scripts.
- `README.md`: This file providing an overview and guidelines for the project.

## Usage
To run the scripts in the project, follow these guidelines:
### Bash Scripts
1. Navigate to the `bash/` directory.
2. Make the script executable if not already (`chmod +x script.sh`).
3. Run the script (`./script.sh`).
### Python Scripts
1. Navigate to the `python/` directory.
2. Make the script executable if not already (`chmod +x script.py`).
3. Run the script (`./script.py`).

## Testing
All scripts have been tested on Ubuntu 20.04 LTS and Python 3.8.5.

## Dependencies
- `python3`: Version 3.8.5.
- `pycodestyle`: Version 2.8.*.

## Documentation
Ensure that all modules, classes, and functions are documented. To check documentation for a module or class, use the following commands:
```bash
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'

