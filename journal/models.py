from django.db import models

from core.models import Institution, Author, User

class Article(models.Model):
    
    title = models.CharField(max_length = 256, help_text = 'Title of the article')
    
    # example format for authorsXML
    # <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    # <author>
    #   <index>7</index>
    #   <position>Head of Surgery at Bleepbloop U.</position>
    # </author>
    authorsXML = models.TextField(help_text = 'Store author index' +
                                  'and the position of that author in XML')
    
    institution = models.ForeignKey(Institution)
    
    abstract = models.TextField(help_text = 'The abstract, in HTML format')
    
    mainText = models.TextField(help_text = 'The main text, in a uniform and' +
                                'easily parsed HTML format')
    
    procedure = models.TextField(help_text = 'The procedure, in a uniform and' +
                                 'easily parsed HTML format')
    
    videoContents = models.TextField(help_text = 'Store the labels and times' +
                                     'for each section in the video')
    
    comments = models.TextField(help_text = 'Store the comments in XML')
    
    annotations = models.TextField(help_text = 'Stores annotations for viewing by the author ' +
                                   'and editorial team in XML', default = '')
    
    publicationDate = models.DateTimeField(help_text = 'The time of publication')
    
    revisions = models.TextField(help_text = 'Store the author, publication time,' +
                                 'and filWename for each change in XML')
    
    PUBLICATION_STATUSES = (
        (0, 'published'),
        (1, 'preprint'),
        (2, 'in production'),
        (3, 'coming soon')
    )
    publicationStatus = models.IntegerField(choices = PUBLICATION_STATUSES, default = 0,
                                            help_text = 'Status of publication')
    
    SUBJECTS = (
        (0, 'General Surgery'),
        (1, 'Fundamentals'),
        (2, 'Orthopedics'),
        (3, 'Orthopedic Trauma'),
        (4, 'Vascular Surgery'),
        (5, 'Ophthalmalogy'),
        (6, 'Neurosurgery')
    )
    subject = models.IntegerField(choices = SUBJECTS, default = 0,
                                  help_text = 'Subject of articles')
    
    tags = models.CharField(max_length = 256)

    articleID = models.IntegerField(default = 0)
    
    volume = models.IntegerField(default = 2014)
    
    issue = models.IntegerField(default = 0)
    
    videoURL = models.CharField(max_length = 128, default = '')
    
    
    
    
    def __str__(self):
        return 'Article: ' + self.title
    
    class Meta:
        permissions = (
            ('can_publish', 'can publish artcles, reserved for editorial staff'),
            ('can_annotate', 'can annotate any article'),
            ('can_view_production', 'can view articles in production'),
            ('can_annotate_own', 'can annotate own article (for authors)'),
            ('can_view_own', 'can view own article (for authors)'),
        )