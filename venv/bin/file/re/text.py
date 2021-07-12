import re
x="[a-z]"
matcher=re.finditer(x,"abt c@5kzabc")
for match in matcher:
    print(match.start())
    print(match.group())