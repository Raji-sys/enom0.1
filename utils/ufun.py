#csv util to avoid print None when model field is empty 
def con(v):
    if v is None:
        return ' '
    else:
        return v

