from django import template
from ..models import StoreCategories, StoreProduct, UserModel
register = template.Library()


@register.simple_tag
def categories():
    return StoreCategories.objects.all()


@register.simple_tag
def products():
    return StoreProduct.objects.all()

@register.simple_tag
def User():
    return UserModel.objects.all()


