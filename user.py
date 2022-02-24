# 注册的业务流程类
import sys
import psycopg2
# 连接数据库
conn = psycopg2.connect(database='DBCoursework', user='postgres', password='DXQ8181/', host='127.0.0.1')
cursor = conn.cursor()
class regipro():
    def Adduser(self, id, name, phonenum, email, dep_id, type):
        #判断是学生/老师
        if (type == 'student'):
            JudgeIfExist = "SELECT name FROM student WHERE student_id = %s"
            cursor.execute(JudgeIfExist, (id,))
            rows = cursor.fetchall()
            if(len(rows) == 0):
                #插入学生信息
                insert_stu = "INSERT INTO student (name, student_id, phonenum, email_address, dep_id) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_stu, (name, id, phonenum, email, dep_id))
                conn.commit()
                return 1
            else:
                #id一样就不插入
                return 0
        else:
            JudgeIfExist = "SELECT name FROM teacher WHERE teacher_id = %s"
            cursor.execute(JudgeIfExist, (id,))
            rows = cursor.fetchall()
            if (len(rows) == 0):
                insert_tec = "INSERT INTO teacher (teacher_id, name, phonenum, email_address, dep_id) VALUES(%s, %s, %s, %s, %s)"
                cursor.execute(insert_tec, (id, name, phonenum, email, dep_id))
                conn.commit()
                return 1
            else:
                return 0
    def CheckStu_Tea(self, id, name, dep_id, stu_teac):
        if (stu_teac == 'student'):
            Check_stu = "SELECT student_id FROM student WHERE student_id = %s AND name = %s AND dep_id = %s"
            cursor.execute(Check_stu, (id, name, dep_id))
            row_stu = cursor.fetchall()
            if (len(row_stu) == 0):
                return 0
            else:
                return 1
        else:
            Check_teac = "SELECT teacher_id FROM teacher WHERE teacher_id = %s AND name = %s AND dep_id = %s"
            cursor.execute(Check_teac, (id, name, dep_id))
            row_teac = cursor.fetchall()
            if (len(row_teac) == 0):
                return 0
            else:
                return 1






