from django.shortcuts import render

# Create your views here.
def home(request):
	context = {'title':'Solitary Pursuits'}
	return render(request,'techblog/index.html',context)

