# coding: utf-8

from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets')
    code = models.TextField()
    language = models.CharField(u'计算机语言', max_length=20)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        formatter = HtmlFormatter(linenos='table', full=True)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
