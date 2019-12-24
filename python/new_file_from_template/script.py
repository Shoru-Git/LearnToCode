import re

name = "SW32-01"
ip = "10.0.32.01"
directory = "SW32"
file = "template.ksr"
collection = {
    '__NAME__': name,
    '__IP__': ip,
    '__DIR__': directory
}

with open(file) as template:
    content = template.read()
    for x, y in collection.items() : 
        content = re.sub(x, y, content)
    template.close
with open("{}.ksr".format(name), "x") as new_file:
    new_file.write(content)
    new_file.close