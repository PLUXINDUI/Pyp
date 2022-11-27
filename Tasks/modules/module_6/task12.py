stroka= input()

first = stroka.find("h")
last = stroka.rfind("h")
new_string = list(stroka.replace("h", "H"))
new_string[first], new_string[last] = "h", "h"

print("".join(new_string))