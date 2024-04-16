import requests
from gpiozero import LED
from time import sleep

# Setup your LEDs or other output devices
led = LED(17)  # Example GPIO pin 17

def fetch_tournament_data(tournament_name):
    api_url = 'https://volleyboll-dev-quiet-mountain-3664.fly.dev'
    endpoint = '/tournament/info/?tournament_name='
    url = f"{api_url}{endpoint}{tournament_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_teams(data):
    if data and 'tournament' in data:
        for tournament in data['tournament']:
            for group in tournament['groups']:
                for team in group['teams']:
                    print(team['name'])
                    # Example action: Blink an LED for each team
                    led.on()
                    sleep(1)
                    led.off()
                    sleep(1)

if __name__ == "__main__":
    tournament_name = "test2"
    data = fetch_tournament_data(tournament_name)
    display_teams(data)
