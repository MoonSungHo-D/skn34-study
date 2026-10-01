from django.shortcuts import render
from datetime import datetime

context = {
    'name': 'Django',
    'age': 13,
    'num': 1,
    'hobby': ['coding', 'reading', 'traveling'],
    'today': datetime.now(),
    'is_authenticated': False,
    'fruits': ['apple', 'banana', 'cherry'],
    'users': [
        {'id': 1234, 'name': 'Alice', 'age': 24, 'married': True},
        {'id': 2345, 'name': 'Bob', 'age': 34, 'married': False},
        {'id': 3456, 'name': 'Charlie', 'age': 25, 'married': True},
    ],
    # 'users': [],
}

# /app/ 요청시 index 템플릿 반환하는 View 함수
def index(request):
    return render(request, 'app/index.html')

# /01_variables_filters/ 요청시 템플릿 변수 활용하는 페이지를 반환하는 View 함수
def _01_variables_filters(request):
    context['today'] = datetime.now()  # 현재 시간 갱신
    return render(request, 'app/01_variables_filters.html', context)

def _02_tags(request):
    return render(request, 'app/02_tags.html', context)

def _03_layout(request):
    return render(request, 'app/03_layout.html')

def _04_static_files(request):
    return render(request, 'app/04_static_files.html')

def _05_urls(request):
    return render(request, 'app/05_urls.html')

def articles_detail(request, id):
    # print(f'{id = }')
    return render(request, 'app/05_urls.html')

def articles_category(request, category, id):
    # print(f'{category = }, {id = }')
    return render(request, 'app/05_urls.html')

def search(request):
    # print(request.GET.urlencode())
    # print(request.GET)
    q = request.GET.getlist('q', [])
    lang = request.GET.get('lang', '')
    # print(f'{q = }, {lang = }')
    return render(request, 'app/05_urls.html', {'q': q, 'lang': lang})

def _06_bootstrap(request):
    return render(request, 'app/06_bootstrap.html')

def _06_my_bootstrap(request):
    return render(request, 'app/06_my_bootstrap.html')

