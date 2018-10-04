from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def listar(request):
    articulos = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'articulos': articulos})

def detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle.html', {'post': post})
