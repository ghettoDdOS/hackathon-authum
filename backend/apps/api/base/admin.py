from django.contrib import admin

from .models import (
    Brand,
    Case,
    Category,
    Comment,
    Exhibitor,
    Location,
    Partner,
    Producer,
    Product,
    ProductPicture,
    TypeCooperation,
)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "exhibitor",
        "name",
        "site_url",
        "type_content",
        "html_content",
        "video_content",
        "import_substitution",
    )
    list_filter = ("exhibitor",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "exhibitor", "name", "parent")
    list_filter = ("exhibitor", "parent")
    search_fields = ("name",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "exhibitor", "picture", "name", "company", "text")
    list_filter = ("exhibitor",)
    search_fields = ("name",)


@admin.register(Exhibitor)
class ExhibitorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "about",
        "logo",
        "main_picture",
        "address",
        "legal_address",
        "producer_address",
        "phone",
        "name_contact_person",
        "inn",
        "display_price",
        "display_price_text",
        "import_substitution",
    )
    search_fields = ("name",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "exhibitor",
        "name",
        "type_cooperation",
        "site_url",
        "address",
    )
    list_filter = ("exhibitor", "type_cooperation")
    search_fields = ("name",)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("id", "exhibitor", "logo", "name")
    list_filter = ("exhibitor",)
    search_fields = ("name",)


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "exhibitor",
        "name",
        "price",
        "description",
        "analogues",
        "type_product",
        "import_substitution",
        "type_purchase",
        "category",
        "delivery_method",
        "payment_method",
        "minimum_batch",
        "producer",
        "brand",
        "video",
    )
    list_filter = ("exhibitor", "category", "producer", "brand")
    search_fields = ("name",)


@admin.register(ProductPicture)
class ProductPictureAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "picture", "keywords")
    list_filter = ("product",)


@admin.register(TypeCooperation)
class TypeCooperationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
