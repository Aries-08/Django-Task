from django.db import models

class ipl(models.Model):
    team1 = models.CharField(max_length = 255)
    team2 = models.CharField(max_length = 255)
    season = models.IntegerField()

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.season}"
