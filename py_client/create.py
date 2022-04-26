import requests
headers={"Authorization": "Bearer ed6d25368fd8effe99f16391a2e9e0e99f914af4"}
endpoint="http://localhost:8000/api/products/"
data={"title":"this field is done",
    "price":32.99
}

post_response=requests.post(endpoint,json=data,headers=headers)
print(post_response.json())