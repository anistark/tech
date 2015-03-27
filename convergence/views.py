from django.shortcuts import render

# Create your views here.
def home(request):
	context = {'title':'Convergence'}
	return render(request,'convergence/index.html',context)

