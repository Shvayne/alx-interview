#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics"""


def print_stats(total_size, status_code_count):
    """Print function to print the stats"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f"{status_code}: {status_code_count[status_code]}")


def main():
    """Main function that processes input and tracks metrics"""
    total_size = 0
    status_code_count = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 
        404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            # Split into parts and validate the format
            try:
                parts = line.split()
                if len(parts) < 2:  # Need at least status code and file size
                    continue
                    
                # Extract file size and status code from the end
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                
                # Update metrics
                total_size += file_size
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_code_count)

            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:
        pass
    
    finally:
        print_stats(total_size, status_code_count)


if __name__ == "__main__":
    import sys
    main()
