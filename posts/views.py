from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Post, Image
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q
from itertools import chain

# Create your views here.
####################     index/ READ     ###########################
def list(request):
   #1.
    # followings = request.user.followings.all()
    # posts = Post.objects.filter(
    #     Q(user__in=followings) | Q(user=request.user.id)
    #     ).order_by('-pk')
    # 역순으로 객체 가지고 오기
    #2
    followings = request.user.followings.all()
    chain_followings = chain(followings, [request.user])
    posts = Post.objects.filter(user__in=chain_followings).order_by('-pk')
    
    # posts = Post.objects.filter(user__in=request.user.followings.all()).order_by('-pk') # 내가 팔로잉하고 있는 모든 유저 - 일치하는 유저가 작성한 포스트를 필터링 , 내가 팔로잉하고 있는 유저가 작성한거
    comment_form = CommentForm()					# 1
    context = {'posts':posts,
        'comment_form': comment_form,			# 2
    }
    return render(request, 'posts/list.html', context)


####################     CREATE     ###########################
@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST) # 이미지는 파일즈에 들어감 request.FILES
        if post_form.is_valid():
            post = post_form.save(commit=False)			# 1
            post.user = request.user			# 2
            post.save()				# 3

            # post = post_form.save() # 게시글 내용 처리 끝
            # 이미지가 여러개이기 때문에 for 문을 돌려야하고, file 하나하나 돌면서 검증해야 함
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False) # 추가로 더 받을 값을 기다림 커밋 안하고
                    image.post = post
                    image.save()
            return redirect('posts:list')
      # GET요청(혹은 다른 메서드)이면 기본 폼을 생성한다
    else: # 그냥 페이지에 들어갔을 때
        post_form = PostForm() # form 많아지면 복잡해지니까 이름을 달리해줘야 함
        image_form = ImageForm()
        # 포스트 요청이고, 유효성 문제에 있어서 문제가 있는 데이터일때
    context = {'post_form': post_form,
               'image_form':image_form,
        
    }
    return render(request, 'posts/form.html', context) # 같은 폼 쓸 예정 update 랑
    
    


####################     UPDATE     ###########################   
@login_required
def update(request, post_pk): # 어떤 글을 수정할지 결정해야하니까 pk 필요함 변수명 post_pk

    post = get_object_or_404(Post,pk=post_pk)
    if request.method == 'POST':
         post_form = PostForm(request.POST, instance=post) # 수정된 값 가져오고, 이전 값도
         
         if post.user != request.user:
            return redirect('posts:list')
         
         
         
         if post_form.is_valid():
             post_form.save()
             return redirect('posts:list')
    else:
        post_form = PostForm(instance=post) # 이렇게 값을 채워넣어야 값이 존재
    context = {'post_form':post_form,}
    return render(request, 'posts/form.html', context)
    
    
    
    
####################     DELETE     ###########################
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':
        post.delete()
    return redirect('posts:list')
    
    
    
    
################ comment #########
@login_required
@require_POST
def comment_create(request, post_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_pk
        comment.save()
    return redirect('posts:list')
    
    
@login_required
@require_POST
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('posts:list')
    comment.delete()
    return redirect('posts:list')
    
    
########################## like  ####################################
@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    user = request.user
    # 이미 해당 유저가 like 를 누른 상태면 좋아요 취소(해당 유저가 like_users 컬럼에 존재하면 해당 유저를 지움)
    if post.like_users.filter(pk=user.pk).exists():
        post.like_users.remove(user)
    # 안 눌렀다면 좋아요
    else:
        post.like_users.add(user)
    return redirect('posts:list')

## 전체글 페이지
@login_required
def explore(request):
    # posts = Post.objects.order_by('-pk')
    posts = Post.objects.exclude(user=request.user).order_by('-pk')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
        
    }
    return render(request, 'posts/explore.html', context)
    