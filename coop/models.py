from django.db import models

class Organization(models.Model):
    short_name = models.CharField(max_length = 25)
    name = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    term_number = models.PositiveIntegerField()
    blurb = models.TextField()

    class Meta:
        ordering = ('-term_number',)

    def get_absolute_url(self):
        return '/portfolio/' + self.short_name

    def __unicode__(self):
        return self.name + ': Work term #' + str(self.term_number)

    def get_month_duration(self):
        #All dates within same year
        return self.end_date.month + 1 - self.start_date.month

