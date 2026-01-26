from django.shortcuts import render, redirect
from post.forms import PostForm, UserRegistrationForm, SearchForm
from post.models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, "index.html")


def post_list(request):
    allPost = Post.objects.all().order_by("-created_at")
    search_form = SearchForm()
    query = request.GET.get('q', '')
    
    if query:
        allPost = allPost.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
        )
    
    return render(request, "post_list.html", {
        "allPost": allPost,
        "search_form": search_form,
        "query": query
    })


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "post_form.html", {"form": form})


@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm(instance=post)
    return render(request, "post_form.html", {"form": form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "post_delete_confirm.html", {"post": post})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})









