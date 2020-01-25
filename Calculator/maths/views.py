from django.shortcuts import render, redirect
from maths.forms import calculation
# Create your views here.


def get(request):
    form = calculation()
    return render(request, 'calc.html', {'form': form})


def post(request):
    form = calculation(request.POST)
    if form.is_valid():
        first = form.cleaned_data['num1']
        second = form.cleaned_data['num2']
        operand = form.cleaned_data['operation']
        if operand == "+":
            text = float(first)+float(second)
            text = str(text)
        if operand == "-":
            text = float(first)-float(second)
            text = str(text)
        if operand == "x":
            text = float(first)*float(second)
            text = str(text)
        if operand == "/":
            text = float(first)/float(second)
            text = str(text)
        if operand == "":
            text = "Please select an operation"
    args = {'form': form, 'text': text}
    return render(request, 'calc.html', args)
