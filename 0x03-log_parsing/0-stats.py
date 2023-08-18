#!/usr/bin/python3
"""module with a reading stdin and computes metrics"""
import sys


"""initialize dict to store status code counts to 0"""
status_code_count = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
}

total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])
            if status_code in status_code_count.keys():
                status_code_count[status_code] += 1
            total_size += file_size
            counter += 1

        if counter == 10:
            print("File size: {}".format(total_size))
            for key, value in sorted(status_code_count.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            counter = 0

except Exception as err:
    pass

finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_code_count.items()):
        if value != 0:
            print("{}: {}".format(key, value))
