# coding: utf-8

from rest_framework import viewsets
import models, serializers

# Create your views here.
class MailHandlerViewSet(viewsets.ModelViewSet):
    queryset = models.MailHandler.objects.all()
    serializer_class = serializers.MailHandlerSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer
