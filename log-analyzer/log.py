class LogAnalyzer:

    def __init__(self, filename):
        self.filename = filename
        self.logs = []
        self.load_logs()

    def load_logs(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    self.logs.append(line.strip())
        except FileNotFoundError:
            print("Log file not found")

    def count_levels(self):
        levels = {}

        for log in self.logs:
            parts = log.split()
            level = parts[2]

            if level in levels:
                levels[level] += 1
            else:
                levels[level] = 1

        return levels

    def most_common_errors(self):
        errors = {}

        for log in self.logs:
            parts = log.split()

            if parts[2] == "ERROR":
                message = " ".join(parts[3:])

                if message in errors:
                    errors[message] += 1
                else:
                    errors[message] = 1

        if len(errors) == 0:
            return None

        return max(errors, key=errors.get)

    def hour_with_most_errors(self):
        hours = {}

        for log in self.logs:
            parts = log.split()

            if parts[2] == "ERROR":
                hour = parts[1].split(":")[0]

                if hour in hours:
                    hours[hour] += 1
                else:
                    hours[hour] = 1

        if len(hours) == 0:
            return None

        return max(hours, key=hours.get)

    def filter_by_level(self, level):
        filtered = []

        for log in self.logs:
            parts = log.split()

            if parts[2] == level:
                filtered.append(log)

        return filtered
    
    def summary(self):
        levels = self.count_levels()

        print("----- Log Summary -----\n")

        print("ERRORS :", levels.get("ERROR", 0))
        print("WARNINGS :", levels.get("WARNING", 0))
        print("INFO :", levels.get("INFO", 0))

        print("\nMost common error:")
        print(self.most_common_errors())

        print("\nHour with most errors:")
        print(self.hour_with_most_errors())

