import re

def solution(new_id):
    new_id = re.sub(r'\.{2,}', '.', re.sub(r'[^a-z0-9\-\_\.]', '', new_id.lower()))
    if new_id.startswith('.'): new_id = new_id[1:]
    if new_id.endswith('.'): new_id = new_id[:-1]
    if not len(new_id): new_id = 'a'
    if len(new_id) > 15: new_id = new_id[:15]
    if new_id.endswith('.'): new_id = new_id[:-1]
    if len(new_id) < 3:
        while len(new_id)<3:
            new_id += new_id[-1]

    return new_id