import sys
from ft_filter import ft_filter

def check_str(s):
    if not s.isprintable():
        return 1;
    for c in s:
        if (c in ('!', ",", "\"", ".", "-", "?", ":")):
            return 1
    return 0

def filterProgr(s, n) -> list:
    list1 = s.split();
    func = lambda word: len(word) > n or check_str(word) == False
    return (list(filter(func, list1)))

if __name__ == "__main__":
    try:
        if not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")
        if not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")
        assert len(sys.argv) == 3, "Invalid number of arguments"
        print(filterProgr(sys.argv[1], int(sys.argv[2])))
    except (AssertionError, TypeError) as e:
        print("AssertionError: " + str(e))
