from django.db import models
import random

class QuestionsManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=models.Count('id'))['ids']
        random_index = random.randint(0, count - 1)
        return self.all()[random_index]
    
class Questions(models.Model):
    Question = models.CharField(max_length=512)
    Answer = models.CharField(max_length=128)
    Difficulty = models.CharField(max_length=16)

    objects = QuestionsManager()


def checkAnswer(Question,Answer):
    with open("questions.txt","r") as f:
        for line in f:
            question = line.split(",")
            if question[0] == Question:
                return question[1] == Answer

    print("Invalid Question")
    raise KeyError

def addQuestion(Question,Answer,Difficulty):
    with open("questions.txt","a") as f:
        f.write(Question+","+Answer+","+Difficulty)
