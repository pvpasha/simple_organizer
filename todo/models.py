from django.db import models
from datetime import date, datetime, timedelta


class ToDo(models.Model):
    owner = models.EmailField()
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(default=datetime.now)
    finished = models.BooleanField(default=False)


class Task(models.Model):
    owner = models.EmailField()
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    creation_datetime = models.DateTimeField(default=datetime.now)
    finishing_datetime = models.DateTimeField()
    ####
    # TODO Чого так не можна кодити????? --- незнаю...))
    MIN15 = 900
    MIN30 = 1800
    MIN45 = 2700
    HOUR1 = 3600
    HOUR1_5 = 5400
    HOUR2 = 7200
    DAY1 = 3600 * 24
    DAY2 = 3600 * 48
    WEEK = DAY1 * 7

    if finishing_datetime.month - 1 in [1, 3, 5, 7, 8, 10, 12]:
        MONTH = DAY1 * 31
    elif finishing_datetime.month - 1 in [4, 6, 9, 11]:
        MONTH = DAY1 * 30
    else:
        if finishing_datetime.year % 4 == 2:
            MONTH = DAY1 * 29
        else:
            MONTH = DAY1 * 28

    ####

    REMINDER_TIMEDELTA_CHOICES = (
        (MIN15, '15 min'), (MIN30, '30 min'), (MIN45, '45 min'), (HOUR1, '1 hour'), (
            HOUR1_5, '1.5 hour'), (HOUR2, '2 hours'), (DAY1, '1 day'), (DAY2, '2 days'), (
            MONTH, 'month')
    )
    reminder = models.BooleanField(default=False)
    reminder_timedelta = models.IntegerField(choices=REMINDER_TIMEDELTA_CHOICES, default=MIN15)

    # time_for_work = models.DurationField(default=0)
    # finished_time = models.DateTimeField(default=datetime.now)
    # alarm_clock_task = models.DateTimeField('Alarm clock:', default=datetime.now)
    # check_task = models.BooleanField(default=False)

    def get_timeleft(self):
        return self.finishing_datetime - self.creation_datetime

    def get_reminder_timedate(self):
        #if self.reminder = True
        return self.finishing_datetime - timedelta(seconds=self.reminder_timedelta)



class Contact(models.Model):
    name_c = models.CharField(max_length=20)
    forename_c = models.CharField(max_length=20)
    phone_num = models.IntegerField(default=0)
    birthday_c = models.DateField(default=date.today)