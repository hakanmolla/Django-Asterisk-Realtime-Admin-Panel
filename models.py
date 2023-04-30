# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlembicVersionConfig(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version_config'


class Extensions(models.Model):
    id = models.BigAutoField(primary_key=True)
    context = models.CharField(max_length=40)
    exten = models.CharField(max_length=40)
    priority = models.IntegerField()
    app = models.CharField(max_length=40)
    appdata = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'extensions'
        unique_together = (('context', 'exten', 'priority'),)



class Meetme(models.Model):
    bookid = models.AutoField(primary_key=True)
    confno = models.CharField(max_length=80)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    pin = models.CharField(max_length=20, blank=True, null=True)
    adminpin = models.CharField(max_length=20, blank=True, null=True)
    opts = models.CharField(max_length=20, blank=True, null=True)
    adminopts = models.CharField(max_length=20, blank=True, null=True)
    recordingfilename = models.CharField(max_length=80, blank=True, null=True)
    recordingformat = models.CharField(max_length=10, blank=True, null=True)
    maxusers = models.IntegerField(blank=True, null=True)
    members = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meetme'


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


class PsAsteriskPublications(models.Model):
    id = models.CharField(unique=True, max_length=40)
    devicestate_publish = models.CharField(max_length=40, blank=True, null=True)
    mailboxstate_publish = models.CharField(max_length=40, blank=True, null=True)
    device_state = models.CharField(max_length=3, blank=True, null=True)
    device_state_filter = models.CharField(max_length=256, blank=True, null=True)
    mailbox_state = models.CharField(max_length=3, blank=True, null=True)
    mailbox_state_filter = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_asterisk_publications'



class PsContacts(models.Model):
    id = models.CharField(unique=True, max_length=255, blank=True, null=True)
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
        unique_together = (('id', 'reg_server'),)




class PsGlobals(models.Model):
    id = models.CharField(unique=True, max_length=40)
    max_forwards = models.IntegerField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    default_outbound_endpoint = models.CharField(max_length=40, blank=True, null=True)
    debug = models.CharField(max_length=40, blank=True, null=True)
    endpoint_identifier_order = models.CharField(max_length=40, blank=True, null=True)
    max_initial_qualify_time = models.IntegerField(blank=True, null=True)
    default_from_user = models.CharField(max_length=80, blank=True, null=True)
    keep_alive_interval = models.IntegerField(blank=True, null=True)
    regcontext = models.CharField(max_length=80, blank=True, null=True)
    contact_expiration_check_interval = models.IntegerField(blank=True, null=True)
    default_voicemail_extension = models.CharField(max_length=40, blank=True, null=True)
    disable_multi_domain = models.CharField(max_length=3, blank=True, null=True)
    unidentified_request_count = models.IntegerField(blank=True, null=True)
    unidentified_request_period = models.IntegerField(blank=True, null=True)
    unidentified_request_prune_interval = models.IntegerField(blank=True, null=True)
    default_realm = models.CharField(max_length=40, blank=True, null=True)
    mwi_tps_queue_high = models.IntegerField(blank=True, null=True)
    mwi_tps_queue_low = models.IntegerField(blank=True, null=True)
    mwi_disable_initial_unsolicited = models.CharField(max_length=3, blank=True, null=True)
    ignore_uri_user_options = models.CharField(max_length=3, blank=True, null=True)
    use_callerid_contact = models.CharField(max_length=5, blank=True, null=True)
    send_contact_status_on_update_registration = models.CharField(max_length=5, blank=True, null=True)
    taskprocessor_overload_trigger = models.CharField(max_length=10, blank=True, null=True)
    norefersub = models.CharField(max_length=5, blank=True, null=True)
    allow_sending_180_after_183 = models.CharField(max_length=5, blank=True, null=True)
    all_codecs_on_empty_reinvite = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_globals'


