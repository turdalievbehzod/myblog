from django.shortcuts import render

# Create your views here.

posts = [
    {"id": 1, "title": "First Post", "text": "This is first post"},
    {"id": 2, "title": "Second Post", "text": "This is second post"},
    {"id": 3, "title": "Third Post", "text": "This is third post"},
]

def index(request):
    return render(request, 'blog/index.html')

def posts_view(request):
    return render(request, 'blog/posts.html', {"posts": posts})

def detail(request, id):
    post = None
    for p in posts:
        if p["id"] == id:
            post = p
            break

    return render(request, 'blog/detail.html', {"post": post})
