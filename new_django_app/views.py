from django.shortcuts import render

# Create your views here.

posts=[
{
'author': 'Corey MS',
'title': 'Blog post 1',
'content' : 'First post content',
'date_posted' : 'August 21,2018'
},
{
'author': 'Jane Doe',
'title': 'Blog post 2',
'content' : 'Second post content',
'date_posted' : 'August 22,2018'
}
]


def home(request):
    context={
    'posts': posts
    }
    return render(request,'new_django_app/home.html',context)


def about(request):
    return render(request,'new_django_app/about.html',{'title': 'About Blog'})
