# Django Admin Panel'i Kullanarak Asterisk Realtime Yönetimi: Telekomünikasyonunuzu Geliştirmenin Yeni Yolu

![Django](https://img.shields.io/badge/Django-3.2-green)
![Asterisk](https://img.shields.io/badge/Asterisk-20.0-blue)


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

## Projeyi Çalıştırmak İçin:

1. Gerekli Python modüllerini yükleyin: `pip install -r requirements.txt`
2. Asterisk Realtime ayarlarını `settings.py` dosyasında yapılandırın.
3. Django admin paneline erişmek için superuser oluşturun: `python manage.py createsuperuser`
4. Django sunucusunu başlatın: `python manage.py runserver`
5. Tarayıcınızda http://localhost:8000/admin adresine gidin ve superuser bilgilerinizle oturum açın.

Asterisk Realtime yönetimini Django Admin Panel'i kullanarak kolaylaştırın ve telekomünikasyonunuzu etkili bir şekilde geliştirin! Güçlü iletişim altyapısını keşfedin ve Django Admin Panel'i kullanarak hızlı, esnek, güvenilir ve kullanıcı dostu bir çözüm elde edin. Ayrıca, zaman ve kaynak tasarrufu sağlayarak Asterisk Realtime verilerini daha akıllıca yönetebilirsiniz.
