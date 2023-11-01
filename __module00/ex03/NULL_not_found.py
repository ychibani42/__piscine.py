import math


def NULL_not_found(object: any) -> int:

    assignated_type = {
        type(None): "Nothing",
        float: "Cheese",
        int: "Zero",
        str: "Empty",
        bool: "Fake"
    }

    message = assignated_type.get(type(object))
    value = object

    if isinstance(object, str):
        if value != "":
            message = "Type not found"

    if message == "Fake":
        if value is not False:
            message = "Type not found"

    if message == "Zero":
        if value:
            message = "Type not found"

    if isinstance(object, float):
        try:
            if math.isnan(object):
                value = "nan"
            else:
                message = "Type not found"
        except TypeError:
            message = "Type not found"

    if message == "Type not found":
        print(message)
        return 1
    else:
        if message == "Empty":
            print(f"{message}: {type(object)}")
        else:
            print(f"{message}: {value} {type(object)}")
        return 0
