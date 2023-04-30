# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cdrtables(models.Model):
    id = models.BigAutoField(primary_key=True)
    clid = models.CharField(max_length=80, blank=True, null=True)
    src = models.CharField(max_length=80, blank=True, null=True)
    dst = models.CharField(max_length=80, blank=True, null=True)
    dcontext = models.CharField(max_length=80, blank=True, null=True)
    channel = models.CharField(max_length=80, blank=True, null=True)
    dstchannel = models.CharField(max_length=80, blank=True, null=True)
    lastapp = models.CharField(max_length=80, blank=True, null=True)
    lastdata = models.CharField(max_length=80, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    billsec = models.IntegerField(blank=True, null=True)
    disposition = models.CharField(max_length=45, blank=True, null=True)
    amaflags = models.IntegerField(blank=True, null=True)
    accountcode = models.CharField(max_length=20, blank=True, null=True)
    uniqueid = models.CharField(max_length=150, blank=True, null=True)
    userfield = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CdrTables'


class Custemcdrtables(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.CharField(db_column='Event', max_length=80, blank=True, null=True)  # Field name made lowercase.
    privilege = models.CharField(db_column='Privilege', max_length=80, blank=True, null=True)  # Field name made lowercase.
    sequencenumber = models.CharField(db_column='SequenceNumber', max_length=80, blank=True, null=True)  # Field name made lowercase.
    file = models.CharField(db_column='File', max_length=80, blank=True, null=True)  # Field name made lowercase.
    line = models.CharField(db_column='Line', max_length=80, blank=True, null=True)  # Field name made lowercase.
    func = models.CharField(db_column='Func', max_length=80, blank=True, null=True)  # Field name made lowercase.
    accountcode = models.CharField(db_column='AccountCode', max_length=80, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=80, blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=80, blank=True, null=True)  # Field name made lowercase.
    destinationcontext = models.CharField(db_column='DestinationContext', max_length=80, blank=True, null=True)  # Field name made lowercase.
    callerid = models.CharField(db_column='CallerID', max_length=80, blank=True, null=True)  # Field name made lowercase.
    channel = models.CharField(db_column='Channel', max_length=80, blank=True, null=True)  # Field name made lowercase.
    destinationchannel = models.CharField(db_column='DestinationChannel', max_length=80, blank=True, null=True)  # Field name made lowercase.
    lastapplication = models.CharField(db_column='LastApplication', max_length=80, blank=True, null=True)  # Field name made lowercase.
    lastdata = models.CharField(db_column='LastData', max_length=80, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=80, blank=True, null=True)  # Field name made lowercase.
    answertime = models.CharField(db_column='AnswerTime', max_length=80, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=80, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    billableseconds = models.IntegerField(db_column='BillableSeconds', blank=True, null=True)  # Field name made lowercase.
    disposition = models.CharField(db_column='Disposition', max_length=80, blank=True, null=True)  # Field name made lowercase.
    amaflags = models.CharField(db_column='AMAFlags', max_length=80, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='UniqueID', max_length=80, blank=True, null=True)  # Field name made lowercase.
    calltype = models.CharField(db_column='Calltype', max_length=80, blank=True, null=True)  # Field name made lowercase.
    carrier = models.CharField(db_column='Carrier', max_length=80, blank=True, null=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='Companyid', max_length=80, blank=True, null=True)  # Field name made lowercase.
    likid = models.CharField(db_column='Likid', max_length=80, blank=True, null=True)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=80, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='Recordid', max_length=80, blank=True, null=True)  # Field name made lowercase.
    specialid = models.CharField(db_column='Specialid', max_length=80, blank=True, null=True)  # Field name made lowercase.
    userfield = models.CharField(db_column='UserField', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustemCdrTables'


class Psjsipadd(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
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
    max_contacts = models.IntegerField(blank=True, null=True)
    qualify_frequency = models.IntegerField(blank=True, null=True)
    auth_type = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    dahiligrup = models.CharField(db_column='DahiliGrup', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sube = models.CharField(db_column='Sube', max_length=40, blank=True, null=True)  # Field name made lowercase.
    psjsipadd_id = models.CharField(db_column='PsjsipAdd_id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ps_aors = models.ForeignKey('PsAors', models.DO_NOTHING)
    ps_auths = models.ForeignKey('PsAuths', models.DO_NOTHING)
    ps_endpoints = models.ForeignKey('PsEndpoints', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'PsjsipAdd'


class AlembicVersionConfig(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version_config'


class Ast20PsjsipaddOlldd(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
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
    max_contacts = models.IntegerField(blank=True, null=True)
    qualify_frequency = models.IntegerField(blank=True, null=True)
    auth_type = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    dahiligrup = models.CharField(db_column='DahiliGrup', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sube = models.CharField(db_column='Sube', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ast20_psjsipadd-olldd'


class Ast20PsjsipaddOolll(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
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
    max_contacts = models.IntegerField(blank=True, null=True)
    qualify_frequency = models.IntegerField(blank=True, null=True)
    auth_type = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    dahiligrup = models.CharField(db_column='DahiliGrup', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sube = models.CharField(db_column='Sube', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ast20_psjsipadd-oolll'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cdr(models.Model):
    calldate = models.DateTimeField(blank=True, null=True)
    clid = models.CharField(max_length=255, blank=True, null=True)
    src = models.CharField(max_length=255, blank=True, null=True)
    dst = models.CharField(max_length=255, blank=True, null=True)
    dcontext = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    dstchannel = models.CharField(max_length=255, blank=True, null=True)
    lastapp = models.CharField(max_length=255, blank=True, null=True)
    lastdata = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    billsec = models.IntegerField(blank=True, null=True)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    amaflags = models.IntegerField(blank=True, null=True)
    accountcode = models.CharField(max_length=255, blank=True, null=True)
    uniqueid = models.CharField(max_length=255, blank=True, null=True)
    userfield = models.CharField(max_length=255, blank=True, null=True)
    peeraccount = models.CharField(max_length=255, blank=True, null=True)
    linkedid = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdr'


class CdrOll(models.Model):
    id = models.BigAutoField(primary_key=True)
    calldate = models.DateTimeField(blank=True, null=True)
    clid = models.CharField(max_length=80, blank=True, null=True)
    src = models.CharField(max_length=80, blank=True, null=True)
    dst = models.CharField(max_length=80, blank=True, null=True)
    dcontext = models.CharField(max_length=80, blank=True, null=True)
    channel = models.CharField(max_length=80, blank=True, null=True)
    dstchannel = models.CharField(max_length=80, blank=True, null=True)
    lastapp = models.CharField(max_length=80, blank=True, null=True)
    lastdata = models.CharField(max_length=80, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    billsec = models.IntegerField(blank=True, null=True)
    disposition = models.CharField(max_length=45, blank=True, null=True)
    amaflags = models.IntegerField(blank=True, null=True)
    accountcode = models.CharField(max_length=20, blank=True, null=True)
    uniqueid = models.CharField(max_length=150, blank=True, null=True)
    userfield = models.CharField(max_length=255, blank=True, null=True)
    peeraccount = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.CharField(max_length=255, blank=True, null=True)
    linkedid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdr-oll'


class DbPsjsipadd(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    transport = models.CharField(max_length=40, blank=True, null=True)
    aors = models.ForeignKey('PsAors', models.DO_NOTHING, blank=True, null=True)
    auth = models.ForeignKey('PsAuths', models.DO_NOTHING, blank=True, null=True)
    context = models.CharField(max_length=40, blank=True, null=True)
    disallow = models.CharField(max_length=200, blank=True, null=True)
    allow = models.CharField(max_length=200, blank=True, null=True)
    direct_media = models.CharField(max_length=3, blank=True, null=True)
    mailboxes = models.CharField(max_length=40, blank=True, null=True)
    deny = models.CharField(max_length=95, blank=True, null=True)
    permit = models.CharField(max_length=95, blank=True, null=True)
    max_contacts = models.IntegerField(blank=True, null=True)
    qualify_frequency = models.IntegerField(blank=True, null=True)
    auth_type = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    psendpoints = models.ForeignKey('PsEndpoints', models.DO_NOTHING, db_column='PsEndpoints_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db_psjsipadd'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Iaxfriends(models.Model):
    name = models.CharField(unique=True, max_length=40)
    type = models.CharField(max_length=6, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    mailbox = models.CharField(max_length=40, blank=True, null=True)
    secret = models.CharField(max_length=40, blank=True, null=True)
    dbsecret = models.CharField(max_length=40, blank=True, null=True)
    context = models.CharField(max_length=40, blank=True, null=True)
    regcontext = models.CharField(max_length=40, blank=True, null=True)
    host = models.CharField(max_length=40, blank=True, null=True)
    ipaddr = models.CharField(max_length=40, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    defaultip = models.CharField(max_length=20, blank=True, null=True)
    sourceaddress = models.CharField(max_length=20, blank=True, null=True)
    mask = models.CharField(max_length=20, blank=True, null=True)
    regexten = models.CharField(max_length=40, blank=True, null=True)
    regseconds = models.IntegerField(blank=True, null=True)
    accountcode = models.CharField(max_length=80, blank=True, null=True)
    mohinterpret = models.CharField(max_length=20, blank=True, null=True)
    mohsuggest = models.CharField(max_length=20, blank=True, null=True)
    inkeys = models.CharField(max_length=40, blank=True, null=True)
    outkeys = models.CharField(max_length=40, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    callerid = models.CharField(max_length=100, blank=True, null=True)
    cid_number = models.CharField(max_length=40, blank=True, null=True)
    sendani = models.CharField(max_length=3, blank=True, null=True)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    trunk = models.CharField(max_length=3, blank=True, null=True)
    auth = models.CharField(max_length=20, blank=True, null=True)
    maxauthreq = models.IntegerField(blank=True, null=True)
    requirecalltoken = models.CharField(max_length=4, blank=True, null=True)
    encryption = models.CharField(max_length=6, blank=True, null=True)
    transfer = models.CharField(max_length=9, blank=True, null=True)
    jitterbuffer = models.CharField(max_length=3, blank=True, null=True)
    forcejitterbuffer = models.CharField(max_length=3, blank=True, null=True)
    disallow = models.CharField(max_length=200, blank=True, null=True)
    allow = models.CharField(max_length=200, blank=True, null=True)
    codecpriority = models.CharField(max_length=40, blank=True, null=True)
    qualify = models.CharField(max_length=10, blank=True, null=True)
    qualifysmoothing = models.CharField(max_length=3, blank=True, null=True)
    qualifyfreqok = models.CharField(max_length=10, blank=True, null=True)
    qualifyfreqnotok = models.CharField(max_length=10, blank=True, null=True)
    timezone = models.CharField(max_length=20, blank=True, null=True)
    adsi = models.CharField(max_length=3, blank=True, null=True)
    amaflags = models.CharField(max_length=20, blank=True, null=True)
    setvar = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iaxfriends'


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


class PsAors(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
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
    psjsipadd = models.CharField(db_column='PsjsipAdd', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ps_aors'


class PsAorsOld(models.Model):
    id = models.CharField(unique=True, max_length=40)
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
    psjsipadd_id = models.CharField(db_column='PsjsipAdd_id', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ps_aors---old'


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


class PsAuths(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    auth_type = models.CharField(max_length=12, blank=True, null=True)
    nonce_lifetime = models.IntegerField(blank=True, null=True)
    md5_cred = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    realm = models.CharField(max_length=40, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    oauth_clientid = models.CharField(max_length=255, blank=True, null=True)
    oauth_secret = models.CharField(max_length=255, blank=True, null=True)
    psjsipadd = models.CharField(db_column='PsjsipAdd', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ps_auths'


class PsAuthsOlldddd(models.Model):
    id = models.CharField(unique=True, max_length=40)
    auth_type = models.CharField(max_length=12, blank=True, null=True)
    nonce_lifetime = models.IntegerField(blank=True, null=True)
    md5_cred = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    realm = models.CharField(max_length=40, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    oauth_clientid = models.CharField(max_length=255, blank=True, null=True)
    oauth_secret = models.CharField(max_length=255, blank=True, null=True)
    psjsipadd_id = models.CharField(db_column='PsjsipAdd_id', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ps_auths-olldddd'


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


class PsDomainAliases(models.Model):
    id = models.CharField(unique=True, max_length=40)
    domain = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_domain_aliases'


class PsEndpointIdIps(models.Model):
    id = models.CharField(unique=True, max_length=40)
    endpoint = models.CharField(max_length=40, blank=True, null=True)
    match = models.CharField(max_length=80, blank=True, null=True)
    srv_lookups = models.CharField(max_length=3, blank=True, null=True)
    match_header = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_endpoint_id_ips'


class PsEndpoints(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
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
    psjsipadd = models.CharField(db_column='PsjsipAdd', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ps_endpoints'


class PsEndpointsOld(models.Model):
    id = models.CharField(unique=True, max_length=40)
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
    psjsipadd_id = models.CharField(db_column='PsjsipAdd_id', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ps_endpoints-old'


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


class QueueLog(models.Model):
    time = models.DateTimeField()
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


class QueueMembers(models.Model):
    queue_name = models.CharField(primary_key=True, max_length=80)  # The composite primary key (queue_name, interface) found, that is not supported. The first column is selected.
    interface = models.CharField(max_length=80)
    membername = models.CharField(max_length=80, blank=True, null=True)
    state_interface = models.CharField(max_length=80, blank=True, null=True)
    penalty = models.IntegerField(blank=True, null=True)
    paused = models.IntegerField(blank=True, null=True)
    uniqueid = models.AutoField(unique=True)
    wrapuptime = models.IntegerField(blank=True, null=True)
    ringinuse = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queue_members'
        unique_together = (('queue_name', 'interface'),)


class QueueRules(models.Model):
    rule_name = models.CharField(max_length=80)
    time = models.CharField(max_length=32)
    min_penalty = models.CharField(max_length=32)
    max_penalty = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'queue_rules'


class Queues(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    musiconhold = models.CharField(max_length=128, blank=True, null=True)
    announce = models.CharField(max_length=128, blank=True, null=True)
    context = models.CharField(max_length=128, blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    ringinuse = models.CharField(max_length=3, blank=True, null=True)
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
    queue_holdtime = models.CharField(max_length=128, blank=True, null=True)
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
    retry = models.IntegerField(blank=True, null=True)
    wrapuptime = models.IntegerField(blank=True, null=True)
    penaltymemberslimit = models.IntegerField(blank=True, null=True)
    autofill = models.CharField(max_length=3, blank=True, null=True)
    monitor_type = models.CharField(max_length=128, blank=True, null=True)
    autopause = models.CharField(max_length=3, blank=True, null=True)
    autopausedelay = models.IntegerField(blank=True, null=True)
    autopausebusy = models.CharField(max_length=3, blank=True, null=True)
    autopauseunavail = models.CharField(max_length=3, blank=True, null=True)
    maxlen = models.IntegerField(blank=True, null=True)
    servicelevel = models.IntegerField(blank=True, null=True)
    strategy = models.CharField(max_length=11, blank=True, null=True)
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


class Sippeers(models.Model):
    name = models.CharField(unique=True, max_length=40)
    ipaddr = models.CharField(max_length=45, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    regseconds = models.IntegerField(blank=True, null=True)
    defaultuser = models.CharField(max_length=40, blank=True, null=True)
    fullcontact = models.CharField(max_length=80, blank=True, null=True)
    regserver = models.CharField(max_length=20, blank=True, null=True)
    useragent = models.CharField(max_length=255, blank=True, null=True)
    lastms = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=40, blank=True, null=True)
    type = models.CharField(max_length=6, blank=True, null=True)
    context = models.CharField(max_length=40, blank=True, null=True)
    permit = models.CharField(max_length=95, blank=True, null=True)
    deny = models.CharField(max_length=95, blank=True, null=True)
    secret = models.CharField(max_length=40, blank=True, null=True)
    md5secret = models.CharField(max_length=40, blank=True, null=True)
    remotesecret = models.CharField(max_length=40, blank=True, null=True)
    transport = models.CharField(max_length=7, blank=True, null=True)
    dtmfmode = models.CharField(max_length=9, blank=True, null=True)
    directmedia = models.CharField(max_length=8, blank=True, null=True)
    nat = models.CharField(max_length=29, blank=True, null=True)
    callgroup = models.CharField(max_length=40, blank=True, null=True)
    pickupgroup = models.CharField(max_length=40, blank=True, null=True)
    language = models.CharField(max_length=40, blank=True, null=True)
    disallow = models.CharField(max_length=200, blank=True, null=True)
    allow = models.CharField(max_length=200, blank=True, null=True)
    insecure = models.CharField(max_length=40, blank=True, null=True)
    trustrpid = models.CharField(max_length=3, blank=True, null=True)
    progressinband = models.CharField(max_length=5, blank=True, null=True)
    promiscredir = models.CharField(max_length=3, blank=True, null=True)
    useclientcode = models.CharField(max_length=3, blank=True, null=True)
    accountcode = models.CharField(max_length=80, blank=True, null=True)
    setvar = models.CharField(max_length=200, blank=True, null=True)
    callerid = models.CharField(max_length=40, blank=True, null=True)
    amaflags = models.CharField(max_length=40, blank=True, null=True)
    callcounter = models.CharField(max_length=3, blank=True, null=True)
    busylevel = models.IntegerField(blank=True, null=True)
    allowoverlap = models.CharField(max_length=3, blank=True, null=True)
    allowsubscribe = models.CharField(max_length=3, blank=True, null=True)
    videosupport = models.CharField(max_length=3, blank=True, null=True)
    maxcallbitrate = models.IntegerField(blank=True, null=True)
    rfc2833compensate = models.CharField(max_length=3, blank=True, null=True)
    mailbox = models.CharField(max_length=40, blank=True, null=True)
    session_timers = models.CharField(db_column='session-timers', max_length=9, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    session_expires = models.IntegerField(db_column='session-expires', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    session_minse = models.IntegerField(db_column='session-minse', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    session_refresher = models.CharField(db_column='session-refresher', max_length=3, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    t38pt_usertpsource = models.CharField(max_length=40, blank=True, null=True)
    regexten = models.CharField(max_length=40, blank=True, null=True)
    fromdomain = models.CharField(max_length=40, blank=True, null=True)
    fromuser = models.CharField(max_length=40, blank=True, null=True)
    qualify = models.CharField(max_length=40, blank=True, null=True)
    defaultip = models.CharField(max_length=45, blank=True, null=True)
    rtptimeout = models.IntegerField(blank=True, null=True)
    rtpholdtimeout = models.IntegerField(blank=True, null=True)
    sendrpid = models.CharField(max_length=3, blank=True, null=True)
    outboundproxy = models.CharField(max_length=40, blank=True, null=True)
    callbackextension = models.CharField(max_length=40, blank=True, null=True)
    timert1 = models.IntegerField(blank=True, null=True)
    timerb = models.IntegerField(blank=True, null=True)
    qualifyfreq = models.IntegerField(blank=True, null=True)
    constantssrc = models.CharField(max_length=3, blank=True, null=True)
    contactpermit = models.CharField(max_length=95, blank=True, null=True)
    contactdeny = models.CharField(max_length=95, blank=True, null=True)
    usereqphone = models.CharField(max_length=3, blank=True, null=True)
    textsupport = models.CharField(max_length=3, blank=True, null=True)
    faxdetect = models.CharField(max_length=3, blank=True, null=True)
    buggymwi = models.CharField(max_length=3, blank=True, null=True)
    auth = models.CharField(max_length=40, blank=True, null=True)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    trunkname = models.CharField(max_length=40, blank=True, null=True)
    cid_number = models.CharField(max_length=40, blank=True, null=True)
    callingpres = models.CharField(max_length=21, blank=True, null=True)
    mohinterpret = models.CharField(max_length=40, blank=True, null=True)
    mohsuggest = models.CharField(max_length=40, blank=True, null=True)
    parkinglot = models.CharField(max_length=40, blank=True, null=True)
    hasvoicemail = models.CharField(max_length=3, blank=True, null=True)
    subscribemwi = models.CharField(max_length=3, blank=True, null=True)
    vmexten = models.CharField(max_length=40, blank=True, null=True)
    autoframing = models.CharField(max_length=3, blank=True, null=True)
    rtpkeepalive = models.IntegerField(blank=True, null=True)
    call_limit = models.IntegerField(db_column='call-limit', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    g726nonstandard = models.CharField(max_length=3, blank=True, null=True)
    ignoresdpversion = models.CharField(max_length=3, blank=True, null=True)
    allowtransfer = models.CharField(max_length=3, blank=True, null=True)
    dynamic = models.CharField(max_length=3, blank=True, null=True)
    path = models.CharField(max_length=256, blank=True, null=True)
    supportpath = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sippeers'


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
