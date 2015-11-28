import json
__author__ = 'safo'


def is_request_post(r, *kargs):
    if not r.method == 'POST':
        return False

    for o in kargs:
        if not o in r.POST or len(r.POST[o]) == 0:
            return False

    return True


def jun_post(r):
    if is_request_post(r):
        return r.POST


def post_to_json(r):
    j = jun_post(r)
    if j:
        return json.loads(j['json'])