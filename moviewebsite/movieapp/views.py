from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.utils.text import slugify

from . forms import MovieForm
from . models import Category,Movie
# Create your views here.

def allMovieCat(request,c_slug=None):
    c_page = None
    products_list = None
    if c_slug!=None:
        c_page = get_object_or_404(Category,slug = c_slug)
        products_list = Movie.objects.all().filter(category = c_page)
    else:
        products_list = Movie.objects.all()
    paginator = Paginator(products_list,8)
    try:
        page = int(request.GET.get('page','1'))
    except :
        page = 1
    try:
        products = paginator.page(page)
    except ( EmptyPage,InvalidPage ):
        products = paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'products':products})

def movieDetail(request,c_slug,product_slug):
    try:
        product = Movie.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,'movie.html',{'product':product})

def movieadd(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    if request.method =='POST':
        username = request.POST['username']
        moviename = request.POST['name']
        category_id = request.POST.get('category')
        category = Category.objects.get(pk=category_id)
        actors = request.POST['actors']
        desc = request.POST['description']
        img = request.FILES['image']
        date = request.POST['date']
        ytlink = request.POST['ytlink']
        slug = slugify(moviename)

        mov = Movie(username=username,name=moviename,description=desc,category=category,image=img,release_date=date,actors=actors,ytlink=ytlink,slug=slug)
        mov.save()
        return redirect('/')
    return render(request,'addmovie.html',context)

def delete(request, c_slug, product_slug):
    movie = get_object_or_404(Movie, category__slug=c_slug, slug=product_slug)
    movie.delete()
    return redirect('movieapp:home')
    # return render(request, 'movie.html')

def update(request,product_slug,c_slug):
    movie = get_object_or_404(Movie, category__slug=c_slug, slug=product_slug)
    form = MovieForm(request.POST or None, request.FILES,instance=movie)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('movieapp:home')
    return render(request,'edit.html',{'form':form,'movie':movie})

def search(request):
    products = None
    query = None

    try:
        if 'q' in request.GET:
            query = request.GET.get('q')
            if query != "":
                products = Movie.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query))
    except Exception as e:
        # Handle the exception (e.g., log it or render an error page)
        print(f"An error occurred: {e}")
        products = None  # Set products to None to indicate an error

    return render(request, 'search.html', {'query': query, 'products': products})


def profile(request):
    if request.method =='POST':
        user = request.user
        user.username = request.POST.get('username','')
        user.first_name = request.POST.get('f_name', '')
        user.last_name = request.POST.get('l_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        return redirect('movieapp:home')
    return render(request,'profile.html')