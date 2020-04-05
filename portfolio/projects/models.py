from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.title
