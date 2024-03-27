import redis

r = redis.Redis(charset="utf-8", decode_responses=True)

# r.hset('family', mapping={
#     'name': 'Sample Family',
#     'desc': 'Sample desc',
#     'adults': 2,
#     'children': 0,
#     'phone': '3780000000'
# })

# print(r.hgetall('family:1'))
# print(r.hgetall('family'))
# print(r.hget('family', 'name'))

# data = {
#     'id': 'test',
#     'name': 'Sample Family',
#     'desc': 'Sample desc',
#     'adults': 2,
#     'children': 0,
#     'phone': '3780000000'
# }

# r.hset('my family', mapping=data)
# print(r.hgetall('family:2'))

def add(data):
    r.hset(data['id'], mapping=data)

def autoadd(data):
    key = str(len(r.keys()) + 1).zfill(3)
    data['id'] = key
    r.hset(key, mapping=data)

def get(key):
    return r.hgetall(key)

def get_all():
    response = []
    for key in r.keys():
        response.append(r.hgetall(key))

    return response

def delete_all():
    for key in r.keys():
        r.delete(key)

def confirm(key, data):
    try:
        r.hset(key, mapping={'confirmed_adults': data['confirmed_adults'], 'confirmed_children': data['confirmed_children'], 'confirmed': data['confirmed']})
    except KeyError:
        return ""
    
def get_totals(category: str) -> dict:
    adults_total = 0
    children_total = 0
    adults_total_confirmed = 0
    children_total_confirmed = 0
    
    for key in r.keys():
        adults_total += int(r.hget(key, 'confirmed_adults'))
        children_total += int(r.hget(key, 'confirmed_children'))
        adults_total += int(r.hget(key, 'adults'))
        children_total += int(r.hget(key, 'children'))

    return {'adults_total': adults_total, 'children_total': children_total}