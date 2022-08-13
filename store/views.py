from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Store,Review
from .tests import TestReviewSerializer,TestStoreSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class TestStoreListAPIView(APIView):
    def get(self,request):
        qs = Store.objects.all()
        serializer = TestStoreSerializer(qs,many = True)
        return Response(serializer.data)
    def post(selfrequest):
        serializer = TestStoreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = 201)
        return Response(serializer.errors,status = 400)

class TestStoreDetailAPIView(APIView):
    def get_object(self,pk):
        return Store.objects.get(pk=pk)

    def get(self, request, pk):
        store = self.get_object(pk)
        serializer = TestStoreSerializer(store)
        return Response(serializer.data)
    
    def put(self, request, pk):
        store = self.get_object(pk)
        serializer = TestStoreSerializer(store)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk):
        store = self.get_object(pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestReviewAPIView(APIView):
    def get(self,request):
        qs = Review.objects.all()
        serializer = TestReviewSerializer(qs,many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = TestReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = 201)
        return Response(serializer.errors,status = 400)