class PsInboundPublications(models.Model):
    id = models.CharField(unique=True, max_length=40)
    endpoint = models.CharField(max_length=40, blank=True, null=True)
    event_asterisk_devicestate = models.CharField(db_column='event_asterisk-devicestate', max_length=40, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    event_asterisk_mwi = models.CharField(db_column='event_asterisk-mwi', max_length=40, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ps_inbound_publications'


class PsOutboundPublishes(models.Model):
    id = models.CharField(unique=True, max_length=40)
    expiration = models.IntegerField(blank=True, null=True)
    outbound_auth = models.CharField(max_length=40, blank=True, null=True)
    outbound_proxy = models.CharField(max_length=256, blank=True, null=True)
    server_uri = models.CharField(max_length=256, blank=True, null=True)
    from_uri = models.CharField(max_length=256, blank=True, null=True)
    to_uri = models.CharField(max_length=256, blank=True, null=True)
    event = models.CharField(max_length=40, blank=True, null=True)
    max_auth_attempts = models.IntegerField(blank=True, null=True)
    transport = models.CharField(max_length=40, blank=True, null=True)
    multi_user = models.CharField(max_length=3, blank=True, null=True)
    field_body = models.CharField(db_column='@body', max_length=40, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_context = models.CharField(db_column='@context', max_length=256, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_exten = models.CharField(db_column='@exten', max_length=256, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'ps_outbound_publishes'


class PsRegistrations(models.Model):
    id = models.CharField(unique=True, max_length=40)
    auth_rejection_permanent = models.CharField(max_length=3, blank=True, null=True)
    client_uri = models.CharField(max_length=255, blank=True, null=True)
    contact_user = models.CharField(max_length=40, blank=True, null=True)
    expiration = models.IntegerField(blank=True, null=True)
    max_retries = models.IntegerField(blank=True, null=True)
    outbound_auth = models.CharField(max_length=40, blank=True, null=True)
    outbound_proxy = models.CharField(max_length=40, blank=True, null=True)
    retry_interval = models.IntegerField(blank=True, null=True)
    forbidden_retry_interval = models.IntegerField(blank=True, null=True)
    server_uri = models.CharField(max_length=255, blank=True, null=True)
    transport = models.CharField(max_length=40, blank=True, null=True)
    support_path = models.CharField(max_length=3, blank=True, null=True)
    fatal_retry_interval = models.IntegerField(blank=True, null=True)
    line = models.CharField(max_length=3, blank=True, null=True)
    endpoint = models.CharField(max_length=40, blank=True, null=True)
    support_outbound = models.CharField(max_length=5, blank=True, null=True)
    contact_header_params = models.CharField(max_length=255, blank=True, null=True)
    max_random_initial_delay = models.IntegerField(blank=True, null=True)
    security_negotiation = models.CharField(max_length=8, blank=True, null=True)
    security_mechanisms = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_registrations'


class PsResourceList(models.Model):
    id = models.CharField(unique=True, max_length=40)
    list_item = models.CharField(max_length=2048, blank=True, null=True)
    event = models.CharField(max_length=40, blank=True, null=True)
    full_state = models.CharField(max_length=3, blank=True, null=True)
    notification_batch_interval = models.IntegerField(blank=True, null=True)
    resource_display_name = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_resource_list'


class PsSubscriptionPersistence(models.Model):
    id = models.CharField(unique=True, max_length=40)
    packet = models.CharField(max_length=2048, blank=True, null=True)
    src_name = models.CharField(max_length=128, blank=True, null=True)
    src_port = models.IntegerField(blank=True, null=True)
    transport_key = models.CharField(max_length=64, blank=True, null=True)
    local_name = models.CharField(max_length=128, blank=True, null=True)
    local_port = models.IntegerField(blank=True, null=True)
    cseq = models.IntegerField(blank=True, null=True)
    tag = models.CharField(max_length=128, blank=True, null=True)
    endpoint = models.CharField(max_length=40, blank=True, null=True)
    expires = models.IntegerField(blank=True, null=True)
    contact_uri = models.CharField(max_length=256, blank=True, null=True)
    prune_on_boot = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_subscription_persistence'


class PsSystems(models.Model):
    id = models.CharField(unique=True, max_length=40)
    timer_t1 = models.IntegerField(blank=True, null=True)
    timer_b = models.IntegerField(blank=True, null=True)
    compact_headers = models.CharField(max_length=3, blank=True, null=True)
    threadpool_initial_size = models.IntegerField(blank=True, null=True)
    threadpool_auto_increment = models.IntegerField(blank=True, null=True)
    threadpool_idle_timeout = models.IntegerField(blank=True, null=True)
    threadpool_max_size = models.IntegerField(blank=True, null=True)
    disable_tcp_switch = models.CharField(max_length=3, blank=True, null=True)
    follow_early_media_fork = models.CharField(max_length=3, blank=True, null=True)
    accept_multiple_sdp_answers = models.CharField(max_length=3, blank=True, null=True)
    disable_rport = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_systems'


class PsTransports(models.Model):
    id = models.CharField(unique=True, max_length=40)
    async_operations = models.IntegerField(blank=True, null=True)
    bind = models.CharField(max_length=40, blank=True, null=True)
    ca_list_file = models.CharField(max_length=200, blank=True, null=True)
    cert_file = models.CharField(max_length=200, blank=True, null=True)
    cipher = models.CharField(max_length=200, blank=True, null=True)
    domain = models.CharField(max_length=40, blank=True, null=True)
    external_media_address = models.CharField(max_length=40, blank=True, null=True)
    external_signaling_address = models.CharField(max_length=40, blank=True, null=True)
    external_signaling_port = models.IntegerField(blank=True, null=True)
    method = models.CharField(max_length=11, blank=True, null=True)
    local_net = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    priv_key_file = models.CharField(max_length=200, blank=True, null=True)
    protocol = models.CharField(max_length=4, blank=True, null=True)
    require_client_cert = models.CharField(max_length=3, blank=True, null=True)
    verify_client = models.CharField(max_length=3, blank=True, null=True)
    verify_server = models.CharField(max_length=3, blank=True, null=True)
    tos = models.CharField(max_length=10, blank=True, null=True)
    cos = models.IntegerField(blank=True, null=True)
    allow_reload = models.CharField(max_length=3, blank=True, null=True)
    symmetric_transport = models.CharField(max_length=3, blank=True, null=True)
    allow_wildcard_certs = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_transports'



class QueueRules(models.Model):
    rule_name = models.CharField(max_length=80)
    time = models.CharField(max_length=32)
    min_penalty = models.CharField(max_length=32)
    max_penalty = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'queue_rules'


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
