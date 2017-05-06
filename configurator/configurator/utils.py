def fmap(value, func):
    if value is not None:
        return func(value)
    else:
        return None
