import requests


def send_requests(url:str = None) -> dict | bool:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False


def main():
    url = "https://swapi.dev/api/people/1/"
    response = send_requests(url)

    if not response:
        print("Ошибка")
        return

    name = response["name"]
    height = response["height"]
    mass = response["mass"]
    hair_color = response["hair_color"]

    print(f"Имя: {name}")
    print(f"Рост: {height}")
    print(f"Масса {mass}")
    print(f"Цвет волос: {hair_color}")


if __name__ == "__main__":
    main()


# response = requests.get("https://swapi.dev/api/people/1/")
# response = response.json()
# # print(response)
#
# name = response["name"]
# height = response["height"]
# mass = response["mass"]
# hair_color = response["hair_color"]
#
# print(f"Имя: {name}")
# print(f"Рост: {height}")
# print(f"Масса {mass}")
# print(f"Цвет волос: {hair_color}")