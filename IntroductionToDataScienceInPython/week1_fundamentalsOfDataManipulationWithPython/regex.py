import re

regex=r"(M|m)"
match=re.search(regex,"mmmmmmMMMMmmm")
print(match)