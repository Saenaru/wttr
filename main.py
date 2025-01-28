import requests


def fetch_weather(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"An error occurred: {e}"


def generate_url(location):
    base_url = "https://wttr.in/{}?n?m??q?TMTqu&lang=ru"
    return base_url.format(location)


def main():
    locations = ["лондон", "аэропорт шереметьево", "череповец"]
    for location in locations:
        url = generate_url(location)
        weather_data = fetch_weather(url)
        print(weather_data)
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
