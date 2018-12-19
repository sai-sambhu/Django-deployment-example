from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')
def other(request):
    return render(request,'basic_app/other.html')
def relative(request):
    my_dict={'b':'basic_app:other'}
    return render(request,'basic_app/relative_url_template.html',context=my_dict)