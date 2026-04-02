text = 'Something to be saved'
read_text = None

try:
    with open('text', 'r') as file:
        read_text = file.read()
except FileNotFoundError:
    print('File not found')
except Exception as exc:
    print(exc)
    print(exc.__class__)
finally:
    print(read_text)

try:
    with open('text', 'w') as file:
        file.write(text)
except Exception as exc:
    print(exc)