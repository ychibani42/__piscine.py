def NULL_not_found(object: any) -> int:

    message = {
        list: "List",
        int: "List",
    }    
    NoneType = type(None);
    if type(object) is NoneType:
        print(f"None : {type(object)}")
    elif type(object) is float:
        print(f"{object.get(type(object))} nan : {type(object)}")
    return 42