import math

def ev(e):
    e = e.replace(" ", "")
    if "(" in e:
        str = e.index("(")
        end = e.index(")")
        ine = e[str + 1:end]
        r = ev(ine)
        e = e.replace(e[str:end + 1], str(r))
        return ev(e)
    if "^" in e:
        p = e.split("^")
        return ev(p[0]) ** ev(p[1])
    if "*" in e or "/" in e:
        p = e.split("*" if "*" in e else "/")
        if "*" in e:
            return ev(p[0]) * ev(p[1])
        else:
            return ev(p[0]) / ev(p[1])
    if "+" in e:
        p = e.split("+")
        return ev(p[0]) + ev(p[1])
    elif "-" in e:
        p = e.split("-")
        return ev(p[0]) - ev(p[1])
    if "sqrt" in e:
        p = e.split("sqrt")
        return math.sqrt(ev(p[1]))
    if e.isdigit():
        return int(e)
    if "." in e:
        return float(e)
    raise ValueError("Invalid expression")


while True:
    e = input(">> ")
    try:
        r = ev(e)
        print("= ", r)
    except ValueError as e:
        print("Error:", e)