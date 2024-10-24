#!/usr/bin/python3
"""This script reads stdin line by line"""
import sys

def main():
    """Main function"""
    total_size = 0
    status_code_count = {200: 0, 301: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            # Split into parts and validate the format
            parts = line.split()
            if len(parts) != 7:
                continue

            # Extract file size and status code
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
            except (ValueError, IndexError):
                continue
            
            total_size += file_size

            if status_code in status_code_count:
                status_code_count[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_code_count)

    except KeyboardInterrupt:
        print_stats(total_size, status_code_count)

def print_stats(total_size, status_code_count):
    """print function to print the stats"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f"{status_code}: {status_code_count[status_code]}")

if __name__ == "__main__":
    main()
