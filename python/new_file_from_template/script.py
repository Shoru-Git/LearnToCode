import argparse, re

parser = argparse.ArgumentParser(description='Tutorial of argparse')
parser.add_argument("--name", required=True, type=str, help="Name of the equipment")
parser.add_argument("--ip", required=True, type=str, help="IP address of the equipment")
parser.add_argument("--directory", required=True, type=str, help="Directory of log files")

args = parser.parse_args()

file = "template.ksr"

collection = {
    '__NAME__': args.name,
    '__IP__': args.ip,
    '__DIR__': args.directory
}

with open(file) as template:
    content = template.read()
    for pattern, value in collection.items() : 
        content = re.sub(pattern, value, content)
with open("{}.ksr".format(args.name), "w") as new_file:
    new_file.write(content)