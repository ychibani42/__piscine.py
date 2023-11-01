import sys


if len(sys.argv) == 1:
    print('\r')
    sys.exit()
try:
    assert len(sys.argv) == 2, "more than one argument is provided"
    __to_check = sys.argv[1]
    try:
        int(__to_check)
    except:
        raise AssertionError("argument is not an integer")
    __to_check = int(__to_check)
    if (__to_check % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print("AssertionError: " + str(e))
