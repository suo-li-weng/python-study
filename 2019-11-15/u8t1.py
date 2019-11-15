import re
s = 'This is is a desk'
s = re.sub(r'(\b\w+) \1', r'\1', s)
print(s)

t = "aaa bbbe ccc dddg feg"
r = re.compile(r'\b[a-zA-Z]{3}\b')
a = r.findall(t)
print(a)
