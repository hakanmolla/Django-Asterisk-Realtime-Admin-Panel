from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver



 
class PsAuths(models.Model):
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    auth_type = models.CharField(max_length=12, blank=True, null=True)
    nonce_lifetime = models.IntegerField(blank=True, null=True)
    md5_cred = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    realm = models.CharField(max_length=40, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    oauth_clientid = models.CharField(max_length=255, blank=True, null=True)
    oauth_secret = models.CharField(max_length=255, blank=True, null=True)
    PsjsipAdd = models.CharField(max_length=255, blank=True, null=True) #models.ForeignKey(PsjsipAdd, on_delete=models.CASCADE, related_name='PsAuths',default='Değer',)
    
    class Meta:
        # managed = False
        db_table = 'ps_auths'
        verbose_name = 'ps_auths'
        verbose_name_plural = 'ps_auths'

class PsAors(models.Model):
    MY_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    contact = models.CharField(max_length=255, blank=True, null=True)
    default_expiration = models.IntegerField(blank=True, null=True)
    mailboxes = models.CharField(max_length=80, blank=True, null=True, choices=MY_CHOICES)
    max_contacts = models.IntegerField(blank=True, null=True,default="1")
    minimum_expiration = models.IntegerField(blank=True, null=True,default="60")
    remove_existing = models.CharField(max_length=3, blank=True, null=True)
    qualify_frequency = models.IntegerField(blank=True, null=True,default="120")
    authenticate_qualify = models.CharField(max_length=3, blank=True, null=True)
    maximum_expiration = models.IntegerField(blank=True, null=True,default="7200")
    outbound_proxy = models.CharField(max_length=40, blank=True, null=True)
    support_path = models.CharField(max_length=3, blank=True, null=True)
    qualify_timeout = models.FloatField(blank=True, null=True)
    voicemail_extension = models.CharField(max_length=40, blank=True, null=True)
    remove_unavailable = models.CharField(max_length=5, blank=True, null=True)
    PsjsipAdd = models.CharField(max_length=255, blank=True, null=True) 
    #PsjsipAdd = models.ForeignKey(PsjsipAdd, on_delete=models.CASCADE, related_name='PsAors',default='Değer',)
    

    class Meta:
        # managed = False
        db_table = 'ps_aors'
        verbose_name = 'ps_aors'
        verbose_name_plural = 'ps_aors'
            
class PsEndpoints(models.Model):
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    transport = models.CharField(max_length=40, blank=True, null=True,default="transport-udp")
    aors = models.CharField(max_length=200, blank=True, null=True)
    auth = models.CharField(max_length=40, blank=True, null=True)
    context = models.CharField(max_length=40, blank=True, null=True,default="testing")
    disallow = models.CharField(max_length=200, blank=True, null=True)
    allow = models.CharField(max_length=200, blank=True, null=True)
    direct_media = models.CharField(max_length=3, blank=True, null=True,default="no")
    connected_line_method = models.CharField(max_length=8, blank=True, null=True)
    direct_media_method = models.CharField(max_length=8, blank=True, null=True)
    direct_media_glare_mitigation = models.CharField(max_length=8, blank=True, null=True)
    disable_direct_media_on_nat = models.CharField(max_length=3, blank=True, null=True)
    dtmf_mode = models.CharField(max_length=9, blank=True, null=True,default="rfc4733")
    external_media_address = models.CharField(max_length=40, blank=True, null=True)
    force_rport = models.CharField(max_length=3, blank=True, null=True,default="yes")
    ice_support = models.CharField(max_length=3, blank=True, null=True,default="no")
    identify_by = models.CharField(max_length=80, blank=True, null=True)
    mailboxes = models.CharField(max_length=40, blank=True, null=True)
    moh_suggest = models.CharField(max_length=40, blank=True, null=True,default="default")
    outbound_auth = models.CharField(max_length=40, blank=True, null=True)
    outbound_proxy = models.CharField(max_length=40, blank=True, null=True)
    rewrite_contact = models.CharField(max_length=3, blank=True, null=True,default="yes")
    rtp_ipv6 = models.CharField(max_length=3, blank=True, null=True)
    rtp_symmetric = models.CharField(max_length=3, blank=True, null=True,default="yes")
    send_diversion = models.CharField(max_length=3, blank=True, null=True)
    send_pai = models.CharField(max_length=3, blank=True, null=True,default="yes")
    send_rpid = models.CharField(max_length=3, blank=True, null=True)
    timers_min_se = models.IntegerField(blank=True, null=True)
    timers = models.CharField(max_length=8, blank=True, null=True,default="yes")
    timers_sess_expires = models.IntegerField(blank=True, null=True)
    callerid = models.CharField(max_length=40, blank=True, null=True)
    callerid_privacy = models.CharField(max_length=23, blank=True, null=True)
    callerid_tag = models.CharField(max_length=40, blank=True, null=True)
    number_100rel = models.CharField(db_column='100rel', max_length=14, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    aggregate_mwi = models.CharField(max_length=3, blank=True, null=True,default="yes")
    trust_id_inbound = models.CharField(max_length=3, blank=True, null=True,default="yes")
    trust_id_outbound = models.CharField(max_length=3, blank=True, null=True)
    use_ptime = models.CharField(max_length=3, blank=True, null=True)
    use_avpf = models.CharField(max_length=3, blank=True, null=True,default="no")
    media_encryption = models.CharField(max_length=4, blank=True, null=True,default="no")
    inband_progress = models.CharField(max_length=3, blank=True, null=True,default="no")
    call_group = models.CharField(max_length=40, blank=True, null=True)
    pickup_group = models.CharField(max_length=40, blank=True, null=True)
    named_call_group = models.CharField(max_length=40, blank=True, null=True)
    named_pickup_group = models.CharField(max_length=40, blank=True, null=True)
    device_state_busy_at = models.IntegerField(blank=True, null=True,default="3")
    fax_detect = models.CharField(max_length=3, blank=True, null=True)
    t38_udptl = models.CharField(max_length=3, blank=True, null=True)
    t38_udptl_ec = models.CharField(max_length=10, blank=True, null=True)
    t38_udptl_maxdatagram = models.IntegerField(blank=True, null=True)
    t38_udptl_nat = models.CharField(max_length=3, blank=True, null=True)
    t38_udptl_ipv6 = models.CharField(max_length=3, blank=True, null=True)
    tone_zone = models.CharField(max_length=40, blank=True, null=True)
    language = models.CharField(max_length=40, blank=True, null=True)
    one_touch_recording = models.CharField(max_length=3, blank=True, null=True,default="no")
    record_on_feature = models.CharField(max_length=40, blank=True, null=True,default="apprecord")
    record_off_feature = models.CharField(max_length=40, blank=True, null=True,default="apprecord")
    rtp_engine = models.CharField(max_length=40, blank=True, null=True)
    allow_transfer = models.CharField(max_length=3, blank=True, null=True)
    allow_subscribe = models.CharField(max_length=3, blank=True, null=True,default="yes")
    sdp_owner = models.CharField(max_length=40, blank=True, null=True)
    sdp_session = models.CharField(max_length=40, blank=True, null=True)
    tos_audio = models.CharField(max_length=10, blank=True, null=True,default="ef")
    tos_video = models.CharField(max_length=10, blank=True, null=True,default="af41")
    sub_min_expiry = models.IntegerField(blank=True, null=True)
    from_domain = models.CharField(max_length=40, blank=True, null=True)
    from_user = models.CharField(max_length=40, blank=True, null=True)
    mwi_from_user = models.CharField(max_length=40, blank=True, null=True)
    dtls_verify = models.CharField(max_length=40, blank=True, null=True)
    dtls_rekey = models.CharField(max_length=40, blank=True, null=True)
    dtls_cert_file = models.CharField(max_length=200, blank=True, null=True)
    dtls_private_key = models.CharField(max_length=200, blank=True, null=True)
    dtls_cipher = models.CharField(max_length=200, blank=True, null=True)
    dtls_ca_file = models.CharField(max_length=200, blank=True, null=True)
    dtls_ca_path = models.CharField(max_length=200, blank=True, null=True)
    dtls_setup = models.CharField(max_length=7, blank=True, null=True)
    srtp_tag_32 = models.CharField(max_length=3, blank=True, null=True)
    media_address = models.CharField(max_length=40, blank=True, null=True)
    redirect_method = models.CharField(max_length=9, blank=True, null=True)
    set_var = models.TextField(blank=True, null=True)
    cos_audio = models.IntegerField(blank=True, null=True,default="5")
    cos_video = models.IntegerField(blank=True, null=True,default="4")
    message_context = models.CharField(max_length=40, blank=True, null=True)
    force_avp = models.CharField(max_length=3, blank=True, null=True)
    media_use_received_transport = models.CharField(max_length=3, blank=True, null=True,default="no")
    accountcode = models.CharField(max_length=80, blank=True, null=True)
    user_eq_phone = models.CharField(max_length=3, blank=True, null=True,default="no")
    moh_passthrough = models.CharField(max_length=3, blank=True, null=True)
    media_encryption_optimistic = models.CharField(max_length=3, blank=True, null=True,default="no")
    rpid_immediate = models.CharField(max_length=3, blank=True, null=True)
    g726_non_standard = models.CharField(max_length=3, blank=True, null=True)
    rtp_keepalive = models.IntegerField(blank=True, null=True)
    rtp_timeout = models.IntegerField(blank=True, null=True,default="120")
    rtp_timeout_hold = models.IntegerField(blank=True, null=True,default="300")
    bind_rtp_to_media_address = models.CharField(max_length=3, blank=True, null=True)
    voicemail_extension = models.CharField(max_length=40, blank=True, null=True)
    mwi_subscribe_replaces_unsolicited = models.CharField(max_length=5, blank=True, null=True)
    deny = models.CharField(max_length=95, blank=True, null=True,default="0.0.0.0/0")
    permit = models.CharField(max_length=95, blank=True, null=True,default="0.0.0.0/0")
    acl = models.CharField(max_length=40, blank=True, null=True)
    contact_deny = models.CharField(max_length=95, blank=True, null=True)
    contact_permit = models.CharField(max_length=95, blank=True, null=True)
    contact_acl = models.CharField(max_length=40, blank=True, null=True)
    subscribe_context = models.CharField(max_length=40, blank=True, null=True)
    fax_detect_timeout = models.IntegerField(blank=True, null=True)
    contact_user = models.CharField(max_length=80, blank=True, null=True)
    preferred_codec_only = models.CharField(max_length=3, blank=True, null=True)
    asymmetric_rtp_codec = models.CharField(max_length=3, blank=True, null=True)
    rtcp_mux = models.CharField(max_length=3, blank=True, null=True,default="no")
    allow_overlap = models.CharField(max_length=3, blank=True, null=True)
    refer_blind_progress = models.CharField(max_length=3, blank=True, null=True)
    notify_early_inuse_ringing = models.CharField(max_length=3, blank=True, null=True)
    max_audio_streams = models.IntegerField(blank=True, null=True)
    max_video_streams = models.IntegerField(blank=True, null=True)
    webrtc = models.CharField(max_length=3, blank=True, null=True)
    dtls_fingerprint = models.CharField(max_length=7, blank=True, null=True)
    incoming_mwi_mailbox = models.CharField(max_length=40, blank=True, null=True)
    bundle = models.CharField(max_length=3, blank=True, null=True)
    dtls_auto_generate_cert = models.CharField(max_length=3, blank=True, null=True)
    follow_early_media_fork = models.CharField(max_length=3, blank=True, null=True)
    accept_multiple_sdp_answers = models.CharField(max_length=3, blank=True, null=True)
    suppress_q850_reason_headers = models.CharField(max_length=3, blank=True, null=True)
    trust_connected_line = models.CharField(max_length=5, blank=True, null=True)
    send_connected_line = models.CharField(max_length=5, blank=True, null=True,default="yes")
    ignore_183_without_sdp = models.CharField(max_length=5, blank=True, null=True)
    codec_prefs_incoming_offer = models.CharField(max_length=128, blank=True, null=True)
    codec_prefs_outgoing_offer = models.CharField(max_length=128, blank=True, null=True)
    codec_prefs_incoming_answer = models.CharField(max_length=128, blank=True, null=True)
    codec_prefs_outgoing_answer = models.CharField(max_length=128, blank=True, null=True)
    stir_shaken = models.CharField(max_length=5, blank=True, null=True)
    send_history_info = models.CharField(max_length=5, blank=True, null=True)
    allow_unauthenticated_options = models.CharField(max_length=5, blank=True, null=True)
    t38_bind_udptl_to_media_address = models.CharField(max_length=5, blank=True, null=True)
    geoloc_incoming_call_profile = models.CharField(max_length=80, blank=True, null=True)
    geoloc_outgoing_call_profile = models.CharField(max_length=80, blank=True, null=True)
    incoming_call_offer_pref = models.CharField(max_length=12, blank=True, null=True)
    outgoing_call_offer_pref = models.CharField(max_length=12, blank=True, null=True)
    stir_shaken_profile = models.CharField(max_length=80, blank=True, null=True)
    security_negotiation = models.CharField(max_length=8, blank=True, null=True)
    security_mechanisms = models.CharField(max_length=512, blank=True, null=True)
    send_aoc = models.CharField(max_length=5, blank=True, null=True)
    overlap_context = models.CharField(max_length=80, blank=True, null=True)
    PsjsipAdd = models.CharField(max_length=255, blank=True, null=True) 
    #PsjsipAdd = models.ForeignKey(PsjsipAdd, on_delete=models.CASCADE, related_name='PsEndpoints',default='Değer' )
    class Meta:
        verbose_name = 'PsEndpoints'
        verbose_name_plural = 'PsEndpoints'
       # managed = False
        db_table = 'ps_endpoints'
                             
class PsjsipAdd(models.Model):
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    transport = models.CharField(max_length=40, blank=True, null=True,default="transport-udp")
    aors = models.CharField(max_length=200, blank=True, null=True)
    auth = models.CharField(max_length=40, blank=True, null=True)
    context = models.CharField(max_length=40, blank=True, null=True,default="testing")
    disallow = models.CharField(max_length=200, blank=True, null=True,default="all")
    allow = models.CharField(max_length=200, blank=True, null=True,default="ulaw,alaw,g722,gsm,vp9,vp8,h264")
    direct_media = models.CharField(max_length=3, blank=True, null=True,default="no")
    mailboxes = models.CharField(max_length=40, blank=True, null=True)
    deny = models.CharField(max_length=95, blank=True, null=True,default="0.0.0.0/0")
    permit = models.CharField(max_length=95, blank=True, null=True,default="0.0.0.0/0")
    max_contacts = models.IntegerField(blank=True, null=True,default="1")
    qualify_frequency = models.IntegerField(blank=True, null=True,default="30")
    auth_type = models.CharField(max_length=12, blank=True, null=True,default="userpass")
    password = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    DahiliGrup = models.CharField(max_length=40, blank=True, null=True)
    Sube = models.CharField(max_length=40, blank=True, null=True)
    ps_aors = models.ForeignKey(PsAors, on_delete=models.CASCADE, blank=True,default='Değer',)
    ps_endpoints = models.ForeignKey(PsEndpoints, on_delete=models.CASCADE, blank=True, default='Değer',)
    ps_auths = models.ForeignKey(PsAuths, on_delete=models.CASCADE, blank=True, default='Değer',)
    
     
    class Meta:
        # managed = False
        db_table = 'PsjsipAdd'
        verbose_name = 'PsjsipAdd'
        verbose_name_plural = 'PsjsipAdd'
    



    def save(self, *args, **kwargs):
        # psauths = PsAuths.objects.get(id=self.id) 
        # PsAors, PsAuths ve PsEndpoints modellerine de veri eklenmesini sağlayan kodlar
        ps_endpoints = PsEndpoints.objects.create( id = self.id,
                        transport =self.transport,
                        aors = self.id,
                        auth = self.id,
                        context = self.context,
                        disallow =self.disallow,
                        allow =self.allow,
                        direct_media =self.direct_media, 
                        mailboxes =self.mailboxes,
                        deny = self.deny,
                        permit = self.permit,
                        )
        ps_endpoints.save()
        ps_aors = PsAors.objects.create(id = self.id,
                           max_contacts=self.max_contacts,
                           qualify_frequency=self.qualify_frequency,
                           
                           )
        ps_aors.save()
        ps_auths = PsAuths.objects.create(id = self.id,
                               auth_type=self.auth_type,
                               password=self.password,
                               username=self.username,
                               
                               )
        ps_auths.save()

        self.ps_aors = ps_aors
        self.ps_auths = ps_auths
        self.ps_endpoints = ps_endpoints

        super(PsjsipAdd, self).save(*args, **kwargs)       
        

class PsContacts(models.Model):
    id = models.CharField(primary_key=True,unique=True, max_length=255, blank=True, )
    uri = models.CharField(max_length=511, blank=True, null=True)
    expiration_time = models.BigIntegerField(blank=True, null=True)
    qualify_frequency = models.IntegerField(blank=True, null=True)
    outbound_proxy = models.CharField(max_length=40, blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    qualify_timeout = models.FloatField(blank=True, null=True)
    reg_server = models.CharField(max_length=255, blank=True, null=True)
    authenticate_qualify = models.CharField(max_length=3, blank=True, null=True)
    via_addr = models.CharField(max_length=40, blank=True, null=True)
    via_port = models.IntegerField(blank=True, null=True)
    call_id = models.CharField(max_length=255, blank=True, null=True)
    endpoint = models.CharField(max_length=40, blank=True, null=True)
    prune_on_boot = models.CharField(max_length=3, blank=True, null=True)
    
    

    class Meta:
        
        managed = False
        db_table = 'ps_contacts'
        verbose_name = 'ps_contacts'
        verbose_name_plural = 'ps_contacts'
        unique_together = (('id', 'reg_server'),)
             

class PsEndpointIdIps(models.Model):
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    endpoint = models.CharField(max_length=40, blank=True, null=True)
    match = models.CharField(max_length=80, blank=True, null=True)
    srv_lookups = models.CharField(max_length=3, blank=True, null=True)
    match_header = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_endpoint_id_ips'
        verbose_name = 'PsEndpointIdIps'
        verbose_name_plural = 'PsEndpointIdIps'
            
class PsDomainAliases(models.Model):
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    domain = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_domain_aliases'
        verbose_name = 'PsDomainAliases'
        verbose_name_plural = 'PsDomainAliases'

class CustemCdrTables(models.Model):
    Event = models.CharField(max_length=80, blank=True, null=True)
    Privilege = models.CharField(max_length=80, blank=True, null=True)
    SequenceNumber = models.CharField(max_length=80, blank=True, null=True)
    File  = models.CharField(max_length=80, blank=True, null=True)
    Line = models.CharField(max_length=80, blank=True, null=True)
    Func = models.CharField(max_length=80, blank=True, null=True)
    AccountCode = models.CharField(max_length=80, blank=True, null=True)
    Source   = models.CharField(max_length=80, blank=True, null=True)
    Destination  = models.CharField(max_length=80, blank=True, null=True)
    DestinationContext= models.CharField(max_length=80, blank=True, null=True) 
    CallerID = models.CharField(max_length=80, blank=True, null=True)
    Channel = models.CharField(max_length=80, blank=True, null=True)
    DestinationChannel  = models.CharField(max_length=80, blank=True, null=True)
    LastApplication = models.CharField(max_length=80, blank=True, null=True)
    LastData = models.CharField(max_length=80, blank=True, null=True)
    StartTime = models.CharField(max_length=80, blank=True, null=True)
    AnswerTime = models.CharField(max_length=80, blank=True, null=True)
    EndTime  = models.CharField(max_length=80, blank=True, null=True)
    Duration = models.IntegerField(blank=True, null=True)
    BillableSeconds = models.IntegerField(blank=True, null=True)
    Disposition = models.CharField(max_length=80, blank=True, null=True)
    AMAFlags = models.CharField(max_length=80, blank=True, null=True)
    UniqueID = models.CharField(max_length=80, blank=True, null=True)
    UserField = models.CharField(max_length=80, blank=True, null=True)
    Rate = models.CharField(max_length=80, blank=True, null=True)
    Carrier = models.CharField(max_length=80, blank=True, null=True)
    Calltype = models.CharField(max_length=80, blank=True, null=True)
    Companyid = models.CharField(max_length=80, blank=True, null=True)
    Specialid = models.CharField(max_length=80, blank=True, null=True)
    Recordid = models.CharField(max_length=80, blank=True, null=True)
    Likid = models.CharField(max_length=80, blank=True, null=True)
    
    class Meta:
        # managed = False
        db_table = 'CustemCdrTables'
        verbose_name = 'CustemCdr_Tables'
        verbose_name_plural = 'CustemCdr_Tables'

#old
class CdrTables(models.Model):
    clid = models.CharField(max_length=80, blank=True, null=True)
    src = models.CharField(max_length=80, blank=True, null=True)
    dst = models.CharField(max_length=80, blank=True, null=True)
    dcontext = models.CharField(max_length=80, blank=True, null=True)
    channel = models.CharField(max_length=80, blank=True, null=True)
    dstchannel = models.CharField(max_length=80, blank=True, null=True)
    lastapp = models.CharField(max_length=80, blank=True, null=True)
    lastdata = models.CharField(max_length=80, blank=True, null=True)
    duration = models.IntegerField( blank=True, null=True)
    billsec = models.IntegerField(blank=True, null=True)
    disposition = models.CharField(max_length=45, blank=True, null=True)
    amaflags = models.IntegerField( blank=True, null=True)
    accountcode = models.CharField(max_length=20, blank=True, null=True)
    uniqueid = models.CharField(max_length=150, blank=True, null=True)
    userfield = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        # managed = False
        db_table = 'CdrTables'
        verbose_name = 'Cdr_Tables'
        verbose_name_plural = 'Cdr_Tables'
    
    
class cdr(models.Model):
    calldate = models.DateTimeField(blank=True, null=True)
    clid = models.CharField(max_length=80, blank=True, null=True)
    src = models.CharField(max_length=80, blank=True, null=True)
    dst = models.CharField(max_length=80, blank=True, null=True)
    dcontext = models.CharField(max_length=80, blank=True, null=True)
    channel = models.CharField(max_length=80, blank=True, null=True)
    dstchannel = models.CharField(max_length=80, blank=True, null=True)
    lastapp = models.CharField(max_length=80, blank=True, null=True)
    lastdata = models.CharField(max_length=80, blank=True, null=True)
    duration = models.IntegerField( blank=True, null=True)
    billsec = models.IntegerField(blank=True, null=True)
    disposition = models.CharField(max_length=45, blank=True, null=True)
    amaflags = models.IntegerField( blank=True, null=True)
    accountcode = models.CharField(max_length=30, blank=True, null=True)
    uniqueid = models.CharField(max_length=150, blank=True, null=True)
    userfield = models.CharField(max_length=255, blank=True, null=True)
    peeraccount = models.CharField(max_length=255, blank=True, null=True)
    linkedid = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.CharField(max_length=255, blank=True, null=True)
    # usegmtime = models.CharField(max_length=255, blank=True, null=True)
    # hrtime = models.CharField(max_length=255, blank=True, null=True)
    # loguniqueid = models.CharField(max_length=255, blank=True, null=True)
    # linkedid = models.CharField(max_length=255, blank=True, null=True)
    # calltype = models.CharField(max_length=255, blank=True, null=True)
    # callresult = models.CharField(max_length=255, blank=True, null=True)
    # callcost = models.CharField(max_length=255, blank=True, null=True)
    # callsource = models.CharField(max_length=255, blank=True, null=True)
    # calldestination = models.CharField(max_length=255, blank=True, null=True)
    # callprotocol = models.CharField(max_length=255, blank=True, null=True)
    # callquality = models.CharField(max_length=255, blank=True, null=True)
    # callrecording = models.CharField(max_length=255, blank=True, null=True)
    # callnote = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        # managed = False
        db_table = 'cdr'
        verbose_name = 'Cdr_Tables'
        verbose_name_plural = 'Cdr_Tables'


class Queues(models.Model):

    Ast_strategy = [
        
        ('ringall', 'Ring All'),
        ('leastrecent', 'Least Recent'),
        ('fewestcalls', 'Fewest Calls'),
        ('random', 'Random'),
        ('roundrobin', 'roundrobin'),
        ('rrmemory', 'Round Robin Memory'),
        ('linear', 'Linear'),
        ('wrandom', 'Weighted Random'),
        ('rrordered', 'Round Robin Ordered')
        
    ]
    yes_no={
        ('yes', 'yes'),
        ('no', 'no'),
        
    }
    
    name = models.CharField(primary_key=True, max_length=128)
    musiconhold = models.CharField(max_length=128, blank=True, null=True,default="default")
    announce = models.CharField(max_length=128, blank=True, null=True)
    context = models.CharField(max_length=128, blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True,default=15)
    ringinuse = models.CharField(max_length=3, blank=True, null=True,default="no", choices=yes_no)
    setinterfacevar = models.CharField(max_length=3, blank=True, null=True)
    setqueuevar = models.CharField(max_length=3, blank=True, null=True)
    setqueueentryvar = models.CharField(max_length=3, blank=True, null=True)
    monitor_format = models.CharField(max_length=8, blank=True, null=True)
    membermacro = models.CharField(max_length=512, blank=True, null=True)
    membergosub = models.CharField(max_length=512, blank=True, null=True)
    queue_youarenext = models.CharField(max_length=128, blank=True, null=True)
    queue_thereare = models.CharField(max_length=128, blank=True, null=True)
    queue_callswaiting = models.CharField(max_length=128, blank=True, null=True)
    queue_quantity1 = models.CharField(max_length=128, blank=True, null=True)
    queue_quantity2 = models.CharField(max_length=128, blank=True, null=True)
    queue_holdtime = models.CharField(max_length=128, blank=True, null=True, choices=yes_no,default="yes",)
    queue_minutes = models.CharField(max_length=128, blank=True, null=True)
    queue_minute = models.CharField(max_length=128, blank=True, null=True)
    queue_seconds = models.CharField(max_length=128, blank=True, null=True)
    queue_thankyou = models.CharField(max_length=128, blank=True, null=True)
    queue_callerannounce = models.CharField(max_length=128, blank=True, null=True)
    queue_reporthold = models.CharField(max_length=128, blank=True, null=True)
    announce_frequency = models.IntegerField(blank=True, null=True)
    announce_to_first_user = models.CharField(max_length=3, blank=True, null=True)
    min_announce_frequency = models.IntegerField(blank=True, null=True)
    announce_round_seconds = models.IntegerField(blank=True, null=True)
    announce_holdtime = models.CharField(max_length=128, blank=True, null=True)
    announce_position = models.CharField(max_length=128, blank=True, null=True)
    announce_position_limit = models.IntegerField(blank=True, null=True)
    periodic_announce = models.CharField(max_length=50, blank=True, null=True)
    periodic_announce_frequency = models.IntegerField(blank=True, null=True)
    relative_periodic_announce = models.CharField(max_length=3, blank=True, null=True)
    random_periodic_announce = models.CharField(max_length=3, blank=True, null=True)
    retry = models.IntegerField(blank=True, null=True,default=5)
    wrapuptime = models.IntegerField(blank=True, null=True,default=5)
    penaltymemberslimit = models.IntegerField(blank=True, null=True)
    autofill = models.CharField(max_length=3, blank=True, null=True)
    monitor_type = models.CharField(max_length=128, blank=True, null=True)
    autopause = models.CharField(max_length=3, blank=True, null=True)
    autopausedelay = models.IntegerField(blank=True, null=True)
    autopausebusy = models.CharField(max_length=3, blank=True, null=True)
    autopauseunavail = models.CharField(max_length=3, blank=True, null=True)
    maxlen = models.IntegerField(blank=True, null=True)
    servicelevel = models.IntegerField(blank=True, null=True)
    strategy = models.CharField(max_length=11, blank=True, null=True, choices=Ast_strategy)
    joinempty = models.CharField(max_length=128, blank=True, null=True)
    leavewhenempty = models.CharField(max_length=128, blank=True, null=True)
    reportholdtime = models.CharField(max_length=3, blank=True, null=True)
    memberdelay = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    timeoutrestart = models.CharField(max_length=3, blank=True, null=True)
    defaultrule = models.CharField(max_length=128, blank=True, null=True)
    timeoutpriority = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queues'



        
class QueueMembers(models.Model):
    QUEUE_CHOICES = [(q.name, q.name) for q in Queues.objects.all()]
    PJSIP_CHOICES = [(q.id, q.id) for q in PsjsipAdd.objects.all()]
    queue_name = models.CharField(choices=QUEUE_CHOICES,primary_key=True, max_length=80)  # The composite primary key (queue_name, interface) found, that is not supported. The first column is selected.
    interface = models.CharField(max_length=80)
    membername = models.CharField(choices=PJSIP_CHOICES,max_length=80, blank=True, null=True)
    state_interface = models.CharField(max_length=80, blank=True, null=True)
    penalty = models.IntegerField(blank=True, null=True)
    paused = models.IntegerField(blank=True, null=True)
    uniqueid = models.IntegerField(unique=True, null=True) 
    wrapuptime = models.IntegerField(blank=True, null=True)
    ringinuse = models.CharField(max_length=5, blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        self.interface = "PJSIP/" + str(self.membername)
        super().save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'queue_members'
        unique_together = (('queue_name', 'interface'),)



@receiver(post_save, sender=Queues)
def update_queue_choices(sender, **kwargs):
    """
    Updates the QUEUE_CHOICES field in QueueMembers model
    """
    QueueMembers.QUEUE_CHOICES = [(q.name, q.name) for q in Queues.objects.all()]
    
@receiver(post_delete, sender=Queues)
def delete_queue_choices(sender, **kwargs):

    global QUEUE_CHOICES
    QUEUE_CHOICES = [(q.name, q.name) for q in Queues.objects.all()]
    
    
    

class QueueLog(models.Model):
    time = models.DateTimeField(primary_key=True)
    data5 = models.CharField(max_length=255, blank=True, null=True)
    data4 = models.CharField(max_length=255, blank=True, null=True)
    data3 = models.CharField(max_length=255, blank=True, null=True)
    data2 = models.CharField(max_length=255, blank=True, null=True)
    data1 = models.CharField(max_length=255, blank=True, null=True)
    event = models.CharField(max_length=50)
    agent = models.CharField(max_length=50, blank=True, null=True)
    queuename = models.CharField(max_length=50)
    callid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queue_log'
        




class Voicemail(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    context = models.CharField(max_length=80)
    mailbox = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    fullname = models.CharField(max_length=80, blank=True, null=True)
    alias = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    pager = models.CharField(max_length=80, blank=True, null=True)
    attach = models.CharField(max_length=3, blank=True, null=True)
    attachfmt = models.CharField(max_length=10, blank=True, null=True)
    serveremail = models.CharField(max_length=80, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    tz = models.CharField(max_length=30, blank=True, null=True)
    deletevoicemail = models.CharField(max_length=3, blank=True, null=True)
    saycid = models.CharField(max_length=3, blank=True, null=True)
    sendvoicemail = models.CharField(max_length=3, blank=True, null=True)
    review = models.CharField(max_length=3, blank=True, null=True)
    tempgreetwarn = models.CharField(max_length=3, blank=True, null=True)
    operator = models.CharField(max_length=3, blank=True, null=True)
    envelope = models.CharField(max_length=3, blank=True, null=True)
    sayduration = models.IntegerField(blank=True, null=True)
    forcename = models.CharField(max_length=3, blank=True, null=True)
    forcegreetings = models.CharField(max_length=3, blank=True, null=True)
    callback = models.CharField(max_length=80, blank=True, null=True)
    dialout = models.CharField(max_length=80, blank=True, null=True)
    exitcontext = models.CharField(max_length=80, blank=True, null=True)
    maxmsg = models.IntegerField(blank=True, null=True)
    volgain = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    imapuser = models.CharField(max_length=80, blank=True, null=True)
    imappassword = models.CharField(max_length=80, blank=True, null=True)
    imapserver = models.CharField(max_length=80, blank=True, null=True)
    imapport = models.CharField(max_length=8, blank=True, null=True)
    imapflags = models.CharField(max_length=80, blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voicemail'
        
        
        
        
class Musiconhold(models.Model):
    name = models.CharField(primary_key=True, max_length=80)
    mode = models.CharField(max_length=10, blank=True, null=True)
    directory = models.CharField(max_length=255, blank=True, null=True)
    application = models.CharField(max_length=255, blank=True, null=True)
    digit = models.CharField(max_length=1, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    format = models.CharField(max_length=10, blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'musiconhold'


class MusiconholdEntry(models.Model):
    name = models.OneToOneField(Musiconhold, models.DO_NOTHING, db_column='name', primary_key=True)  # The composite primary key (name, position) found, that is not supported. The first column is selected.
    position = models.IntegerField()
    entry = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'musiconhold_entry'
        unique_together = (('name', 'position'),)
        
        
        
        
class CEL(models.Model):
    id = models.AutoField(primary_key=True)
    eventtype = models.CharField(max_length=20)
    eventtime = models.DateTimeField()
    cid_name = models.CharField(max_length=80)
    cid_num = models.CharField(max_length=80)
    cid_ani = models.CharField(max_length=80)
    cid_rdnis = models.CharField(max_length=80)
    cid_dnid = models.CharField(max_length=80)
    exten = models.CharField(max_length=80)
    context = models.CharField(max_length=80)
    channame = models.CharField(max_length=80)
    appname = models.CharField(max_length=80)
    appdata = models.CharField(max_length=80)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=80)
    uniqueid = models.CharField(max_length=80)
    linkedid = models.CharField(max_length=80)
    peer = models.CharField(max_length=80)
    userdeftype = models.CharField(max_length=80)
    userfield = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'cel'