import re

with open('day03/input.txt','r') as f:
    data = f.read()

mul_cmds = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)

answer = 0
for mc in mul_cmds:
    a,b = map(int, re.findall(r'\d{1,3}', mc))
    answer += a*b

print(answer)

commands = re.findall(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)', data)
answer=0
enabled = True

for command in commands:
    if command == "do()":
        enabled = True
    elif command == "don't()":
        enabled = False
    elif enabled and command.startswith("mul"):
        a,b = map(int, re.findall(r'\d{1,3}', command))
        answer += a*b

print(answer)