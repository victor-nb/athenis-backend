from django.db import models


def validate_decimals(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(f"{value} is not an integer or a float  number")


class UsersModel(models.Model):
    email = models.CharField(max_length=200, unique=True, blank=False)
    name = models.CharField(max_length=200, blank=False)
    date_of_birth = models.DateField(blank=False)
    phone = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=100, blank=False)
    date_joined = models.DateTimeField(blank=False)
    modified = models.DateTimeField(blank=False)
    acc_type = models.IntegerField(blank=False)
    deleted = models.BooleanField(blank=False)

    def __str__(self):
        return self.name


class CategoriesModel(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class ProductsModel(models.Model):
    category_id = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    video_url = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class ProductDetailsModel(models.Model):
    product_id = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, blank=False)
    size = models.CharField(max_length=15, blank=False)
    color = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"{self.product_id} - {self.size}/{self.color}"


class CartItemModel(models.Model):
    user_id = models.ForeignKey(UsersModel, on_delete=models.CASCADE, blank=False)
    product_details = models.ForeignKey(
        ProductDetailsModel, on_delete=models.CASCADE, blank=False
    )
    saved_for_later = models.BooleanField(blank=False)
    quantity = models.IntegerField(blank=False)
    time_added = models.DateTimeField(blank=False)

    def __str__(self):
        return f"cart_id:{self.id} - user:{self.user_id}"


class AdressModel(models.Model):
    user_id = models.ForeignKey(UsersModel, on_delete=models.CASCADE, blank=False)
    full_name = models.CharField(max_length=100, blank=False)
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=False)
    postcode = models.CharField(max_length=9, blank=False)
    city = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.full_name


class TagsModel(models.Model):
    product_id = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, blank=False)
    tag = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"product:{self.product_id} - tag:{self.tag}"


class DiscountModel(models.Model):
    name = models.CharField(max_length=50, blank=False)
    discount = models.FloatField(max_length=100, validators=[validate_decimals])
    discount_type = models.IntegerField(blank=False)
    created = models.DateTimeField(blank=False)
    valid = models.DateTimeField(blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.name} - {self.discount}"


class OrdersModel(models.Model):
    user_id = models.ForeignKey(UsersModel, on_delete=models.CASCADE, blank=False)
    address_id = models.ForeignKey(AdressModel, on_delete=models.CASCADE, blank=False)
    discount_id = models.ForeignKey(
        DiscountModel, on_delete=models.CASCADE, blank=True, null=True
    )
    created = models.DateTimeField(blank=False)
    modified = models.DateTimeField(blank=False)
    status = models.CharField(max_length=100, blank=False)
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return f"order_id:{self.id} - user:{self.user_id}"


class OrderItemModel(models.Model):
    order_id = models.ForeignKey(OrdersModel, on_delete=models.CASCADE, blank=False)
    product_details = models.ForeignKey(
        ProductDetailsModel, on_delete=models.CASCADE, blank=False
    )
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.product_details} - quantity:{self.quantity}"
