
from rest_framework import serializers
import models

class MailHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MailHandler


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Record
