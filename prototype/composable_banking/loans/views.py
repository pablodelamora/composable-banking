from django.shortcuts import render
from django.http import HttpResponse
from loans.utils import amortization_table

products = [
    {
        'product_name': 'Personal Loan',
        'type_of_loan': 'Fix Term Loan',
        'description': 'Personal Loans to People who can prove an income greater than $20,000'
    },
    {
        'product_name': 'Mortgage Loan',
        'type_of_loan': 'Fix Term Loan',
        'description': 'Mortgage Loans to People who can prove an income greater than $80,000'
    }
]

def home(request):
    context = {
        'products': products
    }
    return render (request, 'loans/home.html', context)

def about(request):
    df, payment_summary = amortization_table(0.06, 3, 12, 19755951)
    #return render(request, 'loans/home.html')
    print(payment_summary)
    return HttpResponse(df.to_html())