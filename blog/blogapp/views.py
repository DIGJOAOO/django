from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .models import Like, Post


ORDENES = {
    'recientes': '-id',
    'antiguos': 'id',
}


def index(request):
    orden = request.GET.get('orden', 'recientes')
    if orden not in ORDENES:
        orden = 'recientes'
    posts = list(
        Post.objects.prefetch_related('fotos')
        .annotate(total_likes=Count('likes'))
        .order_by(ORDENES[orden])
    )
    session_key = request.session.session_key
    liked_ids = set()
    if session_key:
        liked_ids = set(
            Like.objects.filter(session_key=session_key).values_list('post_id', flat=True)
        )
    for post in posts:
        post.liked = post.pk in liked_ids
    return render(request, 'blogapp/blog.html', {'posts': posts, 'orden': orden})


@require_POST
def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    existente = Like.objects.filter(post=post, session_key=session_key)
    if existente.exists():
        existente.delete()
    else:
        Like.objects.create(post=post, session_key=session_key)
    destino = request.POST.get('next', '')
    if not url_has_allowed_host_and_scheme(destino, allowed_hosts={request.get_host()}):
        destino = '/blog/'
    return redirect(f"{destino}#post-{post.pk}")
