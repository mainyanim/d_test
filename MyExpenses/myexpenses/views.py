
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.template import loader
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy, reverse


def exp_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses_list.html',
                  {'expenses': expenses})

def exp_detail(request, pk):
    expenses = Expense.objects.all()
    return render(request, 'exp_detail.html',
                  {'expenses': expenses})

def exp_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.save()
            return redirect('exp_detail', pk=exp.pk)
    else:
        form = ExpenseForm()
    return render(request, 'exp_edit.html', {'form': form})


def exp_edit(request, pk):
    exp = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=exp)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.save()
            return redirect('exp_detail', pk=exp.pk)
    else:
        form = ExpenseForm(instance=exp)
    return render(request, 'exp_edit.html', {'form': form})

class ExpDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('exp_list')

def add_note_to_post(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.post = expense
            note.save()
            return redirect('exp_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'add_note_to_post.html', {'form': form})
