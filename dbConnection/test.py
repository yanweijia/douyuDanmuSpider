# coding:utf-8
'''''

@author: baocheng
'''
from MySqlConn import Mysql
from _sqlite3 import Row

# 申请资源
mysql = Mysql()

sql = "CREATE TABLE IF NOT EXISTS `chatmsg_%s`(`nn` VARCHAR(20),`uid` INT,`ct` TINYINT,`txt` VARCHAR(100),`level` TINYINT,`time` DATETIME)CHARSET=utf8 COLLATE=utf8_unicode_ci"
mysql.update(sql, 111)
sql = 'INSERT INTO chatmsg_1115080(nn,uid,ct,txt,level,time)VALUES(\'粘稠的太阳\',40281825,2,\'有点尴尬\',9,now())'
mysql.insertOne(sql,())





'''
sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
result = mysql.getAll(sqlAll)
if result :
    print "get all"
    for row in result :
        print "%s\t%s"%(row["uid"],row["goodsname"])
sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
result = mysql.getMany(sqlAll,2)
if result :
    print "get many"
    for row in result :
        print "%s\t%s"%(row["uid"],row["goodsname"])


result = mysql.getOne(sqlAll)
print "get one"
print "%s\t%s"%(result["uid"],result["goodsname"])
'''
# 释放资源
mysql.dispose()
