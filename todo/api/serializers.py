from rest_framework import serializers
from todo.models import TodoModel



class TodoModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = "__all__"