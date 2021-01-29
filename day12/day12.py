import re
import json


def rec_remove(container, kw):
    """ recursively remove all dicts with kw in items()
    from json object container
    """
    to_remove = []
    if isinstance(container, list):
        for el in container:
            if isinstance(el, dict):
                if kw in list(el.keys()) + list(el.values()):
                    to_remove.append(el)
                    continue
            if isinstance(el, (list, dict)):
                rec_remove(el, kw)
        for item in to_remove:
            container.remove(item)
    elif isinstance(container, dict):
        for key, el in container.items():
            if isinstance(el, dict):
                if kw in list(el.keys()) + list(el.values()):
                    to_remove.append(key)
                    continue
            if isinstance(el, (list, dict)):
                rec_remove(el, kw)
        for item in to_remove:
            del container[item]
    return


def sum_digits_text(text):
    return sum(map(int, re.findall(r'-?\d+', text)))


INP = open("input.txt").read()
part_1 = sum_digits_text(INP)
print(f"Solution part 1: {part_1}")
json = json.loads(INP)
rec_remove(json, 'red')
part_2 = sum_digits_text(str(json))
print(f"Solution part 2: {part_2}")
