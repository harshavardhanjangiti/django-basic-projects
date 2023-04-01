from django.shortcuts import render
import datetime

# Create your views here.

# def wish(request):
#      date = datetime.datetime.now()
#      my_dict = {'insert_date': date}
#      return render(request,'testapp/wish.html',context=my_dict)
#TO DISPLAY DATE ,TIME AND STUDENT INFO
def wish(request):
     date=datetime.datetime.now()
     name="sunny"
     marks=98
     rollno=101
     my_dict={'insert_date':date,'name':name,'marks':marks,'rollno':rollno}
     return render(request,'testapp/wish.html',context=my_dict)



