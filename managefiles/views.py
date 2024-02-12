from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import FileSerializer
from .models import File

# Create your views here.

class FileAPIView(generics.ListAPIView): ## just a list of items as json
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileAPICreate(generics.CreateAPIView):
    # queryset = File.objects.all()
    serializer_class = FileSerializer

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)