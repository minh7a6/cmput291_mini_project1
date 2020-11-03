from uuid import uuid4


def checkString(x):
    y = str(x)
    if y is None:
        return "None"
    elif (not y.isnumeric()) and len(y) > 50:
        return str(y[:50]) + "..."
    else:
        return str(y)

def numGen(length):
    id = uuid4()
    return str(id)[:length]