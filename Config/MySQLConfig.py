#-*- coding: UTF-8 -*-
__author__ = 'zuohaitao'


'''
数据库相关配置
'''

#地址
host='10.125.192.73'
#端口号
port=3306
#用户名
user='root'
#密  码
password='root1234'
#别名
database='db_name'

charset= 'latin1'




'''
CREATE TABLE `interface_interface` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '接口ID',
  `interface_name` varchar(50) NOT NULL COMMENT '接口名称',
  `interface_address` varchar(500) NOT NULL COMMENT '接口地址',
  `getorpost` int(1) NOT NULL DEFAULT '1' COMMENT '1,get方式 ，2.post方式',
  `module` int(11) DEFAULT NULL COMMENT '模块ID',
  `module_name` varchar(50) NOT NULL,
  `developers` varchar(20) DEFAULT NULL COMMENT '接口开发人员',
  `create_user` int(11) NOT NULL COMMENT '创建人id',
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
  `is_delete` int(1) NOT NULL DEFAULT '1' COMMENT '1，未删除，2。删除',
  `modeltype` int(1) NOT NULL DEFAULT '0' COMMENT '接口类型1,BS,2,CMS,3,BS-V2,4,企业办公',
  `is_login` int(1) DEFAULT '2' COMMENT '是否登录1是2否',
  `wikiaddress` varchar(200) DEFAULT NULL COMMENT 'wiki地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=761 DEFAULT CHARSET=utf8 COMMENT='接口表';
'''