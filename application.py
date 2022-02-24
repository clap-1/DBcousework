import sys
import psycopg2
# 连接数据库
conn = psycopg2.connect(database='DBCoursework', user='postgres', password='DXQ8181/', host='127.0.0.1')
cursor = conn.cursor()

class Manage_Application():
    # 添加申请
    def Add_Application(self,app_id, student_id, teacher_id, apply_time,
                        leave_time, return_time, leave_reason, state, comment_id):
        insert_application = "INSERT INTO application (application_id, student_id, teacher_id, apply_time, leave_time, \
         return_time, leaving_reason, state, comment_id) VALUES (%s, %s, %s, \
         to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone, \
         to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone, \
         to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone, %s, %s, %s)"
        cursor.execute(insert_application, (app_id, student_id, teacher_id, apply_time, leave_time, return_time,
                                            leave_reason, state, comment_id))
        conn.commit()

    # 返回负责该学生申请的老师id
    def FindTeacResForStu(self, student_id):
        Find_Teac = "SELECT t.teacher_id FROM department d JOIN teacher t ON d.dep_id = t.dep_id JOIN student s \
        ON s.dep_id = d.dep_id WHERE s.student_id = %s AND s.dep_id = t.dep_id"
        cursor.execute(Find_Teac, (student_id,))
        #返回所有该系的老师，默认取第一个为负责老师
        TeacRow = cursor.fetchall()
        return TeacRow[0][0]

    #返回负责该学生申请的老师名字
    def FindTeacNameForStu(self, student_id):
        Find_Teac = "SELECT t.name FROM department d JOIN teacher t ON d.dep_id = t.dep_id JOIN student s \
        ON s.dep_id = d.dep_id WHERE s.student_id = %s AND s.dep_id = t.dep_id"
        cursor.execute(Find_Teac, (student_id,))
        # 返回所有该系的老师，默认取第一个为负责老师
        TeacRow = cursor.fetchall()
        return TeacRow[0][0]

    # 返回是否有时间重合
    def CheckTimeOverlap(self, app_id, student_id, leave_time, return_time):
        checkoverlap = "SELECT application_id FROM application WHERE \
        ((((leave_time >= (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone))) AND \
        (leave_time <= (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone)) OR \
        ((leave_time <= (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone)) AND \
        (return_time >= (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone))) OR \
        (return_time >= (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone)) AND \
        (return_time <= (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone))) AND \
        (student_id = %s) AND (application_id != %s) AND (state != 'Cancelled') AND (state != 'Refused'))"
        cursor.execute(checkoverlap, (leave_time, return_time, leave_time, return_time, leave_time, return_time,
                                      student_id, app_id))
        overlaprows = cursor.fetchall()
        if (len(overlaprows) == 0):
            #无重叠时间则返回0
            return 0
        else:
            #有重叠时间则返回1
            return 1

    #向comment中添加
    def Add_comment(self, comment_id, teacher_id, application_id, comment_text):
        insert_comment = "INSERT INTO comment(comment_id, teacher_id, application_id, comment_text) VALUES \
        (%s, %s, %s, %s)"
        cursor.execute(insert_comment, (comment_id, teacher_id, application_id, comment_text))
        conn.commit()

    # #返回某同学的所有离校记录
    def ReturnStuRecord(self, student_id):
        ReturnRecord = "SELECT a.application_id, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
        to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
        to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
        c.comment_text, t.name FROM application a JOIN comment c ON a.comment_id = c.comment_id Join teacher t ON \
        t.teacher_id = a.teacher_id WHERE a.student_id = %s"
        cursor.execute(ReturnRecord, (student_id,))
        Records = cursor.fetchall()
        return Records

    #检查一周内出校的次数
    def CheckLeaveCount(self, app_id, leave_time, return_time, stu_id):
        GetWeek = "SELECT COUNT(application_id) FROM application WHERE ((leave_time > \
        (SELECT date_trunc('week', %s::timestamp))) AND (leave_time < (SELECT date_trunc('week', %s::timestamp) + \
        '7 days'::interval)) AND (application_id != %s) AND ((state = 'Passed') OR (state = 'Pending')) AND \
        (student_id = %s))"
        cursor.execute(GetWeek, (leave_time, leave_time, app_id, stu_id))
        rows = cursor.fetchall()
        return rows[0][0]

    #将取消的申请置为cancelled
    def SetCancel(self, app_id):
        SetCan = "UPDATE application SET state = 'Cancelled' WHERE application_id = %s"
        cursor.execute(SetCan, (app_id,))
        conn.commit()

    #返回新的table
    def ReturnSortAndFilter(self, sorttype, filtertype, stu_id):
        if (filtertype == '全部显示'):
            filtertype = 'All'
        elif (filtertype == '筛选出已通过申请'):
            filtertype = 'Passed'
        elif (filtertype == '筛选出已被拒绝申请'):
            filtertype = 'Refused'
        elif (filtertype == '筛选出已取消申请'):
            filtertype = 'Cancelled'
        elif (filtertype == '筛选出正在审批的申请'):
            filtertype = 'Pending'
        if ((sorttype == '默认方式排序') & (filtertype == 'All')):
            sort = "SELECT a.application_id, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                                c.comment_text, t.name FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                                JOIN teacher t ON t.teacher_id = a.teacher_id WHERE a.student_id = %s"
            cursor.execute(sort, (stu_id,))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '按申请时间排序') & (filtertype == 'All')):
            sort = "SELECT a.application_id, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                    to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                    to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                    c.comment_text, t.name FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                    JOIN teacher t ON t.teacher_id = a.teacher_id WHERE a.student_id = %s ORDER BY a.apply_time ASC"
            cursor.execute(sort, (stu_id,))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '按离校时间排序') & (filtertype == 'All')):
            sort = "SELECT a.application_id, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                                c.comment_text, t.name FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                                JOIN teacher t ON t.teacher_id = a.teacher_id \
                                WHERE a.student_id = %s ORDER BY a.leave_time ASC"
            cursor.execute(sort, (stu_id,))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '默认方式排序') & (filtertype != 'All')):
            sort = "SELECT a.application_id, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                    to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                    to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                    c.comment_text, t.name FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                    JOIN teacher t ON t.teacher_id = a.teacher_id WHERE (a.student_id = %s) AND (a.state = %s)"
            cursor.execute(sort, (stu_id, filtertype))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '按申请时间排序') & (filtertype != 'All')):
            sort = "SELECT a.application_id, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                    to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                    to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                    c.comment_text, t.name FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                    JOIN teacher t ON t.teacher_id = a.teacher_id WHERE (a.student_id = %s) AND (a.state = %s)\
                    ORDER BY a.apply_time ASC"
            cursor.execute(sort, (stu_id, filtertype))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '按离校时间排序') & (filtertype != 'All')):
            sort = "SELECT a.application_id, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                                c.comment_text, t.name FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                                JOIN teacher t ON t.teacher_id = a.teacher_id \
                                WHERE (a.student_id = %s) AND (a.state = %s) ORDER BY a.leave_time ASC"
            cursor.execute(sort, (stu_id, filtertype))
            sortresult = cursor.fetchall()
            return sortresult

    #老师端排序
    def ReturnTeacSort(self, sorttype, filtertype, teac_id):
        if (filtertype == '全部显示'):
            filtertype = 'All'
        elif (filtertype == '筛选出已通过申请'):
            filtertype = 'Passed'
        elif (filtertype == '筛选出已拒绝申请'):
            filtertype = 'Refused'
        elif (filtertype == '筛选出已取消申请'):
            filtertype = 'Cancelled'
        elif (filtertype == '筛选出正在审批的申请'):
            filtertype = 'Pending'
        if ((sorttype == '默认方式排序') & (filtertype == 'All')):
            sort = "SELECT a.application_id, s.name, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                                c.comment_text FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                                JOIN student s ON s.student_id = a.student_id WHERE a.teacher_id = %s"
            cursor.execute(sort, (teac_id,))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '按申请时间排序') & (filtertype == 'All')):
            sort = "SELECT a.application_id, s.name, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                    to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                    to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                    c.comment_text FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                    JOIN student s ON s.student_id = a.student_id WHERE a.teacher_id = %s ORDER BY a.apply_time ASC"
            cursor.execute(sort, (teac_id,))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '按离校时间排序') & (filtertype == 'All')):
            sort = "SELECT a.application_id, s.name, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                                c.comment_text FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                                JOIN student s ON s.student_id = a.student_id \
                                WHERE a.teacher_id = %s  ORDER BY a.leave_time ASC"
            cursor.execute(sort, (teac_id,))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '默认方式排序') & (filtertype != 'All')):
            sort = "SELECT a.application_id, s.name, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                            to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                            to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                                            c.comment_text FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                                            JOIN student s ON s.student_id = a.student_id WHERE (a.teacher_id = %s) AND \
                                            (a.state = %s)"
            cursor.execute(sort, (teac_id, filtertype))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '按申请时间排序') & (filtertype != 'All')):
            sort = "SELECT a.application_id, s.name, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                                c.comment_text FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                                JOIN student s ON s.student_id = a.student_id WHERE (a.teacher_id = %s) AND \
                                (a.state = %s) ORDER BY a.apply_time ASC"
            cursor.execute(sort, (teac_id, filtertype))
            sortresult = cursor.fetchall()
            return sortresult
        elif ((sorttype == '按离校时间排序') & (filtertype != 'All')):
            sort = "SELECT a.application_id, s.name, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                            to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), \
                                            to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), a.leaving_reason, a.state, \
                                            c.comment_text FROM application a JOIN comment c ON a.comment_id = c.comment_id \
                                            JOIN student s ON s.student_id = a.student_id \
                                            WHERE (a.teacher_id = %s) AND (a.state = %s)  ORDER BY a.leave_time ASC"
            cursor.execute(sort, (teac_id, filtertype))
            sortresult = cursor.fetchall()
            return sortresult

    #修改申请
    def ReviseAppl(self, app_id, apply_time, leave_time, return_time, leave_reason, state, comment):
        revisesql = "UPDATE application SET \
        apply_time = (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone),\
        leave_time = (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone), \
        return_time = (to_timestamp(%s, 'yyyy-MM-dd hh24:mi:ss')::timestamp without time zone), \
        leaving_reason = %s, state = %s\
        WHERE application_id = %s"
        cursor.execute(revisesql, (apply_time, leave_time, return_time, leave_reason, state, app_id))
        revisecomment = "UPDATE comment SET comment_text = %s WHERE application_id = %s"
        cursor.execute(revisecomment, (comment, app_id))
        conn.commit()

    #老师取得本系学生的信息
    def GetAllStuApp(self, teac_id):
        GetAll = "SELECT a.application_id, s.name, to_char(a.apply_time, 'YYYY-MM-DD hh24:mi:ss'), \
        to_char(a.leave_time, 'YYYY-MM-DD hh24:mi:ss'), to_char(a.return_time, 'YYYY-MM-DD hh24:mi:ss'), \
        a.leaving_reason, a.state, c.comment_text FROM application a JOIN student s ON a.student_id = s.student_id \
        JOIN comment c ON c.comment_id = a.comment_id WHERE a.teacher_id = %s"
        cursor.execute(GetAll, (teac_id,))
        GetAllInfo = cursor.fetchall()
        return GetAllInfo

    #老师批阅后更改comment
    def InsertCommentText(self, comment_id, comment_text, app_type):
        UpdateText = "UPDATE comment SET comment_text = %s WHERE comment_id = %s"
        cursor.execute(UpdateText, (comment_text, comment_id))
        UpdateState = "UPDATE application SET state = %s WHERE comment_id = %s"
        cursor.execute(UpdateState, (app_type, comment_id))
        conn.commit()