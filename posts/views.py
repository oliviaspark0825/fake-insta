from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
####################     index/ READ     ###########################
def list(request):
    # 역순으로 객체 가지고 오기
    posts = get_list_or_404(Post.objects.order_by('-pk'))
    context = {'posts':posts,}
    return render(request, 'posts/list.html', context)


####################     CREATE     ###########################
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES) # 이미지는 파일즈에 들어감
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
      # GET요청(혹은 다른 메서드)이면 기본 폼을 생성한다
    else: # 그냥 페이지에 들어갔을 때
        post_form = PostForm() # form 많아지면 복잡해지니까 이름을 달리해줘야 함
        # 포스트 요청이고, 유효성 문제에 있어서 문제가 있는 데이터일때
    context = {'post_form': post_form, }
    return render(request, 'posts/form.html', context) # 같은 폼 쓸 예정 update 랑
    
    


####################     UPDATE     ###########################    
def update(request, post_pk): # 어떤 글을 수정할지 결정해야하니까 pk 필요함 변수명 post_pk

    post = get_object_or_404(Post,pk=post_pk)
    if request.method == 'POST':
         post_form = PostForm(request.POST, instance=post) # 수정된 값 가져오고, 이전 값도
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
    if request.method == 'POST':
        post.delete()
    return redirect('posts:list')
    
    