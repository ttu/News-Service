# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Feed(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    url = models.CharField(max_length=765, db_column='Url') # Field name made lowercase.
    class Meta:
        db_table = u'Feed'

class News(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    title = models.CharField(max_length=3000, db_column='Title') # Field name made lowercase.
    url = models.CharField(max_length=6000, db_column='Url') # Field name made lowercase.
    feedid = models.IntegerField(db_column='FeedID') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    class Meta:
        db_table = u'News'

class Stats(models.Model):
    lastupdated = models.DateTimeField(null=True, db_column='LastUpdated', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Stats'

class Tempmatch(models.Model):
    userid_1 = models.IntegerField(primary_key=True, db_column='UserID_1') # Field name made lowercase.
    userid_2 = models.IntegerField(db_column='UserID_2') # Field name made lowercase.
    value = models.IntegerField(db_column='Value') # Field name made lowercase.
    class Meta:
        db_table = u'TempMatch'

class Test(models.Model):
    u1 = models.IntegerField(primary_key=True, db_column='U1') # Field name made lowercase.
    u2 = models.IntegerField(primary_key=True, db_column='U2') # Field name made lowercase.
    value = models.IntegerField(db_column='Value') # Field name made lowercase.
    class Meta:
        db_table = u'Test'

class User(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'User'

class Usermatch(models.Model):
    userid_1 = models.IntegerField(primary_key=True, db_column='UserID_1') # Field name made lowercase.
    userid_2 = models.IntegerField(db_column='UserID_2') # Field name made lowercase.
    matches = models.IntegerField(db_column='Matches') # Field name made lowercase.
    misses = models.IntegerField(db_column='Misses') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    class Meta:
        db_table = u'UserMatch'

class Vote(models.Model):
    userid = models.IntegerField(primary_key=True, db_column='UserID') # Field name made lowercase.
    newsid = models.IntegerField(db_column='NewsID') # Field name made lowercase.
    rate = models.IntegerField(db_column='Rate') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    class Meta:
        db_table = u'Vote'

