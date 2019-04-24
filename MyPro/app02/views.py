from django.shortcuts import render,HttpResponse
import datetime

class Animal():
    def __init__(self,name,age,local):
        self.name = name
        self.age = age
        self.local = local
    def paoxiao(self):
        return "houhou..."



def every_prod(request):
    return render(request,"app02/proc.html")


def show_time(request):
    time = datetime.datetime.now()
    timer = time.strftime("%Y-%m-%d %H:%M:%S")
    dic = {"alex":["男",25,"深圳"],"peiqi":["男",29,"北京"],"eva":["女",26,"北京"]}
    alex = Animal("alex",25,"深圳")
    peiqi = Animal("peiqi",26,"北京")
    eva = Animal("eva",23,"nanjing")
    obj_lst = [alex,peiqi,eva]
    return render(request, "app02/bianliang.html", {"timer":timer, "dic":dic, "obj_lst":obj_lst})


def show_guolv(request):
    timer = datetime.datetime.now()
    booklst = ["列宁格勒","斯大林格勒","泰勒斯威夫特","托马斯杨","基森斯塔森","郭达斯坦森"]
    booklst1 = []
    numb = 86
    dic = {"alex": ["男", 25, "深圳"], "peiqi": ["男", 29, "北京"], "eva": ["女", 26, "北京"]}
    file_size = 89526089
    shici = "我有一个梦想,就是希望有一天能有世界和平,没有战争,没有纷争,在苍茫的大海上,有一只海燕,狂风卷积着乌云"
    shici1 = "i have a dream is that hope the world peace"
    tag = "<h3> 我有一个梦想 </h3>"

    return render(request,"app02/guolv.html",{"timer":timer,"booklst":booklst,"booklst1":booklst1,
                  "numb":numb,"file_size":file_size,"shici1":shici1,"tag":tag,"dic":dic})














