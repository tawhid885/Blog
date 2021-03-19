from django.shortcuts import render,redirect, get_object_or_404
from .models import Post,Comment,Category
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import PostForm,CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DeleteView ,CreateView,DetailView,UpdateView,DeleteView
from django.http import HttpResponseRedirect


# Create your views here.
class Postlistview(ListView):
    model = Post
    template_name = 'blog/allpost.html'
    ordering = ['-post_date']
    # paginate_by = 5
    # context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

    def get_context_data(self, *args, **kwargs):
        cat_menu =Category.objects.all() 
        context =super(Postlistview, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        return context   

# def Postlistview(request):
#     post = Post.objects.all()
#     context={'post':post}
#     return render(request,'blog/allpost.html',context)
class DetailPost(DetailView):
    model =Post

    def get_context_data(self, *args, **kwargs):
        cat_menu =Category.objects.all() 
        stuff =get_object_or_404(Post,id =self.kwargs['pk'])
        total_likes =stuff.total_likes()
        liked=False

        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context =super(DetailPost, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        context['liked']=liked
        context['total_likes']=total_likes
        return context 

class CreatePost(LoginRequiredMixin,CreateView):
    model =Post
    # fields =['title','content']
    form_class= PostForm
    template_name='blog/post_create.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateCategory(LoginRequiredMixin,CreateView):
    model =Category
    # fields =['title','content']
    form_class= CategoryForm
    template_name='blog/cat_create.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin,UpdateView):
    model =Post
    fields =['title','content']
    template_name='blog/post_update.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class DeletePost(LoginRequiredMixin,DeleteView):
    model =Post
    success_url="/"

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentView(ListView):
    model = Post
    template_name = 'blog/allpost.html'
    context_object_name = 'comments'
    
class CreateComment(CreateView):
    model = Comment 
    fields =['name','body']
    template_name='blog/comment_create.html'
    context_object_name = 'comments'
    success_url ='new'


    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def CatPost(request, cats):
    catpost=Post.objects.filter(category=cats.replace('-',' '))
    context={'catpost':catpost,'cat':cats.title().replace('-',' ')}
    return render(request,'blog/catpost.html',context)

def LikeView(request,pk):
    post =get_object_or_404(Post, id =request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('post-detail', args=[int(pk)]))





