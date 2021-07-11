from django.db.models import *
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


def brands_photo(instance, filename):
    return 'reklams/brands/{0}/{1}'.format(instance.category, filename)


class Brands(Model):
    name = CharField(max_length=255, null=True)
    photo = ImageField(upload_to=brands_photo, null=True)
    category = ForeignKey(Category, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name


class SubCategory(Model):
    name = CharField(max_length=255, null=True)
    category = ForeignKey(Category, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name


class Color(Model):
    name = CharField(max_length=255)
    photo = ImageField(upload_to='reklams/colors', null=True)

    def __str__(self):
        return self.name


class Size(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Gender(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Address(Model):
    name = CharField(max_length=255, null=True)
    region_id = IntegerField()

    def __str__(self):
        return self.name


def reklam_photos(instance, filename):
    return 'reklams/{0}/{1}/{2}/{3}'.format(instance.category, instance.brand, instance.category, filename)


class Reklam(Model):
    name = CharField(max_length=255, null=True)
    slug = SlugField(max_length=250, unique_for_date='created')
    photo1 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo2 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo3 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo4 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo5 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo6 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo7 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo8 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo9 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo10 = ImageField(upload_to=reklam_photos, null=True, default=0)
    brand = ForeignKey(Brands, on_delete=CASCADE, null=True, default=0)
    category = ForeignKey(Category, on_delete=CASCADE, null=True)
    subcategory = ForeignKey(SubCategory, on_delete=CASCADE, null=True)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, null=True)
    phone = IntegerField(null=True, default=0)
    address = ForeignKey(Address, on_delete=CASCADE, null=True)
    price = DecimalField(max_digits=8, decimal_places=2, default=0)
    count = IntegerField(null=True, default=1)
    text = TextField(blank=True, null=True)
    created = DateTimeField(auto_now_add=True, null=True)
    ready = BooleanField(null=True, default=False)
    vip = BooleanField(default=False)
    export = BooleanField(default=False)
    #goşmaça maglumat eger ulanylmayan bolsa o-a den
    size = ManyToManyField(Size)
    color = ManyToManyField(Color)
    gender = ForeignKey(Gender, on_delete=CASCADE, null=True)
    kredit = BooleanField(null=True, default=False)
    obmen = BooleanField(null=True, default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('infoReklams', kwargs={"pk": self.pk})

    def get_color(self):
        return "\n".join([c.name for c in self.color.all()])

    def get_size(self):
        return "\n".join([c.name for c in self.size.all()])


class News(Model):
    name = CharField(max_length=255, null=True)
    slug = SlugField(max_length=250, unique_for_date='created')
    photo1 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo2 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo3 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo4 = ImageField(upload_to=reklam_photos, null=True, default=0)
    photo5 = ImageField(upload_to=reklam_photos, null=True, default=0)
    category = ForeignKey(Category, on_delete=CASCADE, null=True)
    subcategory = ForeignKey(SubCategory, on_delete=CASCADE, null=True)
    text = CharField(max_length=1500, null=True)
    created = DateTimeField(auto_now_add=True)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, null=True)
    user_like = ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked', blank=True)

    def __str__(self):
        return self.name


def firmek_photos(instance, filename):
    return 'reklams/firms/{0}/{1}/{2}'.format(instance.address, instance.name, filename)


class FirmReklam(Model):
    name = CharField(max_length=500)
    category = ForeignKey(Category, on_delete=CASCADE, null=True)
    email = EmailField(null=True)
    web_address = CharField(max_length=255, null=True)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, null=True)
    phone = IntegerField(null=True)
    photo1 = ImageField(upload_to=firmek_photos, null=True)
    photo2 = ImageField(upload_to=firmek_photos, null=True)
    photo3 = ImageField(upload_to=firmek_photos, null=True)
    photo4 = ImageField(upload_to=firmek_photos, null=True)
    photo5 = ImageField(upload_to=firmek_photos, null=True)
    text = TextField(blank=True)
    created = DateTimeField(auto_now=True, null=True)
    address = ForeignKey(Address, on_delete=CASCADE, null=True)
    vip = BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('infoFirmReklams', kwargs={"pk": self.pk})


class Favourites(Model):
    name = CharField(max_length=250, null=True)
    price = DecimalField(max_digits=8, decimal_places=2)
    phone = IntegerField(null=True)
    text = TextField(blank=True)
    brands = ForeignKey(Brands, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)
    subcategory = ForeignKey(SubCategory, on_delete=CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Messages(Model):
    text = CharField(max_length=1000, null=True)
    date = DateTimeField(auto_now_add=True)
    recipient = CharField(max_length=500, null=True)
    sender = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.sender


class Contact(Model):
    user_from = ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_from_set', on_delete=CASCADE)
    user_to = ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_to_set', on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


class UserReklam(AbstractUser):
    phone1 = IntegerField(null=True)
    phone2 = IntegerField(null=True)
    email = EmailField(null=True)
    web = CharField(max_length=250, null=True)
    photo = ImageField(upload_to='reklams/users', null=True)
    vip = BooleanField(default=False)
    profession = BooleanField(default=False)
    address = ForeignKey(Address, on_delete=CASCADE, null=True)
    following = ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)
    check = BooleanField(default=False)

    def __str__(self):
        return self.username

