import os
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
joke = data["value"]
print(joke)

library = open("chuck_jokes.txt", "a")
library.write(f"{joke} \n")
