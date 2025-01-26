import json
import os

def loadPages(diction):
    with open("static/json/data.json", 'r') as d:
        data = json.load(d)
        d.close()
    for key, val in diction.items():
        data["pages"][key] = val
    data = json.dumps(data, indent=4, ensure_ascii=False)
    with open("static/json/data.json", 'w', encoding="utf-8") as d:
        d.write(data)
        d.close()


def delPages(diction):
    with open("static/json/data.json", 'r') as d:
        data = json.load(d)
        d.close
    for key in diction.keys():
        data["pages"].pop(key, None)
    data = json.dumps(data, indent=4, ensure_ascii=False)
    with open("static/json/data.json", 'w, encoding="utf-8"') as d:
        d.write(data)
        d.close()