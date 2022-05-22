import json
from exceptions import *


def load_json_data(path):
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_posts_by_substring(posts, substring):
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded


#print(load_json_data("../posts.json"))
#print(search_posts_by_substring("Ага", "../posts.json"))