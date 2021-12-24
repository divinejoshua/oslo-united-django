from django.shortcuts import render
from .forms import CreateEmailList

# Create your views here.

def home_view(request):

	context = {}

	if request.POST:
		form = CreateEmailList(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"

	return render(request, "main/index.html", context)
