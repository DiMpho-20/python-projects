from analyzer import LogAnalyzer
from config import LOG_FILE


def main():
    analyzer = LogAnalyzer(LOG_FILE)

    while True:
        print("\n----- Log Analyzer -----")
        print("1. View log summary")
        print("2. Count log levels")
        print("3. Most common error")
        print("4. Hour with most errors")
        print("5. Filter by level")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            levels = analyzer.count_levels()

            print("\n----- Summary -----")
            print(f"ERROR: {levels.get('ERROR', 0)}")
            print(f"WARNING: {levels.get('WARNING', 0)}")
            print(f"INFO: {levels.get('INFO', 0)}")

        elif choice == "2":
            levels = analyzer.count_levels()

            print("\nLog Levels:")
            for level, count in levels.items():
                print(f"{level}: {count}")

        elif choice == "3":
            error = analyzer.most_common_errors()

            if error:
                print(f"\nMost common error: {error}")
            else:
                print("\nNo errors found.")

        elif choice == "4":
            hour = analyzer.hour_with_most_errors()

            if hour:
                print(f"\nHour with most errors: {hour}:00")
            else:
                print("\nNo errors found.")

        elif choice == "5":
            level = input("Enter level (ERROR, WARNING, INFO): ").upper()

            logs = analyzer.filter_by_level(level)

            if logs:
                print()
                for log in logs:
                    print(log)
            else:
                print(f"\nNo {level} logs found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()