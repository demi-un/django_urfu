import requests


def send_requests(url:str = None) -> dict | bool:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False


def main():
    url = "https://swapi.dev/api/starships/?search-Millennium Falcon"
    response = send_requests(url)
    for results in response["results"]:
        pilots = results["pilots"]
        if len(pilots) > 0:
            print(f"\nПилоты {results['name']}:")
            for pilot in pilots:
                name_response = send_requests(pilot)
                name = name_response["name"]
                print(f"- {name}")


if __name__ == "__main__":
    main()
