# Global Modules
import os
from random import random
import requests
import time
from dotenv import load_dotenv

# Local Modules
from macOS.hardwarerotation import rotatehardware

# Load environment variables from .env file
load_dotenv()


def visit_website(url):
    try:
        response = requests.get(url)
        # You can customize the handling of the response here
        if response.status_code == 200:
            print(f"Visited {url} successfully.")
        else:
            print(f"Failed to visit {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    website_url = os.getenv("WEBSITE_URL")  # Replace with the desired website URL

    while True:
        visit_website(website_url)
        time.sleep(int(os.getenv("SLEEP_TIME")))  # Sleep for 10 seconds before the next request
        # Randomly decide whether to execute the rotate function
        if random() < int(os.getenv("ROTATION_PROBABILITY")): # Adjust the probability threshold (0.2 means 20% chance)
            rotatehardware()

