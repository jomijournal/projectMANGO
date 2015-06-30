from django.db import models

class Article(models.Model):
    # example format for authorsXML
    # <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    # <author>
    #   <index>7</index>
    #   <position>Head of Surgery at Bleepbloop U.</position>
    # </author>
    authorsXML = models.TextField(help_text = 'Store author index' +
                                  'and the position of that author in XML')
    
    institution = models.ForeignKey(Institution)
    
    abstract = models.TextField()
    
    mainText = models.TextField()
    
    procedure = models.TextField()
    
    videoContents = models.TextField(help_text = 'Store the labels and times' +
                                     'for each section in the video')
    