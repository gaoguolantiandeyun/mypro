from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse




def days(request,year,month,day):
    print(request.GET)
    return HttpResponse(f"{year}年{month}月{day}日的文章")


def days2(request,month,year):
    return HttpResponse(f"{year}年{month}月的文章")


def test(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    data = {"name": name, "email": email}
    print(data)
    return HttpResponse("ook")



def login(request):
    return render(request, "app01/login.html")


def auth(request):
    # print("request>>>",request)
    print("-----------------")
    # print(request.POST)
    # print(request.GET)
    # print(request.path)
    # print(request.FILES)
    # print(request.FILES.get("wenjian").name)
    # print(request.FILES.get("wenjian").size)
    # print(request.FILES.get("wenjian").chunks())
    # obj = request.FILES.get("wenjian")
    # with open("files","ab")as f:
    #     for i in obj.chunks():
    #         f.write(i)
    print(request.body)
    info = {"name":"大河马","passwd":"123"}
    if request.POST.get("user") == info["name"] and request.POST.get("psd") == info["passwd"]:
        _url = reverse("zhuye")
        return redirect(_url)
    return HttpResponse("Error...")


def index(request):
    return render(request,"app01/index.html")









