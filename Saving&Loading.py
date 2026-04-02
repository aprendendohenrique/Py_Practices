import json
from random import randint

content = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
read_content = None

try:
    with open('content', 'r') as file:
        read_content = json.load(file)
except FileNotFoundError:
    print('File not found')
except Exception as exc:
    print(exc)
    print(exc.__class__)
finally:
    print(read_content)

try:
    with open('content', 'w') as file:
        json.dump(content, file, indent=4)
except Exception as exc:
    print(exc)