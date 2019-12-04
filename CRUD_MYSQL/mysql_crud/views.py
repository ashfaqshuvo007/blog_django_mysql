from django.shortcuts import render,redirect,get_object_or_404
#Post Form for our model
from . forms import PostForm
#import our post Model
from . models import Post

#import Django's list and detail view to override for our model
from django.views.generic import ListView,DetailView


# Create your views here.

#home View for posts. Posts are displayed in a list
class IndexView(ListView):
    template_name='mysql_crud/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.all()

#details View for Posts. Details view
class PostDetailView(DetailView):
    model=Post
    template_name= 'mysql_crud/post-detail.html'


#New post view(Create new Post)
def postView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = PostForm()
    return render(request,'mysql_crud/post.html',{'form':form})

#EDIT a post
def edit(request,pk,template_name='mysql_crud/edit.html'):
    post = get_object_or_404(Post,pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,template_name,{'form':form})

#DELETE a post
def delete(request,pk,template_name='mysql_crud/confirm_delete.html'):
    post= get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request,template_name,{'object':post})

