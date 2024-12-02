import pdb

input_file = "input.txt"

reports = []

def positive(number: int) -> bool:
    if number >= 0:
        return True
    else:
        return False

def check_report(report):
    unsafe = False

    for i, number in enumerate(report):
        l_exist = True
        r_exist = True
        if i == 0:
            diff = 1
            l_exist = False
            ok_dir = positive(number - report[1])
        else:
            diff = report[i-1] - number

        if not l_exist:
            dir = ok_dir
        else:
            dir = positive(diff)

        if abs(diff) > 3 or diff == 0 or dir != ok_dir:
            unsafe = True

    return unsafe

with open(input_file) as input:
    report = []
    for line in input:
        numbers = line.split()
        report = [ int(x) for x in numbers]
        reports.append(report)

safe = 0

for report in reports:
    unsafe = check_report(report)

    if unsafe:
        pass
    else:
        safe += 1

print(f"Result: {safe} reports are safe")
