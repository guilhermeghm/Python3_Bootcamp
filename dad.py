#Importing everyting that I need
from pyfiglet import figlet_format
from termcolor import colored
from random import choice
import requests

#Creating all variables:
msg = "Dad Joke 3000"
url = "https://icanhazdadjoke.com/search"

#Creating functions for everthing:
def print_msg(msg):
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color="magenta")
    print(colored_ascii)

def get_joke(url,topic):
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": topic}
    )
    return response.json()

def joke_final():
    jokes = joke_full['results']
    jokes_list = []
    for i in jokes:
        jokes_list.append(i["joke"])
    joke = choice(jokes_list)
    return (joke)

#The program itself:
print_msg(msg)

topic = input("Let me tell you a joke! Give me a topic? ")
joke_full = get_joke(url,topic)


if joke_full['total_jokes'] == 0:
    print(f"Sorry, I don't have any jokes about {topic}! Please, try again.")
elif joke_full['total_jokes'] == 1:
    print(f"I've got one joke about {topic}. Here it is:")
    print(joke_final())
else:
    print(f"I've got {joke_full['total_jokes']} jokes about {topic}. Here it is:")
    print(joke_final())
