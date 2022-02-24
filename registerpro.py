# 注册的业务流程类
import sys
import psycopg2

class regipro():
    '''def adduser(id, name, phonenum, email, type):
        # 连接数据库
        conn = psycopg2.connect(database='DBCoursework', user='postgres', \
                                password='DXQ8181/', host='127.0.0.1', post=5432)
        cursor = conn.cursor()
        判断是学生/老师
        if (type == 'student'):
            #cursor.execute('INSERT INTO student (student_id, name, phonenum, email_address) \
            VALUES (id, name, phonenum, email)')
            conn.commit()
        else:
            cursor.execute('INSERT INTO teacher (teacher_id, name, phonenum, email_address) \
                           VALUES(id, name, phonenum, email)')
            conn.commit()
    '''

    def printf(self):
        print("ddd")

