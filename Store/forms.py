
import datetime
from django import forms
from .models import StoreCategories, AuthGroup, StoreProduct, UserModel

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password']
        widgets = {'password': forms.PasswordInput()}

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'password', 'address', 'postalcode', 'city', 'country', 'phone']
        widgets = {'password': forms.PasswordInput()}

class NewProductForm(forms.ModelForm):
    class Meta:
        model = StoreProduct
        exclude = ['created_at']  # Exclude the non-editable field
        widgets = {'description': forms.Textarea, 'updated_at': forms.HiddenInput()}

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = StoreCategories
        fields = ['name', 'description', 'image', 'created_at', 'updated_at']
        widgets = {'description': forms.Textarea, 'created_at': forms.HiddenInput(), 'updated_at': forms.HiddenInput()}
