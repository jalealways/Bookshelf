# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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


class SunpanTemp(models.Model):
    isbn = models.CharField(max_length=13)
    brief_introduction = models.CharField(db_column='BRIEF_INTRODUCTION', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sunpan_temp'


class TbBookBaseInfo(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=13)  # Field name made lowercase.
    book_name = models.CharField(db_column='BOOK_NAME', max_length=100)  # Field name made lowercase.
    publishing_house = models.ForeignKey('TbPublishingHouseBaseInfo', models.DO_NOTHING, db_column='PUBLISHING_HOUSE_ID')  # Field name made lowercase.
    original_proce = models.DecimalField(db_column='ORIGINAL_PROCE', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    author_name = models.CharField(db_column='AUTHOR_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    translator_name = models.CharField(db_column='TRANSLATOR_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    publishing_time = models.CharField(db_column='PUBLISHING_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    book_class_id = models.CharField(db_column='BOOK_CLASS_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    child_class = models.ForeignKey('TbDimBookClass', models.DO_NOTHING, db_column='CHILD_CLASS_ID', blank=True, null=True)  # Field name made lowercase.
    douban_rating = models.DecimalField(db_column='DOUBAN_RATING', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    brief_introduction = models.CharField(db_column='BRIEF_INTRODUCTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cover_pic = models.CharField(db_column='COVER_PIC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.CharField(db_column='CREATE_USER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_user_id = models.CharField(db_column='UPDATE_USER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_book_base_info'


class TbBookRating(models.Model):
    rating_id = models.CharField(db_column='RATING_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    reader_rating = models.DecimalField(db_column='READER_RATING', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    reader_comment = models.CharField(db_column='READER_COMMENT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reader_id = models.CharField(db_column='READER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.CharField(db_column='CUSTOMER_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rating_time = models.DateTimeField(db_column='RATING_TIME', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    original_id = models.CharField(db_column='ORIGINAL_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_book_rating'


class TbBookStatusDetail(models.Model):
    book_id = models.CharField(db_column='BOOK_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    isbn = models.ForeignKey(TbBookBaseInfo, models.DO_NOTHING, db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.CharField(db_column='CUSTOMER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    book_status = models.ForeignKey('TbDicBookStatus', models.DO_NOTHING, db_column='BOOK_STATUS')  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    reader_id = models.CharField(db_column='READER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_book_status_detail'


class TbBookStatusDetailHis(models.Model):
    book_id = models.CharField(db_column='BOOK_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    book_status = models.CharField(db_column='BOOK_STATUS', max_length=1)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    reader_id = models.CharField(db_column='READER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_book_status_detail_his'


class TbBookshelfBaseInfo(models.Model):
    shelf_id = models.CharField(db_column='SHELF_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    customer_id = models.CharField(db_column='CUSTOMER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shelf_position = models.CharField(db_column='SHELF_POSITION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shelf_status = models.ForeignKey('TbDicSheetStatus', models.DO_NOTHING, db_column='SHELF_STATUS', blank=True, null=True)  # Field name made lowercase.
    expire_time = models.DateField(db_column='EXPIRE_TIME', blank=True, null=True)  # Field name made lowercase.
    total_box_num = models.IntegerField(db_column='TOTAL_BOX_NUM', blank=True, null=True)  # Field name made lowercase.
    used_box_num = models.IntegerField(db_column='USED_BOX_NUM', blank=True, null=True)  # Field name made lowercase.
    idled_box_num = models.IntegerField(db_column='IDLED_BOX_NUM', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_bookshelf_base_info'


class TbBookshelfBoxInfo(models.Model):
    shelf = models.ForeignKey(TbBookshelfBaseInfo, models.DO_NOTHING, db_column='SHELF_ID', primary_key=True)  # Field name made lowercase.
    box_id = models.CharField(db_column='BOX_ID', max_length=100)  # Field name made lowercase.
    book_id = models.CharField(db_column='BOOK_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    box_status = models.CharField(db_column='BOX_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    order_open_id = models.CharField(db_column='ORDER_OPEN_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    raspberry_id = models.CharField(db_column='Raspberry_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    raspberry_status = models.CharField(db_column='Raspberry_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lock_board_id = models.CharField(db_column='lock_board_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lock_id = models.CharField(db_column='lock_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lock_status = models.CharField(max_length=10, blank=True, null=True)
    ray_status = models.CharField(max_length=10, blank=True, null=True)
    raspberry_ip = models.CharField(db_column='Raspberry_IP', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_bookshelf_box_info'
        unique_together = (('shelf', 'box_id'),)


class TbBookshelfDetialHis(models.Model):
    sheet_id = models.CharField(db_column='SHEET_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    box_id = models.CharField(db_column='BOX_ID', max_length=100)  # Field name made lowercase.
    book_id = models.CharField(db_column='BOOK_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    box_status = models.CharField(db_column='BOX_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_bookshelf_detial_his'
        unique_together = (('sheet_id', 'box_id'),)


class TbCustomerInfo(models.Model):
    customer_id = models.CharField(db_column='CUSTOMER_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    customer_full_name = models.CharField(db_column='CUSTOMER_FULL_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cust_addr = models.CharField(db_column='CUST_ADDR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emp_number = models.IntegerField(db_column='EMP_NUMBER', blank=True, null=True)  # Field name made lowercase.
    relation_name = models.CharField(db_column='RELATION_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    relation_title = models.CharField(db_column='RELATION_TITLE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    relation_phone = models.CharField(db_column='RELATION_PHONE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    relation_email = models.CharField(db_column='RELATION_EMAIL', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_customer_info'


class TbCustomerOrderInfo(models.Model):
    order_id = models.CharField(db_column='ORDER_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    customer_id = models.CharField(db_column='CUSTOMER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shelf_id = models.CharField(db_column='SHELF_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    begin_date = models.DateField(db_column='BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    onlime_date = models.DateField(db_column='ONLIME_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.
    order_status = models.CharField(db_column='ORDER_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    order_amount = models.BigIntegerField(db_column='ORDER_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    other_info = models.CharField(db_column='OTHER_INFO', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_customer_order_info'


class TbDicBookStatus(models.Model):
    book_status = models.CharField(db_column='BOOK_STATUS', primary_key=True, max_length=2)  # Field name made lowercase.
    status_desc = models.CharField(db_column='STATUS_DESC', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_dic_book_status'


class TbDicManagerRole(models.Model):
    role_id = models.CharField(db_column='ROLE_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    role_name = models.CharField(db_column='ROLE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    authority_desc = models.CharField(db_column='AUTHORITY_DESC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.CharField(db_column='CREATE_USER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_user_id = models.CharField(db_column='UPDATE_USER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_dic_manager_role'


class TbDicSheetStatus(models.Model):
    sheet_status = models.CharField(db_column='SHEET_STATUS', primary_key=True, max_length=1)  # Field name made lowercase.
    status_desc = models.CharField(db_column='STATUS_DESC', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_dic_sheet_status'


class TbDimBookClass(models.Model):
    child_class_id = models.CharField(db_column='CHILD_CLASS_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    child_class = models.CharField(db_column='CHILD_CLASS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    book_class_id = models.CharField(db_column='BOOK_CLASS_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    book_class = models.CharField(db_column='BOOK_CLASS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_dim_book_class'


class TbManagerUserInfo(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    role_id = models.CharField(db_column='ROLE_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    user_password = models.CharField(db_column='USER_PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(db_column='TEL_NO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    user_status = models.CharField(db_column='USER_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    create_tme = models.DateTimeField(db_column='CREATE_TME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_user_id = models.CharField(db_column='UPDATE_USER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_manager_user_info'


class TbPublishingHouseBaseInfo(models.Model):
    publishing_house_id = models.CharField(db_column='PUBLISHING_HOUSE_ID', primary_key=True, max_length=4)  # Field name made lowercase.
    publishing_house_name = models.CharField(db_column='PUBLISHING_HOUSE_NAME', max_length=32)  # Field name made lowercase.
    addr_info = models.CharField(db_column='ADDR_INFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    post_no = models.CharField(db_column='POST_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(db_column='TEL_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    fax_no = models.CharField(db_column='FAX_NO', max_length=16, blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LINKMAN', max_length=32, blank=True, null=True)  # Field name made lowercase.
    linkman_number = models.CharField(db_column='LINKMAN_NUMBER', max_length=11, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.CharField(db_column='CREATE_USER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_user_id = models.CharField(db_column='UPDATE_USER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_publishing_house_base_info'


class TbReaderAuth(models.Model):
    tel_no = models.CharField(db_column='TEL_NO', primary_key=True, max_length=11)  # Field name made lowercase.
    reader_id = models.CharField(db_column='READER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    limit_num = models.IntegerField(db_column='LIMIT_NUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_reader_auth'


class TbReaderInfo(models.Model):
    open_id = models.CharField(db_column='OPEN_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    customer = models.ForeignKey(TbCustomerInfo, models.DO_NOTHING, db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(db_column='TEL_NO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    borrow_limit_num = models.IntegerField(db_column='BORROW_LIMIT_NUM', blank=True, null=True)  # Field name made lowercase.
    borrow_num = models.IntegerField(db_column='BORROW_NUM', blank=True, null=True)  # Field name made lowercase.
    borrow_left = models.IntegerField(db_column='BORROW_Left', blank=True, null=True)  # Field name made lowercase.
    order_limit_num = models.IntegerField(db_column='ORDER_LIMIT_NUM', blank=True, null=True)  # Field name made lowercase.
    order_num = models.IntegerField(db_column='ORDER_NUM', blank=True, null=True)  # Field name made lowercase.
    reader_status = models.CharField(db_column='READER_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    active_time = models.DateTimeField(db_column='ACTIVE_TIME', blank=True, null=True)  # Field name made lowercase.
    active_id = models.CharField(db_column='ACTIVE_ID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reg_shelf_id = models.CharField(db_column='Reg_shelf_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reg_time = models.DateTimeField(db_column='Reg_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_reader_info'
