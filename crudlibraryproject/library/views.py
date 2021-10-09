from django.shortcuts import render,redirect,HttpResponse
from .models import libraryinfo
from .forms import libraryinfoForm


def library_list(request):
	books = libraryinfo.objects.all()
	return render(request,"details.html",{'books':books})

def library_add(request):
	if request.method =='POST':
		form = libraryinfoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("library_list")
	else:
		form = libraryinfoForm()
	return render(request,"add_info.html",{"form":form})


def library_edit(request,id):
	books = libraryinfo.objects.get(id=id)
	form = libraryinfoForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect("/")
	return render(request,"edit_info.html",{'books':books})


def library_update(request,id):
	books = libraryinfo.objects.get(id=id)
	return render(request,"edit_info.html",{"books":books})


def library_trash(request,id):
	books = libraryinfo.objects.get(pk=id)
	books.delete()
	return redirect("/")