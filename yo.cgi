#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

html_body = """
<!DOCTYPE html>
<html lang="ja">
    <head>
        <title>Yoするだけ</title>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
        <p>
            Yo To NYARU!<br />
            僕にYoするだけ。（Yoの通知は音ならないので大丈Ｖ）
        </p>
        <form action="send_yo.cgi" method ="POST">
            <input type="submit" name="Yo" value="Yo"/>
        </form>
        <p>
            NYARUWEBにYoすると↓に名前表示<br />
            %s
        </p>
    </body>
</html>
"""

connector = MySQLdb.connect(host="hostname",db="dbname", user="username", passwd="pass", charset="utf8")
cursor = connector.cursor()
cursor.execute("select * from test_table order by time")

result = cursor.fetchall()

#名前部分の文字列を生成
resultstr =""
for data in result:
	resultstr += str(data[0]) +" >> " + str(data[1]) + "<br />"

cursor.close()
connector.close()

print "Content-Type: text/html\n\n"
print
print html_body % resultstr
