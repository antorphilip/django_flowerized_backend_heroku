from django.db import models


class Item(models.Model):
    name=models.CharField(max_length=1000)
    price=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Categories", on_delete=models.CASCADE, null=True)
    package = models.ForeignKey("Package", on_delete=models.CASCADE, null=True)
    img_url = models.URLField(max_length = 200, default="https://firebasestorage.googleapis.com/v0/b/flowerized-site.appspot.com/o/momo.jpg?alt=media&token=d902bfc4-e239-44cc-bb89-cf9e2e20b1c5")

    def __str__(self):
        return self.name
    


class Categories(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    Category=models.CharField(max_length=1000)

    def __str__(self):
        return self.Category


class Package(models.Model):
    class Meta:
        verbose_name_plural = 'packages'
    Package=models.CharField(max_length=1000)

    def __str__(self):
        return self.Package
