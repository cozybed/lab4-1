from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import models
import random


def index(request):
    latest_book_list = models.books.objects.all()
    length = len(latest_book_list)
    latest_book_list = latest_book_list[length - 5:length]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/index.html', context)


@csrf_exempt
def search(request):
    try:
        post_author = models.author.objects.get(name=request.POST['Author'])
        latest_book_list = models.books.objects.filter(author=post_author.authorID)
    except:
        latest_book_list = []
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/search.html', context)


def login(request):
    for i in range(10):
        pass
        # author = models.author.objects.get(name = "SANDY")
        # newbook = models.books()
        # newbook.author = random.choice(['001', '002', '003', '004'])
        # newbook.ISBN = random.randint(100000000, 999999999)
        # newbook.price = random.randint(10, 100)
        # newbook.publishDate = "1994-08-18"
        # newbook.publisher = random.choice(["HIT", "BUA", "PKU", "FDU", "THU"])
        # newbook.Title = "goodBook" + str(random.randint(10, 999))
        # newbook.save()

    return render(request, 'books/login.html')


def single(request):
    isbn = request.GET['ISBN']
    error_Response = render(request, 'books/error.html')
    try:
        latest_book_list = models.books.objects.get(ISBN=isbn)
    except:
        return error_Response
    latest_book_list = [latest_book_list]
    single_book = latest_book_list[0]
    try:
        single_author = models.author.objects.get(authorID=single_book.author)
    except:
        single_author = models.author()

    context = {'latest_book_list': latest_book_list, 'single_book': single_book, 'single_author':single_author}
    return render(request, 'books/singleBook.html', context)


∂


@csrf_exempt
def saveNewAuthor(request):
    error_Response = render(request, 'books/error.html')
    getAuthorID = request.POST["authorID"]
    successResponse = render(request, "books/success.html")
    try:
        newAuthor = models.author.objects.get(authorID=getAuthorID)
    except:
        return error_Response
    newAuthor.name = request.POST["name"]
    newAuthor.country = request.POST["country"]
    newAuthor.authorID = request.POST["authorID"]
    newAuthor.age = request.POST["age"]
    newAuthor.save()
    return successResponse


def delete(request):
    isbn = request.GET['ISBN']
    try:
        latest_book_list = models.books.objects.get(ISBN=isbn)
        latest_book_list.delete()
    except:
        return render(request, 'books/index.html')

    return render(request, 'books/index.html')


@csrf_exempt
def save(request):
    post = request.POST
    error_Response = render(request, 'books/error.html')
    success_Response = render(request, 'books/success.html')
    post_ISBN = post['ISBN']
    if_new_author = 0
    try:
        post_author = models.author.objects.get(name=post['Author'])
    except:
        post_author = models.author()
        post_author.name = post["Author"]
        post_author.age = "0"
        post_author.authorID = str(len(models.author.objects.all()))
        post_author.country = "China"
        post_author.save()
        if_new_author = 1
    post_Title = post['Title']
    post_Publisher = post['publisher']
    post_Date = post['publishDate']
    post_Price = post['price']
    newBook = models.books()
    newBook.author = post_author.authorID
    newBook.ISBN = post_ISBN
    newBook.Title = post_Title
    newBook.publishDate = post_Date
    newBook.publisher = post_Publisher
    newBook.price = post_Price
    try:
        newBook.save()
    except:
        return error_Response
    if if_new_author:
        context = {'new_author': post_author}
        return render(request, "books/add_author.html", context)
    return success_Response

# Create your views here.
