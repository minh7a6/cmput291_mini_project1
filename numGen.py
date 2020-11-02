from uuid import uuid4


def numGen(length):
    id = uuid4()
    return str(id)[:length]