# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ActivateRecord(models.Model):
    ifa = models.CharField(primary_key=True, max_length=64)
    mac = models.CharField(max_length=64)
    appid = models.IntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    dl_ts = models.DateTimeField()
    reg_ts = models.DateTimeField()
    callback = models.CharField(max_length=256)
    drkey32 = models.CharField(max_length=64)
    callback_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'activate_record'


class ActivityAdsForWebNew(models.Model):
    ads_id = models.AutoField(primary_key=True)
    activity_id = models.BigIntegerField()
    open_type = models.IntegerField()
    open_url = models.CharField(max_length=512)
    order_id = models.IntegerField()
    status = models.CharField(max_length=64)
    intro_photo = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    note = models.TextField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_ads_for_web_new'


class ActivityFeedInfo(models.Model):
    activity_id = models.BigIntegerField()
    feed_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'activity_feed_info'
        unique_together = (('activity_id', 'feed_id'),)


class ActivityInfo(models.Model):
    activity_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    kind_id = models.IntegerField()
    status = models.IntegerField()
    avg_cost = models.FloatField()
    min_user_num = models.IntegerField()
    max_user_num = models.IntegerField()
    source = models.CharField(max_length=32)
    begin_time = models.BigIntegerField()
    end_time = models.BigIntegerField()
    remind_time = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    intro = models.TextField()
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    frequency = models.CharField(max_length=64)
    note = models.TextField()
    collection_site = models.CharField(max_length=255)
    ts = models.DateTimeField()
    update_ts = models.DateTimeField()
    name = models.CharField(max_length=64)
    site_name = models.CharField(max_length=256)
    deadline_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'activity_info'


class ActivityIntroPhotoInfo(models.Model):
    activity_id = models.BigIntegerField()
    photo_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'activity_intro_photo_info'
        unique_together = (('activity_id', 'photo_id'),)


class ActivityKindInfo(models.Model):
    kind_id = models.IntegerField(primary_key=True)
    intro = models.CharField(max_length=255)
    hot = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_kind_info'


class ActivityMember(models.Model):
    activity_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    extend_cnt = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_member'
        unique_together = (('activity_id', 'user_id'),)


class ActivityPhoto(models.Model):
    activity_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    photo_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'activity_photo'
        unique_together = (('activity_id', 'user_id', 'photo_id'),)


class ActivityPraiseInfo(models.Model):
    activity_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_praise_info'
        unique_together = (('activity_id', 'user_id'),)


class ActivityPropertyInfo(models.Model):
    activity_id = models.BigIntegerField()
    send_user_id = models.BigIntegerField()
    recv_user_id = models.BigIntegerField()
    cnt = models.IntegerField()
    kind = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_property_info'
        unique_together = (('activity_id', 'send_user_id'),)


class ActivityScore(models.Model):
    activity_id = models.BigIntegerField()
    member_score = models.IntegerField()
    photo_score = models.IntegerField()
    discussion_score = models.IntegerField()
    feed_score = models.IntegerField()
    seed_score = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_score'


class ActivityTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity_tickets64'


class ActivityTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'activity_tickets64_innodb'


class AdNotify(models.Model):
    ad_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    package_name = models.CharField(max_length=256)
    version_code = models.IntegerField()
    content = models.CharField(max_length=256)
    dl_url = models.CharField(max_length=256)
    pic_url = models.CharField(max_length=256)
    op_type = models.IntegerField()
    range_type = models.IntegerField()
    range_val = models.TextField()
    ts = models.DateTimeField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField()
    priority = models.IntegerField()
    detail_url = models.CharField(max_length=256)
    detail_top_img_url = models.CharField(max_length=256)
    icon_url = models.CharField(max_length=256)
    abstracts = models.CharField(max_length=256, blank=True, null=True)
    version_name = models.CharField(max_length=256)
    detail_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'ad_notify'


class AdReport(models.Model):
    user_id = models.BigIntegerField()
    ad_id = models.IntegerField()
    op_type = models.IntegerField()
    device_token = models.CharField(max_length=64)
    source = models.CharField(max_length=20)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ad_report'


class Address(models.Model):
    id = models.IntegerField()
    levels = models.IntegerField()
    addkey = models.CharField(max_length=10)
    belongkey = models.CharField(max_length=10)
    toponym = models.CharField(max_length=20)
    province_key = models.CharField(max_length=10)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'address'


