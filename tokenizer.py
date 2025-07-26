import requests
def get_data(url: str) -> str:
    response = requests.get(url)
    print(response.text)
