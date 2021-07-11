from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Reklam


class LatestPostsFeed(Feed):
    name = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Reklam.objects.all()[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return truncatewords(item.text, 30)
