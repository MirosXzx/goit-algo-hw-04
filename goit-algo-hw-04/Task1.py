def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0.0
            count = 0

            for line in file:
                name, salary = line.strip().split(",")
                total += float(salary)
                count += 1

            average = total / count if count > 0 else 0.0

            return total, average

    except FileNotFoundError:
        return 0.0, 0.0
    except Exception:
        return 0.0, 0.0
