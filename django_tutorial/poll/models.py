from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=255)
    # option_one = models.CharField(max_length=100)
    option_one = models.CharField(max_length=200, default='Option 1')
    option_two = models.CharField(max_length=100, default='Option 2')
    option_three = models.CharField(max_length=100, default='Option 3')

    # option_two = models.CharField(max_length=100)
    # option_three = models.CharField(max_length=100)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total_votes(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
