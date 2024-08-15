from django.shortcuts import render,redirect
from rest_framework.permissions import AllowAny
from . models import *
from rest_framework import generics
from . serializers import *
from . forms import *
from django.contrib import messages


# Create your views here.
class DestCreate(generics.ListCreateAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer
    permission_classes = [AllowAny]


class DestDetails(generics.RetrieveAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer

class DestUpdate(generics.RetrieveUpdateAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer

class DestDelete(generics.DestroyAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer


def dest_create(request):
    if request.method == 'POST':
        form=DestForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                api_url="http://127.0.0.1:8000/create/"
                data=form.cleaned_data
                print(data)

                response =requests.post(api_url,data=data,files={'image':request.FILES['image']})
                if response.status_code == 400:
                    messages.success(request,"destination created succesfully")
                    return redirect('/')
                else:
                    messages.error(request,'error')
            except request.RequestException as e:
                messages.error(request,f'error during api request{str(e)}')
        else:
            messages.error(request,'Form is not valid')
    else:
        form=DestForm()

    return render(request,"destcreate.html",{'form':form})

def list_dest(request):
    dest = Destinations.objects.all()
    return render(request,'index.html',{'dest':dest})



def update_dest(request,id):
    if request.method == 'POST':
        Placename = request.POST['Placename']
        Weather = request.POST['Weather']
        State = request.POST['State']
        district = request.POST['district']
        print('Image Url',request.FILES.get('image'))
        description = request.POST['description']
        api_url = f"http://127.0.0.1:8000/update/{id}/"
        data = {
            "Title" : Placename,
            "Relesedate" : Weather,
            "Actors" : State,
            "Reviews" : district,
            "description" : description
        }
        files = {'image' : request.FILES.get("image")}
        response = requests.put(api_url,data=data,files=files)
        if response.status_code == 200:
            messages.success(request,'Recipee updated')
            return redirect('/')
        else:
            messages.error(request,"error submitting data to the Rest api")
    return render(request,'destinationupdate.html')

def dest_fetch(request,id):
    dests = Destinations.objects.get(id=id)
    return render(request,'dest_fetch.html',{'dests':dests})

def dest_delete(request,id):
    api_url = f"http://127.0.0.1:8000/delete/{id}/"
    response = requests.delete(api_url)
    if response.status_code == 200:
        print(f'Item with id {id} has been deleted')

    else:
        print(f'Failed to delete item {response.status_code}')
    return redirect('/')







