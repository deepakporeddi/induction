from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Student

@receiver(post_delete, sender=Student)
def delete_Student(sender, instance=None, *args, **kwargs):
    print("Signal called")


@receiver(post_save, sender=Student)
def save_Student(sender, instance=None, *args, **kwargs):
    print("Post_save Signal called For student model")



