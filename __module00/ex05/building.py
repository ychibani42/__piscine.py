import sys


def builder(s):
    d = {"uppercase": 0, "lowercase": 0, "punctuation": 0,
         "space": 0, "digit": 0}
    for c in s:
        if c.isupper():
            d["uppercase"] += 1
        elif c.islower():
            d["lowercase"] += 1
        elif c.isspace():
            d["space"] += 1
        elif c.isdigit():
            d["digit"] += 1
        elif c in ('!', ",", "\'", ";", "\"", ".", "-", "?", ":"):
            d["punctuation"] += 1
        else:
            pass
    val = input("Enter :")
    print("The text contains %d characters: " % len(s))
    print("%d upper letters" % d["uppercase"])
    print("%d lower letters" % d["lowercase"])
    print("%d punctuation marks" % d["punctuation"])
    print("%d spaces" % d["space"])
    print("%d digits" % d["digit"])


builder(sys.argv[1])
