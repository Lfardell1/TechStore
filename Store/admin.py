from django.contrib import admin


from .models import  StoreCategories, StoreProduct, UserModel, AuthGroup




admin.site.register(UserModel)

admin.site.register(StoreCategories)  

admin.site.register(StoreProduct)

admin.site.register(AuthGroup)

