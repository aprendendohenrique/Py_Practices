items = {}

def add_item(item):
    if item[0] in items:
        items[item[0]] = item[1] + items[item[0]]
    else:
        items[item[0]] = item[1]