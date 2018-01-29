import pymysql

conn = pymysql.connect(host = 'localhost', port = 3306, user = 'root',
                        passwd = 'ilovemuxi', db = 'students', use_unicode=True, 
                        charset="utf8")

cur = conn.cursor()

def init_students_table(cur):
    cur.execute('''create table students
    (id         integer(10) NOT NULL AUTO_INCREMENT,
    cid         varchar(12) unique,
    name        varchar(30),
    college     varchar(30),
    politic     varchar(30),
    gender      varchar(12),
    major       varchar(30),
    birth       varchar(12),
    national    varchar(30),
    grade       varchar(12),
    home       varchar(30),
    primary key (id, cid)) 
    ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    AUTO_INCREMENT=1;''')

def insert_students(stus, cur):
    try:
        for stu in stus:
            cur.execute("insert into students (cid, name, college, politic, gender, major, birth, national, grade, home) values " + "('" + str(stu[0]) + "','" + str(stu[1]) + "','" + str(stu[2]) + "','" + str(stu[3]) + "','" + str(stu[4]) + "','" + str(stu[5]) + "','" + str(stu[6]) + "','" + str(stu[7]) + "','"+ str(stu[8]) + "','" + str(stu[9]) + "');")
            print(stu)
    except:
        pass
    conn.commit()
if __name__ == '__main__':
    init_students_table(cur)
