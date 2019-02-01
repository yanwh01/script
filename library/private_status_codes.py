#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# *********************************************************************
# Software : PyCharm
#
# private_status_codes.py
#
# Author    :yanwh(yanwh@digitalchina.com)
#
# Version 1.0.0
#
# Copyright (c) 2004-9999 Digital China Networks Co. Ltd
#
#
# *********************************************************************
# Change log:
#       - 2019/1/19 16:51  add by yanwh
#
# *********************************************************************
"""
module doc string
"""
"""
module doc string
imcloud interface status code for common use
"""
codes = {
    #  通用错误码
    0: ('操作成功', 'SUCCESSFUL_OPERATION'),
    1: ('非法的参数', 'INVALID_PARAMETER'),
    10: ('拦截器错误', 'INTERCEPTOR_ERROR'),
    2: ('数据不存在', 'DATA_NOT_FOUND'),
    3: ('系统异常，请联系管理员', 'SERVER_EXCEPTION'),
    4: ('系统内部错误，请重新操作', 'SERVER_INTERNAL_ERROR'),
    5: ('无权限操作', 'UNAUTHORIZED_OPERATION'),
    6: ('SESSION中当前登录用户为空', 'SESSION_USER_NOT_FOUND'),
    7: ('批量操作部分失败',),
    8: ('管理员登录成功', 'ADMINISTRATOR_LOGIN_SUCCESSFUL'),
    9: ('普通用户登录成功', 'COMMON_USER_LOGIN_SUCCESSFUL'),
    # 	业务相关错误码
    100: ('用户不存在', 'USER_NOT_EXISTS'),
    101: ('密码不正确',),
    102: ('短信验证码不正确', 'SMS_VERIFICATION_CODE_ERROR'),
    103: ('短信验证码超时',),
    104: ('该用户不能使用该SSID',),
    105: ('系统管理员不允许删除',),
    106: ('不允许创建系统管理员',),
    107: ('系统管理员只允许更新密码', 'SYSTEM_ADMIN_ONLY_ALLOWED_UPDATE_PASSWORD'),
    108: ('模板或文件格式不匹配',),
    109: ('未设置静态密码，请通过手机动态验证码登录',),
    111: ('图片分辨率不匹配',),
    112: ('文件超出大小限制',),
    113: ('该模板已被无线网络模块引用',),
    114: ('不允许新建或把已有用户改名为admin', 'COMMON_USER_NOT_ALLOWED_TO_USR_NAME_ADMIN'),
    115: ('静态密码长度要求大于等于8位', 'PASSWORD_LENGTH_SHOULD_GREATER_THEN_EIGHT'),
    120: ('此名称已存在',),
    121: ('用户邮箱已存在',),
    122: ('用户手机号已存在',),
    123: ('用户手机号格式不对', 'PHONE_NUMBER_FORMAT_ERROR'),
    124: ('机构名称为空',),
    125: ('姓名为空',),
    126: ('手机号为空',),
    127: ('邮箱格式不对',),
    128: ('校管理员不能导入其它学校用户',),
    130: ('上级机构名称为空',),
    131: ('IP范围不对',),
    132: ('搜索手机号少于6位',),
    141: ('机构名已存在',),
    142: ('指向的父节点不存在',),
    143: ('机构下存在自定义用户组，不允许删除',),
    144: ('机构下存在下属机构，不允许删除',),
    145: ('机构下存在用户，不允许删除',),
    146: ('根节点不允许修改父节点ID、名称',),
    147: ('根节点不允许删除',),
    148: ('机构下存在设备，不允许删除',),
    149: ('机构下存在用户组、用户，不允许删除',),
    150: ('机构下存在用户组、设备，不允许删除',),
    151: ('机构下存在用户、设备，不允许删除',),
    152: ('机构下存在用户组、用户和设备，不允许删除',),
    153: ('最高只支持5级组织机构',),
    154: ('根机构不存在或者不唯一',),
    155: ('IP格式不正确',),
    156: ('IP段起始值大于IP段结束值',),
    157: ('新增IP段与现存IP段有冲突',),
    158: ('新增IP段之间有冲突',),
    159: ('IP段存在错误',),
    160: ('不允许创建默认组',),
    161: ('用户组名在机构范围内有重名',),
    162: ('用户组下存在用户，不允许删除',),
    163: ('默认组，不允许删除或修改',),
    164: ('不允许修改用户组类型',),
    165: ('SSID正在被使用',),
    166: ('机构下存在AP设备，不允许删除',),
    170: ('调用智云平台短信接口失败',),
    171: ('短信服务参数设置不正确',),
    172: ('调用时间服务器获取当前时间失败',),
    173: ('时间格式错误',),
    174: ('LICENSE文件校验不通过',),
    176: ('获取LICENSE信息失败 ',),
    181: ('设置管理员权限时，被设置用户不是管理员',),
    182: ('已存在根机构',),
    183: ('IP及子网掩码设置不成功',),
    184: ('网关设置不成功',),
    185: ('DNS设置不成功',),
    186: ('AC系统错误',),
    191: ('AC 状态上报时，返回给AC的值，表示 AC不存在 ',),
    192: ('会议已经开始,不能操作',),
    193: ('会议已经结束',),
    194: ('会议开始时间在当前时间之前',),
    197: ('AP已经分组不可新增',),
    198: ('AP处于在线状态',),
    199: ('AP处于离线状态',),
    200: ('AP全部处于在线状态',),
    201: ('AP全处于离线状态',),
    202: ('AP全处于部分离线状态',),
    203: ('SN已经被其他AP占用',),
    204: ('SN为空',),
    205: ('和AC通信失败',),
    206: ('AP 名称为空',),
    207: ('位置为空',),
    208: ('SN重复',),
    209: ('会议结束时间在当前时间之前',),
    210: ('组织机构下没有分组',),
    211: ('当前用户没有个性化桌面图片',),
    212: ('没有对应的SSID',),
    213: ('AP名称太长',),
    214: ('安装位置太长',),
    215: ('SN太长',),
    216: ('获取CPU使用率失败',),
    217: ('获取内存使用率失败',),
    218: ('获取硬盘服务分区信息失败',),
    219: ('根机构不唯一',),
    220: ('根机构不存在',),
    221: ('设置系统时间失败',),
    222: ('设置系统全局参数失败',),
    223: ('重启系统失败',),
    224: ('查询条件的数据不在权限或搜索的范围内',),
    225: ('管理员必须有管理的组织机构',),
    226: ('SSID超过32个字节',),
    230: ('修改AC超级管理员密码失败',),
    231: ('字符串超过长度',),
    232: ('开始时间必须在结束时间之前',),
    233: ('掩码格式不正确',),
    234: ('DNS格式不正确',),
    235: ('网关格式不正确',),
    236: ('vlanId范围不正确',)
}

for number in codes:
    locals()[f"ERROR_CODE_{number}"] = number

    for label in codes[number]:
        locals()[label] = number
