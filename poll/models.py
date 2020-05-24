from django.db import models

# Create your models here.
class Poll(models.Model):
    question=models.TextField()
    option_one=models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four = models.CharField(max_length=30)
    option_five = models.CharField(max_length=30)
    option_six=models.CharField(max_length=30)
    option_seven=models.CharField(max_length=30)
    option_eight=models.CharField(max_length=30)
    option_nine=models.CharField(max_length=30)
    option_ten = models.CharField(max_length=30)
    option_one_count=models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count=models.IntegerField(default=0)
    option_four_count=models.IntegerField(default=0)
    option_five_count=models.IntegerField(default=0)
    option_six_count=models.IntegerField(default=0)
    option_seven_count = models.IntegerField(default=0)
    option_eight_count = models.IntegerField(default=0)
    option_nine_count = models.IntegerField(default=0)
    option_ten_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count+self.option_two_count+self.option_three_count+self.option_four_count+self.option_five_count+self.option_six_count+self.option_seven_count+self.option_eight_count+self.option_nine_count+self.option_ten_count

    def __str__(self):
        return self.question