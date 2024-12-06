
input_file = "input.txt"

with open(input_file) as input:
    rules_list = []
    for line in input:
        if line == '\n':
            break
        rules_list.append([int(x) for x in line.strip().split('|')])

    updates = []
    for line in input:
        updates.append([int(x) for x in line.strip().split(',')])

rule_pages = set([x[0] for x in rules_list])
rules = {}
for page in rule_pages:
    pages_after = []
    for rule in rules_list:
        if rule[0] == page:
            pages_after.append(rule[1])
    rules.update({page: pages_after})

def check_update_ok(update: list) -> bool:
    ok_update = True
    for i, page in enumerate(update):
        if i == 0:
            continue
        elif page > 100:
            update[i] = page - 100
            page = page - 100
        for update_page in update[0:i]:
            try:
                if update_page in rules[page]:
                    ok_update = False
                    update[i] = page + 100
            except KeyError:
                pass

    return ok_update

ok_updates = []
for update in updates:
    ok_update = check_update_ok(update)
    ok_updates.append(ok_update)

updates_to_fix = [x for (x, t) in zip(updates, ok_updates) if not t]

def fix_positions(update):
    for i, page in enumerate(update):
        if page > 100:
            update[i] = page - 100
            update.insert(i-1, update.pop(i))

            if check_update_ok(update):
                return update
            else:
                fix_positions(update)

updates_to_count = []
for update in updates_to_fix:
    fix_positions(update)
    updates_to_count.append(update)

sum = 0
for update in updates_to_count:
    sum += update[len(update)//2]

print(f"Sum of ok middle page numbers: {sum}")
