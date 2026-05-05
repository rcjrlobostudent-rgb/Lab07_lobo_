from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.event}"