from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_created')
    engineer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='tickets_assigned', null=True, blank=True)
    ticket_id = models.CharField(max_length=15, unique=True)
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    SEVERITY_CHOICES = (
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    severity = models.CharField(max_length=15, choices=SEVERITY_CHOICES, default='Low')
    is_assigned_to_engineer = models.BooleanField(default=False)
    resolution_steps = models.TextField()
