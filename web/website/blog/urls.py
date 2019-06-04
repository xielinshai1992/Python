from django.conf.urls import url
from .import views
from blog.models import Entry
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
app_name = 'blog'

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = [
    # 主页 http://127.0.0.1/blog/
    url(r'^$', views.index, name='blog_index'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='blog_detail'),
    #http://127.0.0.1/blog/category/2
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category,name='blog_category'),
    url(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives,name='blog_archives'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag,name='blog_tag'),
    url(r'^search/$', views.search,name='blog_search'),
    url(r'^reply/(?P<comment_id>\d+)/$', views.reply, name='comment_reply'),
    url(r'^sitemap.xml$', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]