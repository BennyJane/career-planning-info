CREATE DATABASE career_plan_service;

use career_plan_service;

DROP TABLE  IF EXISTS `stat_browse`;

create table stat_browse
(
    id        varchar(32)  not null
        primary key,
    ip        varchar(120) null,
    origin    varchar(120) null comment '网站视图函数名称',
    create_at datetime     null,
    update_at datetime     null
);

DROP TABLE  IF EXISTS `stat_info`;

create table stat_info
(
    id        varchar(32)  not null
        primary key,
    ip        varchar(120) null,
    action    varchar(32)  null comment '访客行为: like-点赞, download-下载',
    count     int          null comment '统计单个IP下载次数',
    create_at datetime     null,
    update_at datetime     null
);

DROP TABLE  IF EXISTS `user`;
create table user
(
    create_at datetime                               null,
    update_at datetime                               null,
    id        varchar(32)                            not null
        primary key,
    username  varchar(32) collate utf8mb4_unicode_ci null,
    email     varchar(64)                            null comment '留言者的邮箱',
    avatar    text                                   null comment 'base64格式存储的用户头像',
    is_admin  tinyint(1)                             null comment '是否是网站的管理者'
)
    charset = latin1;

DROP TABLE  IF EXISTS `message`;
create table message
(
    create_at datetime                        null,
    update_at datetime                        null,
    id        varchar(32)                     not null
        primary key,
    body      text collate utf8mb4_unicode_ci null,
    reviewed  tinyint(1)                      null comment '是否已经被审核',
    user_id   varchar(32)                     null,
    constraint message_ibfk_1
        foreign key (user_id) references user (id)
)
    charset = latin1;

create index user_id
    on message (user_id);

DROP TABLE  IF EXISTS `warning_para`;

create table warning_para
(
    create_at datetime    null,
    update_at datetime    null,
    id        varchar(32) not null
        primary key,
    para      mediumtext  null
);


ALTER DATABASE career_plan_service CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE career_plan_service.warning_para CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE career_plan_service.message CHANGE body body  TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE career_plan_service.user CHANGE username username  VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;