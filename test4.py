from string import Template

t1 = Template("$who like $you")
print(t1.safe_substitute(who="he", you="she"))
d = {"dd": 2, "dd": 3}
s = {1, 2, 3, 3}
s = set(s)
print(d)
print(s)
