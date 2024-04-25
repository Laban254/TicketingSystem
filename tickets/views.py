from django.shortcuts import render, redirect
import random
from django.shortcuts import get_object_or_404, render
import string
from django.db import IntegrityError
from django.contrib import messages
from .form import CreateTicketForm, AssignTicketForm
from.models import Ticket

def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            while not var.ticket_id:
                id = ''.join(random.choices(string.digits, k=6))
                try:
                    var.ticket_id = id
                    var.save()
                    messages.success(request, 'your ticket has been submitted')
                    return redirect('customer-active-tickets')
                except IntegrityError:
                    continue
            
        else:
            messages.warning(request, 'submiting went wrong, please check form errors')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form': form}
        return render(request, 'tickets/create_ticket.html', context)
    

def customer_active_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'tickets/customer_active_tickets.html', context)


def customer_resolved_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'tickets/customer_resolved_tickets.html', context)

def engineer_active_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'tickets/engineer_active_tickets.html', context)


def engineer_resolved_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'tickets/engineer_resolved_tickets.html', context)

def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.filter(ticket_id=ticket_id)
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance = ticket)
        if form.is_valid():
            var = form.save()
            messages.success(request, f'Ticket has been assigned to {var.rngineer}')
            return redirect('ticket-queue')
        else:
            messages.warning(request, 'something went wrong please check your input')
            return redirect('assign-ticket')
    else:
        form = AssignTicketForm()
        context = {'form': form}
        return render(request, 'ticket/assign_ticket.html', context)
    


def ticket_details(request, ticket_id):
    # Retrieve the ticket object using get_object_or_404 to handle the case when the ticket doesn't exist
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    context = {'ticket': ticket}
    return render(request, 'tickets/ticket_details.html', context)


def ticket_queue(request):
    tickets =Ticket.objects.filter(is_assigned_to_engineer=False)
    context = {'tickets': tickets}
    return render(request, 'ticket/ticket_queue.html')