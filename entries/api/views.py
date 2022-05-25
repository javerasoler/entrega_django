from rest_framework.views import APIView
from rest_framework.response import Response

from entries.models import Entry
from entries.api.serializers import EntrySerializer


class EntryListAPI(APIView):
    def get(self, request):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        # entry = Entry(datetime=request.data.get("datetime"), 
        #               amount=request.data.get("amount"),
        #               concept=request.data.get("concept"))
        
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        
        return Response(status=400, data=serializer.errors)