# Import libraries
import requests
from twilio.rest import Client


def main():
    weather_data = make_api_connection()
    if weather_data:
        weather_id = get_current_weather(weather_data)
        message = check_weather(weather_id)
        text_weather_details(message)


def make_api_connection() -> list[dict]:
    """
    Summary:
        Attempts to obtain the openweathermap API data for current weather
    Returns:
        list[dict]: JSON data of current weather
    Called By:
        weather_data in main() function
    """
    # Set API parameters
    parameters = {
        "lat" : 37.687176,
        "lon" : -97.330055,
        "appid" : "48f05eecbd8328ad9353b4ab488b3ace"
    }

    # Attempt to obtain API
    try:
        weather_response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
        weather_response.raise_for_status()
        # Store weather API data via JSON
        return weather_response.json()
    except requests.exceptions.RequestException as e:
        print("Unable to obtain the API, error: ", str(e))
        return None


def get_current_weather(weather:list[dict]) -> int:
    """
    Summary:
        Takes the argument weather and extracts the weather ID from the list of dictionaries
    Args:
        weather (list[dict]): A list of dictionaries containing all pertinent data for the current weather
    Returns:
        int: The weather "id", which directly correlates to the atmospheric conditions
    Called by:
        weather_id in main() function
    """
    weather_id = weather["weather"][0]["id"]
    return weather_id


def check_weather(weather_id:int) -> str:
    """
    Summary:
        Takes an int as input and compares it vs known Openweathermap Weather Codes 
        to alert you to current weather conditions
    Args:
        weather_id (int): Takes an ID code as an argument
    Returns:
        None: Sends an sms with current weather data
    Called by:
        main()
    """
    if 200 <= weather_id <= 600:
        return "Its raining outside, bring an umbrella" 
    elif 600 <= weather_id <= 700:
        return "It's going to snow, dress warm"
    elif weather_id == 800:
        return "It's going to be a clear day! Enjoy the sun."
    elif weather_id > 800:
        return "It's going to be cloudy outside"


def text_weather_details(message: str) -> None:
    """
    Summary:
        Takes a message as a parameter and then sends the message via sms using Twilio
    Args:
        message (_type_): Takes a message and then sends it via the 'body' portion
    Returns:
        None
    Called by:
        main()
    """
    account_sid = "AC38cd4634ff2945173a457bf8114c9ca1"
    auth_token = "1751ac21fc5a468bce809ea0b83fc40a"
    client = Client(account_sid, auth_token)
    text_message = client.messages.create(
            body=message,
            from_="+18556373199", 
            to="+14099519944",  
        )


if __name__ == "__main__":
    main()