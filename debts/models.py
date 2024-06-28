from django.db import models

class Debt(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSED', 'Processed'),
        ('CONFIRMED', 'Confirmed'),
    ]

    name = models.TextField(max_length=100, verbose_name="Nome")
    government_id = models.IntegerField(verbose_name="Número do Documento")
    email = models.EmailField(max_length=254, verbose_name="Email do Sacado")
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    debt_due_date = models.DateField(verbose_name="Data de Vencimento")
    debt_id = models.UUIDField(unique=True, verbose_name="UUID para Débito")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Boleto"

    @classmethod
    def exists_by_debt_id(cls, debt_id):
        return cls.objects.filter(debt_id=debt_id).exists()