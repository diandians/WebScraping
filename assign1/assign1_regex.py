import re

# data = open('regex_sum_42.txt')
data = open('regex_sum_306888.txt')

sum = 0
for line in data:
	line = line.rstrip()
	for number in re.findall('[0-9]+', line):
		sum += int(number)

print(sum)
