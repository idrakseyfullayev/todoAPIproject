from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from todo.models import TodoModel
from todo.api.serializers import (
    TodoModelListSerializer
)



class TodoModelListAPIview(ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelListSerializer

class TodoModelCreateAPIView(CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelListSerializer

class TodoModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = TodoModel.objects.all()
    lookup_field = "id"
    serializer_class = TodoModelListSerializer

class TodoModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = TodoModel.objects.all()
    lookup_field = "id"
    serializer_class = TodoModelListSerializer
    
        

