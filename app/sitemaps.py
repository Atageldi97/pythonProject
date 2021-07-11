from django.contrib.sitemaps import Sitemap
from .models import Reklam


class ReklamSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def itemss(self):
        return Reklam.objects.all()


