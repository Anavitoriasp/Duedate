from datetime import date

# ANSI color codes (work on Linux terminals)
RED = "\033[91m"
ORANGE = "\033[93m"
RESET = "\033[0m"

today = date.today()
current_year = today.year
current_month = today.month

with open("clients.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        day_str, name = line.split(",", 1)
        day = int(day_str.strip())
        name = name.strip()

        try:
            due_date = date(current_year, current_month, day)
        except ValueError:
            continue

        diff_days = (due_date - today).days

        if -7 <= diff_days <= 0:
            if diff_days < 0:
                status = f"{RED}OVERDUE{RESET}"
            else:
                status = f"{ORANGE}DUE TODAY{RESET}"

            print(
                f"{due_date.strftime('%d/%m')} | "
                f"{name} | "
                f"{status} ({abs(diff_days)} days)"
            )

