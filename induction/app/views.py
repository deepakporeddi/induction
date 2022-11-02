from django.shortcuts import render
from .forms import *
from .serializers import *
from rest_framework import viewsets
from .models import *
from django.core.cache import cache
from django.http import HttpResponse,JsonResponse
#from  . import handle_uploaded_file
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,RemoteUserAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from rest_framework.generics import *
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from time import sleep
from django.db.models import F, Prefetch
from django.db import transaction,connection
from django_seed import seeder

def home_view(request):
    context={}
    #context['vehicle']=vehicle
    nums=car.objects.all()
    context['nums'] = nums
    return render(request,'homepage.html',context)

def truck_view(request):
    context={}
    form=Truckform(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']=Truckform()
    return render(request,'list.html',context)
def car_view(request):
    context={}
    form=carform(request.POST or None,request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data['manufacturer'])
        print(form.cleaned_data['model_name'])

        form.save()

    context['form']=carform()
    return render(request,'list.html',context)
#----------------CSRF-----------------------------
@csrf_protect
def vehicle_view(request):
    context={}
    form=Vehicleform(request.POST,request.FILES)
    if form.is_valid():
        form.save()

    context['form']=Vehicleform()
    return render(request,'list.html',context)

def student_view(request):
    context={}
    form=studentform(request.POST)
    if form.is_valid():
        form.save()
    context['form']=studentform()
    return render(request,'list.html',context)
@transaction.atomic
def payment_view(request):
    context={}
    form=paymentform(request.POST,request.FILES)
    if form.is_valid():
        x=form.cleaned_data['name']
        y=form.cleaned_data['paid_to']
        z=int(form.cleaned_data['amount'])
        try:
            with transaction.atomic():
                payer=customer.objects.get(name=x)
                payer = customer.objects.get(name=x)
                payer.amount -= z
                payer.save()
                paid_to = customer.objects.get(name=y)
                paid_to = customer.objects.get(name=y)
                paid_to.amount += z
                paid_to.save()
        except:
            return HttpResponse('invalid credentials')

    context['form']=paymentform()
    return render(request,'list.html',context)
class vehcilesinfo(viewsets.ModelViewSet):
    queryset = vehicle.objects.all()
    serializer_class = vehser
    search_fields = ['model_name', 'manufacturer']
    #for locally giving authenication
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]


class carsinfo(viewsets.ModelViewSet):
    queryset = car.objects.all()
    serializer_class = carser
class trucksinfo(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = truser
    filter_fields=('wheel_count','max_goods_weight')

class studentsinfo(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = stuser
    filter_fields=('id','first_name')

class paymentinfo(viewsets.ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = payser

class trsdemo(ListCreateAPIView):
    def get(self,request,*args,**kwargs):
        with transaction.atomic():
            all_cust = customer.objects.all()
            all_veh=vehicle.objects.all()
            cust=trsser(all_cust,many=True)
            veh=vehser(all_veh,many=True)

            res={
                'cust':cust.data,
                'veh':veh.data,
            }
        return Response(res)
'''def myobjects(request,model_name):
    queryset=vehicle.objects.values().filter(model_name__exact=model_name)
    serializers=vehser(queryset)
    return JsonResponse(serializers.data)'''

class objcount(viewsets.ModelViewSet):
    queryset = vehicle.objects.all()
    serializer_class = vehser



def http_call_sync():
    for num in range(1,5):
        sleep(1)
        print(num)

def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")

def file_handler(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = car(file=file)
        obj.save()

        # return the path of the file
        # this value will be kept in the JSON data
        return JsonResponse({'value': obj.file.name})

#------------------------------------ORM--------------------------------------------------------------------------------
#---------------------------------EXERCISES----------------------------------------------------------------------------
@api_view(['GET'])
def Scenario2(request):
    queryset = Student.objects.annotate(new_id=F('id') + 100).values('new_id')
    return Response(queryset)

class Scenario1(RetrieveAPIView,UpdateAPIView):
    serializer_class = stuser

    def get_queryset(self):
        if self.request.method =='GET':
            queryset=Student.objects.all()
            id=self.request.GET.get('id',None)
            name=self.request.GET.get('name',None)
            if name is not None:
                queryset = Student.objects.filter(first_name__iendswith=name)
            #print(len(connection.queries))
            print(queryset.values('department'))
            return queryset

class Scenario5(ListCreateAPIView):
    serializer_class = stuser

    def post(self, request, *args, **kwargs):
        if self.request.method=='POST':
            #data=self.request.data.get('lis')
            data=request.POST.get('lis')
            data=data[1:-1]
            data=list(data.split(','))
            for i in data:
                print(i)
            qs=Student.objects.filter(first_name__in=data).count()
            print(qs)
            return Response(qs)
@csrf_exempt
def update(request):
    for k,v in request.POST.items():
        print(v)
    return HttpResponse('printed')

class Scenario6(ListAPIView):   #------------------Scenario7------------Scenario8---------
    serializer_class = stuser

    def get_queryset(self):
        qs=Student.objects.all()
        for i in qs:
            print(i.id)
            print(i.department)
            print(i.accesscard)
            print(i.clubs)
        print(len(connection.queries))
        print('------------------------------------------------------------------------------------------------')
        qs2=Student.objects.all()
        qs2=stuser(qs2,many=True)
        print(qs2)
        print('------------------------------------------------------------------------------------------------')
        qs3 = Student.objects.all().values_list()
        print(qs3)
        print('------------------------------------------------------------------------------------------------')
        qs4 = Student.objects.select_related('department').order_by('first_name')
        print(qs4)
        print('------------------------------------------------------------------------------------------------')
        qs5=Student.objects.prefetch_related(Prefetch('clubs', queryset=club.objects.all()))
        print(qs5)
        return qs

class Scenario9(ListCreateAPIView,UpdateAPIView):
    #serializer_class = deptser

    def post(self, request, *args, **kwargs):
        if self.request.method=='POST':
            id=request.data.get('id',None)
            name=request.data.get('name')
            if id is not None: #-----If id key is defined for each of the JSON objects then assume that there exists a matching entry in the database with that "id"
                qs=dept.objects.get(id=id)
                qs.branch=name
                qs.save()
                return Response(data="updated object successfully")
            else:
                qs=dept(id=id,branch=name)
                qs.save()
                return Response(data="Created object successfully")

class Scenario11(RetrieveAPIView,UpdateAPIView):
    serializer_class = vehser
    #queryset = vehicle.objects.all()
    def get_queryset(self):
        if self.request.method =='GET':
            queryset = vehicle.objects.all()
            model_name = self.request.GET.get('model_name', None)
            if model_name is not None:
                queryset = queryset.filter(model_name__iexact=model_name)
            #http_call_sync()
            return queryset