class AdmanagerAds(models.Model):
    campaign = models.ForeignKey('AdmanagerCampaigns', models.DO_NOTHING, blank=True, null=True)
    image = models.ForeignKey('MediaMedia', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    new_window = models.IntegerField()
    position = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    activityid = models.IntegerField(db_column='activityId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admanager__ads'


class AdmanagerCampaigns(models.Model):
    code = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admanager__campaigns'


class AdmanagerInteractions(models.Model):
    code = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    page_id = models.CharField(max_length=255, blank=True, null=True)
    page_type = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_ip = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admanager__interactions'


class AgentMoney(models.Model):
    order_id = models.BigIntegerField()
    agent_id = models.BigIntegerField()
    rule_id = models.BigIntegerField()
    money = models.IntegerField()
    angent_level = models.IntegerField()
    status = models.IntegerField()
    online = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_money'
        unique_together = (('order_id', 'agent_id'),)


class AgentPeople(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    parent1_id = models.BigIntegerField(blank=True, null=True)
    parent2_id = models.BigIntegerField(blank=True, null=True)
    parent3_id = models.BigIntegerField(blank=True, null=True)
    children1_cnt = models.IntegerField()
    children2_cnt = models.IntegerField()
    children3_cnt = models.IntegerField()
    status = models.IntegerField()
    all_money = models.BigIntegerField()
    confirm_money = models.BigIntegerField()
    unconfirm_money = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_people'


class AgentRule(models.Model):
    rule_id = models.BigIntegerField(primary_key=True)
    goods_id = models.BigIntegerField()
    ratio1 = models.BigIntegerField()
    ratio2 = models.BigIntegerField()
    ratio3 = models.BigIntegerField()
    status = models.IntegerField()
    extra = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_rule'


class AppFinished(models.Model):
    finish_id = models.AutoField(primary_key=True)
    task_id = models.IntegerField()
    app_id = models.IntegerField()
    user_id = models.IntegerField()
    ts = models.DateTimeField()
    yueb = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_finished'


class AppFinishedV2(models.Model):
    finish_id = models.AutoField(primary_key=True)
    task_id = models.IntegerField()
    app_id = models.IntegerField()
    user_id = models.IntegerField()
    yueb = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_finished_v2'


class AppMarketList(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    sort_score = models.IntegerField()
    short_desc = models.CharField(max_length=100)
    desc_intro = models.CharField(max_length=400, blank=True, null=True)
    desc_images = models.CharField(max_length=400)
    download_url = models.CharField(max_length=200)
    yueb = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    package = models.CharField(max_length=100)
    down_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_market_list'


class AppMarketListV2(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    sort_score = models.IntegerField()
    short_desc = models.CharField(max_length=100)
    desc_intro = models.CharField(max_length=400)
    desc_images = models.CharField(max_length=400)
    download_url = models.CharField(max_length=200)
    yueb = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    package = models.CharField(max_length=100)
    down_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_market_list_v2'


class AppTask(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    app_id = models.BigIntegerField()
    type_id = models.IntegerField()
    pre_id = models.IntegerField()
    reward = models.IntegerField()
    prompt_action = models.CharField(max_length=256)
    prompt = models.CharField(max_length=256)
    finish_action = models.CharField(max_length=256)
    times_pre_day = models.CharField(max_length=256)
    repeat_days = models.CharField(max_length=256)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_task'


class AppTaskV2(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    app_id = models.BigIntegerField()
    pre_id = models.IntegerField()
    yueb = models.IntegerField()
    prompt_action = models.CharField(max_length=256)
    prompt = models.CharField(max_length=256)
    times_pre_day = models.CharField(max_length=256)
    repeat_days = models.CharField(max_length=256)
    use_time = models.IntegerField()
    ts = models.DateTimeField()
    status = models.IntegerField()
    sort_score = models.IntegerField(blank=True, null=True)
    delay_min = models.IntegerField(blank=True, null=True)
    delay_max = models.IntegerField(blank=True, null=True)
    delay_type = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_task_v2'


class AppType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'app_type'


class AppYuebDetail(models.Model):
    yueb_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    app_id = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_yueb_detail'


class ArmyPasswd(models.Model):
    passwd = models.CharField(primary_key=True, max_length=16)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'army_passwd'


class ArmyReportUser(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    num = models.IntegerField()
    avg_speed = models.IntegerField()
    status_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'army_report_user'
        unique_together = (('user_id', 'group_run_id'),)


class ArmyReportUser50(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    num = models.IntegerField()
    avg_speed = models.IntegerField()
    status_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'army_report_user_50'
        unique_together = (('user_id', 'group_run_id'),)


class ArmyReportUserTmp(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    num = models.IntegerField()
    avg_speed = models.IntegerField()
    status_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'army_report_user_tmp'
        unique_together = (('user_id', 'group_run_id'),)


class ArmyRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    types = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'army_run_info'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BeanQqUpload(models.Model):
    user_id = models.IntegerField(primary_key=True)
    qq = models.BigIntegerField()
    status = models.IntegerField()
    share_ts = models.DateTimeField()
    getqqb = models.IntegerField()
    get_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bean_qq_upload'


class BeanQqUploadStat(models.Model):
    day = models.CharField(primary_key=True, max_length=32)
    activity_user_num = models.IntegerField()
    activity_qq_num = models.IntegerField()
    getqq_user_num = models.IntegerField()
    getqq_qq_num = models.IntegerField()
    no_qq_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bean_qq_upload_stat'


class BlacklistWord(models.Model):
    word = models.CharField(primary_key=True, max_length=64)
    weight = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blacklist_word'


class BraceletMsgTable(models.Model):
    templateid = models.IntegerField(primary_key=True)
    templatename = models.CharField(max_length=128)
    templatetitle = models.CharField(max_length=128)
    templatecontent = models.CharField(max_length=512)
    pushlink = models.IntegerField()
    pushlinkcontent = models.CharField(max_length=128)
    pushtab = models.IntegerField()
    pushtabcontent = models.CharField(max_length=128)
    runstatus = models.IntegerField()
    runbegin = models.CharField(max_length=32)
    runend = models.CharField(max_length=32)
    walkstatus = models.IntegerField()
    walkbegin = models.CharField(max_length=32)
    walkend = models.CharField(max_length=32)
    rankstatus = models.IntegerField()
    rankbegin = models.CharField(max_length=32)
    rankend = models.CharField(max_length=32)
    verstatus = models.IntegerField()
    verbegin = models.CharField(max_length=32)
    verend = models.CharField(max_length=32)
    sexstatus = models.IntegerField()
    sexvalue = models.CharField(max_length=32)
    grayuserid = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'bracelet_msg_table'


class BraceletMsgTemplateTable(models.Model):
    templateid = models.IntegerField(primary_key=True)
    templatename = models.CharField(unique=True, max_length=128)
    templatetitle = models.CharField(max_length=128)
    templatecontent = models.CharField(max_length=512)
    pushlink = models.IntegerField()
    pushlinkcontent = models.CharField(max_length=128)
    pushtab = models.IntegerField()
    pushtabcontent = models.CharField(max_length=128)
    runstatus = models.IntegerField()
    runbegin = models.CharField(max_length=32)
    runend = models.CharField(max_length=32)
    walkstatus = models.IntegerField()
    walkbegin = models.CharField(max_length=32)
    walkend = models.CharField(max_length=32)
    rankstatus = models.IntegerField()
    rankbegin = models.CharField(max_length=32)
    rankend = models.CharField(max_length=32)
    verstatus = models.IntegerField()
    verbegin = models.CharField(max_length=32)
    verend = models.CharField(max_length=32)
    sexstatus = models.IntegerField()
    sexvalue = models.CharField(max_length=32)
    grayuserid = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'bracelet_msg_template_table'


class BraceletRunnerInfo(models.Model):
    user_id = models.IntegerField()
    kind_id = models.IntegerField()
    day_id = models.CharField(max_length=32)
    step_target = models.IntegerField()
    bracelet_uuid = models.CharField(max_length=64)
    device_id = models.CharField(max_length=64)
    detail = models.TextField()
    source = models.CharField(max_length=64)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bracelet_runner_info'
        unique_together = (('user_id', 'day_id', 'bracelet_uuid', 'device_id'),)


class BraceletUserAreaStat(models.Model):
    stattype = models.CharField(max_length=32)
    statkey = models.CharField(max_length=32)
    user_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bracelet_user_area_stat'
        unique_together = (('stattype', 'statkey'),)


class BraceletUserPlatStat(models.Model):
    day = models.CharField(max_length=32)
    plat = models.CharField(max_length=32)
    user_regnum = models.IntegerField()
    user_installnum = models.IntegerField()
    user_active_sum = models.IntegerField()
    user_regsum = models.IntegerField()
    user_installsum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bracelet_user_plat_stat'
        unique_together = (('day', 'plat'),)


class BraceletUserRunStat(models.Model):
    day = models.CharField(primary_key=True, max_length=32)
    run_num = models.IntegerField()
    run_km = models.IntegerField()
    walk_num = models.IntegerField()
    walk_km = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bracelet_user_run_stat'


class BraceletUserSexKeyrangeStat(models.Model):
    sex = models.CharField(max_length=32)
    statkey = models.CharField(max_length=64)
    statrange = models.CharField(max_length=64)
    user_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bracelet_user_sex_keyrange_stat'
        unique_together = (('sex', 'statkey', 'statrange'),)


class BraceletVersion(models.Model):
    ver = models.CharField(primary_key=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'bracelet_version'


class BusinessSettingInfo(models.Model):
    is_vedio_open = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'business_setting_info'


class Cat1(models.Model):
    name = models.CharField(unique=True, max_length=45)
    title = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat1'


class Cat2(models.Model):
    name = models.CharField(unique=True, max_length=45)
    title = models.CharField(max_length=45, blank=True, null=True)
    cat1_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cat2'


class Cat3(models.Model):
    name = models.CharField(unique=True, max_length=45)
    title = models.CharField(max_length=45, blank=True, null=True)
    cat2_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cat3'


class ChangjiangChallengeCircleInfo(models.Model):
    group_run_id = models.BigIntegerField()
    circle_id = models.BigIntegerField()
    ts = models.DateTimeField()
    steps = models.IntegerField()
    rank = models.IntegerField()
    status = models.IntegerField()
    circle_title = models.CharField(max_length=128)
    user_cnt = models.IntegerField()
    url = models.TextField()
    donate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'changjiang_challenge_circle_info'
        unique_together = (('circle_id', 'group_run_id'),)


class ChangjiangChallengeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()
    user_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'changjiang_challenge_run_info'


class ChangjiangChallengeUserDayInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    day_id = models.CharField(max_length=10)
    ts = models.DateTimeField()
    steps = models.IntegerField()
    status = models.IntegerField()
    yessteps = models.IntegerField()
    donate_tag = models.IntegerField()
    donate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'changjiang_challenge_user_day_info'
        unique_together = (('user_id', 'group_run_id', 'day_id'),)


class ChangjiangChallengeUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    ts = models.DateTimeField()
    steps = models.IntegerField()
    days = models.IntegerField()
    status = models.IntegerField()
    circle_id = models.BigIntegerField()
    donate_tag = models.IntegerField()
    donate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'changjiang_challenge_user_info'
        unique_together = (('user_id', 'group_run_id'),)


class ChannelComment(models.Model):
    hash_id = models.CharField(primary_key=True, max_length=64)
    channel = models.CharField(max_length=64)
    app_name = models.CharField(max_length=64)
    author_name = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    time = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'channel_comment'


class CircleActivityInfo(models.Model):
    activity_id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    reward_type = models.IntegerField()
    reward_money = models.IntegerField()
    reward_comment = models.CharField(max_length=255)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    circle_id = models.IntegerField()
    user_id = models.IntegerField()
    contact = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    kind_id = models.IntegerField()
    user_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_activity_info'


class CircleExtraInfo(models.Model):
    circle_id = models.BigIntegerField(primary_key=True)
    valid_type = models.IntegerField()
    question = models.CharField(max_length=128)
    answer = models.CharField(max_length=128)
    longitude = models.FloatField()
    latitude = models.FloatField()
    circle_flag = models.IntegerField()
    circle_flag_info = models.CharField(max_length=128)
    province = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    diqu = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'circle_extra_info'


class CircleGroupRunInfo(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigAutoField(primary_key=True)
    circle_id = models.IntegerField()
    status = models.IntegerField()
    aim_type = models.IntegerField()
    sport_type = models.IntegerField()
    aim_distance = models.IntegerField()
    aim_rank = models.IntegerField()
    reward_type = models.IntegerField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    real_pay_money = models.IntegerField()
    hot_rank = models.IntegerField()
    join_cnt = models.IntegerField()
    chal_type = models.BigIntegerField()
    sub_circle_list = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'circle_group_run_info'


class CircleGroupRunInfoHot(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigAutoField(primary_key=True)
    circle_id = models.IntegerField()
    status = models.IntegerField()
    aim_type = models.IntegerField()
    sport_type = models.IntegerField()
    aim_distance = models.IntegerField()
    aim_rank = models.IntegerField()
    reward_type = models.IntegerField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    real_pay_money = models.IntegerField()
    hot_rank = models.IntegerField()
    join_cnt = models.IntegerField()
    chal_type = models.BigIntegerField()
    sub_circle_list = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'circle_group_run_info_hot'


class CircleGroupRunnerTop(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_group_runner_top'
        unique_together = (('user_id', 'top_index'),)


class CircleGroupRunnerTopRide(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_group_runner_top_ride'
        unique_together = (('user_id', 'top_index'),)


class CircleGroupRunnerTopStep(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_group_runner_top_step'
        unique_together = (('user_id', 'top_index'),)


class CircleImported(models.Model):
    old_circle_id = models.IntegerField(primary_key=True)
    new_circle_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_imported'


class CircleInfo(models.Model):
    circle_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    member_cnt = models.BigIntegerField()
    topic_cnt = models.BigIntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    url = models.TextField()
    ts = models.DateTimeField()
    phone = models.CharField(max_length=128)
    type = models.IntegerField()
    manager = models.CharField(max_length=256)
    hx_group_id = models.BigIntegerField()
    last_topic_ts = models.DateTimeField()
    apply_cnt = models.IntegerField()
    parent_circle_id = models.BigIntegerField()
    circle_type = models.IntegerField()
    last_topic_title = models.CharField(max_length=128, blank=True, null=True)
    last_topic_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circle_info'


class CircleInfo4Yinhua(models.Model):
    circle_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    member_cnt = models.BigIntegerField()
    topic_cnt = models.BigIntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    url = models.TextField()
    ts = models.DateTimeField()
    phone = models.CharField(max_length=128)
    type = models.IntegerField()
    manager = models.CharField(max_length=256)
    hx_group_id = models.BigIntegerField()
    last_topic_ts = models.DateTimeField()
    apply_cnt = models.IntegerField()
    city = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'circle_info_4_yinhua'


class CircleInfoEx(models.Model):
    circle_id = models.BigAutoField(primary_key=True)
    slogan = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'circle_info_ex'


class CircleStat(models.Model):
    day = models.CharField(max_length=32)
    circle_id = models.IntegerField()
    topic_sum = models.IntegerField()
    user_sum = models.IntegerField()
    userquit_sum = models.IntegerField()
    discuss_sum = models.IntegerField()
    read_sum = models.IntegerField()
    read_all_sum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_stat'
        unique_together = (('day', 'circle_id'),)


class CircleTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'circle_tickets64'


class CircleTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'circle_tickets64_innodb'


class CircleUserGroupRun(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    distance = models.IntegerField()
    steps = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    reward_source = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    sub_circle_id = models.IntegerField()
    reward_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_user_group_run'
        unique_together = (('user_id', 'group_run_id'),)


class CircleUserGroupRunDel(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    distance = models.IntegerField()
    steps = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    reward_source = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    sub_circle_id = models.IntegerField()
    reward_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_user_group_run_del'


class CircleUserGroupRunOrder(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    sub_circle_id = models.BigIntegerField()
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circle_user_group_run_order'
        unique_together = (('user_id', 'group_run_id'),)


class City(models.Model):
    name = models.CharField(unique=True, max_length=128)
    title = models.CharField(max_length=128, blank=True, null=True)
    province_name = models.CharField(max_length=45)
    is_hot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class CityActivity(models.Model):
    activity_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    circle_id = models.IntegerField()
    face_pic_id = models.IntegerField()
    kind_id = models.IntegerField()
    status = models.IntegerField()
    fee = models.FloatField()
    fee_intro = models.CharField(max_length=32)
    min_user_num = models.IntegerField()
    max_user_num = models.IntegerField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    report_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    update_ts = models.DateTimeField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    user_city = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    note = models.TextField()
    deadline_time = models.IntegerField()
    remind_time = models.IntegerField()
    need_name = models.IntegerField()
    need_phone = models.IntegerField()
    need_qq = models.IntegerField()
    need_wx = models.IntegerField()
    user_cnt = models.IntegerField()
    over_reason = models.CharField(max_length=128)
    notify_begin = models.IntegerField()
    status_sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'city_activity'


class CityActivityUserInfo(models.Model):
    activity_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    pay = models.IntegerField()
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    qq = models.CharField(max_length=32)
    wx = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'city_activity_user_info'
        unique_together = (('activity_id', 'user_id'),)


class CityAddress(models.Model):
    name = models.CharField(unique=True, max_length=128)
    title = models.CharField(max_length=128, blank=True, null=True)
    area_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'city_address'


class CityArea(models.Model):
    name = models.CharField(unique=True, max_length=128)
    title = models.CharField(max_length=128, blank=True, null=True)
    city_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'city_area'


class CloudTrack(models.Model):
    runner_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cloud_track'
        unique_together = (('user_id', 'runner_id'),)


class CoachDepositCmsV2(models.Model):
    day = models.CharField(primary_key=True, max_length=12)
    sum_money = models.IntegerField()
    add_money = models.IntegerField()
    sub_money = models.IntegerField()
    sum_people = models.IntegerField(blank=True, null=True)
    add_people = models.IntegerField(blank=True, null=True)
    sub_people_by_cms = models.IntegerField(blank=True, null=True)
    sub_people_by_own = models.IntegerField(blank=True, null=True)
    sub_money_by_cms = models.IntegerField(blank=True, null=True)
    add_people_by_own = models.IntegerField(blank=True, null=True)
    add_money_by_caoch = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coach_deposit_cms_v2'


class CoachGrabCoachUser(models.Model):
    grab_id = models.BigIntegerField()
    coach_user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coach_grab_coach_user'
        unique_together = (('grab_id', 'coach_user_id'),)


class CoachGrabInfo(models.Model):
    grab_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=20)
    status = models.IntegerField()
    sex = models.IntegerField()
    run_type = models.CharField(max_length=32)
    coach_user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    day = models.CharField(max_length=16)
    begin_hour = models.IntegerField()
    end_hour = models.IntegerField()
    min_fee = models.IntegerField()
    max_fee = models.IntegerField()
    place = models.CharField(max_length=64)
    ts = models.DateTimeField()
    wx_notify = models.IntegerField()
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    fee = models.IntegerField()
    pay_status = models.IntegerField()
    back_fee = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coach_grab_info'


class CoachHotLocation(models.Model):
    geo = models.CharField(max_length=16)
    longitude = models.FloatField()
    latitude = models.FloatField()
    address = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'coach_hot_location'


class CoachNotify(models.Model):
    notify_type = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    user_type = models.IntegerField()
    range_type = models.IntegerField()
    range_val = models.TextField()
    ts = models.DateTimeField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField()
    priority = models.IntegerField()
    right_but_text = models.CharField(max_length=32)
    left_but_text = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'coach_notify'


class CoachOrder(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    coach_user_id = models.BigIntegerField()
    day = models.CharField(max_length=16)
    begin_hour = models.IntegerField()
    end_hour = models.IntegerField()
    user_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=64)
    place = models.CharField(max_length=64)
    d2d = models.IntegerField()
    safe_name = models.CharField(max_length=16)
    safe_id = models.CharField(db_column='safe_ID', max_length=32)  # Field name made lowercase.
    status = models.IntegerField()
    ts = models.DateTimeField()
    coach_status = models.IntegerField()
    score = models.IntegerField()
    feel = models.CharField(max_length=128)
    fee = models.IntegerField()
    feel_ts = models.DateTimeField()
    notify_coach2accp = models.IntegerField()
    notify_user2deal = models.IntegerField()
    notify_before1hour = models.IntegerField()
    bg_status = models.IntegerField()
    back_money = models.IntegerField()
    is_revisit = models.IntegerField()
    note = models.CharField(max_length=4096)
    user_argue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coach_order'


class CoachUserId(models.Model):
    user_id = models.BigIntegerField()
    safe_name = models.CharField(max_length=16)
    safe_id = models.CharField(db_column='safe_ID', max_length=32)  # Field name made lowercase.
    ts = models.DateTimeField()
    phone = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'coach_user_ID'


class CoachUserVinfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    id = models.CharField(db_column='ID', max_length=20)  # Field name made lowercase.
    idface = models.IntegerField()
    idback = models.IntegerField()
    idpeople = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coach_user_Vinfo'


class CoachUserDate(models.Model):
    user_id = models.BigIntegerField()
    day = models.CharField(max_length=32)
    hours = models.CharField(max_length=96)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coach_user_date'
        unique_together = (('user_id', 'day'),)


class CoachUserExpand(models.Model):
    user_id = models.BigIntegerField(unique=True)
    user_recommand_count = models.IntegerField()
    user_new_tip = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coach_user_expand'


class CoachUserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    status = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    phone = models.CharField(max_length=20)
    fee = models.IntegerField()
    fee_ts = models.DateTimeField()
    description = models.TextField()
    photos = models.CharField(max_length=64)
    longitude = models.FloatField()
    latitude = models.FloatField()
    v = models.IntegerField()
    d = models.IntegerField()
    star = models.IntegerField()
    sign_ts = models.DateTimeField()
    sign_update_ts = models.DateTimeField()
    sign_score = models.IntegerField()
    grab_recommand = models.IntegerField()
    user_recommand = models.IntegerField()
    type = models.IntegerField()
    sex = models.IntegerField()
    avg_score = models.IntegerField()
    like_cnt = models.IntegerField()
    run_cnt = models.IntegerField()
    full_cnt = models.IntegerField()
    head_photo_id = models.IntegerField()
    ts = models.DateTimeField()
    fail_msg = models.CharField(max_length=64)
    v_fail_msg = models.CharField(max_length=64)
    work_type1 = models.CharField(max_length=64)
    work_type2 = models.CharField(max_length=64)
    score_marathon = models.IntegerField()
    score_10km = models.IntegerField()
    score_run_sum = models.IntegerField()
    invite_user_id = models.BigIntegerField()
    sort_score = models.IntegerField()
    notify_status = models.IntegerField()
    editer_photo = models.CharField(max_length=40)
    editer_comment = models.CharField(max_length=100)
    editer_tag = models.CharField(max_length=100)
    active_day = models.IntegerField()
    con_day = models.IntegerField()
    new_start = models.IntegerField()
    order_status = models.IntegerField()
    first_coupon = models.IntegerField()
    share_coupon = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coach_user_info'


class CoachUserInfoPre(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    status = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    phone = models.CharField(max_length=20)
    fee = models.IntegerField()
    fee_ts = models.DateTimeField()
    description = models.TextField()
    photos = models.CharField(max_length=64)
    longitude = models.FloatField()
    latitude = models.FloatField()
    v = models.IntegerField()
    type = models.IntegerField()
    sex = models.IntegerField()
    avg_score = models.IntegerField()
    run_cnt = models.IntegerField()
    full_cnt = models.IntegerField()
    head_photo_id = models.IntegerField()
    ts = models.DateTimeField()
    fail_msg = models.CharField(max_length=20)
    v_fail_msg = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'coach_user_info_pre'


class CoachUserLike(models.Model):
    user_id = models.BigIntegerField()
    coach_user_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coach_user_like'
        unique_together = (('user_id', 'coach_user_id'),)


class CoachUserLocation(models.Model):
    user_id = models.BigIntegerField()
    index_all = models.CharField(max_length=64)
    avg_score = models.IntegerField()
    sex = models.IntegerField()
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    d2d = models.IntegerField()
    ts = models.DateTimeField()
    priority = models.IntegerField()
    place = models.CharField(max_length=64)
    location_id = models.BigIntegerField()
    v = models.IntegerField()
    d = models.IntegerField()
    status = models.IntegerField()
    user_recommand = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coach_user_location'
        unique_together = (('user_id', 'location_id'),)


class CoachUserLocationPre(models.Model):
    user_id = models.BigIntegerField()
    index_all = models.CharField(max_length=64)
    avg_score = models.IntegerField()
    sex = models.IntegerField()
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    d2d = models.IntegerField()
    ts = models.DateTimeField()
    priority = models.IntegerField()
    place = models.CharField(max_length=64)
    location_id = models.BigIntegerField()
    v = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coach_user_location_pre'
        unique_together = (('user_id', 'location_id'),)


class CoachUserTags(models.Model):
    user_id = models.BigIntegerField()
    ts = models.DateTimeField()
    tag = models.CharField(max_length=128)
    cnt = models.IntegerField()
    coach_user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'coach_user_tags'
        unique_together = (('user_id', 'tag'),)


class CoachlocationTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coachlocation_tickets64'


class CoachlocationTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'coachlocation_tickets64_innodb'


class CoachorderTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coachorder_tickets64'


class CoachorderTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'coachorder_tickets64_innodb'


class CouponInfo(models.Model):
    coupon = models.CharField(primary_key=True, max_length=32)
    source = models.CharField(max_length=32)
    intro = models.CharField(max_length=128)
    money = models.IntegerField()
    need_money = models.IntegerField()
    total_cnt = models.IntegerField()
    used_cnt = models.IntegerField()
    active_expire_day = models.IntegerField()
    expire_time = models.DateTimeField()
    ts = models.DateTimeField()
    user_id = models.BigIntegerField()
    kind = models.IntegerField()
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon_info'


class CustomServiceQuestion(models.Model):
    question_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    kind = models.IntegerField()
    qq = models.CharField(max_length=64)
    version = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    solution = models.CharField(max_length=512)
    appear_time = models.DateTimeField()
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_service_question'


class DayChannelStat(models.Model):
    day = models.CharField(max_length=32)
    channel = models.CharField(max_length=64)
    outdoor_cnt = models.IntegerField()
    indoor_cnt = models.IntegerField()
    great_1000m_cnt = models.IntegerField()
    less_1000m_cnt = models.IntegerField()
    great_2000m_cnt = models.IntegerField()
    less_2000m_cnt = models.IntegerField()
    run_cnt = models.IntegerField()
    ride_cnt = models.IntegerField()
    step_cnt = models.IntegerField()
    reward_cnt = models.IntegerField()
    step_great_2000_cnt = models.IntegerField()
    step_less_2000_cnt = models.IntegerField()
    screen_on_cnt = models.IntegerField()
    screen_off_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'day_channel_stat'
        unique_together = (('day', 'channel'),)


class DayRemain(models.Model):
    day = models.CharField(max_length=32)
    cnt = models.IntegerField()
    kind = models.IntegerField()
    channel = models.CharField(max_length=64)
    day1 = models.FloatField()
    day2 = models.FloatField()
    day3 = models.FloatField()
    day4 = models.FloatField()
    day5 = models.FloatField()
    day6 = models.FloatField()
    day7 = models.FloatField()
    day8 = models.FloatField()
    day9 = models.FloatField()
    day10 = models.FloatField()
    day11 = models.FloatField()
    day12 = models.FloatField()
    day13 = models.FloatField()
    day14 = models.FloatField()
    day15 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'day_remain'
        unique_together = (('day', 'kind', 'channel'),)


class DayStat(models.Model):
    day = models.CharField(primary_key=True, max_length=32)
    total_user = models.IntegerField()
    active_user = models.IntegerField()
    android_app_active_user = models.IntegerField()
    ios_app_active_user = models.IntegerField()
    cms_seed_user = models.IntegerField()
    android_app_user = models.IntegerField()
    android_app_pre_user = models.IntegerField()
    ios_app_user = models.IntegerField()
    ios_app_pre_user = models.IntegerField()
    mobileweb_user = models.IntegerField()
    marketing_user = models.IntegerField()
    not_need_phone_code = models.IntegerField()
    need_phone_code = models.IntegerField()
    register_fail_cnt = models.IntegerField()
    runner_cnt = models.IntegerField()
    runner_autorecord_cnt = models.IntegerField()
    runner_indoor_distance = models.IntegerField()
    runner_outdoor_distance = models.IntegerField()
    runner_autorecord_distance = models.IntegerField()
    runner_distance = models.IntegerField()
    runner_indoor_cnt = models.IntegerField()
    runner_outdoor_cnt = models.IntegerField()
    runner_nomal_cnt = models.IntegerField()
    runner_trick_cnt = models.IntegerField()
    activity_normal_cnt = models.IntegerField()
    activity_seed_cnt = models.IntegerField()
    activity_invite_cnt = models.IntegerField()
    activity_apply_cnt = models.IntegerField()
    activity_join_cnt = models.IntegerField()
    discussion_cnt = models.IntegerField()
    feed_cnt = models.IntegerField()
    photo_cnt = models.IntegerField()
    intro_photo_cnt = models.IntegerField()
    feed_photo_cnt = models.IntegerField()
    wangcai_download = models.IntegerField()
    wangcai_register = models.IntegerField()
    runner_outdoor_user_cnt = models.IntegerField()
    pv = models.IntegerField()
    cumsum_user = models.IntegerField()
    ignore_new_user = models.IntegerField()
    runner_autorecord_user_cnt = models.IntegerField()
    runner_indoor_user_cnt = models.IntegerField()
    runner_all_user_cnt = models.IntegerField()
    runner_ride_user_cnt = models.IntegerField()
    runner_ride_cnt = models.IntegerField()
    runner_ride_distance = models.IntegerField()
    web_cnt = models.IntegerField()
    gongzhonghao_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'day_stat'


class DayStatAd(models.Model):
    key = models.CharField(primary_key=True, max_length=64)
    day = models.CharField(max_length=32)
    source = models.CharField(max_length=32)
    download = models.IntegerField()
    register = models.IntegerField()
    sport = models.IntegerField()
    all_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'day_stat_ad'


class DeviceInfo(models.Model):
    device_id = models.CharField(max_length=128)
    source = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'device_info'
        unique_together = (('device_id', 'user_id'),)


class DiscussPhotoInfo(models.Model):
    discuss_id = models.BigIntegerField()
    photo_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'discuss_photo_info'
        unique_together = (('discuss_id', 'photo_id'),)


class DiscussTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'discuss_tickets64'


class DiscussTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'discuss_tickets64_innodb'


class DiscussionInfo(models.Model):
    discuss_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    parent_discuss_id = models.BigIntegerField()
    feed_id = models.BigIntegerField()
    status = models.IntegerField()
    content = models.CharField(max_length=256)
    ts = models.DateTimeField()
    photo_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'discussion_info'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class DrawCashRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    qq_num = models.BigIntegerField()
    phone = models.CharField(max_length=16)
    alipay_account = models.CharField(max_length=64)
    alipay_realname = models.CharField(max_length=64)
    reward = models.IntegerField()
    reason = models.CharField(max_length=255)
    apply_ts = models.DateTimeField()
    process_ts = models.DateTimeField()
    operator = models.CharField(max_length=255)
    fail_msg = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'draw_cash_record'


class DrawRewardRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    qq_num = models.BigIntegerField()
    phone = models.CharField(max_length=16)
    alipay_account = models.CharField(max_length=64)
    alipay_realname = models.CharField(max_length=64)
    reward = models.IntegerField()
    reason = models.CharField(max_length=255)
    apply_ts = models.DateTimeField()
    process_ts = models.DateTimeField()
    operator = models.CharField(max_length=255)
    fail_msg = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'draw_reward_record'


class DrawWhitelist(models.Model):
    account = models.CharField(primary_key=True, max_length=64)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'draw_whitelist'


class DynamicFeedDiscuss(models.Model):
    discuss_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    feed_id = models.BigIntegerField()
    status = models.IntegerField()
    content = models.TextField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_feed_discuss'


class DynamicFeedId(models.Model):
    user_id = models.BigIntegerField()
    feed_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'dynamic_feed_id'
        unique_together = (('user_id', 'feed_id'),)


class DynamicFeedIdTmp(models.Model):
    user_id = models.BigIntegerField()
    feed_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'dynamic_feed_id_tmp'
        unique_together = (('user_id', 'feed_id'),)


class DynamicFeedInfo(models.Model):
    feed_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.IntegerField()
    type_id = models.BigIntegerField()
    photo_ids = models.CharField(max_length=128)
    media_ids = models.CharField(max_length=128)
    status = models.IntegerField()
    title = models.CharField(max_length=256)
    content = models.TextField()
    ts = models.DateTimeField()
    like_num = models.IntegerField()
    discuss_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynamic_feed_info'


class DynamicFeedInfoAd(models.Model):
    feed_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.IntegerField()
    type_id = models.BigIntegerField()
    photo_ids = models.CharField(max_length=128)
    media_ids = models.CharField(max_length=128)
    status = models.IntegerField()
    title = models.CharField(max_length=256)
    content = models.TextField()
    ts = models.DateTimeField()
    photo_urls = models.TextField()
    dl_url = models.TextField()
    dl_web = models.TextField()
    position = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'dynamic_feed_info_ad'


class DynamicFeedInfoBk(models.Model):
    feed_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.IntegerField()
    type_id = models.BigIntegerField()
    photo_ids = models.CharField(max_length=128)
    media_ids = models.CharField(max_length=128)
    status = models.IntegerField()
    title = models.CharField(max_length=256)
    content = models.TextField()
    ts = models.DateTimeField()
    like_num = models.IntegerField()
    discuss_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynamic_feed_info_bk'


class DynamicFeedLike(models.Model):
    user_id = models.BigIntegerField()
    feed_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_feed_like'
        unique_together = (('user_id', 'feed_id'),)


class DynamicReport(models.Model):
    feed_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_report'
        unique_together = (('feed_id', 'user_id'),)


class EnumIndex(models.Model):
    kind = models.CharField(max_length=32)
    id = models.IntegerField()
    intro = models.CharField(max_length=32)
    quote_field = models.CharField(max_length=32)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'enum_index'
        unique_together = (('kind', 'id'),)


class ErrorSign(models.Model):
    user_id = models.BigIntegerField()
    req_name = models.CharField(max_length=64)
    req_args = models.CharField(max_length=256)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'error_sign'


class ErrorStat(models.Model):
    day = models.CharField(max_length=32)
    source = models.CharField(max_length=128)
    comment = models.CharField(max_length=256)
    status = models.IntegerField()
    type = models.IntegerField()
    ts = models.DateTimeField()
    ok_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'error_stat'


class FacebookUserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    fb_user_id = models.CharField(max_length=128)
    expires_in = models.IntegerField()
    machine_id = models.CharField(max_length=128)
    ct = models.DateTimeField()
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'facebook_user_info'


class FaqGroup(models.Model):
    group_id = models.BigIntegerField(primary_key=True)
    group_name = models.CharField(max_length=64)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faq_group'


class FaqQuestion(models.Model):
    faq_id = models.BigAutoField(primary_key=True)
    group_id = models.BigIntegerField()
    question = models.TextField()
    answer = models.TextField()
    platfom = models.IntegerField()
    remark = models.CharField(max_length=256)
    ts = models.DateTimeField()
    status = models.IntegerField()
    read_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faq_question'


class FeedInfo(models.Model):
    feed_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    status = models.IntegerField()
    content = models.TextField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feed_info'


class FeedPhotoInfo(models.Model):
    feed_id = models.BigIntegerField()
    photo_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'feed_photo_info'
        unique_together = (('feed_id', 'photo_id'),)


class FeedPraiseInfo(models.Model):
    feed_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feed_praise_info'
        unique_together = (('feed_id', 'user_id'),)


class FeedTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feed_tickets64'


class FeedTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'feed_tickets64_innodb'


class FeedType(models.Model):
    feed_type_id = models.AutoField(primary_key=True)
    intro = models.CharField(max_length=255)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feed_type'


class FitnessPlan(models.Model):
    fitness_id = models.BigIntegerField(primary_key=True)
    main_title = models.CharField(max_length=32)
    week_cnt = models.IntegerField()
    status = models.IntegerField()
    week_per_cnt = models.IntegerField()
    all_cnt = models.IntegerField()
    ts = models.DateTimeField()
    icon_url = models.TextField()
    plan_info_url = models.TextField()
    btn_normal_color = models.CharField(max_length=32)
    btn_press_color = models.CharField(max_length=32)
    bg_color = models.CharField(max_length=32)
    bg_icon_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'fitness_plan'


class FitnessPlanDays(models.Model):
    fitness_id = models.BigIntegerField()
    week_index = models.IntegerField()
    week_day = models.IntegerField()
    day_index = models.IntegerField()
    day_after = models.IntegerField()
    aim_distance = models.IntegerField()
    aim_time = models.IntegerField()
    day_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fitness_plan_days'


class FitnessPlanDaysDesc(models.Model):
    fitness_id = models.BigIntegerField()
    day_index = models.IntegerField()
    day_index_order = models.IntegerField()
    detail = models.TextField()
    loop = models.IntegerField()
    suggest = models.TextField()

    class Meta:
        managed = False
        db_table = 'fitness_plan_days_desc'


class FitnessPlanDaysSport(models.Model):
    fitness_id = models.BigIntegerField()
    day_index = models.IntegerField()
    day_index_order = models.IntegerField()
    min_uint = models.IntegerField()
    total_count = models.IntegerField()
    sport_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fitness_plan_days_sport'


class FitnessUserDetail(models.Model):
    fitness_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    day_index = models.IntegerField()
    runner_id = models.BigIntegerField()
    begin_time = models.DateTimeField()
    cost_time = models.IntegerField()
    ts = models.DateTimeField()
    distance = models.IntegerField()
    user_plan_id = models.IntegerField()
    status = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'fitness_user_detail'


class FitnessUserDetailHistory(models.Model):
    fitness_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    day_index = models.IntegerField()
    runner_id = models.BigIntegerField()
    begin_time = models.DateTimeField()
    cost_time = models.IntegerField()
    ts = models.DateTimeField()
    distance = models.IntegerField()
    user_plan_id = models.IntegerField()
    status = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'fitness_user_detail_history'


class FitnessUserPlan(models.Model):
    user_plan_id = models.BigAutoField(primary_key=True)
    fitness_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    complete = models.IntegerField()
    miss = models.IntegerField()
    ts = models.DateTimeField()
    total_times = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'fitness_user_plan'


class GeoIdList(models.Model):
    runner_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'geo_id_list'
        unique_together = (('user_id', 'runner_id'),)


class GeoList(models.Model):
    geo = models.CharField(max_length=10)
    runner_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    seq = models.IntegerField()
    g = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'geo_list'
        unique_together = (('geo', 'runner_id', 'seq'),)


class GetCoachNotifyUserTs(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'get_coach_notify_user_ts'


class GetNotify(models.Model):
    notify_type = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    button_cnt = models.IntegerField()
    need_resp = models.IntegerField()
    url = models.CharField(max_length=256)
    range_type = models.IntegerField()
    range_val = models.TextField()
    ts = models.DateTimeField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField()
    priority = models.IntegerField()
    right_but_text = models.CharField(max_length=32)
    left_but_text = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'get_notify'


class GetNotifyGuide(models.Model):
    notify_type = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    link_url = models.CharField(max_length=256)
    link_name = models.CharField(max_length=256)
    icon_url = models.CharField(max_length=256)
    range_type = models.IntegerField()
    range_val = models.TextField()
    ts = models.DateTimeField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'get_notify_guide'


class GetNotifyUserTs(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'get_notify_user_ts'


class GlobalGroupRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    reward_cnt = models.IntegerField()
    suprise_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    suprise_money = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    circle_id = models.IntegerField()
    reward_type = models.IntegerField()
    steps = models.IntegerField()
    join_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'global_group_run_info'


class GlobalNkmChallengeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'global_nkm_challenge_run_info'


class GlobalNkmChallengeUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    num = models.IntegerField()
    avg_speed = models.IntegerField()
    status_level = models.IntegerField()
    comeons = models.TextField(db_column='ComeOns')  # Field name made lowercase.
    reward = models.IntegerField()
    timezone = models.IntegerField()
    language = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'global_nkm_challenge_user_info'
        unique_together = (('user_id', 'group_run_id'),)


class GlobalUserGroupRun(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    type = models.IntegerField()
    steps = models.IntegerField()
    reward_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'global_user_group_run'
        unique_together = (('user_id', 'group_run_id'),)


class GoodsCollection(models.Model):
    user_id = models.BigIntegerField()
    goods_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_collection'
        unique_together = (('user_id', 'goods_id'),)


class GroupRunBannerAds(models.Model):
    ads_id = models.BigAutoField(primary_key=True)
    pic_url = models.CharField(max_length=512)
    open_url = models.CharField(max_length=512)
    open_type = models.IntegerField()
    last_update_time = models.DateTimeField()
    banner_pos = models.IntegerField()
    ads_stat = models.CharField(max_length=512)
    ts = models.DateTimeField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    is_online = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_run_banner_ads'


class GroupRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    reward_cnt = models.IntegerField()
    suprise_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    suprise_money = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    circle_id = models.IntegerField()
    reward_type = models.IntegerField()
    steps = models.IntegerField()
    join_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_run_info'


class GroupRunInfoTime(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    begin_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_run_info_time'


class GroupRunStat(models.Model):
    group_run_id = models.BigIntegerField(primary_key=True)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    apply_cnt = models.BigIntegerField()
    runner_cnt = models.BigIntegerField()
    not_runner_cnt = models.BigIntegerField()
    total_reward_num = models.BigIntegerField()
    challenge_success_cnt = models.BigIntegerField()
    challenge_fail_cnt = models.BigIntegerField()
    draw_reward_cnt = models.BigIntegerField()
    now_draw_reward_cnt = models.BigIntegerField()
    kind_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_run_stat'


class Guomeng(models.Model):
    idfa = models.CharField(primary_key=True, max_length=64)
    mac = models.CharField(max_length=64)
    openudid = models.CharField(max_length=64)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    dl_ts = models.DateTimeField()
    reg_ts = models.DateTimeField()
    callback_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guomeng'


class Gym(models.Model):
    gym_id = models.AutoField(primary_key=True)
    gym_name = models.CharField(max_length=100, blank=True, null=True)
    gym_address = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gym'


class GymBody(models.Model):
    user_id = models.BigIntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    zhifang_rate = models.DecimalField(max_digits=11, decimal_places=2)
    muscle = models.DecimalField(max_digits=11, decimal_places=2)
    heart_rate = models.DecimalField(max_digits=11, decimal_places=2)
    blood = models.DecimalField(max_digits=11, decimal_places=2)
    create_time = models.DateTimeField()
    shousuo_ya = models.IntegerField()
    shuzhang_ya = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gym_body'


class GymCoach(models.Model):
    gym_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gym_coach'
        unique_together = (('gym_id', 'user_id'),)


class GymComment(models.Model):
    user_id = models.BigIntegerField()
    gym_id = models.IntegerField()
    course_id = models.IntegerField()
    comment = models.CharField(max_length=256)
    score = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    score_level = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'gym_comment'


class GymCourse(models.Model):
    course_id = models.IntegerField()
    gym_id = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    info = models.CharField(max_length=200, blank=True, null=True)
    fee = models.IntegerField(blank=True, null=True)
    fee_orig = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField()
    comment_cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gym_course'
        unique_together = (('gym_id', 'course_id'),)


class GymOrder(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    coach_user_id = models.BigIntegerField()
    gym_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    coach_status = models.IntegerField(blank=True, null=True)
    fee = models.FloatField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    phone = models.CharField(max_length=15)
    feel = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)
    feel_time = models.DateTimeField()
    back_money = models.IntegerField(blank=True, null=True)
    bg_status = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField()
    day_id = models.IntegerField()
    time_range = models.CharField(max_length=256)
    order_code = models.CharField(max_length=32)
    scored = models.IntegerField()
    sign = models.IntegerField()
    sign_ts = models.DateTimeField()
    sign_time_range = models.CharField(max_length=256)
    scored_time_range = models.CharField(max_length=256)
    comment = models.CharField(max_length=256)
    score_level = models.CharField(max_length=64)
    comment_coach_user_id = models.BigIntegerField()
    notify_2_coach = models.IntegerField()
    notify_2_user_begin = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gym_order'


class GymScore(models.Model):
    gym_score_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    student_user_id = models.BigIntegerField()
    order_id = models.IntegerField()
    cost_time = models.IntegerField()
    caloric = models.IntegerField()
    rate = models.IntegerField()
    distance = models.IntegerField()
    area_str = models.CharField(max_length=64)
    type_str = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    shuiyin_pic_id = models.IntegerField()
    sport_type = models.IntegerField()
    time_range_one = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'gym_score'


class GymorderTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gymorder_tickets64'


class GymorderTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gymorder_tickets64_innodb'


class HardTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'hard_tickets64_innodb'


class HardwareStep(models.Model):
    user_id = models.BigIntegerField()
    step_id = models.BigIntegerField()
    field_id = models.BigIntegerField(db_column='_id')  # Field renamed because it started with '_'.
    step_count = models.IntegerField()
    device_identify = models.CharField(max_length=64)
    extra = models.TextField()
    start_time_sec = models.IntegerField()
    end_time_sec = models.IntegerField()
    source = models.CharField(max_length=64)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hardware_step'
        unique_together = (('user_id', 'device_identify', 'start_time_sec', 'end_time_sec'),)


class HardwareWeight(models.Model):
    user_id = models.BigIntegerField()
    weight_id = models.BigIntegerField()
    field_id = models.BigIntegerField(db_column='_id')  # Field renamed because it started with '_'.
    weight_g = models.IntegerField()
    body_fat_per = models.FloatField()
    body_muscle_per = models.FloatField()
    body_mass_index = models.FloatField()
    basal_metabolism_rate = models.FloatField()
    body_water_percentage = models.FloatField()
    device_identify = models.CharField(max_length=64)
    extra = models.TextField()
    time_sec = models.IntegerField()
    source = models.CharField(max_length=64)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hardware_weight'
        unique_together = (('user_id', 'device_identify', 'time_sec'),)


class HistoryUserDayStep(models.Model):
    user_id = models.BigIntegerField()
    steps = models.IntegerField()
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'history_user_day_step'
        unique_together = (('user_id', 'day'),)


class HistoryUserRunnerNew(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    u_report_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'history_user_runner_new'


class HundredBatchallFlag(models.Model):
    hundred_id = models.IntegerField()
    ts = models.DateTimeField()
    circle_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_batchall_flag'
        unique_together = (('circle_id', 'hundred_id'),)


class HundredCircleGroupRun(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    circle_id = models.IntegerField()
    join = models.IntegerField()
    score = models.IntegerField()
    user_cnt = models.IntegerField()
    left_score = models.IntegerField()
    left_user_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_circle_group_run'
        unique_together = (('circle_id', 'hundred_id'),)


class HundredCircleGroupRunDel(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    circle_id = models.IntegerField()
    join = models.IntegerField()
    score = models.IntegerField()
    user_cnt = models.IntegerField()
    left_score = models.IntegerField()
    left_user_cnt = models.IntegerField()
    del_ts = models.DateTimeField()
    del_user_id = models.BigIntegerField()
    del_reason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'hundred_circle_group_run_del'


class HundredCircleGroupRunExtra(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    circle_id = models.IntegerField()
    join = models.IntegerField()
    score = models.IntegerField()
    user_cnt = models.IntegerField()
    left_user_cnt = models.IntegerField()
    left_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_circle_group_run_extra'
        unique_together = (('circle_id', 'hundred_id'),)


class HundredCircleGroupRunScore(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    circle_id = models.IntegerField()
    join = models.IntegerField()
    score = models.IntegerField()
    user_cnt = models.IntegerField()
    left_score = models.IntegerField()
    left_user_cnt = models.IntegerField()
    money = models.IntegerField()
    host_money = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_circle_group_run_score'
        unique_together = (('circle_id', 'hundred_id'),)


class HundredGroupRunExtra(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    circle_id = models.BigIntegerField()
    ts = models.DateTimeField()
    status = models.IntegerField()
    wx_push = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_group_run_extra'


class HundredGroupRunInfo(models.Model):
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    reward_cnt = models.IntegerField()
    suprise_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    suprise_money = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    circle_id = models.IntegerField()
    reward_type = models.IntegerField()
    hundred_id = models.BigAutoField(primary_key=True)
    ad = models.CharField(max_length=255)
    group_num = models.IntegerField()
    report = models.IntegerField()
    allow_change = models.IntegerField()
    type = models.IntegerField()
    session_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_group_run_info'


class HundredHostGroupRun(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    reward = models.IntegerField()
    ts = models.DateTimeField()
    comment = models.CharField(max_length=128)
    circle_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_host_group_run'
        unique_together = (('user_id', 'hundred_id', 'circle_id'),)


class HundredUserApply(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    circle_id = models.IntegerField()
    ts = models.DateTimeField()
    status = models.IntegerField()
    phone = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'hundred_user_apply'
        unique_together = (('user_id', 'hundred_id', 'circle_id'),)


class HundredUserApplyHistory(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    circle_id = models.IntegerField()
    ts = models.DateTimeField()
    status = models.IntegerField()
    phone = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'hundred_user_apply_history'
        unique_together = (('user_id', 'hundred_id', 'circle_id'),)


class HundredUserGroupRun(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    circle_id = models.IntegerField()
    user_status = models.IntegerField()
    score = models.IntegerField()
    day_distance = models.CharField(max_length=150)
    day_step = models.CharField(max_length=150)
    day_inner = models.CharField(max_length=150)
    phone = models.CharField(max_length=16)
    source = models.CharField(max_length=16)
    wx_bind_tips = models.IntegerField()
    reward_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_user_group_run'
        unique_together = (('user_id', 'hundred_id'),)


class HundredUserGroupRunBk(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    circle_id = models.IntegerField()
    user_status = models.IntegerField()
    score = models.IntegerField()
    day_distance = models.CharField(max_length=150)
    day_step = models.CharField(max_length=150)
    day_inner = models.CharField(max_length=150)
    phone = models.CharField(max_length=16)
    source = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'hundred_user_group_run_bk'
        unique_together = (('user_id', 'hundred_id'),)


class HundredUserGroupRunDel(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    circle_id = models.IntegerField()
    user_status = models.IntegerField()
    score = models.IntegerField()
    day_distance = models.CharField(max_length=150)
    day_step = models.CharField(max_length=150)
    day_inner = models.CharField(max_length=150)
    phone = models.CharField(max_length=16)
    source = models.CharField(max_length=16)
    wx_bind_tips = models.IntegerField()
    del_ts = models.DateTimeField()
    del_user_id = models.BigIntegerField()
    del_reason = models.CharField(max_length=100)
    reward_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_user_group_run_del'


class HundredUserPhone(models.Model):
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'hundred_user_phone'


class HundredUserResReward(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    reward = models.IntegerField()
    circle_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_user_res_reward'
        unique_together = (('user_id', 'hundred_id'),)


class HundredUserResReward1(models.Model):
    user_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    distance = models.IntegerField()
    reward = models.IntegerField()
    circle_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_user_res_reward1'
        unique_together = (('user_id', 'hundred_id'),)


class HundredYinhuaMemory(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    hundred_id = models.IntegerField()
    last_succ = models.IntegerField()
    status = models.IntegerField()
    last_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hundred_yinhua_memory'


class HxUserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hx_user_info'


class InviteOpenid(models.Model):
    open_id = models.CharField(max_length=64)
    access_token = models.CharField(max_length=64)
    type = models.IntegerField()
    source = models.IntegerField()
    user_id = models.IntegerField()
    circle_id = models.IntegerField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    status = models.IntegerField()
    union_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'invite_openid'
        unique_together = (('open_id', 'type'),)


class InviteUserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    from_user_id = models.BigIntegerField()
    invite_reward = models.IntegerField()
    run_reward = models.IntegerField()
    ts = models.DateTimeField()
    step_reward = models.IntegerField()
    run_status = models.IntegerField()
    step_status = models.IntegerField()
    login_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invite_user_info'


class InviteUserInfoSum(models.Model):
    from_user_id = models.BigIntegerField(primary_key=True)
    invite_reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invite_user_info_sum'


class InviteUserTop(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    from_user_id = models.BigIntegerField()
    money = models.IntegerField()
    ts = models.DateTimeField()
    rank = models.IntegerField()
    people_cnt = models.IntegerField()
    nick = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'invite_user_top'


class InviteUserid(models.Model):
    user_id = models.BigIntegerField()
    from_user_id = models.BigIntegerField()
    type = models.IntegerField()
    source = models.IntegerField()
    circle_id = models.IntegerField()
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invite_userid'
        unique_together = (('user_id', 'type', 'circle_id'),)


class InvitedUserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    from_user_id = models.BigIntegerField()
    invite_reward = models.IntegerField()
    run_reward = models.IntegerField()
    ts = models.DateTimeField()
    step_reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invited_user_info'


class IpArea(models.Model):
    ip = models.CharField(primary_key=True, max_length=16)
    area = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'ip_area'


class Jiaolian(models.Model):
    name = models.CharField(max_length=128)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=45, blank=True, null=True)
    city_area = models.CharField(max_length=64, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    work_time = models.CharField(max_length=45, blank=True, null=True)
    work_type = models.CharField(max_length=45, blank=True, null=True)
    work_years = models.CharField(max_length=45, blank=True, null=True)
    member_count = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    qq = models.CharField(max_length=45, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    province_name = models.CharField(max_length=45, blank=True, null=True)
    city_name = models.CharField(max_length=64, blank=True, null=True)
    city_area_name = models.CharField(max_length=64, blank=True, null=True)
    cat1_name = models.CharField(max_length=64, blank=True, null=True)
    cat2_name = models.CharField(max_length=64, blank=True, null=True)
    cat3_name = models.CharField(max_length=64, blank=True, null=True)
    city_address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jiaolian'


class LogQuery(models.Model):
    activity_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    command = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'log_query'


class LogReportUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    status = models.IntegerField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_report_user'


class LongMarchCircleTop(models.Model):
    circle_id = models.BigIntegerField()
    top_index = models.CharField(max_length=32)
    distance = models.IntegerField()
    tree = models.IntegerField()
    top_50_distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'long_march_circle_top'
        unique_together = (('top_index', 'circle_id'),)


class LongMarchFeed(models.Model):
    circle_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    place_id = models.IntegerField()
    finish_ts = models.DateTimeField()
    kind_id = models.IntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'long_march_feed'


class LongMarchFeedCircle(models.Model):
    circle_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    place_id = models.IntegerField()
    finish_ts = models.DateTimeField()
    kind_id = models.IntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'long_march_feed_circle'
        unique_together = (('circle_id', 'group_run_id', 'place_id'),)


class LongMarchPlace(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=128)
    total_distance = models.BigIntegerField()
    diff_distance = models.BigIntegerField()
    ts = models.DateTimeField()
    next_distance = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'long_march_place'


class LongMarchReward(models.Model):
    user_id = models.BigIntegerField()
    reward_index = models.CharField(max_length=255)
    circle_id = models.BigIntegerField()
    reward = models.IntegerField()
    is_draw = models.IntegerField()
    content = models.CharField(max_length=255)
    ts = models.DateTimeField()
    place_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'long_march_reward'


class LongMarchTop(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    circle_id = models.BigIntegerField()
    distance = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'long_march_top'
        unique_together = (('user_id', 'top_index'),)


class LongMarchUserInfo(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    circle_id = models.BigIntegerField()
    distance = models.IntegerField()
    tree_cnt = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    user_ms_flag = models.IntegerField(blank=True, null=True)
    circle_ms_flag = models.IntegerField(blank=True, null=True)
    last_start_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'long_march_user_info'
        unique_together = (('group_run_id', 'user_id', 'circle_id'),)


class LongMarchUserTop(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=32)
    circle_id = models.BigIntegerField()
    distance = models.IntegerField()
    tree = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'long_march_user_top'
        unique_together = (('user_id', 'circle_id', 'top_index'),)


class LotteryInfo(models.Model):
    lottery_id = models.BigAutoField(primary_key=True)
    lottery_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lottery_info'
        unique_together = (('lottery_type', 'status'),)


class LotteryPool(models.Model):
    pool_id = models.BigAutoField(primary_key=True)
    lottery_id = models.BigIntegerField()
    reward_type = models.IntegerField()
    title = models.CharField(max_length=100)
    money = models.IntegerField()
    icon_nomal = models.CharField(max_length=100)
    icon_press = models.CharField(max_length=100)
    cnt = models.IntegerField()
    use_cnt = models.IntegerField()
    position = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lottery_pool'


class LotteryResult(models.Model):
    result_id = models.BigAutoField(primary_key=True)
    pool_id = models.BigIntegerField()
    activity_type = models.CharField(max_length=100)
    activity_id = models.IntegerField()
    sub_id = models.CharField(max_length=100)
    user_id = models.BigIntegerField()
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    reward_flag = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lottery_result'
        unique_together = (('activity_type', 'activity_id', 'sub_id', 'user_id'),)


class LuzhengChallengeCircleInfo(models.Model):
    group_run_id = models.BigIntegerField()
    circle_id = models.BigIntegerField()
    ts = models.DateTimeField()
    steps = models.IntegerField()
    days = models.IntegerField()
    rank = models.IntegerField()
    status = models.IntegerField()
    circle_title = models.CharField(max_length=128)
    user_cnt = models.IntegerField()
    url = models.TextField()
    recommed_rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'luzheng_challenge_circle_info'
        unique_together = (('circle_id', 'group_run_id'),)


class LuzhengChallengeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()
    user_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'luzheng_challenge_run_info'


class LuzhengChallengeUserDayInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    day_id = models.CharField(max_length=10)
    ts = models.DateTimeField()
    steps = models.IntegerField()
    status = models.IntegerField()
    yessteps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'luzheng_challenge_user_day_info'
        unique_together = (('user_id', 'group_run_id', 'day_id'),)


class LuzhengChallengeUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    ts = models.DateTimeField()
    steps = models.IntegerField()
    days = models.IntegerField()
    status = models.IntegerField()
    circle_id = models.BigIntegerField()
    reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'luzheng_challenge_user_info'
        unique_together = (('user_id', 'group_run_id'),)


class MallActivityInfo(models.Model):
    mall_activity_id = models.BigAutoField(primary_key=True)
    the_goal = models.IntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()
    user_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mall_activity_info'


class MallActivityTop(models.Model):
    activity_top_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    mall_activity_id = models.IntegerField()
    money_reward = models.IntegerField()
    real_reward = models.IntegerField()
    real_name = models.CharField(max_length=32)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mall_activity_top'


class MallActivityUserInfo(models.Model):
    mall_activity_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    day_id = models.CharField(max_length=10)
    ts = models.DateTimeField()
    rep_draw = models.IntegerField()
    use_draw = models.IntegerField()
    money_reward = models.IntegerField()
    real_reward = models.IntegerField()
    real_name = models.CharField(max_length=32)
    status = models.IntegerField()
    share_draw_once = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mall_activity_user_info'
        unique_together = (('user_id', 'mall_activity_id', 'day_id'),)


class MallBuyer(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    phone = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mall_buyer'


class MallBuyerAddressLkb(models.Model):
    buyer_id = models.BigIntegerField()
    phone = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    province = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    street = models.CharField(max_length=256)
    user_id = models.BigIntegerField(primary_key=True)
    default_address = models.IntegerField()
    address_number = models.CharField(max_length=32)
    ts = models.DateTimeField()
    address = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'mall_buyer_address_lkb'


class MallBuyerNew(models.Model):
    buyer_id = models.BigIntegerField(primary_key=True)
    phone = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    province = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    street = models.CharField(max_length=256)
    user_id = models.BigIntegerField()
    default_address = models.IntegerField()
    address_number = models.CharField(max_length=32)
    ts = models.DateTimeField()
    address = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'mall_buyer_new'


class MallCar(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    circle_id = models.BigIntegerField()
    status = models.IntegerField()
    color = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    order_num = models.IntegerField()
    cre_ts = models.DateTimeField()
    invalid_ts = models.DateTimeField()
    remark = models.CharField(max_length=512)
    attribute_id = models.BigIntegerField()
    isdel = models.IntegerField()
    product_price = models.IntegerField()
    ts = models.DateTimeField()
    express_name = models.CharField(max_length=64)
    express_id = models.CharField(max_length=64)
    check_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mall_car'


class MallCircleProduct(models.Model):
    circle_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    sale = models.IntegerField()
    ts = models.DateTimeField()
    comment = models.CharField(max_length=256)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mall_circle_product'
        unique_together = (('circle_id', 'product_id'),)


class MallCoupon(models.Model):
    coupon_id = models.BigAutoField(primary_key=True)
    coupon_name = models.CharField(max_length=256)
    product_ids = models.CharField(max_length=256)
    user_id = models.BigIntegerField()
    cat_ids = models.CharField(max_length=256)
    coupon_description = models.CharField(max_length=512)
    coupon_pic_ids = models.CharField(max_length=256)
    circle_id = models.IntegerField()
    status = models.IntegerField()
    coupon_amount = models.IntegerField()
    get_amount = models.IntegerField()
    use_amount = models.IntegerField()
    type = models.IntegerField()
    coupon_type = models.IntegerField()
    coupon_limit_1 = models.IntegerField()
    coupon_reward = models.IntegerField()
    coupon_sale = models.IntegerField()
    cre_ts = models.DateTimeField()
    issue_ts = models.DateTimeField()
    start_ts = models.DateTimeField()
    end_ts = models.DateTimeField()
    coupon_priority = models.IntegerField()
    remark = models.CharField(max_length=512)
    ts = models.DateTimeField()
    type_turn = models.IntegerField()
    isdel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mall_coupon'


class MallCouponRecords(models.Model):
    coupon_record_id = models.BigAutoField(primary_key=True)
    coupon_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    status = models.IntegerField()
    cre_ts = models.DateTimeField()
    issue_ts = models.DateTimeField()
    isdel = models.IntegerField()
    remark = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'mall_coupon_records'


class MallOrder(models.Model):
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField(primary_key=True)
    product_id = models.BigIntegerField()
    status = models.IntegerField()
    order_ts = models.DateTimeField()
    pay_ts = models.DateTimeField()
    send_ts = models.DateTimeField()
    got_ts = models.DateTimeField()
    ts = models.DateTimeField()
    phone = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    comment = models.CharField(max_length=512)
    pay_money = models.IntegerField()
    remark = models.CharField(max_length=512)
    express_name = models.CharField(max_length=64)
    express_id = models.CharField(max_length=64)
    circle_id = models.IntegerField()
    order_num = models.IntegerField()
    isdel = models.IntegerField()
    color = models.TextField()
    size = models.TextField()
    pay_cash = models.IntegerField()
    buyer_id = models.BigIntegerField()
    attribute_id = models.BigIntegerField()
    car_ids = models.CharField(max_length=256)
    coupon_reward = models.IntegerField()
    send_type = models.IntegerField()
    check_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mall_order'


class MallOrderPayDetail(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    pay_money = models.IntegerField()
    pay_cash = models.IntegerField()
    pay_price = models.IntegerField()
    comment = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'mall_order_pay_detail'


class MallPcRelation(models.Model):
    pc_relation_id = models.BigAutoField(primary_key=True)
    cat_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    sort = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    remark = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'mall_pc_relation'


class MallProduct(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    express_type = models.IntegerField()
    price = models.IntegerField()
    reward_muli = models.FloatField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    photo_ids = models.CharField(max_length=256)
    buyer_num = models.IntegerField()
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    description = models.TextField()
    prioriy = models.IntegerField()
    real_price = models.IntegerField()
    type = models.IntegerField()
    sale = models.IntegerField()
    rebates = models.IntegerField()
    brand_id = models.BigIntegerField()
    slogan = models.CharField(max_length=256)
    icon_text = models.CharField(max_length=256)
    type_special = models.IntegerField()
    owner = models.CharField(max_length=32)
    self_type = models.IntegerField()
    cost = models.IntegerField()
    supplier_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mall_product'


class MallProductBrand(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    cat_id = models.BigIntegerField()
    ch_name = models.CharField(max_length=128)
    en_name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    logo_id = models.BigIntegerField()
    status = models.IntegerField()
    url = models.TextField()
    introduction = models.TextField()
    ts = models.DateTimeField()
    remark = models.CharField(max_length=512)
    sort = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mall_product_brand'


class MallProductCat(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    sort = models.BigIntegerField()
    parent_cat_id = models.BigIntegerField()
    parent_show = models.IntegerField()
    icon_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    remark = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'mall_product_cat'


class MallProductCommit(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    express_type = models.IntegerField()
    price = models.IntegerField()
    reward_muli = models.FloatField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    photo_ids = models.CharField(max_length=256)
    buyer_num = models.IntegerField()
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    prioriy = models.IntegerField()
    real_price = models.IntegerField()
    type = models.IntegerField()
    sale = models.IntegerField()
    rebates = models.IntegerField()
    brand_id = models.BigIntegerField()
    slogan = models.CharField(max_length=256)
    icon_text = models.CharField(max_length=256)
    type_special = models.IntegerField()
    owner = models.CharField(max_length=32)
    self_type = models.IntegerField()
    cost = models.IntegerField()
    supplier_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mall_product_commit'


class MallProductRelations(models.Model):
    mpr_id = models.BigAutoField(primary_key=True)
    m_rid = models.BigIntegerField()
    m_pid = models.BigIntegerField()
    sort = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    remark = models.CharField(max_length=512)
    source = models.CharField(max_length=32)
    m_title = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mall_product_relations'


class MallRewardRealInfo(models.Model):
    user_id = models.BigIntegerField()
    mall_activity_id = models.IntegerField()
    reward_type = models.IntegerField()
    reward_pos = models.IntegerField()
    reward_name = models.CharField(max_length=32)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mall_reward_real_info'


class MallSmsSend(models.Model):
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=32)
    content = models.CharField(max_length=512)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mall_sms_send'


class MallSupplier(models.Model):
    s_id = models.BigAutoField(primary_key=True)
    s_name = models.CharField(max_length=128)
    s_description = models.CharField(max_length=255)
    s_status = models.IntegerField()
    s_person = models.CharField(max_length=40)
    s_address = models.CharField(max_length=50)
    s_zipcode = models.CharField(max_length=6)
    s_tel = models.CharField(max_length=40)
    s_qq = models.CharField(max_length=40)
    s_email = models.CharField(max_length=40)
    s_url = models.CharField(max_length=40)
    ts = models.DateTimeField()
    remark = models.CharField(max_length=512)
    source = models.CharField(max_length=32)
    s_express_address = models.CharField(max_length=50)
    s_express_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'mall_supplier'


class MallTheme(models.Model):
    mt_id = models.BigAutoField(primary_key=True)
    mt_title = models.CharField(max_length=128)
    mt_subtitle = models.CharField(max_length=256)
    mt_status = models.IntegerField()
    mt_sort = models.BigIntegerField()
    mt_content = models.CharField(max_length=512)
    mt_pic_ids = models.CharField(max_length=256)
    mt_icon_ids = models.CharField(max_length=128)
    mt_count = models.IntegerField()
    mt_parent_id = models.BigIntegerField()
    mt_remark = models.CharField(max_length=512)
    mt_source = models.CharField(max_length=32)
    mt_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mall_theme'


class MallorderTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mallorder_tickets64'


class MallorderTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mallorder_tickets64_innodb'


class MarathonRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    types = models.CharField(max_length=255)
    join_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'marathon_run_info'


class MarathonRunnerInfo(models.Model):
    phone = models.CharField(max_length=16)
    teamid = models.IntegerField()
    teamtype = models.IntegerField()
    runtype = models.IntegerField()
    name = models.CharField(max_length=64)
    sex = models.IntegerField()
    birthday = models.CharField(max_length=32)
    bloodtype = models.IntegerField()
    country = models.CharField(max_length=32)
    idtype = models.IntegerField()
    id = models.CharField(max_length=32)
    contactname = models.CharField(max_length=16)
    contactphone = models.CharField(max_length=16)
    ts = models.DateTimeField()
    relayrace = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'marathon_runner_info'


class MarathonTeamInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    phonereg = models.CharField(db_column='phoneReg', max_length=16)  # Field name made lowercase.
    teamname = models.CharField(max_length=64)
    teamleader = models.CharField(max_length=16)
    teamleaderphone = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'marathon_team_info'


class MarathonTop(models.Model):
    user_id = models.BigIntegerField()
    sex = models.IntegerField()
    type = models.IntegerField()
    rank = models.IntegerField()
    join_cnt = models.IntegerField()
    cost_time = models.IntegerField()
    marathon_id = models.BigIntegerField()
    complete_ts = models.DateTimeField()
    flag = models.IntegerField()
    reward_cnt = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marathon_top'
        unique_together = (('user_id', 'type'),)


class MarathonTop100(models.Model):
    user_id = models.BigIntegerField()
    sex = models.IntegerField()
    type = models.IntegerField()
    rank = models.IntegerField()
    join_cnt = models.IntegerField()
    cost_time = models.IntegerField()
    marathon_id = models.BigIntegerField()
    complete_ts = models.DateTimeField()
    flag = models.IntegerField()
    reward_cnt = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marathon_top_100'
        unique_together = (('user_id', 'type'),)


class MarathonTopReward100(models.Model):
    user_id = models.BigIntegerField()
    sex = models.IntegerField()
    type = models.IntegerField()
    rank = models.IntegerField()
    join_cnt = models.IntegerField()
    cost_time = models.IntegerField()
    marathon_id = models.BigIntegerField()
    complete_ts = models.DateTimeField()
    flag = models.IntegerField()
    reward_cnt = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marathon_top_reward_100'
        unique_together = (('user_id', 'type'),)


class MarathonUserRunInfo(models.Model):
    marathon_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.IntegerField()
    distance = models.IntegerField()
    begin_ts = models.DateTimeField()
    end_ts = models.DateTimeField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    group_run_id = models.BigIntegerField()
    comeons = models.TextField(db_column='ComeOns')  # Field name made lowercase.
    reward = models.IntegerField()
    reward_comment = models.CharField(max_length=256)
    report_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marathon_user_run_info'


class MarathonUserRunInfoTop(models.Model):
    marathon_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.IntegerField()
    distance = models.IntegerField()
    begin_ts = models.DateTimeField()
    end_ts = models.DateTimeField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    group_run_id = models.BigIntegerField()
    comeons = models.TextField(db_column='ComeOns')  # Field name made lowercase.
    reward = models.IntegerField()
    reward_comment = models.CharField(max_length=256)
    report_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marathon_user_run_info_top'


class MediaGallery(models.Model):
    name = models.CharField(max_length=255)
    context = models.CharField(max_length=64)
    default_format = models.CharField(max_length=255)
    enabled = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'media__gallery'


class MediaGalleryMedia(models.Model):
    gallery = models.ForeignKey(MediaGallery, models.DO_NOTHING, blank=True, null=True)
    media = models.ForeignKey('MediaMedia', models.DO_NOTHING, blank=True, null=True)
    position = models.IntegerField()
    enabled = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'media__gallery_media'


class MediaMedia(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    enabled = models.IntegerField()
    provider_name = models.CharField(max_length=255)
    provider_status = models.IntegerField()
    provider_reference = models.CharField(max_length=255)
    provider_metadata = models.TextField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    content_type = models.CharField(max_length=64, blank=True, null=True)
    content_size = models.IntegerField(blank=True, null=True)
    copyright = models.CharField(max_length=255, blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=64, blank=True, null=True)
    cdn_is_flushable = models.IntegerField(blank=True, null=True)
    cdn_flush_at = models.DateTimeField(blank=True, null=True)
    cdn_status = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'media__media'


class MessageDelete(models.Model):
    user_id = models.BigIntegerField()
    message_id = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'message_delete'
        unique_together = (('user_id', 'message_id'),)


class MessageInfo(models.Model):
    message_id = models.BigIntegerField()
    from_user_id = models.BigIntegerField()
    to_user_id = models.BigIntegerField()
    content = models.CharField(max_length=1024)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_info'


class MessageInfoOld(models.Model):
    message_id = models.BigIntegerField()
    from_user_id = models.BigIntegerField()
    to_user_id = models.BigIntegerField()
    content = models.CharField(max_length=512)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_info_old'


class MessageInfoUniq(models.Model):
    message_id = models.BigIntegerField()
    from_user_id = models.BigIntegerField()
    to_user_id = models.BigIntegerField()
    content = models.CharField(max_length=1024)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_info_uniq'


class MessageInfoUniqOld(models.Model):
    message_id = models.BigIntegerField()
    from_user_id = models.BigIntegerField(primary_key=True)
    to_user_id = models.BigIntegerField()
    content = models.CharField(max_length=512)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_info_uniq_old'


class MessageTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'message_tickets64'


class MessageTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'message_tickets64_innodb'


class MessageUnread(models.Model):
    from_user_id = models.BigIntegerField()
    to_user_id = models.BigIntegerField()
    message_id = models.BigIntegerField()
    is_read = models.IntegerField()
    ts = models.DateTimeField()
    content = models.CharField(max_length=512)
    is_friend = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_unread'
        unique_together = (('from_user_id', 'to_user_id'),)


class MillChallengeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()
    kind_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mill_challenge_run_info'


class MillChallengeUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    ts = models.DateTimeField()
    avg_speed = models.IntegerField()
    status_level = models.IntegerField()
    comeons = models.TextField(db_column='ComeOns')  # Field name made lowercase.
    reward = models.IntegerField()
    status = models.IntegerField()
    wx_bind_tips = models.IntegerField()
    distance = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mill_challenge_user_info'
        unique_together = (('user_id', 'group_run_id'),)


class MonkeyDrawInfo(models.Model):
    monkey_id = models.IntegerField()
    user_id = models.BigIntegerField()
    sex = models.IntegerField()
    name = models.CharField(max_length=50)
    monkey = models.CharField(max_length=5)
    content = models.CharField(max_length=50)
    p_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'monkey_draw_info'


class MonthRemain(models.Model):
    month = models.CharField(max_length=32)
    begin_day = models.CharField(max_length=32)
    end_day = models.CharField(max_length=32)
    kind = models.IntegerField()
    channel = models.CharField(max_length=64)
    cnt = models.IntegerField()
    month1 = models.FloatField()
    month2 = models.FloatField()
    month3 = models.FloatField()
    month4 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'month_remain'
        unique_together = (('month', 'kind', 'channel'),)


class MonthStat(models.Model):
    month = models.CharField(primary_key=True, max_length=32)
    total_user = models.IntegerField()
    active_user = models.IntegerField()
    android_app_active_user = models.IntegerField()
    ios_app_active_user = models.IntegerField()
    cms_seed_user = models.IntegerField()
    android_app_user = models.IntegerField()
    android_app_pre_user = models.IntegerField()
    ios_app_user = models.IntegerField()
    ios_app_pre_user = models.IntegerField()
    mobileweb_user = models.IntegerField()
    marketing_user = models.IntegerField()
    not_need_phone_code = models.IntegerField()
    need_phone_code = models.IntegerField()
    register_fail_cnt = models.IntegerField()
    runner_cnt = models.IntegerField()
    runner_autorecord_cnt = models.IntegerField()
    runner_indoor_distance = models.IntegerField()
    runner_outdoor_distance = models.IntegerField()
    runner_autorecord_distance = models.IntegerField()
    runner_distance = models.IntegerField()
    runner_indoor_cnt = models.IntegerField()
    runner_outdoor_cnt = models.IntegerField()
    runner_nomal_cnt = models.IntegerField()
    runner_trick_cnt = models.IntegerField()
    activity_normal_cnt = models.IntegerField()
    activity_seed_cnt = models.IntegerField()
    activity_invite_cnt = models.IntegerField()
    activity_apply_cnt = models.IntegerField()
    activity_join_cnt = models.IntegerField()
    discussion_cnt = models.IntegerField()
    feed_cnt = models.IntegerField()
    photo_cnt = models.IntegerField()
    intro_photo_cnt = models.IntegerField()
    feed_photo_cnt = models.IntegerField()
    wangcai_download = models.IntegerField()
    wangcai_register = models.IntegerField()
    runner_outdoor_user_cnt = models.IntegerField()
    pv = models.IntegerField()
    cumsum_user = models.IntegerField()
    ignore_new_user = models.IntegerField()
    runner_autorecord_user_cnt = models.IntegerField()
    runner_indoor_user_cnt = models.IntegerField()
    runner_all_user_cnt = models.IntegerField()
    runner_ride_user_cnt = models.IntegerField()
    runner_ride_cnt = models.IntegerField()
    runner_ride_distance = models.IntegerField()
    web_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'month_stat'


class NdayChallengeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    session_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nday_challenge_run_info'


class NdayChallengeUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    days = models.IntegerField()
    distances = models.IntegerField()
    steps = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nday_challenge_user_info'
        unique_together = (('user_id', 'group_run_id'),)


class NewUserStat(models.Model):
    begin_day = models.CharField(max_length=16)
    end_day = models.CharField(max_length=16)
    new_cnt = models.IntegerField()
    kind_id = models.IntegerField()
    step_cnt = models.FloatField()
    run_cnt = models.FloatField()
    ride_cnt = models.FloatField()
    can_draw_reward_cnt = models.FloatField()
    draw_reward_cnt = models.FloatField()
    join_yinhua_cnt = models.FloatField()
    complete_yinhua_cnt = models.FloatField()
    join_circle_cnt = models.FloatField()
    join_circle_game_cnt = models.FloatField()
    add_ugc_cnt = models.FloatField()
    share_cnt = models.FloatField()
    add_follow_cnt = models.FloatField()
    client_new_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'new_user_stat'
        unique_together = (('begin_day', 'end_day', 'kind_id'),)


class NkmChallengeReportUser(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    num = models.IntegerField()
    avg_speed = models.IntegerField()
    status_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nkm_challenge_report_user'
        unique_together = (('user_id', 'group_run_id'),)


class NkmChallengeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nkm_challenge_run_info'


class NkmChallengeStat(models.Model):
    session_num = models.IntegerField(primary_key=True)
    group_run_id = models.IntegerField()
    join_cnt = models.IntegerField()
    complete_cnt = models.IntegerField()
    new_join_cnt = models.IntegerField()
    new_complete_cnt = models.IntegerField()
    reward_cnt = models.IntegerField()
    reward_sum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nkm_challenge_stat'


class NkmChallengeUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    num = models.IntegerField()
    avg_speed = models.IntegerField()
    status_level = models.IntegerField()
    comeons = models.TextField(db_column='ComeOns')  # Field name made lowercase.
    reward = models.IntegerField()
    wx_bind_tips = models.IntegerField()
    reward_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nkm_challenge_user_info'
        unique_together = (('user_id', 'group_run_id'),)


class NkmChallengeUserInfoCity(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    num = models.IntegerField()
    avg_speed = models.IntegerField()
    status_level = models.IntegerField()
    comeons = models.TextField(db_column='ComeOns')  # Field name made lowercase.
    reward = models.IntegerField()
    wx_bind_tips = models.IntegerField()
    country_rank = models.IntegerField()
    city_rank = models.IntegerField()
    city = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'nkm_challenge_user_info_city'
        unique_together = (('user_id', 'group_run_id'),)


class NkmndayChallengeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()
    user_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nkmnday_challenge_run_info'


class NkmndayChallengeTop(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.IntegerField()
    money_reward = models.IntegerField()
    real_reward = models.IntegerField()
    real_name = models.CharField(max_length=32)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nkmnday_challenge_top'


class NkmndayChallengeUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    day_id = models.CharField(max_length=10)
    ts = models.DateTimeField()
    cmp_draw = models.IntegerField()
    rep_draw = models.IntegerField()
    share_draw = models.IntegerField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    score = models.IntegerField()
    money_reward = models.IntegerField()
    real_reward = models.IntegerField()
    real_name = models.CharField(max_length=32)
    status = models.IntegerField()
    share_draw_once = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nkmnday_challenge_user_info'
        unique_together = (('user_id', 'group_run_id', 'day_id'),)


class NoRideCircle(models.Model):
    circle_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'no_ride_circle'


class OpenAppKey(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    app_key = models.CharField(max_length=150)
    icon = models.CharField(max_length=150)
    status = models.IntegerField()
    api_list = models.CharField(max_length=200)
    ts = models.DateTimeField()
    safe_domain = models.CharField(max_length=100)
    wait_check = models.IntegerField()
    app_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'open_app_key'


class OpenidInfo(models.Model):
    open_id = models.CharField(primary_key=True, max_length=128)
    source = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    access_token = models.CharField(max_length=512)
    union_id = models.CharField(max_length=128)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'openid_info'


class OpenidInfoUnbind(models.Model):
    open_id = models.CharField(max_length=128)
    source = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    access_token = models.CharField(max_length=512)
    union_id = models.CharField(max_length=128)
    type = models.IntegerField()
    insert_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'openid_info_unbind'


class OpenidUnionidInfo(models.Model):
    open_id = models.CharField(primary_key=True, max_length=128)
    source = models.CharField(max_length=32)
    status = models.IntegerField()
    ts = models.DateTimeField()
    access_token = models.CharField(max_length=512)
    union_id = models.CharField(max_length=128)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'openid_unionid_info'


class OpenidUnionidRegister(models.Model):
    open_id = models.CharField(primary_key=True, max_length=128)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'openid_unionid_register'


class OpenidUnionidRegisterFromApp(models.Model):
    union_id = models.CharField(primary_key=True, max_length=128)
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'openid_unionid_register_from_app'


class Page(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'page'


class PayTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pay_tickets64'


class PayTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pay_tickets64_innodb'


class PhoneCodeTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.IntegerField()
    phone = models.CharField(max_length=16)
    content = models.CharField(max_length=1024)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'phone_code_tickets64'


class PhoneCodeTickets64Bk(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.IntegerField()
    phone = models.CharField(max_length=16)
    content = models.CharField(max_length=1024)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'phone_code_tickets64_bk'


class PhoneCodeTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.IntegerField()
    phone = models.CharField(max_length=16)
    content = models.CharField(max_length=1024)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'phone_code_tickets64_innodb'


class PhotoInfo(models.Model):
    photo_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    upload_id = models.BigIntegerField()
    feed_id = models.BigIntegerField()
    topic_id = models.BigIntegerField()
    status = models.IntegerField()
    note = models.CharField(max_length=256)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'photo_info'


class PhotoTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'photo_tickets64'


class PhotoTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'photo_tickets64_innodb'


class PkInfo(models.Model):
    pk_id = models.BigIntegerField(primary_key=True)
    active_user_id = models.BigIntegerField()
    active_user_step = models.IntegerField()
    passive_user_id = models.BigIntegerField()
    passive_user_step = models.IntegerField()
    ts = models.DateTimeField()
    pk_back_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pk_info'


class PkPushInfo(models.Model):
    pk_id = models.BigIntegerField(primary_key=True)
    active_user_id = models.BigIntegerField()
    passive_user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    sign = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pk_push_info'


class PkTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pk_tickets64_innodb'


class PlatformAuthApilistInfo(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_level = models.IntegerField()
    description = models.CharField(max_length=300)
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'platform_auth_apilist_info'


class PlatformAuthAppInfo(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    app_key = models.CharField(max_length=150)
    icon = models.CharField(max_length=150)
    api_list = models.CharField(max_length=200)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'platform_auth_app_info'


class PlatformExtraInfo(models.Model):
    app_id = models.BigIntegerField(primary_key=True)
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    legal_person = models.CharField(max_length=100)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'platform_extra_info'


class PrizeDynamic(models.Model):
    dynamic_id = models.BigAutoField(primary_key=True)
    pool_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    rank_group_id = models.BigIntegerField()
    nick = models.CharField(max_length=100)
    prize_id = models.BigIntegerField()
    money_reward = models.IntegerField()
    real_reward = models.CharField(max_length=100)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'prize_dynamic'


class PrizeInfo(models.Model):
    prize_id = models.BigAutoField(primary_key=True)
    group_run_id = models.BigIntegerField()
    title = models.CharField(max_length=100)
    type = models.IntegerField()
    icon_nomal = models.CharField(max_length=100)
    icon_press = models.CharField(max_length=400, blank=True, null=True)
    cnt = models.IntegerField()
    use_cnt = models.IntegerField()
    position = models.IntegerField()
    begin_days = models.IntegerField()
    end_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prize_info'


class PrizePool(models.Model):
    pool_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    prize_id = models.BigIntegerField()
    money = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'prize_pool'


class ProductAttribute(models.Model):
    product_attribute_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    status = models.IntegerField()
    color = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    stock = models.IntegerField()
    ts = models.DateTimeField()
    sequence = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'product_attribute'


class ProductBanner(models.Model):
    banner_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    url = models.TextField()
    ts = models.DateTimeField()
    redirect_type = models.IntegerField()
    redirect_id = models.BigIntegerField()
    redirect_url = models.TextField()
    sort = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'product_banner'


class ProductContentPic(models.Model):
    product_frag_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    product_order = models.BigIntegerField()
    photo_id = models.BigIntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    content = models.TextField()
    isdel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_content_pic'


class ProductContentPicCommit(models.Model):
    product_frag_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    product_order = models.BigIntegerField()
    photo_id = models.BigIntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    content = models.TextField()
    isdel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_content_pic_commit'


class ProvinceCity(models.Model):
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'province_city'
        unique_together = (('province', 'city'),)


class PusherInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    pusher_user_id = models.CharField(max_length=32)
    pusher_channel_id = models.CharField(max_length=32)
    device_token = models.CharField(max_length=128)
    platform = models.CharField(max_length=16)
    login = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pusher_info'


class PusherRecord(models.Model):
    id = models.AutoField()
    user_id = models.BigIntegerField()
    message = models.TextField()
    is_send = models.IntegerField()
    is_read = models.IntegerField()
    platform = models.CharField(max_length=16)
    ts = models.DateTimeField()
    dead_time = models.DateTimeField()
    is_hx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pusher_record'


class PusherRecordBk(models.Model):
    id = models.AutoField()
    user_id = models.BigIntegerField()
    message = models.TextField()
    is_send = models.IntegerField()
    is_read = models.IntegerField()
    platform = models.CharField(max_length=16)
    ts = models.DateTimeField()
    dead_time = models.DateTimeField()
    is_hx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pusher_record_bk'


class QqrankChallengeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    user_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qqrank_challenge_run_info'


class QqrankChallengeUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    days = models.IntegerField()
    distances = models.IntegerField()
    steps = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'qqrank_challenge_user_info'
        unique_together = (('user_id', 'group_run_id'),)


class RankGroupRewardInfo(models.Model):
    reward_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    rank_group_id = models.BigIntegerField()
    rank = models.IntegerField()
    reward_type = models.IntegerField()
    money = models.IntegerField()
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    ts = models.DateTimeField()
    reward_flag = models.IntegerField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rank_group_reward_info'
        unique_together = (('rank_group_id', 'rank'),)


class RankGroupRunInfo(models.Model):
    rank_group_id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    join_cnt = models.IntegerField()
    session_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rank_group_run_info'


class RankHistory(models.Model):
    day_id = models.CharField(max_length=50)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    script_type = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'rank_history'


class RankList(models.Model):
    rank = models.BigIntegerField(primary_key=True)
    growth_value = models.BigIntegerField()
    title = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rank_list'


class RankUserGroupRun(models.Model):
    user_id = models.BigIntegerField()
    rank_group_id = models.BigIntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward_flag = models.IntegerField()
    money_reward = models.IntegerField()
    real_reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rank_user_group_run'
        unique_together = (('user_id', 'rank_group_id'),)


class ReportStat(models.Model):
    day = models.DateField()
    ver = models.CharField(max_length=32)
    cmd = models.CharField(max_length=32)
    phone_type = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    location_sdk = models.IntegerField()
    time = models.IntegerField()
    ts = models.DateTimeField()
    detail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report_stat'


class ReportStat20160309(models.Model):
    day = models.DateField()
    ver = models.CharField(max_length=32)
    cmd = models.CharField(max_length=32)
    phone_type = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    location_sdk = models.IntegerField()
    time = models.IntegerField()
    ts = models.DateTimeField()
    detail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report_stat_20160309'


class ReportStat20160310(models.Model):
    day = models.DateField()
    ver = models.CharField(max_length=32)
    cmd = models.CharField(max_length=32)
    phone_type = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    location_sdk = models.IntegerField()
    time = models.IntegerField()
    ts = models.DateTimeField()
    detail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report_stat_20160310'


class ReportStat20160311(models.Model):
    day = models.DateField()
    ver = models.CharField(max_length=32)
    cmd = models.CharField(max_length=32)
    phone_type = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    location_sdk = models.IntegerField()
    time = models.IntegerField()
    ts = models.DateTimeField()
    detail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report_stat_20160311'


class ReportStat20160312(models.Model):
    day = models.DateField()
    ver = models.CharField(max_length=32)
    cmd = models.CharField(max_length=32)
    phone_type = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    location_sdk = models.IntegerField()
    time = models.IntegerField()
    ts = models.DateTimeField()
    detail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report_stat_20160312'


class ReportStat20160313(models.Model):
    day = models.DateField()
    ver = models.CharField(max_length=32)
    cmd = models.CharField(max_length=32)
    phone_type = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    location_sdk = models.IntegerField()
    time = models.IntegerField()
    ts = models.DateTimeField()
    detail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report_stat_20160313'


class ReportStat20160314(models.Model):
    day = models.DateField()
    ver = models.CharField(max_length=32)
    cmd = models.CharField(max_length=32)
    phone_type = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    location_sdk = models.IntegerField()
    time = models.IntegerField()
    ts = models.DateTimeField()
    detail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report_stat_20160314'


class RequestDetail(models.Model):
    name = models.CharField(max_length=128)
    kind = models.CharField(max_length=32)
    time = models.IntegerField()
    code_2xx = models.IntegerField()
    code_4xx = models.IntegerField()
    code_5xx = models.IntegerField()
    avg_byte = models.IntegerField()
    cnt = models.IntegerField()
    ts = models.DateTimeField()
    sec = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'request_detail'


class RewardLoginUser(models.Model):
    user_id = models.BigIntegerField()
    reward_id = models.IntegerField()
    reward_type = models.IntegerField()
    reward_pos = models.IntegerField()
    ts = models.DateTimeField()
    reward_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'reward_login_user'


class RewardLoginUserBk(models.Model):
    user_id = models.BigIntegerField()
    reward_id = models.IntegerField()
    reward_type = models.IntegerField()
    reward_pos = models.IntegerField()
    ts = models.DateTimeField()
    reward_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'reward_login_user_bk'


class RewardRealInfo(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.IntegerField()
    reward_type = models.IntegerField()
    reward_pos = models.IntegerField()
    reward_name = models.CharField(max_length=32)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reward_real_info'


class RideCircle(models.Model):
    circle_id = models.BigIntegerField(primary_key=True)
    slogan = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'ride_circle'


class RideUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ride_user'


class RoadBookContent(models.Model):
    book_id = models.BigIntegerField(primary_key=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'road_book_content'


class RoadBookInfo(models.Model):
    book_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    star = models.FloatField()
    distance = models.BigIntegerField()
    discuss_cnt = models.IntegerField()
    read_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=128)
    photo = models.CharField(max_length=128)
    ts = models.DateTimeField()
    update_ts = models.DateTimeField()
    hotrank = models.IntegerField()
    hotrank_type = models.IntegerField()
    note = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'road_book_info'


class RoadBookPhoto(models.Model):
    book_id = models.BigIntegerField()
    photo_id = models.BigIntegerField(primary_key=True)
    photo_url = models.CharField(max_length=128)
    order_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'road_book_photo'


class RrdStat(models.Model):
    day = models.CharField(max_length=32)
    sec = models.IntegerField(primary_key=True)
    req = models.IntegerField()
    avg_time = models.IntegerField()
    number_4xx = models.IntegerField(db_column='4xx')  # Field renamed because it wasn't a valid Python identifier.
    number_5xx = models.IntegerField(db_column='5xx')  # Field renamed because it wasn't a valid Python identifier.
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rrd_stat'


class RunGame(models.Model):
    run_id = models.CharField(max_length=32)
    run_name = models.CharField(max_length=128)
    filename = models.CharField(max_length=128)
    ts = models.DateTimeField()
    rotate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'run_game'
        unique_together = (('run_id', 'run_name', 'filename'),)


class RunnerGeoArea(models.Model):
    geo = models.CharField(primary_key=True, max_length=16)
    geo_cnt = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    jingwei_province = models.CharField(max_length=32)
    jingwei_city = models.CharField(max_length=32)
    jingwei_district = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'runner_geo_area'


class RunnerGeoAreaBak(models.Model):
    geo = models.CharField(primary_key=True, max_length=16)
    geo_cnt = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    jingwei_province = models.CharField(max_length=32)
    jingwei_city = models.CharField(max_length=32)
    jingwei_district = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'runner_geo_area_bak'


class RunnerGeoMemory(models.Model):
    geo = models.CharField(primary_key=True, max_length=16)
    geo_cnt = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'runner_geo_memory'


class RunnerIdCompare(models.Model):
    ride_runner_id = models.BigIntegerField()
    sport_runner_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'runner_id_compare'
        unique_together = (('ride_runner_id', 'sport_runner_id'),)


class RunnerInfo(models.Model):
    runner_id = models.BigIntegerField(primary_key=True)
    kind_id = models.IntegerField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    avg_pace = models.IntegerField()
    avg_speed = models.IntegerField()
    caloric = models.IntegerField()
    weather = models.CharField(max_length=64)
    feeling = models.CharField(max_length=512)
    detail = models.TextField()
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    audio_id = models.BigIntegerField()
    location_sdk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_info'


class RunnerInfo20150914(models.Model):
    runner_id = models.BigIntegerField(primary_key=True)
    kind_id = models.IntegerField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    avg_pace = models.IntegerField()
    avg_speed = models.IntegerField()
    caloric = models.IntegerField()
    weather = models.CharField(max_length=64)
    feeling = models.CharField(max_length=512)
    detail = models.TextField()
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    audio_id = models.BigIntegerField()
    location_sdk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_info_20150914'


class RunnerInfoCompress(models.Model):
    runner_id = models.BigIntegerField(primary_key=True)
    kind_id = models.IntegerField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    avg_pace = models.IntegerField()
    avg_speed = models.IntegerField()
    caloric = models.IntegerField()
    weather = models.CharField(max_length=64)
    feeling = models.CharField(max_length=512)
    detail_compress = models.TextField()
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    audio_id = models.BigIntegerField()
    location_sdk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_info_compress'


class RunnerInfoCompressHistory(models.Model):
    runner_id = models.BigIntegerField(primary_key=True)
    kind_id = models.IntegerField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    avg_pace = models.IntegerField()
    avg_speed = models.IntegerField()
    caloric = models.IntegerField()
    weather = models.CharField(max_length=64)
    feeling = models.CharField(max_length=512)
    detail_compress = models.TextField()
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    audio_id = models.BigIntegerField()
    location_sdk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_info_compress_history'


class RunnerInfoCompressNewer(models.Model):
    runner_id = models.BigIntegerField(primary_key=True)
    kind_id = models.IntegerField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    avg_pace = models.IntegerField()
    avg_speed = models.IntegerField()
    caloric = models.IntegerField()
    weather = models.CharField(max_length=64)
    feeling = models.CharField(max_length=512)
    detail_compress = models.TextField()
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    audio_id = models.BigIntegerField()
    location_sdk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_info_compress_newer'


class RunnerInfoDelLkb(models.Model):
    runner_id = models.BigIntegerField(primary_key=True)
    kind_id = models.IntegerField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    avg_pace = models.IntegerField()
    avg_speed = models.IntegerField()
    caloric = models.IntegerField()
    weather = models.CharField(max_length=64)
    feeling = models.CharField(max_length=512)
    detail = models.TextField()
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'runner_info_del_lkb'


class RunnerInfoExtra(models.Model):
    runner_id = models.BigIntegerField(primary_key=True)
    kind_id = models.IntegerField()
    inner_kind = models.CharField(max_length=128)
    inner_detail = models.TextField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'runner_info_extra'


class RunnerInfoHistory(models.Model):
    runner_id = models.BigIntegerField(primary_key=True)
    kind_id = models.IntegerField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    avg_pace = models.IntegerField()
    avg_speed = models.IntegerField()
    caloric = models.IntegerField()
    weather = models.CharField(max_length=64)
    feeling = models.CharField(max_length=512)
    detail = models.TextField()
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    audio_id = models.BigIntegerField()
    location_sdk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_info_history'


class RunnerMcInfo(models.Model):
    user_id = models.BigIntegerField()
    day = models.DateTimeField()
    step = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'runner_mc_info'
        unique_together = (('user_id', 'day'),)


class RunnerPathList(models.Model):
    runner_id = models.BigIntegerField()
    seq = models.IntegerField()
    geo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'runner_path_list'
        unique_together = (('runner_id', 'seq'),)


class RunnerTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'runner_tickets64'


class RunnerTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'runner_tickets64_innodb'


class RunnerTickets64Old(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'runner_tickets64_old'


class RunnerTop(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_top'
        unique_together = (('user_id', 'top_index'),)


class RunnerTopHistory(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_top_history'
        unique_together = (('user_id', 'top_index'),)


class RunnerTopLike(models.Model):
    from_user_id = models.BigIntegerField()
    to_user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'runner_top_like'
        unique_together = (('from_user_id', 'to_user_id', 'top_index'),)


class RunnerTopLikeStep(models.Model):
    from_user_id = models.BigIntegerField()
    to_user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'runner_top_like_step'
        unique_together = (('from_user_id', 'to_user_id', 'top_index'),)


class RunnerTopRide(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_top_ride'
        unique_together = (('user_id', 'top_index'),)


class RunnerTopStep(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_top_step'
        unique_together = (('user_id', 'top_index'),)


class RunnerTopStepBk(models.Model):
    user_id = models.BigIntegerField()
    top_index = models.CharField(max_length=64)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'runner_top_step_bk'
        unique_together = (('user_id', 'top_index'),)


class ShareRewardInfo(models.Model):
    share_id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    kind_id = models.IntegerField()
    reward_cnt = models.IntegerField()
    suprise_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    suprise_money = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    day = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'share_reward_info'


class ShareRewardStat(models.Model):
    day = models.CharField(primary_key=True, max_length=32)
    user_cnt = models.BigIntegerField()
    reward_sum = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'share_reward_stat'


class ShareUserRewardInfo(models.Model):
    user_id = models.BigIntegerField()
    share_id = models.BigIntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    reward_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'share_user_reward_info'
        unique_together = (('user_id', 'share_id'),)


class ShuiyinMaskInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    ts = models.DateTimeField()
    masks = models.TextField()

    class Meta:
        managed = False
        db_table = 'shuiyin_mask_info'


class ShuiyinRecord(models.Model):
    user_id = models.BigIntegerField()
    shuiyin_id = models.BigIntegerField(primary_key=True)
    dynamic_id = models.BigIntegerField()
    runner_id = models.BigIntegerField()
    kind_id = models.IntegerField()
    detail_pic_id = models.IntegerField()
    status = models.IntegerField()
    distance = models.IntegerField()
    sum_up = models.IntegerField()
    cost_time = models.IntegerField()
    avg_pace = models.IntegerField()
    avg_speed = models.IntegerField()
    caloric = models.IntegerField()
    feeling = models.CharField(max_length=512)
    run_ts = models.DateTimeField()
    update_t = models.DateTimeField()
    shuiyin_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shuiyin_record'


class ShuiyinRecordLike(models.Model):
    user_id = models.BigIntegerField()
    shuiyin_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shuiyin_record_like'
        unique_together = (('user_id', 'shuiyin_id'),)


class ShuiyinRecordNum(models.Model):
    shuiyin_id = models.BigIntegerField(primary_key=True)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shuiyin_record_num'


class ShuiyinTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shuiyin_tickets64'


class ShuiyinTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'shuiyin_tickets64_innodb'


class SlaveReadStat(models.Model):
    day = models.CharField(max_length=32)
    sec = models.IntegerField()
    error = models.IntegerField()
    io = models.CharField(max_length=11)
    sq = models.CharField(max_length=11)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'slave_read_stat'


class SlaveStat(models.Model):
    day = models.CharField(max_length=32)
    sec = models.IntegerField()
    error = models.IntegerField()
    io = models.CharField(max_length=11)
    sq = models.CharField(max_length=11)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'slave_stat'


class SlaveStatLocal(models.Model):
    day = models.CharField(max_length=32)
    sec = models.IntegerField()
    error = models.IntegerField()
    io = models.CharField(max_length=11)
    sq = models.CharField(max_length=11)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'slave_stat_local'


class SmsSend(models.Model):
    phone = models.CharField(max_length=32)
    content = models.CharField(max_length=512)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms_send'


class SpotAdBanner(models.Model):
    spot_id = models.IntegerField(primary_key=True)
    gotourl = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    android_s_image = models.CharField(max_length=100)
    android_b_image = models.CharField(max_length=100)
    ios_s_image = models.CharField(max_length=100)
    ios_normal_image = models.CharField(max_length=100)
    ios_big_image = models.CharField(max_length=100)
    ios_xbig_image = models.CharField(max_length=100)
    time_second = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    begin_ts = models.DateTimeField()
    end_ts = models.DateTimeField()
    title = models.CharField(max_length=100)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spot_ad_banner'


class SpotAdBannerConfig(models.Model):
    sort_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    begin_ts = models.DateTimeField()
    end_ts = models.DateTimeField()
    cnt = models.IntegerField()
    status = models.IntegerField()
    b_spot_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spot_ad_banner_config'


class SystemNotifyInfo(models.Model):
    system_notify_id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    url = models.CharField(max_length=512)
    activity_id = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'system_notify_info'


class SystemNotifyRecord(models.Model):
    system_notify_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'system_notify_record'
        unique_together = (('system_notify_id', 'user_id'),)


class TeamInfo(models.Model):
    team_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=128)
    passwd = models.CharField(max_length=20)
    ts = models.DateTimeField()
    end_ts = models.DateTimeField()
    all_ditance = models.IntegerField()
    join_cnt = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_info'


class TestDetail(models.Model):
    case_id = models.AutoField(primary_key=True)
    suite_id = models.IntegerField()
    priority = models.IntegerField()
    status = models.CharField(max_length=32)
    title = models.CharField(max_length=512)
    step = models.CharField(max_length=512)
    expect_value = models.CharField(max_length=512)
    pre_condition = models.CharField(max_length=512)
    post_condition = models.CharField(max_length=512)
    note = models.CharField(max_length=512)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_detail'


class TestSuite(models.Model):
    suite_id = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    note = models.CharField(max_length=64)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_suite'


class TestUser(models.Model):
    user_name = models.CharField(max_length=64)
    realname = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    mail = models.CharField(max_length=64)
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_user'


class ThemeInfo(models.Model):
    theme_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    url = models.TextField()
    ts = models.DateTimeField()
    phone = models.CharField(max_length=128)
    redirect_type = models.IntegerField()
    redirect_id = models.BigIntegerField()
    redirect_url = models.TextField()
    stat_name = models.CharField(max_length=64)
    wh_ratio = models.FloatField(blank=True, null=True)
    loc = models.IntegerField(blank=True, null=True)
    export_url = models.IntegerField(blank=True, null=True)
    is_online = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'theme_info'


class ToSendNotify(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'to_send_notify'


class ToSendSms(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    status = models.IntegerField()
    phone = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'to_send_sms'


class TopicDiscussionInfo(models.Model):
    discuss_id = models.BigIntegerField()
    topic_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    parent_discuss_id = models.BigIntegerField()
    status = models.IntegerField()
    content = models.TextField()
    ts = models.DateTimeField()
    note = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'topic_discussion_info'


class TopicDiscussionInfoV2(models.Model):
    discuss_id = models.BigIntegerField()
    topic_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    sex = models.IntegerField()
    nick = models.CharField(max_length=32)
    rank = models.IntegerField()
    parent_discuss_id = models.BigIntegerField()
    status = models.IntegerField()
    content = models.TextField()
    photo_ids = models.CharField(max_length=256)
    like_cnt = models.IntegerField()
    ts = models.DateTimeField()
    note = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'topic_discussion_info_v2'
        unique_together = (('discuss_id', 'topic_id'),)


class TopicInfo(models.Model):
    topic_id = models.BigIntegerField(primary_key=True)
    circle_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    discuss_cnt = models.IntegerField()
    read_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    ts = models.DateTimeField()
    update_ts = models.DateTimeField()
    hotrank = models.IntegerField()
    hotrank_type = models.IntegerField()
    note = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'topic_info'


class TopicInfoBackground(models.Model):
    id = models.BigIntegerField()
    kind_id = models.IntegerField()
    hotrank = models.IntegerField()
    hotrank_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'topic_info_background'
        unique_together = (('id', 'kind_id'),)


class TopicInfoCircleTime(models.Model):
    topic_id = models.BigIntegerField()
    circle_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    ts = models.DateTimeField()
    update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'topic_info_circle_time'


class TopicLike(models.Model):
    topic_id = models.BigIntegerField()
    discuss_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'topic_like'
        unique_together = (('topic_id', 'discuss_id', 'user_id'),)


class TopicPhotoInfo(models.Model):
    topic_id = models.BigIntegerField()
    photo_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'topic_photo_info'
        unique_together = (('topic_id', 'photo_id'),)


class TopicReport(models.Model):
    topic_id = models.BigIntegerField()
    discuss_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'topic_report'
        unique_together = (('topic_id', 'discuss_id', 'user_id'),)


class TopicSubject(models.Model):
    subject_id = models.BigAutoField(primary_key=True)
    subject_title = models.CharField(max_length=128)
    user_id = models.BigIntegerField()
    circle_id = models.IntegerField()
    isdel = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'topic_subject'


class TopicSubjectOne(models.Model):
    topic_id = models.BigAutoField(primary_key=True)
    subject_id = models.IntegerField()
    subject_order = models.IntegerField()
    photo_id = models.BigIntegerField()
    topic_title = models.CharField(max_length=128)
    status = models.IntegerField()
    ts = models.DateTimeField()
    isdel = models.IntegerField()
    discuss_cnt = models.IntegerField()
    read_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    update_ts = models.DateTimeField()
    hotrank = models.IntegerField()
    hotrank_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'topic_subject_one'


class TopicSubjectOneFragment(models.Model):
    topic_frag_id = models.BigAutoField(primary_key=True)
    topic_id = models.BigIntegerField()
    topic_order = models.BigIntegerField()
    photo_id = models.BigIntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    content = models.TextField()
    isdel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'topic_subject_one_fragment'


class TopicSubjectOneUrl(models.Model):
    topic_url_id = models.BigAutoField(primary_key=True)
    topic_id = models.BigIntegerField()
    type = models.IntegerField()
    url = models.TextField()
    icon = models.TextField()
    url_title = models.CharField(max_length=128)
    status = models.IntegerField()
    isdel = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'topic_subject_one_url'


class TopicTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'topic_tickets64'


class TopicTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'topic_tickets64_innodb'


class TreeDonateNum(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    reward_num = models.IntegerField()
    tree_num = models.IntegerField()
    reward_sum = models.IntegerField()
    ts = models.DateTimeField()
    run_num = models.IntegerField()
    city = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'tree_donate_num'


class TreeDonateReward(models.Model):
    user_id = models.BigIntegerField()
    reward = models.IntegerField()
    ts = models.DateTimeField()
    group_run_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tree_donate_reward'
        unique_together = (('user_id', 'group_run_id'),)


class TreeDonateStat(models.Model):
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    reward_num = models.IntegerField()
    tree_num = models.IntegerField()
    tree_reward_num = models.IntegerField()
    reward_sum = models.IntegerField()
    run_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tree_donate_stat'
        unique_together = (('province', 'city'),)


class TreeDonateTree(models.Model):
    tree_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    begin_day = models.CharField(max_length=32)
    end_day = models.CharField(max_length=32)
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tree_donate_tree'


class TreeReportUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tree_report_user'


class TreeRunInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ts = models.DateTimeField()
    types = models.CharField(max_length=255)
    join_num = models.IntegerField()
    circle_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tree_run_info'


class TwitterUserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    t_user_id = models.CharField(max_length=128)
    t_token = models.CharField(max_length=128)
    t_secret = models.CharField(max_length=128)
    ct = models.DateTimeField()
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'twitter_user_info'


class UbanInfo(models.Model):
    uban_name = models.CharField(primary_key=True, max_length=128)
    source = models.CharField(max_length=32)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'uban_info'


class UbanRegInfo(models.Model):
    uban_name = models.CharField(primary_key=True, max_length=128)
    sex = models.IntegerField()
    nick = models.CharField(max_length=128)
    head = models.CharField(max_length=1024)
    reg_ts = models.DateTimeField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'uban_reg_info'


class UmengComment(models.Model):
    feedback_id = models.CharField(primary_key=True, max_length=128)
    os = models.CharField(max_length=64)
    app_version = models.CharField(max_length=64)
    os_version = models.CharField(max_length=64)
    channel = models.CharField(max_length=64)
    yuedong_id = models.CharField(max_length=64)
    reply_num = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    qq = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    device_model = models.CharField(max_length=64)
    access = models.CharField(max_length=64)
    content = models.CharField(max_length=512)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'umeng_comment'


class UploadTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'upload_tickets64'


class UploadTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'upload_tickets64_innodb'


class UserActivity(models.Model):
    user_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    identity = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_activity'
        unique_together = (('user_id', 'activity_id'),)


class UserAim(models.Model):
    user_id = models.BigIntegerField()
    aim_index = models.CharField(max_length=64)
    aim = models.IntegerField()
    aim_add = models.IntegerField()
    kind_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_aim'
        unique_together = (('user_id', 'aim_index', 'kind_id'),)


class UserAimMemory(models.Model):
    user_id = models.BigIntegerField()
    aim = models.IntegerField()
    aim_add = models.IntegerField()
    kind_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_aim_memory'
        unique_together = (('user_id', 'kind_id'),)


class UserAimMemoryBk(models.Model):
    user_id = models.BigIntegerField()
    aim = models.IntegerField()
    aim_add = models.IntegerField()
    kind_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_aim_memory_bk'
        unique_together = (('user_id', 'kind_id'),)


class UserAimMemorySmall(models.Model):
    user_id = models.BigIntegerField()
    aim = models.IntegerField()
    aim_add = models.IntegerField()
    kind_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_aim_memory_small'
        unique_together = (('user_id', 'kind_id'),)


class UserAimNotify(models.Model):
    user_id = models.BigIntegerField()
    aim_index = models.CharField(max_length=64)
    status = models.IntegerField()
    kind_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_aim_notify'
        unique_together = (('user_id', 'aim_index', 'kind_id'),)


class UserAlipay(models.Model):
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    alipay_account = models.CharField(max_length=64)
    alipay_realname = models.CharField(max_length=64)
    apply_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_alipay'


class UserBind(models.Model):
    user_id_master = models.IntegerField()
    user_id_slave = models.IntegerField()
    status = models.IntegerField()
    comment = models.CharField(max_length=256)
    ts = models.DateTimeField()
    hx_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_bind'
        unique_together = (('user_id_master', 'user_id_slave'),)


class UserCheckVerify(models.Model):
    user_id = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_check_verify'


class UserCircle(models.Model):
    user_id = models.BigIntegerField()
    circle_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    apply_msg = models.CharField(max_length=256)
    user_type = models.IntegerField()
    hx_group_id = models.BigIntegerField()
    last_week_distance = models.IntegerField()
    comment = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'user_circle'
        unique_together = (('user_id', 'circle_id'),)


class UserCircleActivity(models.Model):
    user_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_circle_activity'
        unique_together = (('user_id', 'activity_id'),)


class UserCircleBlack(models.Model):
    user_id = models.BigIntegerField()
    circle_id = models.CharField(max_length=128)
    black = models.CharField(max_length=128)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_circle_black'
        unique_together = (('user_id', 'circle_id'),)


class UserCircleExt(models.Model):
    user_id = models.BigIntegerField()
    circle_id = models.BigIntegerField()
    yinhua_cnt = models.IntegerField()
    distance = models.IntegerField()
    top_index = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'user_circle_ext'
        unique_together = (('user_id', 'circle_id'),)


class UserCircleOffice(models.Model):
    user_id = models.BigIntegerField()
    circle_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    apply_msg = models.CharField(max_length=256)
    user_type = models.IntegerField()
    hx_group_id = models.BigIntegerField()
    last_week_distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_circle_office'
        unique_together = (('user_id', 'circle_id'),)


class UserCircleOfficeV2(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    circle_ids = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'user_circle_office_v2'


class UserCircleRank(models.Model):
    circle_id = models.IntegerField()
    user_id = models.BigIntegerField()
    sign_day_cnt = models.IntegerField()
    sign_last_day = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_circle_rank'
        unique_together = (('user_id', 'circle_id'),)


class UserCircleYueb(models.Model):
    user_id = models.BigIntegerField()
    yueb_id = models.BigIntegerField()
    type = models.CharField(max_length=64)
    last_day = models.IntegerField()
    ts = models.DateTimeField()
    order_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_circle_yueb'
        unique_together = (('user_id', 'type', 'last_day'),)


class UserColor(models.Model):
    user_id = models.BigIntegerField()
    kind = models.CharField(max_length=32)
    update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_color'
        unique_together = (('user_id', 'kind'),)


class UserContact(models.Model):
    phone = models.CharField(max_length=64)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=32)
    flag = models.IntegerField()
    activity_id = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_contact'
        unique_together = (('phone', 'user_id'),)


class UserCoupon(models.Model):
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    coupon = models.CharField(max_length=32)
    status = models.IntegerField()
    used_ts = models.DateTimeField()
    expire_time = models.DateTimeField()
    ts = models.DateTimeField()
    phone_notify = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_coupon'
        unique_together = (('user_id', 'coupon'),)


class UserCurrencyInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    currency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_currency_info'


class UserDataImported(models.Model):
    old_user_id = models.BigIntegerField(primary_key=True)
    new_user_id = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_data_imported'


class UserEvil(models.Model):
    user_id = models.BigIntegerField()
    kind = models.CharField(max_length=32)
    update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_evil'
        unique_together = (('user_id', 'kind'),)


class UserFollow(models.Model):
    user_id = models.BigIntegerField()
    follow_user_id = models.BigIntegerField()
    status = models.IntegerField()
    channel = models.CharField(max_length=32)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_follow'
        unique_together = (('user_id', 'follow_user_id'),)


class UserFriend(models.Model):
    user_id = models.BigIntegerField()
    friend_user_id = models.BigIntegerField()
    status = models.IntegerField()
    channel = models.CharField(max_length=32)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_friend'
        unique_together = (('user_id', 'friend_user_id'),)


class UserGroupRun(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    type = models.IntegerField()
    steps = models.IntegerField()
    reward_flag = models.IntegerField()
    reward_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_group_run'
        unique_together = (('user_id', 'group_run_id'),)


class UserGroupRun0128(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_group_run_0128'
        unique_together = (('user_id', 'group_run_id'),)


class UserGroupRunDelLkb(models.Model):
    user_id = models.BigIntegerField()
    group_run_id = models.BigIntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    draw_ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    draw_ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_group_run_del_lkb'
        unique_together = (('user_id', 'group_run_id'),)


class UserHonorInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    day_max_step = models.IntegerField()
    day_step_5000 = models.IntegerField()
    day_step_10000 = models.IntegerField()
    day_step_20000 = models.IntegerField()
    day_step_50000 = models.IntegerField()
    day_step_100000 = models.IntegerField()
    all_step = models.IntegerField()
    all_step_500000 = models.IntegerField()
    all_step_1000000 = models.IntegerField()
    all_step_5000000 = models.IntegerField()
    comp_step = models.IntegerField()
    comp_step_3 = models.IntegerField()
    comp_step_7 = models.IntegerField()
    day_max_run = models.IntegerField()
    day_run_2000 = models.IntegerField()
    day_run_5000 = models.IntegerField()
    day_run_10000 = models.IntegerField()
    day_run_21000 = models.IntegerField()
    day_run_42000 = models.IntegerField()
    all_run = models.IntegerField()
    all_run_100000 = models.IntegerField()
    all_run_200000 = models.IntegerField()
    all_run_400000 = models.IntegerField()
    all_run_800000 = models.IntegerField()
    all_run_1500000 = models.IntegerField()
    comp_run = models.IntegerField()
    comp_run_3 = models.IntegerField()
    comp_run_7 = models.IntegerField()
    yinhua_score = models.IntegerField()
    yinhua_3 = models.IntegerField()
    yinhua_7 = models.IntegerField()
    circle_cnt = models.IntegerField()
    circle_1 = models.IntegerField()
    circle_5 = models.IntegerField()
    invite_cnt = models.IntegerField()
    invite_5 = models.IntegerField()
    invite_10 = models.IntegerField()
    share_cnt = models.IntegerField()
    share_5 = models.IntegerField()
    share_10 = models.IntegerField()
    last_update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_honor_info'


class UserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    sex = models.IntegerField()
    status = models.IntegerField()
    rank = models.IntegerField()
    new_rank = models.IntegerField()
    day = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    phone = models.CharField(max_length=16)
    province = models.CharField(max_length=16)
    nick = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    source = models.CharField(max_length=32)
    head = models.CharField(max_length=128)
    ip = models.CharField(max_length=16)
    love_sports = models.CharField(max_length=64)
    signature = models.CharField(max_length=256)
    ts = models.DateTimeField()
    reg_ts = models.DateTimeField()
    phone_type = models.CharField(max_length=64)
    os = models.CharField(max_length=64)
    ver = models.CharField(max_length=16)
    now_ver = models.CharField(max_length=16)
    device_id = models.CharField(max_length=128)
    channel = models.CharField(max_length=64, blank=True, null=True)
    last_login_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_info'


class UserInfoMall(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    sex = models.IntegerField()
    status = models.IntegerField()
    rank = models.IntegerField()
    new_rank = models.IntegerField()
    day = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    phone = models.CharField(max_length=16)
    province = models.CharField(max_length=16)
    nick = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    source = models.CharField(max_length=32)
    head = models.CharField(max_length=128)
    ip = models.CharField(max_length=16)
    love_sports = models.CharField(max_length=64)
    signature = models.CharField(max_length=256)
    ts = models.DateTimeField()
    reg_ts = models.DateTimeField()
    phone_type = models.CharField(max_length=64)
    os = models.CharField(max_length=64)
    ver = models.CharField(max_length=16)
    now_ver = models.CharField(max_length=16)
    device_id = models.CharField(max_length=128)
    channel = models.CharField(max_length=64, blank=True, null=True)
    last_login_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_info_mall'


class UserInfoTmp(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    sex = models.IntegerField()
    status = models.IntegerField()
    rank = models.IntegerField()
    new_rank = models.IntegerField()
    day = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    phone = models.CharField(max_length=16)
    province = models.CharField(max_length=16)
    nick = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    source = models.CharField(max_length=32)
    head = models.CharField(max_length=128)
    ip = models.CharField(max_length=16)
    love_sports = models.CharField(max_length=64)
    signature = models.CharField(max_length=256)
    ts = models.DateTimeField()
    reg_ts = models.DateTimeField()
    phone_type = models.CharField(max_length=64)
    os = models.CharField(max_length=64)
    ver = models.CharField(max_length=16)
    now_ver = models.CharField(max_length=16)
    device_id = models.CharField(max_length=128)
    channel = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info_tmp'


class UserInviteEvil(models.Model):
    user_id = models.BigIntegerField()
    kind = models.CharField(max_length=32)
    update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_invite_evil'
        unique_together = (('user_id', 'kind'),)


class UserLaunch(models.Model):
    user_id = models.BigIntegerField()
    source = models.IntegerField()
    ver = models.CharField(max_length=16)
    day = models.DateField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_launch'
        unique_together = (('user_id', 'day'),)


class UserLaunchAll(models.Model):
    user_id = models.BigIntegerField()
    source = models.IntegerField()
    ver = models.CharField(max_length=16)
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'user_launch_all'
        unique_together = (('user_id', 'day'),)


class UserLaunchNew(models.Model):
    user_id = models.CharField(max_length=64)
    kind = models.IntegerField()
    source = models.IntegerField()
    ver = models.CharField(max_length=16)
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'user_launch_new'
        unique_together = (('user_id', 'day'),)


class UserLaunchOld(models.Model):
    user_id = models.BigIntegerField()
    ver = models.CharField(max_length=32)
    ts = models.DateTimeField()
    source = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'user_launch_old'


class UserLiving(models.Model):
    user_id = models.BigIntegerField()
    day = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_living'
        unique_together = (('user_id', 'day'),)


class UserLocation(models.Model):
    user_id = models.BigIntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_location'


class UserLogin(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    phone = models.CharField(max_length=16)
    nick = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'user_login'


class UserMarketing(models.Model):
    user_id = models.BigIntegerField()
    friend_user_id = models.BigIntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_marketing'
        unique_together = (('user_id', 'friend_user_id'),)


class UserMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.BigIntegerField(blank=True, null=True)
    ts = models.DateTimeField()
    title = models.TextField(blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    expiration = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_message'


class UserNewReward(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    login_reward = models.IntegerField()
    login_status = models.IntegerField()
    run_reward = models.IntegerField()
    run_status = models.IntegerField()
    step_reward = models.IntegerField()
    step_status = models.IntegerField()
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_new_reward'


class UserNotifyToken(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    notify_type = models.IntegerField()
    umeng_token = models.CharField(max_length=128)
    mi_token = models.CharField(max_length=128)
    ts = models.DateTimeField()
    bd_token = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'user_notify_token'


class UserOnlineInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.IntegerField()
    ip = models.CharField(max_length=32)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_online_info'


class UserOnlineInfoArea(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.IntegerField()
    ip = models.CharField(max_length=32)
    ts = models.DateTimeField()
    jingwei_province = models.CharField(max_length=32)
    jingwei_city = models.CharField(max_length=32)
    ip_province = models.CharField(max_length=32)
    ip_city = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    district = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user_online_info_area'


class UserPayInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    order_id = models.CharField(max_length=256)
    access_token = models.CharField(max_length=256)
    money = models.BigIntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    pay_time = models.DateTimeField()
    ordersign = models.CharField(db_column='orderSign', max_length=256)  # Field name made lowercase.
    comment = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'user_pay_info'


class UserPayInfoCash(models.Model):
    user_id = models.BigIntegerField()
    pay_id = models.BigIntegerField()
    pay_source = models.CharField(max_length=32)
    pay_step = models.IntegerField()
    pay_money = models.BigIntegerField()
    ts = models.DateTimeField()
    comment = models.CharField(max_length=256)
    pay_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_pay_info_cash'
        unique_together = (('user_id', 'pay_id', 'pay_source', 'pay_step', 'pay_flag'),)


class UserPayInfoMall(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    order_id = models.CharField(max_length=256)
    access_token = models.CharField(max_length=256)
    money = models.BigIntegerField()
    type = models.IntegerField()
    sub_type = models.IntegerField()
    status = models.IntegerField()
    pay_time = models.DateTimeField()
    ordersign = models.CharField(db_column='orderSign', max_length=256)  # Field name made lowercase.
    comment = models.CharField(max_length=256)
    pay_id = models.BigIntegerField()
    pay_action = models.CharField(max_length=32)
    pay_source = models.CharField(max_length=32)
    https = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_pay_info_mall'


class UserPhoto(models.Model):
    user_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    photo_id = models.BigIntegerField()
    md5 = models.CharField(max_length=64)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_photo'
        unique_together = (('activity_id', 'user_id', 'photo_id'),)


class UserPk(models.Model):
    user_id = models.BigIntegerField()
    pk_id = models.BigIntegerField()
    score = models.IntegerField()
    reward = models.IntegerField()
    kind = models.IntegerField()
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'user_pk'


class UserPortrait(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    day = models.IntegerField()
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    total_distance = models.IntegerField()
    total_cost_time = models.IntegerField()
    day_max_distance = models.IntegerField()
    run_moment = models.IntegerField()
    day_avg_cost_time = models.IntegerField()
    week_run_cnt = models.FloatField()
    week_cnt = models.IntegerField()
    last_run_ts = models.DateTimeField()
    update_ts = models.DateTimeField()
    notify_read_precent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_portrait'


class UserPropertyInfo(models.Model):
    recv_user_id = models.BigIntegerField()
    send_user_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    cnt = models.IntegerField()
    kind = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_property_info'
        unique_together = (('activity_id', 'send_user_id', 'recv_user_id'),)


class UserRankInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_score = models.IntegerField()
    user_update_level = models.IntegerField()
    update_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_rank_info'


class UserRankReward(models.Model):
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    rank = models.IntegerField()
    reward = models.IntegerField()
    score = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_rank_reward'
        unique_together = (('user_id', 'rank'),)


class UserRankTask(models.Model):
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    rank = models.IntegerField()
    task_id = models.IntegerField()
    begin_time = models.DateTimeField()
    ts = models.DateTimeField()
    cur_val = models.IntegerField()
    aim_val = models.IntegerField()
    flag = models.IntegerField()
    score = models.IntegerField()
    type = models.CharField(max_length=32)
    realrank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_rank_task'
        unique_together = (('user_id', 'rank'),)


class UserRankTaskAllMemory(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    rank = models.IntegerField()
    task = models.CharField(max_length=128)
    ts = models.DateTimeField()
    cur_val = models.IntegerField()
    aim_val = models.IntegerField()
    flag = models.IntegerField()
    score = models.IntegerField()
    type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    native = models.CharField(max_length=64)
    native_int = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_rank_task_all_memory'


class UserReport(models.Model):
    from_user_id = models.BigIntegerField()
    to_user_id = models.BigIntegerField()
    kind = models.CharField(max_length=32)
    message = models.CharField(max_length=512)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_report'


class UserRewardAllRecord(models.Model):
    user_id = models.BigIntegerField()
    reward = models.IntegerField()
    kind = models.IntegerField()
    ts = models.DateTimeField()
    group_ts = models.DateTimeField()
    group_table = models.CharField(max_length=64)
    group_id = models.BigIntegerField()
    group_type = models.BigIntegerField()
    status = models.IntegerField()
    what = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'user_reward_all_record'
        unique_together = (('user_id', 'group_id', 'group_table', 'group_type'),)


class UserRewardCustomRecord(models.Model):
    user_id = models.BigIntegerField()
    reward = models.IntegerField()
    ts = models.DateTimeField()
    comment = models.CharField(max_length=128)
    order_id = models.BigIntegerField()
    status = models.IntegerField()
    what = models.CharField(max_length=128)
    type = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'user_reward_custom_record'
        unique_together = (('user_id', 'order_id', 'type'),)


class UserRewardCustomRecordTest(models.Model):
    user_id = models.BigIntegerField()
    reward = models.IntegerField()
    ts = models.DateTimeField()
    comment = models.CharField(max_length=128)
    order_id = models.BigIntegerField()
    status = models.IntegerField()
    what = models.CharField(max_length=128)
    type = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'user_reward_custom_record_test'
        unique_together = (('user_id', 'order_id', 'type'),)


class UserRewardMallRecord(models.Model):
    user_id = models.BigIntegerField()
    reward = models.IntegerField()
    ts = models.DateTimeField()
    comment = models.CharField(max_length=128)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_reward_mall_record'


class UserRobot(models.Model):
    user_id = models.BigIntegerField()
    kind = models.CharField(max_length=32)
    update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_robot'
        unique_together = (('user_id', 'kind'),)


class UserRobotInfo(models.Model):
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_robot_info'


class UserRunRankHistory(models.Model):
    user_id = models.BigIntegerField()
    day = models.CharField(max_length=32)
    time_type = models.CharField(max_length=32)
    area_type = models.CharField(max_length=32)
    distance = models.IntegerField()
    rank = models.IntegerField()
    update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_run_rank_history'
        unique_together = (('user_id', 'day', 'time_type', 'area_type'),)


class UserRunner(models.Model):
    user_id = models.BigIntegerField()
    runner_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    status = models.IntegerField()
    group_run_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    u_kind_id = models.IntegerField()
    u_distance = models.IntegerField()
    u_cost_time = models.IntegerField()
    u_avg_pace = models.IntegerField()
    u_avg_speed = models.IntegerField()
    u_caloric = models.IntegerField()
    u_weather = models.CharField(max_length=64)
    u_feeling = models.CharField(max_length=512)
    u_ts = models.DateTimeField()
    u_report_ts = models.DateTimeField()
    u_audio_id = models.BigIntegerField()
    u_location_sdk = models.IntegerField()
    source = models.CharField(max_length=128)
    u_center_longitude = models.FloatField()
    u_center_latitude = models.FloatField()
    u_steps = models.IntegerField()
    sensor_steps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_runner'
        unique_together = (('user_id', 'runner_id'),)


class UserRunnerBracelet(models.Model):
    user_id = models.IntegerField()
    kind_id = models.IntegerField()
    day_id = models.CharField(max_length=32)
    step_target = models.IntegerField()
    steps = models.IntegerField()
    cost_time = models.IntegerField()
    caloric = models.IntegerField()
    bracelet_uuid = models.CharField(max_length=64)
    bracelet_address_id = models.CharField(max_length=64)
    device_id = models.CharField(max_length=64)
    detail = models.TextField()
    source = models.CharField(max_length=64)
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    status = models.IntegerField()
    runner_id = models.BigIntegerField()
    brace_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_runner_bracelet'
        unique_together = (('user_id', 'day_id', 'bracelet_uuid', 'device_id'),)


class UserRunnerBraceletBk1(models.Model):
    user_id = models.IntegerField()
    kind_id = models.IntegerField()
    day_id = models.CharField(max_length=32)
    step_target = models.IntegerField()
    steps = models.IntegerField()
    cost_time = models.IntegerField()
    caloric = models.IntegerField()
    bracelet_uuid = models.CharField(max_length=64)
    bracelet_address_id = models.CharField(max_length=64)
    device_id = models.CharField(max_length=64)
    detail = models.TextField()
    source = models.CharField(max_length=64)
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    status = models.IntegerField()
    runner_id = models.BigIntegerField()
    brace_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_runner_bracelet_bk1'
        unique_together = (('user_id', 'day_id', 'bracelet_uuid', 'device_id'),)


class UserRunnerBraceletCompress(models.Model):
    user_id = models.IntegerField()
    kind_id = models.IntegerField()
    day_id = models.CharField(max_length=32)
    step_target = models.IntegerField()
    steps = models.IntegerField()
    cost_time = models.IntegerField()
    caloric = models.IntegerField()
    bracelet_uuid = models.CharField(max_length=64)
    bracelet_address_id = models.CharField(max_length=64)
    device_id = models.CharField(max_length=64)
    detail_compress = models.TextField()
    source = models.CharField(max_length=64)
    ts = models.DateTimeField()
    report_ts = models.DateTimeField()
    status = models.IntegerField()
    runner_id = models.BigIntegerField()
    brace_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_runner_bracelet_compress'
        unique_together = (('user_id', 'day_id', 'bracelet_uuid', 'device_id'),)


class UserRunnerBraceletSleep(models.Model):
    user_id = models.IntegerField()
    kind_id = models.IntegerField()
    day_id = models.CharField(max_length=32)
    bracelet_uuid = models.CharField(max_length=64)
    bracelet_address_id = models.CharField(max_length=64)
    device_id = models.CharField(max_length=64)
    detail = models.TextField()
    source = models.CharField(max_length=64)
    report_ts = models.DateTimeField()
    brace_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_runner_bracelet_sleep'
        unique_together = (('user_id', 'day_id', 'bracelet_uuid', 'device_id'),)


class UserRunnerSource(models.Model):
    user_id = models.BigIntegerField()
    runner_id = models.BigIntegerField()
    distance = models.IntegerField()
    run_source = models.CharField(max_length=64)
    ts = models.DateTimeField()
    infos = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user_runner_source'
        unique_together = (('user_id', 'runner_id'),)


class UserRunnerStep(models.Model):
    user_id = models.BigIntegerField()
    runner_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    status = models.IntegerField()
    group_run_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    u_kind_id = models.IntegerField()
    u_distance = models.IntegerField()
    u_cost_time = models.IntegerField()
    u_avg_pace = models.IntegerField()
    u_avg_speed = models.IntegerField()
    u_caloric = models.IntegerField()
    u_weather = models.CharField(max_length=64)
    u_feeling = models.CharField(max_length=512)
    u_ts = models.DateTimeField()
    u_report_ts = models.DateTimeField()
    u_audio_id = models.BigIntegerField()
    u_location_sdk = models.IntegerField()
    source = models.CharField(max_length=128)
    u_center_longitude = models.FloatField()
    u_center_latitude = models.FloatField()
    u_steps = models.IntegerField()
    u_subtype = models.IntegerField()
    u_from = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_runner_step'
        unique_together = (('user_id', 'runner_id'),)


class UserRunnerStepBk(models.Model):
    user_id = models.BigIntegerField()
    runner_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    status = models.IntegerField()
    group_run_id = models.BigIntegerField()
    hundred_id = models.IntegerField()
    u_kind_id = models.IntegerField()
    u_distance = models.IntegerField()
    u_cost_time = models.IntegerField()
    u_avg_pace = models.IntegerField()
    u_avg_speed = models.IntegerField()
    u_caloric = models.IntegerField()
    u_weather = models.CharField(max_length=64)
    u_feeling = models.CharField(max_length=512)
    u_ts = models.DateTimeField()
    u_report_ts = models.DateTimeField()
    u_audio_id = models.BigIntegerField()
    u_location_sdk = models.IntegerField()
    source = models.CharField(max_length=128)
    u_center_longitude = models.FloatField()
    u_center_latitude = models.FloatField()
    u_steps = models.IntegerField()
    u_subtype = models.IntegerField()
    u_from = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_runner_step_bk'
        unique_together = (('user_id', 'runner_id'),)


class UserRunnerStepDay(models.Model):
    user_id = models.BigIntegerField()
    day_id = models.CharField(max_length=32)
    cost_time = models.IntegerField()
    ts = models.DateTimeField()
    seg_steps = models.IntegerField()
    m7_steps = models.IntegerField()
    bracelet_steps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_runner_step_day'
        unique_together = (('user_id', 'day_id'),)


class UserRunnerTotalNum(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    total_distance = models.IntegerField()
    ride_distance = models.IntegerField()
    autorecord_distance = models.IntegerField()
    day_max_step = models.IntegerField()
    week_distance = models.IntegerField()
    week_ride = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_runner_total_num'


class UserRunning(models.Model):
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_running'


class UserSetting(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    auto_add_friend = models.IntegerField()
    allow_be_add_friend = models.IntegerField()
    ts = models.DateTimeField()
    allow_circle_notify = models.IntegerField()
    supp_huanxing = models.IntegerField()
    begin_sensor_distance = models.IntegerField()
    end_sensor_distance = models.IntegerField()
    week_report = models.IntegerField()
    voice_report = models.IntegerField()
    voice_type = models.IntegerField()
    run_map = models.IntegerField()
    auto_step = models.IntegerField()
    notify_type = models.IntegerField()
    reg_huanxing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_setting'


class UserSid(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    sid = models.CharField(max_length=32)
    ts = models.DateTimeField()
    up_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_sid'


class UserTeam(models.Model):
    team_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    distance = models.IntegerField()
    runner_id = models.BigIntegerField()
    ts = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_team'
        unique_together = (('team_id', 'user_id'),)


class UserTeamOnline(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_team_online'


class UserTickets64(models.Model):
    id = models.BigAutoField(primary_key=True)
    stub = models.CharField(unique=True, max_length=1)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_tickets64'


class UserTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_tickets64_innodb'


class UserWeekData(models.Model):
    user_id = models.IntegerField()
    week_index = models.CharField(max_length=32)
    steps = models.IntegerField()
    distances = models.IntegerField()
    caloric = models.IntegerField()
    source = models.CharField(max_length=64)
    rank = models.IntegerField()
    status = models.IntegerField()
    ts = models.DateTimeField()
    days_distances = models.CharField(max_length=256)
    days_steps = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'user_week_data'
        unique_together = (('user_id', 'week_index'),)


class UserWelcome(models.Model):
    user_id = models.BigIntegerField()
    from_user_id = models.BigIntegerField()
    welcome_type = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_welcome'
        unique_together = (('user_id', 'from_user_id'),)


class UserYearInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    nick = models.CharField(max_length=32)
    ts = models.DateTimeField()
    reg_ts = models.DateTimeField()
    first_sport_ts = models.DateTimeField()
    first_sport_distance = models.IntegerField()
    first_sport_steps = models.IntegerField()
    comp_year = models.IntegerField()
    reward_year = models.IntegerField()
    run_year = models.IntegerField()
    step_year = models.IntegerField()
    yinhua_cnt = models.IntegerField()
    marathon_cnt = models.IntegerField()
    marathon_half_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_year_info'


class UserYuebCustomRecord(models.Model):
    yueb_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    yueb = models.IntegerField()
    ts = models.DateTimeField()
    comment = models.CharField(max_length=128)
    order_id = models.BigIntegerField()
    status = models.IntegerField()
    what = models.CharField(max_length=128)
    type = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'user_yueb_custom_record'
        unique_together = (('user_id', 'order_id', 'type'),)


class UserYuebInfo(models.Model):
    yueb_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    yueb = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_yueb_info'


class UserYuebInfoTickets64Innodb(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_yueb_info_tickets64_innodb'


class VersionStat(models.Model):
    ver = models.CharField(max_length=32)
    day = models.CharField(max_length=32)
    active_person_cnt = models.IntegerField()
    register_person_cnt = models.FloatField()
    unregister_person_cnt = models.FloatField()
    run_person_cnt = models.FloatField()
    step_person_cnt = models.FloatField()
    step_reward_person_cnt = models.FloatField()
    run_reward_person_cnt = models.FloatField()
    share_person_cnt = models.FloatField()
    join_circle_person_cnt = models.FloatField()
    add_follow_person_cnt = models.FloatField()
    zero_step_person_cnt = models.FloatField()
    avg_steps = models.FloatField()
    avg_run_distance = models.FloatField()
    running_crash = models.FloatField()
    avg_gps_time = models.FloatField()
    ride_reward_person_cnt = models.FloatField()
    ride_person_cnt = models.FloatField()
    avg_ride_distance = models.FloatField()
    uninstall_cnt = models.FloatField()
    zero_step_person_cnt2 = models.FloatField()
    zero_step_person_cnt3 = models.FloatField()
    avg_gps_time2 = models.FloatField()
    running_crash2 = models.FloatField()
    crash_autostart_cnt = models.FloatField()
    avg_autostart_time = models.FloatField()
    lowmemory_cnt = models.FloatField()

    class Meta:
        managed = False
        db_table = 'version_stat'
        unique_together = (('day', 'ver'),)


class VersionStatOld(models.Model):
    ver = models.CharField(max_length=32)
    day = models.CharField(max_length=32)
    active_person_cnt = models.IntegerField()
    register_person_cnt = models.FloatField()
    unregister_person_cnt = models.FloatField()
    run_person_cnt = models.FloatField()
    step_person_cnt = models.FloatField()
    step_reward_person_cnt = models.FloatField()
    run_reward_person_cnt = models.FloatField()
    share_person_cnt = models.FloatField()
    join_circle_person_cnt = models.FloatField()
    add_follow_person_cnt = models.FloatField()
    zero_step_person_cnt = models.FloatField()
    avg_steps = models.FloatField()
    avg_run_distance = models.FloatField()
    running_crash = models.FloatField()
    avg_gps_time = models.FloatField()
    ride_reward_person_cnt = models.FloatField()
    ride_person_cnt = models.FloatField()
    avg_ride_distance = models.FloatField()
    uninstall_cnt = models.FloatField()
    zero_step_person_cnt2 = models.FloatField()
    zero_step_person_cnt3 = models.FloatField()
    avg_gps_time2 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'version_stat_old'
        unique_together = (('day', 'ver'),)


class Wangcai(models.Model):
    idfa = models.CharField(max_length=64)
    mac = models.CharField(max_length=64)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    dl_ts = models.DateTimeField()
    reg_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wangcai'
        unique_together = (('idfa', 'mac'),)


class WangcaiYingyongbao(models.Model):
    idfa = models.CharField(max_length=64)
    mac = models.CharField(max_length=64)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    dl_ts = models.DateTimeField()
    reg_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wangcai_yingyongbao'
        unique_together = (('idfa', 'mac'),)


class WechatTicket(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    ticket = models.CharField(max_length=256)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wechat_ticket'


class WeekRemain(models.Model):
    week = models.CharField(max_length=32)
    begin_day = models.CharField(max_length=32)
    end_day = models.CharField(max_length=32)
    cnt = models.IntegerField()
    kind = models.IntegerField()
    channel = models.CharField(max_length=64)
    week1 = models.FloatField()
    week2 = models.FloatField()
    week3 = models.FloatField()
    week4 = models.FloatField()
    week5 = models.FloatField()
    week6 = models.FloatField()
    week7 = models.FloatField()
    week8 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'week_remain'
        unique_together = (('week', 'kind', 'channel'),)


class WeixinReport(models.Model):
    user_id = models.BigIntegerField()
    day_id = models.CharField(max_length=32)
    steps = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'weixin_report'
        unique_together = (('user_id', 'day_id'),)


class XlshowGirlInfo(models.Model):
    group_run_id = models.BigIntegerField()
    girl_id = models.IntegerField()
    phone = models.CharField(max_length=64)
    nick = models.CharField(max_length=64)
    ts = models.DateTimeField()
    head_url = models.CharField(max_length=128)
    pic_urls = models.CharField(max_length=1024)
    desc = models.CharField(max_length=128)
    user_cnt = models.IntegerField()
    distance = models.IntegerField()
    rank = models.IntegerField()
    circle_id = models.IntegerField()
    status = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    work = models.CharField(max_length=64)
    place = models.CharField(max_length=64)
    like_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xlshow_girl_info'
        unique_together = (('group_run_id', 'girl_id'),)


class XlshowInfo(models.Model):
    group_run_id = models.BigAutoField(primary_key=True)
    distance = models.IntegerField()
    status = models.IntegerField()
    kind_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    run_begin_time = models.DateTimeField()
    run_end_time = models.DateTimeField()
    ts = models.DateTimeField()
    reward_cnt = models.IntegerField()
    reward_money = models.IntegerField()
    session_num = models.IntegerField()
    user_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xlshow_info'


class XlshowRecommend(models.Model):
    user_id = models.BigIntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    name = models.CharField(max_length=32)
    birth = models.CharField(max_length=32)
    work = models.CharField(max_length=32)
    three_data = models.CharField(max_length=32)
    head_id = models.IntegerField()
    ts = models.DateTimeField()
    head_ids = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'xlshow_recommend'


class XlshowUserInfo(models.Model):
    group_run_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    girl_id = models.IntegerField()
    ts = models.DateTimeField()
    distance = models.IntegerField()
    cost_time = models.IntegerField()
    score = models.IntegerField()
    money_reward = models.IntegerField()
    real_reward = models.IntegerField()
    real_name = models.CharField(max_length=32)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xlshow_user_info'
        unique_together = (('user_id', 'group_run_id', 'girl_id'),)


class XlshowUserLike(models.Model):
    user_id = models.BigIntegerField()
    girl_id = models.BigIntegerField()
    flag = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'xlshow_user_like'
        unique_together = (('user_id', 'girl_id'),)


class YinhuaStat(models.Model):
    session_num = models.IntegerField(primary_key=True)
    hundred_id = models.IntegerField()
    join_cnt = models.IntegerField()
    complete_cnt = models.IntegerField()
    join_circle_cnt = models.IntegerField()
    complete_circle_cnt = models.IntegerField()
    new_join_cnt = models.IntegerField()
    new_complete_cnt = models.IntegerField()
    new_join_circle_cnt = models.IntegerField()
    new_complete_circle_cnt = models.IntegerField()
    reward_cnt = models.IntegerField()
    reward_sum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'yinhua_stat'


class YuepaoUserInfo(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    weibo_uid = models.BigIntegerField()
    mail = models.CharField(max_length=64)
    nick = models.CharField(max_length=32)
    faceurl = models.CharField(max_length=256)
    type = models.IntegerField()
    gender = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    birthday = models.IntegerField()
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    allmeter = models.IntegerField()
    allsecond = models.IntegerField()
    allcalorie = models.IntegerField()
    allpo = models.IntegerField()
    allzpo = models.IntegerField()
    runnerlevel = models.IntegerField()
    logtime = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'yuepao_user_info'
