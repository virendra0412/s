import json
from bs4 import BeautifulSoup
import requests
def scrap(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    Quora_json = dict()
    question = soup.find("title")
    Quora_json["question"] = question.text.replace("- Quora", " ")
    answers = soup.find("script", {"type": "application/ld+json"})
    ans_list = json.loads(answers.string)  
    Quora_json["answers"] = []
    for i in range(0, 10):
        answer_val = {"name": ans_list["mainEntity"]["suggestedAnswer"][i]["author"]["name"],
                      "text": ans_list["mainEntity"]["suggestedAnswer"][i]["text"],
                      "upvoteCount": ans_list["mainEntity"]["suggestedAnswer"][i]["upvoteCount"]}
        Quora_json["answers"].append(answer_val)

        with open("quora.json", 'w')as outfile:
            json.dump(Quora_json, outfile, indent=4)