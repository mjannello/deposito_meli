import re


def validate_location_string(location_string):
    r = re.compile("^[A-Z]{2}-\d{2}-\d{2}-(DE|IZ)$")
    if not r.match(location_string):
        raise ValueError
