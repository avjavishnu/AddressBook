from django.shortcuts import render
from address.models import AddressBook
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'address/homepage.html')


def aaddr(request):
    return render(request, 'address/addaddress.html')


def done(request):
    return render(request, 'address/success.html')


def add_address_method(request):
    a = request.POST['sname']
    b = request.POST['smobile']
    c = request.POST['sstreet']
    d = request.POST['scity']
    query = AddressBook(Name_Student=a, Mobile_Number=b, Street=c, City=d)
    query.save()
    return HttpResponseRedirect(reverse('w_added'))


def get_data(request):
    query = AddressBook.objects.all()
    context = {'query': query}
    return render(request, 'address/display.html', context)


def update_address(request, id):
    query = AddressBook.objects.get(id=id)
    context = {'query': query}
    return render(request, 'address/update.html', context)


def update_record(request, id):
    a=request.POST['sname']
    b=request.POST['smobile']
    c=request.POST['sstreet']
    d=request.POST['scity']
    query = AddressBook.objects.get(id=id)
    query.Name_Student=a
    query.Mobile_Number=b
    query.Street=c
    query.City=d
    query.save()
    return HttpResponseRedirect(reverse('w_displayD'))


def delete_record(request, _id):
    query = AddressBook.objects.get(id=_id)
    query.delete()
    return HttpResponseRedirect(reverse('w_displayD'))