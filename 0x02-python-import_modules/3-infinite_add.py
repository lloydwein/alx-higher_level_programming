#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = 0
    for index in range(len(sys.argv) - 1):
        count += int(sys.argv[index + 1])
    print("{}".format(count))
