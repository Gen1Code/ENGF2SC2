from django.db import models


def checkAnswer(Question,Answer):
    with open("questions.txt","r") as f:
        for line in f:
            question = line.split(",")
            if question[0] == Question:
                return question[1] == Answer

    print("Invalid QID")
    raise KeyError

def addQuestion(Question,Answer,Difficulty):
    with open("questions.txt","a") as f:
        f.write(Question+","+Answer+","+Difficulty)
