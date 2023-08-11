#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    list_name = dir(hidden_4)
    for name in list_name:
        if name[0] != '_':
            print(name)
