from django.db.models.signals import post_save,post_init,pre_delete,post_migrate
from django.dispatch import receiver
from .models import PsContacts,PsjsipAdd


print('******buladasın kardeim********')

@receiver(post_save, sender=PsContacts)
def my_model_post_save(sender, instance, **kwargs):
    # Burada post_save signal'ini dinleyen fonksiyonunuzu tanımlayabilirsiniz
    # instance, veri tabanına yazılan verinin ilgili model örneğidir
    # Diğer işlemlerinizi burada gerçekleştirebilirsiniz
    print('Veri yazıldı:', instance)
    
@receiver(post_init, sender=PsContacts)
def my_model_post_save(sender, instance, **kwargs):
    # Burada post_save signal'ini dinleyen fonksiyonunuzu tanımlayabilirsiniz
    # instance, veri tabanına yazılan verinin ilgili model örneğidir
    # Diğer işlemlerinizi burada gerçekleştirebilirsiniz
    print('Veri yazıldı:', instance)
    
@receiver(pre_delete, sender=PsContacts)
def my_model_post_save(sender, instance, **kwargs):
    # Burada post_save signal'ini dinleyen fonksiyonunuzu tanımlayabilirsiniz
    # instance, veri tabanına yazılan verinin ilgili model örneğidir
    # Diğer işlemlerinizi burada gerçekleştirebilirsiniz
    print('Veri yazıldı:', instance)
    
@receiver(post_migrate, sender=PsContacts)
def my_model_post_save(sender, instance, **kwargs):
    # Burada post_save signal'ini dinleyen fonksiyonunuzu tanımlayabilirsiniz
    # instance, veri tabanına yazılan verinin ilgili model örneğidir
    # Diğer işlemlerinizi burada gerçekleştirebilirsiniz
    print('Veri yazıldı:', instance)
    
    
@receiver(post_save, sender=PsjsipAdd)
def my_model_post_save(sender, instance, **kwargs):
    # Burada post_save signal'ini dinleyen fonksiyonunuzu tanımlayabilirsiniz
    # instance, veri tabanına yazılan verinin ilgili model örneğidir
    # Diğer işlemlerinizi burada gerçekleştirebilirsiniz
    print('Veri yazıldı:', instance)