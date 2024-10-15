from django import forms
from transaction.models import TransactionModel

class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['transaction_amount']
        labels = {
            'transaction_amount': 'Amount',
        }
    
    def clean_transaction_amount(self):
        amount=self.cleaned_data.get('transaction_amount')
        return amount