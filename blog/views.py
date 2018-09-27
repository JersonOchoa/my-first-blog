from django.shortcuts import render
from django.utils import timezone
from .models import Post

def listar(request):
    articulos = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'articulos', articulos})
# Create your views here.
