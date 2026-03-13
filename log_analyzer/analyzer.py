import re
with open('server.log', 'r') as f:
    lines = f.readlines()
#pattern = re.compile(r'\b (?:(?: 25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?: 25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')
for line in lines:
    line = line.strip()