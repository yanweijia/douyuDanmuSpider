# coding:utf-8
'''''
@author: weijia
'''
from douyu.chat.room import ChatRoom
from MySqlConn import Mysql
import sys
import time

roomid = '138286'

def on_chat_message(msg):
    print '弹幕[%s]:%s' % (msg.attr('nn'), msg.attr('txt'))
    sql = 'INSERT INTO chatmsg_%s(nn,uid,ct,txt,level,time)VALUES(%s,%s,%s,%s,%s,NOW())'
    #print sql % (int(roomid), msg.attr('nn'), msg.attr('uid'), msg.attr('ct'), msg.attr('txt'), msg.attr('level'))
    mysql.insertOne(sql, (int(roomid), msg.attr('nn'), msg.attr('uid'), msg.attr('ct'), msg.attr('txt'), msg.attr('level')))
    mysql.commit()

def on_gift_message(msg):
    print '礼物[%s]:%s' % (msg.attr('nn'),msg.attr('gfid'))
    sql = 'INSERT INTO giftmsg_%s(nn,uid,level,gfid,time)VALUES(%s,%s,%s,%s,NOW())'
    mysql.insertOne(sql, (int(roomid), msg.attr('nn'), msg.attr('uid'), msg.attr('level'), msg.attr('gfid')))
    mysql.commit()

def run():
    room = ChatRoom(roomid)
    room.on('chatmsg', on_chat_message)
    room.on('dgb',on_gift_message)
    room.knock()

def createTable():
    tableChatMsg = 'CREATE TABLE IF NOT EXISTS `chatmsg_%s`(`nn` VARCHAR(20),`uid` INT,`ct` TINYINT,`txt` VARCHAR(100),`level` TINYINT,`time` DATETIME)CHARSET=utf8 COLLATE=utf8_unicode_ci'
    mysql.update(tableChatMsg, int(roomid))
    tableGiftMsg = 'CREATE TABLE IF NOT EXISTS `giftmsg_%s`(`nn` VARCHAR(20),`uid` INT,`level` TINYINT,`gfid` SMALLINT,`time` DATETIME)CHARSET=utf8 COLLATE=utf8_unicode_ci'
    mysql.update(tableGiftMsg, int(roomid))

if __name__ == '__main__':
    roomid = sys.argv[1]
    mysql = Mysql()
    createTable()
    run()
    mysql.dispose()
