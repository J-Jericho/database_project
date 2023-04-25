from django.db.models.signals import post_save
from django.dispatch import receiver
from custom_auth.models import BaseUser, Employee, Student


@receiver(post_save, sender=BaseUser)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_staff:
        employee, created = Employee.objects.get_or_create(user=instance, defaults={'job_role': "Librarian",
                                                                                    'salary': 50000.00})
    if instance.is_student:
        student, created = Student.objects.get_or_create(user=instance)