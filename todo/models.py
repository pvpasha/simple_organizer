from django.db import models
from datetime import date, datetime, timedelta


class ShortTask(models.Model):
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
    finishing_datetime = models.DateTimeField(default=datetime.now)
    ####
    MIN15 = 900
    MIN30 = 1800
    MIN45 = 2700
    HOUR1 = 3600
    HOUR1_5 = 5400
    HOUR2 = 7200
    DAY1 = 3600 * 24
    DAY2 = 3600 * 48
    WEEK = DAY1 * 7
    MONTH = DAY1 * 31
    #
    # if finishing_datetime.month - 1 in [1, 3, 5, 7, 8, 10, 12]:
    #     MONTH = DAY1 * 31
    # elif finishing_datetime.month - 1 in [4, 6, 9, 11]:
    #     MONTH = DAY1 * 30
    # else:
    #     if finishing_datetime.year % 4 == 2:
    #         MONTH = DAY1 * 29
    #     else:
    #         MONTH = DAY1 * 28
    ####

    REMINDER_TIMEDELTA_CHOICES = (
        (MIN15, '15 min'), (MIN30, '30 min'), (MIN45, '45 min'), (HOUR1, '1 hour'), (
            HOUR1_5, '1.5 hour'), (HOUR2, '2 hours'), (DAY1, '1 day'), (DAY2, '2 days')
    )
    reminder = models.BooleanField(default=False)
    reminder_timedelta = models.IntegerField(choices=REMINDER_TIMEDELTA_CHOICES, default=MIN15)

    def get_timeleft(self):
        return self.finishing_datetime - self.creation_datetime

    def get_reminder_timedate(self):
        #if self.reminder = True
        return self.finishing_datetime - timedelta(seconds=self.reminder_timedelta)

    PER0 = 0
    PER25 = 25
    PER50 = 50
    PER75 = 75
    PER100 = 100

    TASK_PERCENT_CHOICES = (
        (PER0, '0%'), (PER25, '25%'), (PER50, '50%'), (PER75, '75%'), (
            PER100, '100%')
    )

    percent = models.IntegerField(choices=TASK_PERCENT_CHOICES, default=PER0)

    def get_percent(self):
        return self.percent
    # # TODO CATEGORY ------
    # CAT01 = Work
    # CAT02 = Family
    # CAT03 = Home
    # CAT04 = Sport
    # CAT05 = Other
    #
    # TASK_PERCENT_CHOICES = (
    #     (CAT01, 'Work'), (CAT02, 'Family'), (CAT03, 'Home'), (CAT04, 'Sport'), (
    #         CAT05, 'Other')
    # )
    #
    # category = models.IntegerField(choices=CATEGORY_CHOICES, default=CAT03)


class Event(models.Model):
    owner = models.EmailField()
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)

    # CAT01 = Work
    # CAT02 = Family
    # CAT03 = Home
    # CAT04 = Sport
    # CAT05 = Other
    #
    # TASK_PERCENT_CHOICES = (
    #     (CAT01, 'Work'), (CAT02, 'Family'), (CAT03, 'Home'), (CAT04, 'Sport'), (
    #         CAT05, 'Other')
    # )
    #
    # category = models.IntegerField(choices=CATEGORY_CHOICES, default=CAT03)
    event_datetime = models.DateTimeField(default=datetime.now)

    # E_DAY = event_datetime.day + 1
    # E_WEEK = event_datetime.day + 7
    # E_MONTH = event_datetime.day + 30 # EVERY Month its not good
    # E_YEAR = event_datetime.year + 1
    #
    # REPEAT_EVERY_CHOICES = (
    #     (E_DAY, 'every day'), (E_WEEK, 'every week'), (E_MONTH, 'every month'), (
    #         E_YEAR, 'every year')
    # )

    repeat = models.BooleanField(default=False)
    #repeat_every = models.IntegerField(choices=REPEAT_EVERY_CHOICES, default=None)

    # def get_repeate_time(self):
    #     return self.repeat_every

class Diary(models.Model):
    owner = models.EmailField()
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True) #auto_now_add=True

class Budget(models.Model):
    owner = models.EmailField()
    cash = models.FloatField(null=True, blank=True, default=0)

    class Currency(models.Model):
        USD = 1
        EUR = 1
        UAH = 1
        CURRENCY_CHOICES = ((USD, '$'), (EUR, 'E'), (UAH, 'hrn'))
        currency = models.IntegerField(choices=CURRENCY_CHOICES, default=USD)

    income = models.FloatField(null=True, blank=True, default=0)
    outcome = models.FloatField(null=True, blank=True, default=0)

    def get_income(self):
        return self.cash + self.income

    def get_outcome(self):
        return self.cash - self.outcome


class Contact(models.Model):
    name = models.CharField(max_length=20)
    forename = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    birthday = models.DateField(default=date.today)
    add_reminder = models.BooleanField(default=False) #add birthday to reminder

class PasswordOrganizer(models.Model):
    pass