from django.shortcuts import render
#If not using forms, import the model only
#from apptwo.models import User
from apptwo.forms import NewUserForm
# Create your views here.

# The view needs to know the file name and path
def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    #this view gets the model, transforms it into a dictionary, then displays it
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Form invalid')

    return render(request,'apptwo/users.html',{'form':form})
