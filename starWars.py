import requests

response = requests.get("https://swapi.dev/api/people/1/")
response = response.json()
# print(response)

name = response["name"]
height = response["height"]
mass = response["mass"]
hair_color = response["hair_color"]

print(f"Имя: {name}")
print(f"Рост: {height}")
print(f"Масса {mass}")
print(f"Цвет волос: {hair_color}")