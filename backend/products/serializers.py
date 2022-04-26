from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from . import validators
from api.serializers import UserPublicSerilizer

class ProductInlineSerializer(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk",read_only=True)
    title=serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):

    owner=UserPublicSerilizer(source="user",read_only=True)
    my_discount=serializers.SerializerMethodField(read_only=True)
    title=serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
    name=serializers.CharField(source="title",read_only=True)
    #url=serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk")
    email=serializers.EmailField(write_only=True)
    class Meta:
        model=Product
        fields=["owner","email","name","title","content","price","sale_price","my_discount","public","path","endpoint"]


    def validate_title(self,value):
        request=self.context.get("request")
        user=request.user
        qs=Product.objects.filter(user=user,title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product")
        return value
    """
    def create(self,validated_data):
        obj=super().create(validated_data)
        return obj
    """

    def get_my_discount(self,obj):
        if not hasattr(obj,"id"):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()

    def get_url(self,obj):
        request=self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk":obj.pk},request=request)

