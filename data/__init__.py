import re
pattern = re.compile('^[a-zA-Z0-9 _\-\"“+/.:]*$')

print(bool(pattern.match("")))