from django.db import models


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

    class Meta:
        managed = False
        db_table = 'ps_auths'
        verbose_name = 'ps_auths'
        verbose_name_plural = 'ps_auths'


class PsAors(models.Model):

    
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    contact = models.CharField(max_length=255, blank=True, null=True)
    default_expiration = models.IntegerField(blank=True, null=True)
    mailboxes = models.CharField(max_length=80, blank=True, null=True)
    max_contacts = models.IntegerField(blank=True, null=True)
    minimum_expiration = models.IntegerField(blank=True, null=True)
    remove_existing = models.CharField(max_length=3, blank=True, null=True)
    qualify_frequency = models.IntegerField(blank=True, null=True)
    authenticate_qualify = models.CharField(max_length=3, blank=True, null=True)
    maximum_expiration = models.IntegerField(blank=True, null=True)
    outbound_proxy = models.CharField(max_length=40, blank=True, null=True)
    support_path = models.CharField(max_length=3, blank=True, null=True)
    qualify_timeout = models.FloatField(blank=True, null=True)
    voicemail_extension = models.CharField(max_length=40, blank=True, null=True)
    remove_unavailable = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_aors'
        verbose_name = 'ps_aors'
        verbose_name_plural = 'ps_aors'
            

class PsEndpoints(models.Model):
    id = models.CharField(primary_key=True,unique=True, max_length=40)
    transport = models.CharField(max_length=40, blank=True, null=True)
    aors = models.CharField(max_length=200, blank=True, null=True)
    auth = models.CharField(max_length=40, blank=True, null=True)
    context = models.CharField(max_length=40, blank=True, null=True)
    disallow = models.CharField(max_length=200, blank=True, null=True)
    allow = models.CharField(max_length=200, blank=True, null=True)
    direct_media = models.CharField(max_length=3, blank=True, null=True)
    connected_line_method = models.CharField(max_length=8, blank=True, null=True)
    direct_media_method = models.CharField(max_length=8, blank=True, null=True)
    direct_media_glare_mitigation = models.CharField(max_length=8, blank=True, null=True)
    disable_direct_media_on_nat = models.CharField(max_length=3, blank=True, null=True)
    dtmf_mode = models.CharField(max_length=9, blank=True, null=True)
    external_media_address = models.CharField(max_length=40, blank=True, null=True)
    force_rport = models.CharField(max_length=3, blank=True, null=True)
    ice_support = models.CharField(max_length=3, blank=True, null=True)
    identify_by = models.CharField(max_length=80, blank=True, null=True)
    mailboxes = models.CharField(max_length=40, blank=True, null=True)
    moh_suggest = models.CharField(max_length=40, blank=True, null=True)
    outbound_auth = models.CharField(max_length=40, blank=True, null=True)
    outbound_proxy = models.CharField(max_length=40, blank=True, null=True)
    rewrite_contact = models.CharField(max_length=3, blank=True, null=True)
    rtp_ipv6 = models.CharField(max_length=3, blank=True, null=True)
    rtp_symmetric = models.CharField(max_length=3, blank=True, null=True)
    send_diversion = models.CharField(max_length=3, blank=True, null=True)
    send_pai = models.CharField(max_length=3, blank=True, null=True)
    send_rpid = models.CharField(max_length=3, blank=True, null=True)
    timers_min_se = models.IntegerField(blank=True, null=True)
    timers = models.CharField(max_length=8, blank=True, null=True)
    timers_sess_expires = models.IntegerField(blank=True, null=True)
    callerid = models.CharField(max_length=40, blank=True, null=True)
    callerid_privacy = models.CharField(max_length=23, blank=True, null=True)
    callerid_tag = models.CharField(max_length=40, blank=True, null=True)
    number_100rel = models.CharField(db_column='100rel', max_length=14, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    aggregate_mwi = models.CharField(max_length=3, blank=True, null=True)
    trust_id_inbound = models.CharField(max_length=3, blank=True, null=True)
    trust_id_outbound = models.CharField(max_length=3, blank=True, null=True)
    use_ptime = models.CharField(max_length=3, blank=True, null=True)
    use_avpf = models.CharField(max_length=3, blank=True, null=True)
    media_encryption = models.CharField(max_length=4, blank=True, null=True)
    inband_progress = models.CharField(max_length=3, blank=True, null=True)
    call_group = models.CharField(max_length=40, blank=True, null=True)
    pickup_group = models.CharField(max_length=40, blank=True, null=True)
    named_call_group = models.CharField(max_length=40, blank=True, null=True)
    named_pickup_group = models.CharField(max_length=40, blank=True, null=True)
    device_state_busy_at = models.IntegerField(blank=True, null=True)
    fax_detect = models.CharField(max_length=3, blank=True, null=True)
    t38_udptl = models.CharField(max_length=3, blank=True, null=True)
    t38_udptl_ec = models.CharField(max_length=10, blank=True, null=True)
    t38_udptl_maxdatagram = models.IntegerField(blank=True, null=True)
    t38_udptl_nat = models.CharField(max_length=3, blank=True, null=True)
    t38_udptl_ipv6 = models.CharField(max_length=3, blank=True, null=True)
    tone_zone = models.CharField(max_length=40, blank=True, null=True)
    language = models.CharField(max_length=40, blank=True, null=True)
    one_touch_recording = models.CharField(max_length=3, blank=True, null=True)
    record_on_feature = models.CharField(max_length=40, blank=True, null=True)
    record_off_feature = models.CharField(max_length=40, blank=True, null=True)
    rtp_engine = models.CharField(max_length=40, blank=True, null=True)
    allow_transfer = models.CharField(max_length=3, blank=True, null=True)
    allow_subscribe = models.CharField(max_length=3, blank=True, null=True)
    sdp_owner = models.CharField(max_length=40, blank=True, null=True)
    sdp_session = models.CharField(max_length=40, blank=True, null=True)
    tos_audio = models.CharField(max_length=10, blank=True, null=True)
    tos_video = models.CharField(max_length=10, blank=True, null=True)
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
    cos_audio = models.IntegerField(blank=True, null=True)
    cos_video = models.IntegerField(blank=True, null=True)
    message_context = models.CharField(max_length=40, blank=True, null=True)
    force_avp = models.CharField(max_length=3, blank=True, null=True)
    media_use_received_transport = models.CharField(max_length=3, blank=True, null=True)
    accountcode = models.CharField(max_length=80, blank=True, null=True)
    user_eq_phone = models.CharField(max_length=3, blank=True, null=True)
    moh_passthrough = models.CharField(max_length=3, blank=True, null=True)
    media_encryption_optimistic = models.CharField(max_length=3, blank=True, null=True)
    rpid_immediate = models.CharField(max_length=3, blank=True, null=True)
    g726_non_standard = models.CharField(max_length=3, blank=True, null=True)
    rtp_keepalive = models.IntegerField(blank=True, null=True)
    rtp_timeout = models.IntegerField(blank=True, null=True)
    rtp_timeout_hold = models.IntegerField(blank=True, null=True)
    bind_rtp_to_media_address = models.CharField(max_length=3, blank=True, null=True)
    voicemail_extension = models.CharField(max_length=40, blank=True, null=True)
    mwi_subscribe_replaces_unsolicited = models.CharField(max_length=5, blank=True, null=True)
    deny = models.CharField(max_length=95, blank=True, null=True)
    permit = models.CharField(max_length=95, blank=True, null=True)
    acl = models.CharField(max_length=40, blank=True, null=True)
    contact_deny = models.CharField(max_length=95, blank=True, null=True)
    contact_permit = models.CharField(max_length=95, blank=True, null=True)
    contact_acl = models.CharField(max_length=40, blank=True, null=True)
    subscribe_context = models.CharField(max_length=40, blank=True, null=True)
    fax_detect_timeout = models.IntegerField(blank=True, null=True)
    contact_user = models.CharField(max_length=80, blank=True, null=True)
    preferred_codec_only = models.CharField(max_length=3, blank=True, null=True)
    asymmetric_rtp_codec = models.CharField(max_length=3, blank=True, null=True)
    rtcp_mux = models.CharField(max_length=3, blank=True, null=True)
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
    send_connected_line = models.CharField(max_length=5, blank=True, null=True)
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

    class Meta:
        verbose_name = 'PsEndpoints'
        verbose_name_plural = 'PsEndpoints'
        managed = False
        db_table = 'ps_endpoints'
              

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







      

