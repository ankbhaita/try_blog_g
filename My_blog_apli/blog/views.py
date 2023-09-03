from django.shortcuts import render,HttpResponseRedirect
from blog.forms import SignUpForm,loginForm,PostForm,PostForm_status
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post

def home(request):
	post=Post.objects.all()
	return render(request,'blog/home.html',{'post':post})

def about(request):
	return render(request,'blog/about.html')

def contact(request):
	return render(request,'blog/contact.html')

def dashboard(request):
	speci_email=["asdfg@gmail.com","guria.bharti22@gmail.com","chotumotu@gmail.com"]
	if request.user.is_authenticated:
		if request.user.email in speci_email:
			post=Post.objects.all()
		else:
			post=Post.objects.filter(author=request.user)	
		return render(request,'blog/dashboard.html',{'post':post})
	else:
		return HttpResponseRedirect('/login/')
		
	

def signup(request):
	if request.method=="POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			messages.success(request,'Congratulation!! you have become an author')
			form.save()
	else:
		form = SignUpForm()

			
	return render(request,'blog/signup.html',{'form':form})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
	
	

def ulogin(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = loginForm(request=request,data=request.POST)
			if form.is_valid():
				print("inside valid")
				uemail=form.cleaned_data['username']
				upass=form.cleaned_data['password']
				user=authenticate(email=uemail,password=upass)
				if user is not None:
					login(request,user)
					messages.success(request,'logged in Successfully!!')
					return HttpResponseRedirect('/dashboard/')
				else:
					print("print in else part")
					form=loginForm()
					messages.error(request, "Invalid Credentials")
					return render(request, 'blog/home.html')
		else:
			form=loginForm()
		return render(request,'blog/login.html',{'form':form})
	else:
		return HttpResponseRedirect('/dashboard/')
#add new post				
def add_post(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form=PostForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data['title']
				desc=form.cleaned_data['desc']
				author=request.user
				post=Post(author=author,desc=desc,title=title)
				post.save()
				form=PostForm()
		else:
			form=PostForm()				
		return render(request,'blog/addpost.html',{'form':form})
	else:
		return HttpResponseRedirect('/login/')

#update Post
def update_post(request,id):
	speci_email=["asdfg@gmail.com","guria.bharti22@gmail.com","chotumotu@gmail.com"]
	if request.user.is_authenticated:
		if request.user.email in speci_email:
			if request.method == 'POST':
				pi=Post.objects.get(pk=id)
				form = PostForm_status(request.POST,instance=pi)
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/dashboard/')
			else:
				pi=Post.objects.get(pk=id)
				form=PostForm_status(instance=pi)							
		return render(request,'blog/updatepost.html',{'form':form})
	else:
		return HttpResponseRedirect('/login/')


def update__post(request,id):
	if request.user.is_authenticated:		
		if request.method == 'POST':
			pi=Post.objects.get(pk=id)
			form = PostForm(request.POST,instance=pi)
			if form.is_valid():
				form.save()
				form=PostForm()
		else:
			pi=Post.objects.get(pk=id)
			form=PostForm(instance=pi)
		return render(request,'blog/updatepost.html',{'form':form})
	else:
		return HttpResponseRedirect('/login/')
def update___post(request,id):
	speci_email=["asdfg@gmail.com","guria.bharti22@gmail.com","chotumotu@gmail.com"]
	if request.user.email in speci_email:
		return update_post(request,id)
	else:
		return update__post(request,id)

		





def delete_post(request,id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			pi=Post.objects.get(pk=id)
			pi.delete()
		return render(request,'blog/updatepost.html')
	else:
		return HttpResponseRedirect('/login/')		


