# Django Asterisk Realtime Admin Panel

![Django](https://img.shields.io/badge/Django-3.2-green)
![Asterisk](https://img.shields.io/badge/Asterisk-18.4-blue)

Bu proje, Django admin paneli üzerinden Asterisk Realtime aracılığıyla aşağıdaki modülleri yönetmenize olanak sağlar:

- ps_endpoints
- ps_auths
- ps_aors
- ps_domain_aliases
- ps_endpoint_id_ips
- ps_contacts
- voicemail
- queues
- queue_members
- sipusers
- sippeers
- extensions

Projeyi çalıştırmak için:

1. Gerekli Python modüllerini yükleyin: `pip install -r requirements.txt`
2. Asterisk Realtime ayarlarını `settings.py` dosyasında yapılandırın.
3. Django admin paneline erişmek için superuser oluşturun: `python manage.py createsuperuser`
4. Django sunucusunu başlatın: `python manage.py runserver`
5. Tarayıcınızda `http://localhost:8000/admin` adresine gidin ve superuser bilgilerinizle oturum açın.

![Admin Panel](https://i.ibb.co/mcnh8rX/admin-panel.png)
