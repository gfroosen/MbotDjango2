from rest_framework import serializers

from portal.models import Robot


class RobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = ('robot', 'task_number')
