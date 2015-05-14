from django.shortcuts import render

# Create your views here.
def home(request):
	context = {'title':'AniTech'}
	return render(request,'index.html',context)

