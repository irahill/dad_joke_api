import requests 
from random import choice
from pyfiglet import figlet_format #format output will show how line is written
from termcolor import colored #colour uses

header = figlet_format("DAD JOKE 3000!")
header = colored(header, color ="magenta")
print(header)

user_input = input("On what topic you want Joke: ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(
                        url,
                        headers={"Accept":"application/json"},
                        params = {"term":user_input}
                        ).json()


num_jokes = response["total_jokes"]
results = response["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here's one: ")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke about {user_input}. Here's one: ")
    print((results)[0]["joke"])
else:
    print(f"there are no jokes on {user_input}")
