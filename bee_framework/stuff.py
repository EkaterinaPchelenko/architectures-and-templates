# def parse_data(func):
#     def wrapper(*args):
#         data = func(args)
#         res = {}
#         if data:
#             items = data.split('&')
#             for item in items:
#                 key, value = item.split('=')
#                 res[key] = value
#         return res
#     return wrapper

def parse_data(data: str):
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            key, value = item.split('=')
            result[key] = value
    return result