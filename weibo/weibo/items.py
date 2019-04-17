# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Field, Item


class UserItem(Item):
    collection = 'users'
    id = Field()
    name = Field()
    avatar = Field()  # 主页
    cover = Field()  # 头像
    gender = Field()  # 性别
    description = Field()  # 描述
    fans_count = Field()  # 粉丝数
    follows_count = Field()  # 关注数
    weibos_count = Field()  # 微博总数
    verified = Field()  # 认证状态
    verified_reason = Field()  # 认证原因
    verified_type = Field()  # 认证分类
    follows = Field()  #
    fans = Field()
    crawled_at = Field()


class UserRelationItem(Item):
    collection = 'users'
    id = Field()
    follows = Field()
    fans = Field()


class WeiboItem(Item):
    collection = 'weibos'
    id = Field()
    attitudes_count = Field()
    comments_count = Field()
    reposts_count = Field()
    picture = Field()
    pictures = Field()
    source = Field()
    text = Field()
    raw_text = Field()
    thumbnail = Field()
    user = Field()
    created_at = Field()
    crawled_at = Field()


