import requests

def fetch_weather(base_url, params):
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.text

def generate_url(location):
    return f"https://wttr.in/{location}"

def main():
    params = {
        'n': '',
        'm': '',
        'q': '',
        'T': '',
        'M': '',
        'lang': 'ru'
    }


    locations = ["лондон", "аэропорт шереметьево", "череповец"]
    for location in locations:
        base_url = generate_url(location)
        weather_data = fetch_weather(base_url, params)
        print(weather_data)
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()