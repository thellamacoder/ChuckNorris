# get_chuck_joke.py is a script to call the chucknorris.io api (https://api.chucknorris.io/) and append it to a text file with all the other jokes returned.
# By Scott Klein 24 March 2026

import os
import requests

if os.path.exists("chuck_jokes.txt"):
    pass

else:
    print("No existing Chuck jokes!")
    open("chuck_jokes.txt", "a")

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
joke = data["value"]
print(joke)

library = open("chuck_jokes.txt", "a")
library.write(f"{joke} \n")
