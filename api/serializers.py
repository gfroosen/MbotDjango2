from rest_framework import serializers

from portal.models import Robot


class RobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = ('robot','task_number', 'task1_speed', 'task1_duration', 'task1_mode', 'task1_command')
