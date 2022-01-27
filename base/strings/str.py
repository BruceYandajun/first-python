from datetime import datetime

my_str = "abc{%Y%m%d00}fljf"
print(my_str.find("{"))
print(my_str[my_str.find("{") + 1: my_str.find("}")])

print(my_str.replace("123", "000"))


def replace_str_between_brackets(old_str):
    i = 0
    outer_list = list()
    inner_list = None
    for s in old_str:
        if s == "{":
            inner_list = list()
            inner_list.append(i)
        if s == "}":
            inner_list.append(i)
            outer_list.append(inner_list)
        i += 1
    replace_list = list()
    for inner in outer_list:
        replace_list.append(old_str[inner[0] + 1: inner[1]])
    print(replace_list)
    now = datetime.now()
    for r in replace_list:
        old_str = old_str.replace("{" + r + "}", now.strftime(r))
    return old_str


print(replace_str_between_brackets(my_str))

my_str = ""
print(not my_str)
