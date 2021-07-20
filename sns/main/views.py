from django.shortcuts import render, redirect, get_object_or_404 #django.shortcuts에 있는 render라는 함수를 사용한다. 이것은 html파일을 전송하는 함수이다.
#렌더는 템플릿을 부르고 리다이렉트는 URL로 부름
from .models import Blog, Comment #이 폴더의 models에서 Blog테이블을 들고와서 뿌릴 예정이다.
from django.utils import timezone

# Create your views here.

def index(request): #함수이름은 index이고 request는 '요청시'를 의미하는 인자이다.
    return render(request, 'index.html') #함수 실행시 html파일을 부른다.

def place(request):
    return render(request, 'place.html')

def message(request, id):
    blog = get_object_or_404(Blog, pk = id)
    all_comments = blog.comments.all().order_by('-created_at') #-가 붙으면 댓글을 최신순으로
    return render(request, 'message.html', {'blog':blog, 'comments':all_comments})

def messageList(request):
    blogs = Blog.objects.all() #blogs라는 변수에 Blog의 모든 객체를 저장한다.
    return render(request, 'messageList.html', {'blogs':blogs})

def writeM(request):
    return render(request, 'writeM.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.user
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.image = request.FILES.get('image')
    new_blog.save()
    return redirect('message',new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'blog' : edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.user
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('message', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('messageList')

def create_comment(request, blog_id):
    if request.method == "POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, blog=blog)
    return redirect('message', blog_id)




