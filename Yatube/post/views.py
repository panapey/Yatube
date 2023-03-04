from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)

# yatube
# ├── yatube/
# ├── posts/
# ├── templates
# │    ├── posts
# │    │   ├── group_list.html
# │    │   └── index.html
# │    ├── includes
# │    │   ├── header.html
# │    │   └── footer.html
# │    └──  base.html
# └──  manage.py
