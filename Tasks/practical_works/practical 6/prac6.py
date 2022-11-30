import re

pattern = (r"^Рейс (\d+) (?:прибыл|отправился) (из|в) (\w+) в (\d{2}:\d{2}:\d{2})")

with open("old.txt", "r", encoding="utf-8") as o:
    with open("new.txt", "w", encoding="utf-8") as n:
        for line in o:
            res = re.search(pattern, line)
            if res:
                n.write( f"[{res.groups()[3]}] Поезд № {res.groups()[0]} {res.groups()[1]} {res.groups()[2]}\n")