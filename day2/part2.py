input_file = "input.txt"

reports = []

def positive(number: int) -> str:
    if number >= 0:
        return "pos"
    else:
        return "neg"

def check_inner_reports(report: list) -> bool:
    for i, number in enumerate(report):
        new_report = list(report)
        new_report.pop(i)
        safe = check_report(new_report)
        if safe:
            break
    return safe


def check_report(report: list) -> bool:
    safe = True
    prev_dir = None

    for i, number in enumerate(report):
        if i == 0:
            continue

        diff = report[i-1] - number
        dir = positive(diff)
        if not prev_dir:
            prev_dir = dir

        if abs(diff) > 3 or diff == 0 or dir != prev_dir:
            safe = False
            break

    return safe

with open(input_file) as input:
    report = []
    for line in input:
        numbers = line.split()
        report = [ int(x) for x in numbers]
        reports.append(report)

safe_reports = 0
fixed_reports = 0

for report in reports:

    safe = check_report(report)

    if safe:
        safe_reports += 1
    else:
        safe = check_inner_reports(report)
        if safe:
            safe_reports += 1
            fixed_reports += 1

print(f"Result: {safe_reports} reports are safe")
