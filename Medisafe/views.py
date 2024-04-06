from django.http import JsonResponse
from django.shortcuts import render
from Medisafe.models import Account, Emergency, Pharmacy2
from django.db.models import Q
import Medisafe

# Create your views here.

def Registration(request):
    nm=request.GET.get("Patient_name")
    age=request.GET.get("DOB")
    add=request.GET.get("Address")
    Contact=request.GET.get('Contact_No')
    data=Account.objects.filter(Patient_name=nm)
    if len(data)>0:
        return JsonResponse("this Patient_details already exist",safe=False)
    account=Account(Patient_name=nm,DOB=age,Address=add,Contact_No=Contact)
    account.save()
    return JsonResponse("You are registered now",safe=False)


def emergency(request):
    data=Account.objects.filter(Patient_name=request.GET.get("nm"))
    add=str(data[0].Address)
    data1=Emergency.objects.filter(Address=add)
    if len(data1)==0:
        d={"Ambulance not available in :add"}
        return JsonResponse(d)
    return JsonResponse("Ambulance Coming Soon", safe=False)


def Patient_diseases(request):
    p_diseases=request.GET.get('Diseases2')
    p_medicine=request.GET.get('Medicine2')
    data=Pharmacy2.objects.filter(Diseases2=p_diseases)
    if len(data)>=0:
        return JsonResponse("Your Medicine Arrived Soon",safe=False)
    pd=Pharmacy2(Diseases2=p_diseases,Medicine2=p_medicine)
    pd.save()
    return JsonResponse("You are Normal",safe=False)



