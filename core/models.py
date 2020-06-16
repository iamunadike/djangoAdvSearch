from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Author(models.Model):
    name = models.CharField(_("Author Name"), max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_("Category"), max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

class Journal(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    author = models.ForeignKey("core.Author", verbose_name=_("Author"), on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    published = models.DateTimeField(_("Publish Date"))
    views = models.IntegerField(_("Views"), default=0)
    reviewed = models.BooleanField(_("Reviewed"), default=False)

    def __str__(self):
        return self.title
