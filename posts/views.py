from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return JsonResponse({
                'status': 'success',
                'post': {
                    'id': post.id,
                    'content': post.content,
                    'author': post.author.username,
                    'created_at': post.created_at.strftime('%b %d, %Y %H:%M'),
                    'likes_count': post.like_count(),
                    'location': post.location or '',
                    'image_url': post.image.url if post.image else None,
                }
            })
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)

@login_required
@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({
        'status': 'success',
        'liked': liked,
        'likes_count': post.like_count()
    })

@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        return JsonResponse({
            'status': 'success',
            'comment': {
                'id': comment.id,
                'content': comment.content,
                'author': comment.author.username,
                'created_at': comment.created_at.strftime('%b %d, %Y %H:%M'),
            }
        })
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@login_required
def get_post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.select_related('author').all()
    return JsonResponse({
        'status': 'success',
        'comments': [{
            'id': comment.id,
            'content': comment.content,
            'author': comment.author.username,
            'created_at': comment.created_at.strftime('%b %d, %Y %H:%M'),
        } for comment in comments]
    })
