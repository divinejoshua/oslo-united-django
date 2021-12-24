from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import CreateCatelogueForm, CreateProductForm, UpdateCatelogueForm, UpdateProductForm
from django.shortcuts import render
from operator import attrgetter



from .models import Catelogues, Products
from django.db.models import Q

from decouple import config



# catelogue_PER_PAGE = 1


# Create your views here.

# List of all categories 
def category_view(request):
	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	catelogue = sorted(get_blog_queryset(query), key=attrgetter('date'), reverse=True)
	context['catelogue'] = catelogue

	return render(request, "catalogueapp/category.html", context)


def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = Catelogues.objects.filter(
				Q(title__icontains=q) | 
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))	

# Add category view 
def addCategory_view(request):
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('/')

	form = CreateCatelogueForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':     
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			form = CreateCatelogueForm()
			return redirect("/catelogue")
		else:
			context['error'] = "Error submitting form"
		
	context['form'] = form
	return render(request, "catalogueapp/addcategory.html", context)




# Inside a category_view
def product_view(request, slug):
	context = {}
	catelogue = Catelogues.objects.filter(slug=slug).first()

	product = Products.objects.filter(catelogue=catelogue)

	context['product'] = product
	context['catelogue'] = catelogue
	phoneNumber = config('PhoneNumber')
	context['link'] =  request.scheme+'://'+request.META['HTTP_HOST']+"/catelogue/purchase/"
	context['whatsapp']= "https://api.whatsapp.com/send/?phone=%2B"+phoneNumber+"&text=Hi,+I+want+to+purchase+this+product+"


	return render(request, "catalogueapp/product.html", context)


def purchase_view(request, id):
	context = {}
	product = Products.objects.filter(id=id).first()
	context['product'] = product

	return render(request, "catalogueapp/purchase.html", context)



# Add Product to category 
def addProduct_view(request, slug):
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('/')

	form = CreateProductForm(request.POST or None, request.FILES or None)
	catelogue = get_object_or_404(Catelogues, slug=slug)

	if request.method == 'POST':     
		if form.is_valid():
			obj = form.save(commit=False)
			obj.catelogue = catelogue
			obj.save()
			form = CreateProductForm()
			return redirect("/catelogue/product/"+slug)
		else:
			context['error'] = "Error submitting form"
		
	context['form'] = form
	context['catelogue'] = catelogue
	return render(request, "catalogueapp/addProduct.html", context)


def edit_product_view(request, id):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("/")

	product = get_object_or_404(Products, id=id)


	if request.POST:
		if request.POST.get("delete"):
			product.delete()
			return redirect("/catelogue/")

			

		form = UpdateProductForm(request.POST or None, request.FILES or None, instance=product)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			product = obj

	form = UpdateProductForm(
			initial = {
					"title": product.title,
					"price": product.price,
					"thumb": product.thumb,
			}
		)

	context['form'] = form
	return render(request, 'catalogueapp/editProduct.html', context)





def edit_catelogue_view(request, id):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("/")

	catelogue = get_object_or_404(Catelogues, slug=id)


	if request.POST:
		if request.POST.get("delete"):
			catelogue.delete()
			return redirect("/catelogue/")

			

		form = UpdateCatelogueForm(request.POST or None, request.FILES or None, instance=catelogue)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			catelogue = obj

	form = UpdateCatelogueForm(
			initial = {
					"title": catelogue.title,
					"body": catelogue.body,
					"thumb": catelogue.thumb,
			}
		)

	context['form'] = form
	return render(request, 'catalogueapp/editCategory.html', context)