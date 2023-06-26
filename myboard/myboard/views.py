from django.shortcuts import render, redirect
from django.utils import timezone
from .models import MyBoard


def index(request):
    dto = MyBoard.objects.all()
    return render(request, 'index.html', {'list': dto})


def insert(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']
        mydate = timezone.now()

        result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=mydate)

        if result:
            return redirect('index')
        else:  # 안 만들어졌으면 다시 인서트 페이지 reload
            return redirect('insert')
    else:
        return redirect('index')


def detail(request, id):
    dto = MyBoard.objects.get(id=id)
    return render(request, 'detail.html', {'list': dto})


def update(request, id):
    if request.method == 'GET':
        dto = MyBoard.objects.get(id=id)
        return render(request, 'update.html', {'dto': dto})
    elif request.method == 'POST':
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']
        mydate = timezone.now()

        result = MyBoard.objects.filter(id=id).update(mytitle=mytitle, mycontent=mycontent, mydate=mydate)

        if result:
            return redirect(f'/detail/{id}/')
        else:
            return redirect(f'/update/{id}/')
    else:
        return redirect('index')


def delete(request, id):
    delBoard = MyBoard.objects.filter(id=id)
    result = delBoard.delete()
    # delete() 경과로 리턴되는 값은 tuple이다 (삭제된 갯수, dict(삭제된 객체))
    # [0] 이니까 0번지에 있는 삭제된 갯수를 가져온다

    if result[0]:
        return redirect('index')
    else:
        return redirect(f'detail/{id}')