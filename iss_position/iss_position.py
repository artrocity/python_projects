# Import Libraries
import requests
from datetime import datetime
from twilio.rest import Client
import time

# Set your current Lat/Long Position
parameters = {"lat": 37.687176, "lng": -97.330055, "formatted": 0}
my_lat = parameters["lat"]
my_long = parameters["lng"]
my_position = (my_lat, my_long)

# Request Sunrise and Sunset time and store in results in variables
sunset_response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters
)
sunset_response.raise_for_status()
sunset_data = sunset_response.json()
sunrise_hour = int(sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(sunset_data["results"]["sunset"].split("T")[1].split(":")[0])

# Get current time and hour
time_now = datetime.now()
hour_now = time_now.hour

# Check if ISS Station is within +/- 5 to my location
def check_position(iss_position: tuple, my_position: tuple) -> bool:
    return (
        abs(iss_position[0] - my_position[0]) <= 5
        and abs(iss_position[1] - my_position[1]) <= 5
    )

# Check if its night time
def check_time(current_hour: int, sunrise: int, sunset: int) -> bool:
    """
    Summary:
        Checks current time and returns a boolean if between sunrise and sunset
    Args:
        current_hour (int): Current Hour
        sunrise (int): Sunrise Hour
        sunset (int): Sunset Hour
    Returns:
        bool: Returns True if current hour is between Sunset and Sunrise
    """
    return current_hour < sunrise or current_hour > sunset

account_sid = "AC38cd4634ff2945173a457bf8114c9ca1"
auth_token = "1751ac21fc5a468bce809ea0b83fc40a"
client = Client(account_sid, auth_token)

# Send a text message to me to look up
def is_ISS_close_to_me() -> None:
    if check_position(iss_position, my_position) and check_time(
        hour_now, sunrise_hour, sunset_hour
    ):
        message = client.messages.create(
            body="The International Space Station is Above you!",
            from_="+18556373199",  # Replace with your Twilio number
            to="+14093516669",  # Replace with the recipient's phone number
        )

# Have the code run every 60 seconds
while True:
    try:
        # Update ISS position
        iss_reponse = requests.get(url="http://api.open-notify.org/iss-now.json")
        iss_reponse.raise_for_status()
        iss_data = iss_reponse.json()
        iss_longitude = float(iss_data["iss_position"]["longitude"])
        iss_latitude = float(iss_data["iss_position"]["latitude"])
        iss_position = (iss_latitude, iss_longitude)

        # Update time
        time_now = datetime.now()
        hour_now = time_now.hour

        is_ISS_close_to_me()

        print(f"My position is: {my_position}")
        print(f"ISS Position is: {iss_position}")
        print(f"The current hour is: {hour_now}")
        print(f"Sunrise is: {sunrise_hour}, Sunset is: {sunset_hour}")
        print(f"Position: {check_position(iss_position, my_position)}")
        print(f"Time: {check_time(hour_now, sunrise_hour, sunset_hour)}")
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(60)
