import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name":"Joe", "views" : 1000},
		{"likes": 7, "name":"Tim", "views" : 100},
		{"likes": 9000, "name":"May", "views" : 1000000}]

for i in range(len(data)):
	response = requests.post(BASE + "video/" + str(i), data[i])
	print(response)

response = requests.get(BASE + "video/1")
print(response.json())

reponse = requests.put(BASE + "video/0", {"likes": 500, "name":"Joe", "views" : 1000})
print(response.json())

response = requests.get(BASE + "video/0")
print(response.json())

response = requests.delete(BASE + "video/1")

response = requests.get(BASE + "video/1")
print(response.json())
