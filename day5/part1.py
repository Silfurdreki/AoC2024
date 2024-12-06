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

ok_updates = []
for update in updates:
    ok_update = True
    for i, page in enumerate(update):
        if i == 0:
            continue
        for update_page in update[0:i]:
            try:
                if update_page in rules[page]:
                    ok_update = False
            except KeyError:
                pass

    ok_updates.append(ok_update)

updates_to_count = [x for (x, t) in zip(updates, ok_updates) if t]
sum = 0
for update in updates_to_count:
    sum += update[len(update)//2]

print(f"Sum of ok middle page numbers: {sum}")
