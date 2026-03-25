# get_chuck_joke.py is a script to call the chucknorris.io api (https://api.chucknorris.io/) and append it to a text file with all the other jokes returned.
# By Scott Klein 24 March 2026

import os
import requests
from easygui import *

# opens or creates file and opens it in append mode

library = open("chuck_jokes.txt", "a")

# calls chucknorris.io api and parses it

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
joke = data["value"]
print(joke)

display = msgbox(joke, "Real Chuck Norris Facts", "lol?")

library.write(f"{joke} \n")
library.close()
