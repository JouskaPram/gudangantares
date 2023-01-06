from django.db import models

# class Scanner(models.Model):
#     name = models.CharField(max_length=9)

#     def __str__(self):
#         return self.name

SCANNER = (
    ('angle', 'angle'),
    ('latif', 'latif'),
    ('fazza', 'fazza'),
    ('antarestar', 'antarestar'),
)


class Sortir(models.Model):
    barcode = models.CharField(max_length=40)

    scanner = models.CharField(max_length=40, null=True, choices=SCANNER)
    # scanner = models.ForeignKey(
    #     Scanner,max_length=40, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.barcode


class Double(models.Model):
    barcode = models.CharField(max_length=40)

    scanner = models.CharField(max_length=40, null=True, choices=SCANNER)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.barcode