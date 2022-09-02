from django.shortcuts import render, redirect
from . models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import User
from . forms import PostCreateForm, PostEditForm

def index(request):
    blog = Post.objects.all()
    return render(request, 'index.html',{'blog':blog})

def posts(request, pk):
    blog = Post.objects.get(id=pk)
    return render(request, 'posts.html',{'blog':blog})


def user_blog(request):
    form = PostCreateForm()

    if request.method == 'POST':
        form=PostCreateForm(request.POST)
        if form.is_valid():
            heading=form.cleaned_data['heading']
            body=form.cleaned_data['body']       
            current_user=request.user
        
            if len(heading)>0:
                if len(body)>0:
                    new_post = Post.objects.create(heading=heading, body=body, user=current_user )
                    new_post.save()

                    return redirect('/')
                else:
                    messages.info(request, 'please type a body')
                    return redirect('user_blog')
            else:
                messages.info(request, 'please type a heading')
                return redirect('user_blog')
        else:
            messages.info('unsuccessful :(')
            return redirect('user_blog')
    
    else:
        return render(request, 'user_blog.html', {'form':form})

def search(request):
    if request.method=='POST':
        search=request.POST['search']
        blog = Post.objects.filter(heading__contains=search)
        return render(request, 'search.html', {'search':search, 'blog':blog})
    else:
        return render(request, 'search.html',{})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            password2=request.POST['password2']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']

        
            if len(email)>0:
                if len(username)>0:
                    if len(password)>0:
                        if password==password2:
                            if User.objects.filter(email=email).exists():
                                messages.info(request, 'Email already exists')
                                return redirect('signup')
                            elif User.objects.filter(username=username).exists():
                                messages.info(request, 'username already exists')
                                return redirect('signup')
                            else:
                                user = User.objects.create_user(username=username, password=password, email=email)
                                user.save()
                                return redirect('login')
                        else:
                                messages.info(request, 'passwords do not match')
                                return redirect('signup')
                    else:
                        messages.info(request, 'password field required')
                        return redirect('signup')
                else:
                    messages.info(request, 'username field required')
                    return redirect('signup')
                
            else:
                messages.info(request, 'email field required')
                return redirect('signup')
        else:
            return render(request, 'signup.html')



def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']

            if len(email)>0:
                if len(username)>0:
                    if len(password)>0:
                        user = auth.authenticate(username=username, password=password)

                        if user is None:
                            messages.info(request,'User not found')
                            return redirect('login')
                        else:
                            auth.login(request, user)
                            return redirect('/')
                    else:
                        messages.info(request, 'password field required')
                        return redirect('login')
                else:
                    messages.info(request, 'username field required')
                    return redirect('login')
            else:
                messages.info(request, 'email field required')
                return redirect('login')
        else:
            return render(request, 'login.html')

def changes(request):
    if request.user.is_authenticated:
        changes_view = Post.objects.filter(user=request.user)
        return render(request, 'changes_view.html', {'view':changes_view})
    else:
        messages.info(request,'Please login')
        return redirect('login')

def user_posts(request, pk):
    blog = Post.objects.get(id=pk)
    return render(request, 'user_posts.html',{'blog':blog})

def edit_blog(request, pk):
    if request.user.is_authenticated:
        blog=Post.objects.get(id=pk)
        form = PostEditForm(instance=blog)
        if request.method =='POST':       
            form = PostEditForm(request.POST, instance=blog)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                messages.info(request, 'invalid form')
                return redirect('edit_blog')
        else:
            return render(request, 'edit_blog.html', {'form':form})
    else:
        messages.info(request,'Please login')
        return redirect('login')

def delete_blog(request, pk):
    if request.user.is_authenticated:
        blog = Post.objects.get(id=pk)
        blog.delete()
        messages.success(request, 'blog deleted successfully')
        return redirect('/')
    else:
        messages.info(request,'Please login')
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('login')




