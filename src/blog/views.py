from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import BlogPost

def blog_post_detail_page(request, slug):
    print("DJANGO SAYS", request.method, request.path, request.user)
    #queryset = BlogPost.objects.filter(slug=slug)
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = {'object_list': qs }
    return render(request, template_name, context)

def blog_post_create_view(request):
    #obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_create.html'
    context = {'form': None }
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj }
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj }
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_delete_view.html'
    context = {"object": obj }
    return render(request, template_name, context)