# Fetch random developer jokes from a public API
import urllib.request
import json

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    with urllib.request.urlopen(url) as response:
        joke = json.loads(response.read().decode())
    return f"{joke['setup']} ... {joke['punchline']}"

if __name__ == "__main__":
    for i in range(3):
        print(f"Joke {i+1}: {get_joke()}")
        print()
