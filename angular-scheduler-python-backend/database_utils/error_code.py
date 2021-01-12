import json

err = {10000: "Exception Occurred",
       1000: "An Unexpected error occured",
       1001: 'args keyword not found in the input parameters.',
       1002: 'One or more argument missing in request url',
       1003: 'Database Connection Failed',
       1010: 'date from not in mm-dd-yy format',
       1013: 'Document Update Conflict',
       1014: 'Database update failed',
       1020: 'Invalid Data',
       2001: 'Some InternalSQL error occurred while creating records',
       2002: 'Duplicate keys for PrimaryKeyField detected.',
       2003: 'Integrity Error. Primary Key already exists',
       }


def error(code, *args):
    try:
        desc = err[code]
    except KeyError:
        desc = err[1000]

    for args in args:
        desc += str(args)
    return json.dumps({"code": code, "description": desc, "status": "failure"}, indent=4)
