from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Test(models.Model):
    #test=
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    test_time=models.DateTimeField(default=timezone.now)

class Song(models.Model):
    #song=
    singer=models.CharField(max_length=30,null=True)
    song_name=models.CharField(max_length=40)
    url=models.CharField(max_length=800)
    lyrics=models.TextField()

    def __str__(self):
        return self.song_name

class Question(models.Model):
    #question=
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    question=models.CharField(max_length=500)
    start_time=models.IntegerField()
    finish_time=models.IntegerField()

class History(models.Model):
    test=models.ForeignKey(Test,on_delete=models.CASCADE)
    turn=models.IntegerField()
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=30)

class Wordlist(models.Model):
    #word=
    word=models.CharField(max_length=20)
    target=models.IntegerField()

# Create your models here.
