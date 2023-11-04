def oxford_comma(items):
    if len(items) <= 1:
        return "".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    else:
        comma_separated = ', '.join(items[:-1])
        return f"{comma_separated}, and {items[-1]}"