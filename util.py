from uuid import uuid4

"""
Function: checkString(x)
Description: this is purposely built for the SearchMain function, it will return None if the input x is none, if x is longer than 50 
                characters, it will return the truncated string to fit better on the terminal
"""
def checkString(x):
    y = str(x)
    if y is None:
        return "None"
    elif (not y.isnumeric()) and len(y) > 50:
        return str(y[:50]) + "..."
    else:
        return str(y)
"""
Function: numGen(length)
Description: this is to generate a unique id based on the length that the implementers required.
"""
def numGen(length):
    id = uuid4()
    return str(id)[:length]