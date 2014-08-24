#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import datetime
import MySQLdb

form = cgi.FieldStorage()
#Yoされるとusernameのパラメータが渡される
name = form["username"].value

connector = MySQLdb.connect(host="hostname",db="databasename", user="username", passwd="pass", charset="utf8")
cursor = connector.cursor()

#テーブルはTIMESTAMPとTEXTの２つを使っています。
#TIMESTAMPのNOW関数とusernameで渡された名前をデータベースに登録
sql = u"insert into test_table values(NOW(),'%s')" % name
cursor.execute(sql)

cursor.close()
connector.close()

#何も出ないのも寂しいので出力しとく
print "Content-type:text/html\n\n"
print "Yo catch ok"
