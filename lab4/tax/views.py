from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
tax_rate=15
def default1(request):
	return render(request,"tax/first.html")

def calculate(request,num):
	try:
		num2=float(num)
	except ValueError:
		return HttpResponse("enter a number  or (taxrate) or empty")
	after=((tax_rate/100)*num2)+num2
	return HttpResponse(f"the total price after 15% tax is {after}")

def therate(request):
	return render(request,"tax/second.html",{"taxrate":tax_rate})


