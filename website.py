import random
import requests

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.openai.com",
    # Add more websites here
]

random_websites = random.sample(websites, k=100)

for website in random_websites:
    try:
        response = requests.get(website)
        status = response.status_code
        print(f"{website} - Status: {status}")
    except requests.exceptions.RequestException as e:
        print(f"{website} - Error: {e}")
