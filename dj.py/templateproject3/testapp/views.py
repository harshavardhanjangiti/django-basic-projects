from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    msg="helo very very good"
    h=int(date.strftime('%H'))
    if h<12:
        msg=msg+"goodmorning"
    elif h<16:
        msg=msg+"good afternoon"
    elif h<21:
        msg=msg+"good evening"
    else:
        msg=msg+"good night"
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'testapp/wish.html',context=my_dict)
