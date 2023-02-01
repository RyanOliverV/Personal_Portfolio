from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

#function based view that defines how likes are viewed on the blog posts
def LikeView (request, pk):
    #get_object is a built-in function that raises a 404 error if the post doesn't exist
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)])) #redirects user to the blog post that was liked (using primary key)

#class based views that show the posts created in the database on the blog html page
class PostListView(ListView):
    model = Post #defines what database model to retrieve data from
    template_name = 'blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3 #limits the number of posts on a page

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    #this function assigns the author of the blog post to the user, then validates the form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #this function creates a test to check whether the current logged in user is the author of the post
    #only allows users that passes the test to update a post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#LoginRequiredMixin redirects all requests by non-authenticated users to the login page
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    #this function creates a test to check whether the current logged in user is the author of the post
    #only allows users that passes the test to delete a post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            fromEmail = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            form.save()
            #Django provides a mail sending interface with wrappers called send_mail
            #https://docs.djangoproject.com/en/4.1/topics/email/
            send_mail(subject, message, fromEmail, ['ryanoliverv@gmail.com'])
            #messages.success is used to display flash messages
            messages.success(request, f'Your message has been sent')
            return redirect('home')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

class CommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ('comment',)

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk'] #assigns pk so the comment is made on the correct post
        form.instance.user = self.request.user  #comment is attached to the user that created it
        return super().form_valid(form)