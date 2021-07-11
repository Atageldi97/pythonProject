from rest_framework import generics
from .models import Brands, Reklam, FirmReklam, Size, Gender, Color, Category, Messages, SubCategory, News, \
    Address, UserReklam
from .serializers import FirmSerializers, ReklamSerializers, MessageSerializers, \
    NewsSerializers, BrandsSerializers, SubCategorySerializers, SizeSerializers, ColorSerializers, CategorySerializers, \
    GenderSerializers, AddressSerializers, UserSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse


class BrandList(generics.ListCreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializers
    name = 'brands-list'


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializers
    name = 'brands-detail'


class ReklamList(generics.ListCreateAPIView):
    queryset = Reklam.objects.all()
    serializer_class = ReklamSerializers
    name = 'reklam-list'


class ReklamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reklam.objects.all()
    serializer_class = ReklamSerializers
    name = 'reklam-detail'


class FirmsList(generics.ListCreateAPIView):
    queryset = FirmReklam.objects.all()
    serializer_class = FirmSerializers
    name = 'firmreklam-list'


class FirmsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirmReklam.objects.all()
    serializer_class = FirmSerializers
    name = 'firmreklam-detail'


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers
    name = 'address-list'


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers
    name = 'address-detail'


class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers
    name = 'subcategory-list'


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers
    name = 'subcategory-detail'


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    name = 'category-list'


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    name = 'category-detail'


class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers
    name = 'color-list'


class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers
    name = 'color-detail'


class GenderList(generics.ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializers
    name = 'gender-list'


class GenderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializers
    name = 'gender-detail'


class SizeList(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers
    name = 'size-list'


class SizeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers
    name = 'size-detail'


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    name = 'news-list'


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    name = 'news-detail'


class MessageList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializers
    name = 'messages-list'


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializers
    name = 'messages-detail'


class UserList(generics.ListCreateAPIView):
    queryset = UserReklam.objects.all()
    serializer_class = UserSerializer
    name = 'userreklam-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserReklam.objects.all()
    serializer_class = UserSerializer
    name = 'userreklam-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'reklams'

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'reklams': reverse(ReklamList.name, request=request),
            'firms': reverse(FirmsList.name, request=request),
            'message': reverse(MessageList.name, request=request),
            'news': reverse(NewsList.name, request=request),
            'categories': reverse(CategoryList.name, request=request),
            'brands': reverse(BrandList.name, request=request),
            'subcategories': reverse(SubCategoryList.name, request=request),
            'colors': reverse(ColorList.name, request=request),
            'genders': reverse(GenderList.name, request=request),
            'sizes': reverse(SizeList.name, request=request),
            'address': reverse(AddressList.name, request=request),


        })
