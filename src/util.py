import unidecode


def normalize(_str):
    if(_str):
        return unidecode.unidecode(_str)
    return ""
