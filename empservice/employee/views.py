from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import Emps,SignUpSer
from .models import Emp
from rest_framework import authentication 
from rest_framework import permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class SignUp(ViewSet):
    def create(self,request,*args,**kwargs):
        ser = SignUpSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"user created"})
        return Response(data=ser.errors)

class Empview(ModelViewSet):
    serializer_class=Emps
    queryset=Emp.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Emp.objects.filter(id=id).delete()
        return Response({"msg":"Deleted"})