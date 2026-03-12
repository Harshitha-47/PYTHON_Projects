# Log Analyzer using Python
# This program reads and analyzes a system log file.
# It counts different log levels such as INFO, WARNING, and ERROR.
# The analyzer generates a summary report with statistics.
# This project demonstrates file handling, text processing, and log analysis.

def analyze_log(file_name):

    info_count = 0
    warning_count = 0
    error_count = 0
    total_lines = 0

    try:
        with open(file_name, "r") as file:

            for line in file:
                total_lines += 1

                if "INFO" in line:
                    info_count += 1

                elif "WARNING" in line:
                    warning_count += 1

                elif "ERROR" in line:
                    error_count += 1

        print("\n========== Log Analysis Report ==========")
        print(f"Total Log Entries : {total_lines}")
        print(f"INFO Messages     : {info_count}")
        print(f"WARNING Messages  : {warning_count}")
        print(f"ERROR Messages    : {error_count}")

        if total_lines > 0:
            error_rate = (error_count / total_lines) * 100
            print(f"Error Rate        : {error_rate:.2f}%")

        print("=========================================")

    except FileNotFoundError:
        print("Error: Log file not found.")


def main():

    print("\n----- Simple Log Analyzer -----")

    file_name = input("Enter log file name: ")

    analyze_log(file_name)


if __name__ == "__main__":
    main()