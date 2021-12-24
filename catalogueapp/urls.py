from django.urls import path, include

app_name = 'catelogueapp'


from . import views
urlpatterns = [
    path('', views.category_view, name="category"),
    path('product/<slug>', views.product_view, name="product"),
    path('add/category', views.addCategory_view, name="addCategory"),
    path('add/product/<slug>', views.addProduct_view, name="addProduct"),
    path('edit/product/<id>', views.edit_product_view, name="editProduct"),
    path('edit/category/<id>', views.edit_catelogue_view, name="editCategory"),
    path('purchase/<id>', views.purchase_view, name="makePurchase"),
]


