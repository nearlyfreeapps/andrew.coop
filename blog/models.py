from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Blog Article'
        verbose_name_plural = 'Blog Articles'
        ordering = ('-date',)

    def get_absolute_url(self):
        return '/portfolio/blog/%s' % self.id

    def __unicode__(self):
        return self.title + ' - ' + unicode(self.date)

