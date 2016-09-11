
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippet', views.SnippetViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/user/$', views.UserList.as_view()),
    url(r'^api/user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)
