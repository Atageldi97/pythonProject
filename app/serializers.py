from django.utils.safestring import mark_safe
from rest_framework import serializers
from .models import Brands, Reklam, FirmReklam, Size, Gender, Color, Category, Messages, SubCategory, News, \
    Address, UserReklam, Contact, Favourites


class FirmSerializers(serializers.HyperlinkedModelSerializer):

    address = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='city-detail'
    )

    class Meta:
        model = FirmReklam
        fields = ('url', 'pk', 'name', 'email', 'web_address', 'phone', 'address', 'text', 'photo1', 'photo2', 'photo3',
                  'photo4', 'photo5', 'vip', 'user', 'category')


class ReklamSerializers(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(queryset=Brands.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    subcategory = serializers.SlugRelatedField(queryset=SubCategory.objects.all(), slug_field='name')

    address = serializers.SlugRelatedField(queryset=Address.objects.all(), slug_field='name')

    class Meta:
        model = Reklam
        fields = ('url', 'pk', 'name', 'slug', 'phone', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6',
                  'photo7', 'photo8', 'photo9', 'photo10', 'address', 'category', 'brand', 'subcategory', 'price', 'count', 'text',
                  'created', 'check', 'size', 'vip', 'export', 'color', 'gender', 'kredit', 'obmen')


class FavouriteSerializers(serializers.ModelSerializer):
    brands = serializers.SlugRelatedField(queryset=Brands.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    subcategory = serializers.SlugRelatedField(queryset=SubCategory.objects.all(), slug_field='name')

    address = serializers.SlugRelatedField(queryset=Address.objects.all(), slug_field='name')

    class Meta:
        model = Favourites
        fields = ('url', 'pk', 'name', 'price', 'phone', 'text', 'brands', 'category', 'subcategory',
                  'user', 'created')


class MessageSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Messages
        fields = ('url', 'pk', 'text', 'date', 'recipient', 'sender')


class NewsSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = News
        fields = ('url', 'pk', 'name', 'category', 'subcategory', 'text', 'created', 'user', 'user_like',
                  'photo1', 'photo2', 'photo3', 'photo4', 'photo5', )


class BrandsSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Brands
        fields = ('url', 'pk', 'name', 'photo', 'category')


class SubCategorySerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = SubCategory
        fields = ('url', 'pk', 'name', 'category')


class SizeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ('url', 'pk', 'name')


class ColorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('url', 'pk', 'name', 'photo')


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('url', 'pk', 'name')


class GenderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = ('url', 'pk', 'name')


class AddressSerializers(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('url', 'pk', 'name', 'region_id')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserReklam
        fields = ('url', 'pk', 'username', 'first_name', 'phone1', 'phone2', 'email', 'password', 'address', 'following',
                  'vip', 'profession', 'check', 'photo')
        write_only_fields = 'password'

        def create(self, validated_data):
            user = UserReklam.objects.create(username=validated_data['username'],
                                             email=validated_data['email'],
                                             phone1= validated_data['phone1'],
                                             phone2= validated_data['phone2'],
                                             password=validated_data['password'])
            user.set_password(validated_data['password'])
            user.save()
            return user

