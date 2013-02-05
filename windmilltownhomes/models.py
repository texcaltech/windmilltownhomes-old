from django.db import models

# Model for text blocks
class TextBlock(models.Model):
    key = models.CharField(max_length=20)
    text = models.TextField()
    
    def  __unicode__(self):
        return '%s: %s' % (self.key, self.text[:20])