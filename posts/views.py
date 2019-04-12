from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Post, Image
from .forms import PostForm, ImageForm

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
        post_form = PostForm(request.POST) # 이미지는 파일즈에 들어감 request.FILES
        if post_form.is_valid():
            post = post_form.save() # 게시글 내용 처리 끝
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
    
    