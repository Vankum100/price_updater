import re
txt = "'SONY PS 5 Disk (JP)"

x = txt.split()
y = re.sub("'","",txt).split()
print(y)
print(x)
