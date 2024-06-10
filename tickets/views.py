from django.shortcuts import render, redirect
import random
from django.shortcuts import get_object_or_404, render
import string
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


from .form import CreateTicketForm, AssignTicketForm
from.models import Ticket

User = get_user_model()

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
                    # send email functionality
                    subject = f"{var.ticket_title} #{var.ticket_id}"
                    message = "Thank you for creating a ticket , we will assign an Engineer soon"
                    email_from = "kibe#gmail.com"
                    recipient_list = [request.user.email]
                    send_mail(subject, message, email_from, recipient_list)
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
    ticket_instance = Ticket.objects.get(ticket_id=ticket_id)
    
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance=ticket_instance)  # Pass request.POST to populate the form
        if form.is_valid():
            var = form.save(commit=False)
            var.is_assigned_to_engineer = True
            var.status = "Active"
            var = form.save()
            messages.success(request, f'Ticket has been assigned to {var.engineer}')  # Use var.engineer instead of var.rngineer
            return redirect('ticket-queue')
        else:
            messages.warning(request, 'Something went wrong. Please check your input.')
            return redirect('assign-ticket', ticket_id=ticket_id)  # Redirect with ticket_id
    else:
        form = AssignTicketForm(instance=ticket_instance)
        form.fields['engineer'].queryset = User.objects.filter(is_engineer=True)
        context = {'form': form, 'ticket': ticket_instance}
        return render(request, 'tickets/assign_ticket.html', context)


def ticket_details(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    context = {'ticket': ticket}
    return render(request, 'tickets/ticket_details.html', context)

def ticket_queue(request):
    tickets = Ticket.objects.filter(is_assigned_to_engineer=False)
    context = {'tickets': tickets}  # Pass 'tickets' in the context
    return render(request, 'tickets/ticket_queue.html', context)

def resolve_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    
    if request.method == "POST":
        resolution = request.POST.get('resolution', '')
        if resolution:
            ticket.resolution_steps = resolution
            ticket.is_resolved = True
            ticket.status = "Resolved"
            ticket.save()
            messages.success(request, "Ticket is now resolved and closed.")
            return redirect('ticket-details', ticket_id=ticket_id)
        else:
            messages.error(request, "Resolution steps are required.")
    
    return redirect('ticket-details', ticket_id=ticket_id)