from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404


from entries.models import Entry
from entries.api.serializers import EntrySerializer



class EntryListAPI(APIView):
    def get(self, request):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        
        return Response(status=400, data=serializer.errors)
    
    
class EntryDetailAPI(APIView):

    def get_entry(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        return entry

    def get(self, request, pk):

        entry = self.get_entry(request, pk)

        serializer = EntrySerializer(instance=entry)
        return Response(serializer.data)


    def put(self, request, pk):

        entry = get_object_or_404(Entry, pk=pk)

        serializer = EntrySerializer(instance=entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


    def delete(self, request, pk):

        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)