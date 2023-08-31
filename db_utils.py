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