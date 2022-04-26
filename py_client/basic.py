import requests
endpoint="http://localhost:8000/api/"
post_response=requests.post(endpoint,json={"content":"Hello World"})

print(post_response.json())
