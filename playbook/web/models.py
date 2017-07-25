from django.db import models

class Play(models.Model):
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    actors = models.CharField(max_length=1023)
    group = models.CharField(max_length=255)
    plot = models.TextField()
    rating = models.IntegerField()
    youtube_link = models.CharField(max_length=1023)

    def __str__(self):
        return ' '.join([self.name, self.group])

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    play = models.ForeignKey('Play', on_delete=models.CASCADE)

    def __str__(self):
        return ' '.join([self.name, self.timestamp])
