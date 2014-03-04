from django.db import models

# Create your models here.
class Employer(models.Model):
    name = models.CharField(max_length=30)
    linkedin_id = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

'''
class Job(models.Model):
    employer = models.ForeignKey(Employer)
    linkedin_id = models.IntegerField(default=0)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    close_date = models.DateTimeField('date closed')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.position
'''