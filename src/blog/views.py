from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import BlogPost

def blog_post_detail_page(request, post_id):
    #queryset = BlogPost.objects.filter(slug=slug)
    obj = get_object_or_404(BlogPost, id=id)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)