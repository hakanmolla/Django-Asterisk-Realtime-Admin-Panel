from django.db import models
from ast20.models import PsAors,PsAuths,PsEndpoints

# Create your models here.




class QueueLog(models.Model):
    time = models.CharField(max_length=40, blank=True, null=True)
    callid = models.CharField(max_length=32, default='')
    queuename = models.CharField(max_length=32, default='')
    agent = models.CharField(max_length=32, default='')
    event = models.CharField(max_length=32, default='')
    data1 = models.CharField(max_length=255, default='')
    data2 = models.CharField(max_length=255, default='')
    data3 = models.CharField(max_length=255, default='')
    data4 = models.CharField(max_length=255, default='')
    data5 = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'queue_log2'


class PsjsipAdd(models.Model):
    
    # MyCustomModel modeline ait alanlar
    #endpoisnt ortakları start
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    transport = models.CharField(max_length=40, blank=True, null=True)
    aors = models.CharField(max_length=200, blank=True, null=True)
    auth = models.CharField(max_length=40, blank=True, null=True)
    context = models.CharField(max_length=40, blank=True, null=True)
    disallow = models.CharField(max_length=200, blank=True, null=True)
    allow = models.CharField(max_length=200, blank=True, null=True)
    direct_media = models.CharField(max_length=3, blank=True, null=True)
    mailboxes = models.CharField(max_length=40, blank=True, null=True)
    deny = models.CharField(max_length=95, blank=True, null=True)
    permit = models.CharField(max_length=95, blank=True, null=True)
    #endpoisnt ortakları end
    #aours ortakları start
    # id = models.CharField(unique=True, max_length=40)
    max_contacts = models.IntegerField(blank=True, null=True)
    qualify_frequency = models.IntegerField(blank=True, null=True)
    #aours ortakları end
    #PsAuths ortakları start
    #id = models.CharField(unique=True, max_length=40)
    auth_type = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    aors = models.ForeignKey(PsAors, on_delete=models.CASCADE,related_name='aors',null=True)
    auth = models.ForeignKey(PsAuths, on_delete=models.CASCADE,related_name='auth',null=True)
    PsEndpoints = models.ForeignKey(PsEndpoints, on_delete=models.CASCADE,related_name='endpoints',null=True)
    

    # def save(self, *args, **kwargs):
    #     # PsAors, PsAuths ve PsEndpoints modellerine de veri eklenmesini sağlayan kodlar
    #     ps_aors = PsEndpoints( id = self.id,
    #                     transport =self.transport,
    #                     aors =self.aors,
    #                     auth = self.auth,
    #                     context = self.context,
    #                     disallow =self.disallow,
    #                     allow =self. allow,
    #                     direct_media =self.direct_media, 
    #                     mailboxes =self.mailboxes,
    #                     deny = self.deny,
    #                     permit = self.permit,)
    #     ps_aors.save()
    #     ps_auths = PsAors(id = self.id,
    #                        max_contacts=self.max_contacts,
    #                        qualify_frequency=self.qualify_frequency,
                           
    #                        )
    #     ps_auths.save()
    #     ps_endpoints = PsAuths(id = self.id,
    #                            auth_type=self.auth_type,
    #                            password=self.password,
    #                            username=self.username,
    #                            )
    #     ps_endpoints.save()

    #     self.ps_aors = ps_aors
    #     self.ps_auths = ps_auths
    #     self.ps_endpoints = ps_endpoints

    #     super(PsjsipAdd, self).save(*args, **kwargs)