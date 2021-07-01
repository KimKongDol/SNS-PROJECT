from django.shortcuts import render
#django.shortcuts에 있는 render라는 함수를 사용한다. 이것은 html파일을 전송하는 함수이다.

# Create your views here.

def index(request): #함수이름은 index이고 request는 '요청시'를 의미하는 인자이다.
    return render(request, 'index.html') #함수 실행시 html파일을 부른다.
