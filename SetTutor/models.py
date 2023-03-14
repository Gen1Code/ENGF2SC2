from django.db import models
import random

class QuestionsManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=models.Count('id'))['ids']
        random_index = random.randint(0, count - 1)
        return self.all()[random_index]
    
class Questions(models.Model):
    Question = models.CharField(max_length=512,unique=True)
    Answer = models.CharField(max_length=128)
    Difficulty = models.CharField(max_length=16)

    objects = QuestionsManager()

def getAnswer(Q):
    return Questions.objects.values("Answer").get(Question=Q)['Answer']