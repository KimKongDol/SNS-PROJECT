from django.shortcuts import render, get_object_or_404, redirect
from main.models import Blog, Comment
from django.utils import timezone
# from users.models import User

# Create your views here.
def mypage(request):
    user = request.user
    blogs = Blog.objects.filter(writer=user)#로그인한 유저이름과 글 작성자 이름이 동일한 글 필터링
    return render(request,'users/mypage.html', {'blogs':blogs})

def create_comment(request, blog_id):
    if request.method == "POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, blog=blog)
    return redirect('message', blog_id)