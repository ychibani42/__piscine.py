import sys


def builder():
    if len(sys.argv) < 2:
        val = input("What is the text to count?\n")
    elif len(sys.argv > 2):
          raise AssertionError("Wrong Number of argument")
    else:
        val = sys.argv[1];
    d = {"uppercase": 0, "lowercase": 0, "punctuation": 0,
         "space": 0, "digit": 0}
    for c in val:
        if c.isupper():
            d["uppercase"] += 1
        elif c.islower():
            d["lowercase"] += 1
        elif c.isspace():
            d["space"] += 1
        elif c.isdigit():
            d["digit"] += 1
        elif c in ['!', ",", "\'", ";", "\"", ".", "-", "?", ":"]:
            d["punctuation"] += 1
        else:
            pass
    print("The text contains %d characters: " % len(val))
    print("%d upper letters" % d["uppercase"])
    print("%d lower letters" % d["lowercase"])
    print("%d punctuation marks" % d["punctuation"])
    print("%d spaces" % d["space"])
    print("%d digits" % d["digit"])


if __name__ == "__main__":
    builder()
