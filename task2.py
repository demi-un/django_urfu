import requests


def send_requests(url:str = None) -> dict | bool:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False


def main():
    url = "https://swapi.dev/api/people/1/"
    person_response = send_requests(url)
    planet_response = send_requests(person_response["homeworld"])
    print(f"Люк Скайуокер родился на планете {planet_response['name']}.")


if __name__ == "__main__":
    main()
