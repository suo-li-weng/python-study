import xlrd
import sqlite3

def build_db():
    '''读取xls文件建立数据库'''
    file_path = "C:\\Users\\god\\python\\2019-11-19\\python名单.xls"
    data = xlrd.open_workbook(file_path)
    table = data.sheets()[0]
    nrows = table.nrows
    head = str(table.row_values(0))[1:-1]
    l = []
    for i in range(1, nrows):
        l.append(table.row_values(i))
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('create table student(' + head + ')')
    c.executemany('insert into student values(?,?,?,?)', l)
    conn.commit()
    conn.close()


import xlwt
def write_xls():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('select * from student')
    l=c.fetchall()
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('Sheet1')
    for i in range(len(l)):
        for j in range(len(l[i])):
            worksheet.write(i, j, l[i][j])
    workbook.save('formatting.xls')
    conn.close()


def delete_student():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("DELETE from student where 序号==2;")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    conn.close()


def insert_student():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("INSERT INTO student \
      VALUES (1, 17110501124,'Paul', 'California')");
    conn.commit()
    conn.close()


def update_student():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("UPDATE student set 学号 = 25000 where 序号=3")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)
    conn.close()


def select_student():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    cursor = c.execute("SELECT 序号,学号,班级,姓名 from student where 1=1")
    for row in cursor:
       print("序号 = ", row[0])
       print("学号 = ", row[1])
       print("班级 = ", row[2])
       print("姓名 = ", row[3], "\n")


def main():
    build_db()
    write_xls()

if __name__ == '__main__':
    main()
