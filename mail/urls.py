
from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'mailhandler', views.MailHandlerViewSet)
router.register(r'record', views.RecordViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls))
)
