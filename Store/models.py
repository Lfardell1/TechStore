from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class StoreCategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    

    class Meta:
        db_table = 'Store_categories'


class StoreProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    unique_id = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    description = models.TextField()
    sales = models.IntegerField( blank=True, null=True)
    costPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Store_product'
        
        
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'authorised_group'
        
        
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class UserModel(AbstractBaseUser):
    # Make all fields except email and password optional
    User_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True , default="User")
    email = models.EmailField(unique=True, null=True, blank=False,
                              error_messages={'unique': "This email has already been registered"},
                              help_text="Enter a valid email address", verbose_name="Email")
    password = models.TextField(max_length=50)
    address = models.CharField(max_length=50, blank=True, null=True , default="Address")
    postalcode = models.CharField(max_length=50, blank=True, null=True , default="Postal Code")
    city = models.CharField(max_length=50, blank=True, null=True , default="City")
    country = models.CharField(max_length=50, blank=True, null=True , default="Country")
    phone = models.CharField(max_length=50, blank=True, null=True , default="Phone")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    
    objects = UserManager()

    

    @property
    def is_anonymous(self):
        return False

    @property
    def is_staff(self):
        return self.is_admin   

    @property
    def is_authenticated(self):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        db_table = 'Store_UserModel'