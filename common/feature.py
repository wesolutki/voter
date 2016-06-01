from common.models import *
from common.localization import verbose_names
from common.admin import AksonBaseAdmin


@verbose_names
class Feature(models.Model):
    name = models.CharField(max_length=200)
    description = DescriptionField(blank=True, null=True)

    def short_description(self):
        max_length = 255
        if len(self.description) > max_length:
            return self.description[:max_length] + '...'
        return self.description

    def __str__(self):
        if self.short_description() == "":
            return self.name
        return u"{0} - {1}".format(self.name, self.short_description())

    class Meta:
        abstract = True
        ordering = ('name',)


class FeatureCardAdmin(AksonBaseAdmin):
    list_per_page = 1000
    list_display = ('name', 'description')
