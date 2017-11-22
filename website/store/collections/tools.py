def RepresentInt(object):
    try:
        int(object)
        return True
    except ValueError:
        return False