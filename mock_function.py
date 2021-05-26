# Using fake placeholder API call per docs
# https://jsonplaceholder.typicode.com/?userId=1

import requests

def get_todo_from_id(id):
    url = 'https://jsonplaceholder.typicode.com/todos/' + str(id)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

print(get_todo_from_id(300))