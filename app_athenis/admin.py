from django.contrib import admin
from .models import (
    UsersModel,
    CategoriesModel,
    ProductsModel,
    ProductDetailsModel,
    CartItemModel,
    AdressModel,
    TagsModel,
    DiscountModel,
    OrdersModel,
    OrderItemModel,
)

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "name",
        "date_of_birth",
        "phone",
        "password",
        "date_joined",
        "modified",
        "acc_type",
        "deleted",
    ]


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ProductsAdmin(admin.ModelAdmin):
    list_display = ["category_id", "name", "description", "video_url", "price"]


class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ["product_id", "size", "color"]


class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "product_details",
        "saved_for_later",
        "quantity",
        "time_added",
    ]


class AdressAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "full_name",
        "address1",
        "address2",
        "postcode",
        "city",
        "phone",
    ]


class TagsAdmin(admin.ModelAdmin):
    list_display = ["product_id", "tag"]


class DiscountAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "discount",
        "discount_type",
        "created",
        "valid",
        "quantity",
    ]


class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "address_id",
        "discount_id",
        "created",
        "modified",
        "status",
        "amount",
    ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order_id", "product_details", "quantity"]


admin.site.register(UsersModel, UsersAdmin)
admin.site.register(CategoriesModel, CategoriesAdmin)
admin.site.register(ProductsModel, ProductsAdmin)
admin.site.register(ProductDetailsModel, ProductDetailsAdmin)
admin.site.register(CartItemModel, CartItemAdmin)
admin.site.register(AdressModel, AdressAdmin)
admin.site.register(TagsModel, TagsAdmin)
admin.site.register(DiscountModel, DiscountAdmin)
admin.site.register(OrdersModel, OrdersAdmin)
admin.site.register(OrderItemModel, OrderItemAdmin)