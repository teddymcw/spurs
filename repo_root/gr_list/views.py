from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    groc_list = Post.objects.all()
    context = {'groc_list': groc_list}
    return render(request, 'gr_list/main.html', context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('gr_list.views.post_list')
    else:
        form = PostForm()
    return render(request, 'gr_list/post_edit.html', {'form': form})

def spurs_blog(request):
    #spurs_list = None
    return render(request, 'spurs/main.html', )