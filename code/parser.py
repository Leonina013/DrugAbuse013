
with open('data.txt') as f:
    data = f.readlines()

last_group = ''
out = []

for line_num in range(len(data)):
    line_txt = data[line_num]

    if line_txt.startswith('Codebook Creation Date:') and last_group is not data[line_num - 1]:
        last_group = data[line_num - 1][:-1]
        print('New group found: ' + last_group)
        continue

    parts = line_txt.split(' ')
    # Found variable to save
    if len(parts) > 4 and parts[1] == 'Len' and parts[2] == ':' and parts[3].isdigit():
        out.append((last_group, parts[0], ' '.join(parts[4:-1])))


with open('parsed.csv', 'w') as f:
    f.write('\n'.join([';'.join(line) for line in out]))
