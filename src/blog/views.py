from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost

def blog_post_detail_view(request, slug):
    print("DJANGO SAYS", request.method, request.path, request.user)
    #queryset = BlogPost.objects.filter(slug=slug)
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'object_list': qs }
    return render(request, template_name, context)

@staff_member_required
@login_required
def blog_post_create_view(request):
    #obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form }
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {"object": obj }
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {"object": obj }
    return render(request, template_name, context)