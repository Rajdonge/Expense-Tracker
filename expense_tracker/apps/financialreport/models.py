from django.db import models
from django.contrib.auth.models import User

class ExpenseIncome(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('credit', 'Credit'),
        ('debit', 'Debit')
    ]
    TAX_TYPE_CHOICES = [
        ('flat', 'Flat'),
        ('percentage', 'Percentage')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_type = models.CharField(max_length=10, choices=TAX_TYPE_CHOICES, default='flat')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        if self.tax_type == 'flat':
            return self.amount + self.tax
        elif self.tax_type == 'percentage':
            return self.amount + (self.amount * self.tax / 100)
        return self.amount
    
    @property
    def total(self):
        return self.calculate_total()
    
    def __str__(self):
        return f'{self.title} ({self.transaction_type}): {self.total}'