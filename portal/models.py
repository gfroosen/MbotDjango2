from django.db import models
from django.utils import timezone


class Robot(models.Model):

    controler = models.ForeignKey('auth.User')

    robot = models.CharField(max_length=20)

    task_number = models.FloatField()

    task1_speed = models.FloatField()
    task1_duration = models.FloatField()
    task1_mode = models.CharField(max_length=20)
    task1_command = models.CharField(max_length=20)
    task1_num=models.FloatField()
    task1_char=models.CharField(max_length=20)
    task1_bool=models.BooleanField()

    task2_speed = models.FloatField()
    task2_duration = models.FloatField()
    task2_mode = models.CharField(max_length=20)
    task2_command = models.CharField(max_length=20)
    task2_num=models.FloatField()
    task2_char= models.CharField(max_length=20)
    task2_bool= models.BooleanField()

    task3_speed = models.FloatField()
    task3_duration = models.FloatField()
    task3_mode = models.CharField(max_length=20)
    task3_command = models.CharField(max_length=20)
    task3_num= models.FloatField()
    task3_char= models.CharField(max_length=20)
    task3_bool= models.BooleanField()

    task_loop= models.BooleanField(default=False)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.robot
