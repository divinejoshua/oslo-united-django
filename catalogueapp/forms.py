from django import forms

from .models import Catelogues, Products 


class CreateCatelogueForm(forms.ModelForm):

	class Meta:
		model = Catelogues
		fields = ['title', 'body', 'thumb']


class CreateProductForm(forms.ModelForm):

	class Meta:
		model = Products
		fields = ['title', 'price', 'thumb']



class UpdateCatelogueForm(forms.ModelForm):

	class Meta:
		model = Catelogues
		fields = ['title', 'body', 'thumb']

	def save(self, commit=True):
		catelogue = self.instance
		catelogue.title = self.cleaned_data['title']
		catelogue.price = self.cleaned_data['body']

		if self.cleaned_data['thumb']:
			catelogue.thumb = self.cleaned_data['thumb']

		if commit:
			catelogue.save()
		return catelogue

class UpdateProductForm(forms.ModelForm):

	class Meta:
		model = Products
		fields = ['title', 'price', 'thumb']

	def save(self, commit=True):
		product = self.instance
		product.title = self.cleaned_data['title']
		product.price = self.cleaned_data['price']

		if self.cleaned_data['thumb']:
			product.thumb = self.cleaned_data['thumb']

		if commit:
			product.save()
		return product

