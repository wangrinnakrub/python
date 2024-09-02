import sqlite3
import os


class StudentDatabase:
    def __init__(self, db_path):
        self.connect = sqlite3.connect(db_path)
        self.cursor = self.connect.cursor()

    def insert(self):
        try:
            data = self.get_student_data()
            self.cursor.execute(
                '''INSERT INTO student (flname,email,gender,age,grade) VALUES (?,?,?,?,?)''', data)
            self.connect.commit()
            print('\nเพิ่มข้อมูลนักเรียนเรียบร้อยแล้ว\n')
        except sqlite3.Error as e:
            print(f'Failed to insert : {e}')

    def select(self):
        try:
            results = self.cursor.execute('SELECT * FROM student')
            self.connect.commit()
            return results
        except sqlite3.Error as e:
            print(f'Failed to select : {e}')

    def update(self, od):
        try:
            data = self.get_student_data() + (od,)
            self.cursor.execute('''UPDATE student SET flname = ?, email = ?, gender = ?, age = ?, grade = ?
                      WHERE od = ? ''', data)
            self.connect.commit()
            print(f'\nแก้ไขข้อมูลนักเรียนเรียบร้อยแล้ว\n')
        except sqlite3.Error as e:
            print(f'Failed to update : {e}')

    def delete(self, od):
        try:
            self.cursor.execute('''DELETE FROM student WHERE od = ?''', (od,))
            self.connect.commit()

            self.reset_primary_key()

            print(f'\nลบข้อมูลนักเรียนเรียบร้อยแล้ว\n')
        except sqlite3.Error as e:
            print(f'Failed to delete : {e}')

    def reset_primary_key(self):
        try:
            self.cursor.execute('''CREATE TABLE student_temp AS
                                   SELECT flname, email, gender, age, grade FROM student''')
            self.connect.commit()

            self.cursor.execute('DROP TABLE student')
            self.connect.commit()

            self.cursor.execute('''CREATE TABLE student (
                                    od INTEGER PRIMARY KEY AUTOINCREMENT,
                                    flname TEXT,
                                    email TEXT,
                                    gender TEXT,
                                    age INTEGER,
                                    grade INTEGER )''')
            self.connect.commit()

            self.cursor.execute('''INSERT INTO student (flname, email, gender, age, grade)
                                   SELECT flname, email, gender, age, grade FROM student_temp''')
            self.connect.commit()

            self.cursor.execute('DROP TABLE student_temp')
            self.connect.commit()
        except sqlite3.Error as e:
            print(f'Failed to reset primary key : {e}')

    def get_student_data(self):
        flname = input('กรุณาใส่ ชื่อ-นามสกุล : ')
        email = input('กรุณาใส่ อีเมล : ')
        gender = input('กรุณาใส่ เพศ : ')
        while True:
            try:
                age = int(input('กรุณาใส่ อายุ : '))
                break
            except ValueError:
                print('กรุณากรอกอายุเป็นตัวเลขเท่านั้น\n')
                continue

        while True:
            try:
                grade = int(input('กรุณาใส่ ชั้นปี : '))
                break
            except ValueError:
                print('กรุณากรอกชั้นปีเป็นตัวเลขเท่านั้น\n')
                continue

        return (flname, email, gender, age, grade)

    def show_students(self):
        results = self.select()
        print(
            f"\nข้อมูลนักเรียน\n{'-'*110}\nลำดับที่\t    ชื่อ-นามสกุล\t\t     อีเมลล์\t\t     เพศ\tอายุ\t    ชั้นมัธยมศึกษาปีที่\n{'-'*110}")
        for value in results:
            print(
                f'{" ":<2}{value[0]:<11}{value[1]:<30}{value[2]:<30}{value[3]:<12}{value[4]:<16}{value[5]:<15}')
        print('\n')

    def exit_program(self):
        choice = input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ').lower()
        if choice == 'y':
            print('\nออกจากโปรแกรมเรียบร้อยแล้ว\n')
            self.cursor.close()
            exit()

    def main(self):
        while True:
            choice = input(
                f'\n{"-"*12} ระบบทะเบียนนักเรียน {"-"*12}\n\n\tเพิ่มนักเรียน        [a]\n\tแสดงข้อมูลนักเรียน   [s]\n\tแก้ไขข้อมูลนักเรียน   [e]\n\tลบข้อมูลนักเรียน     [d]\n\tออกจากโปรแกรม    [x]\n\nกรุณาเลือกทำรายการ : ').lower()
            if choice == 'a':
                self.insert()
                os.system('pause')
            elif choice == 's':
                self.show_students()
                os.system('pause')
            elif choice == 'e':
                od = int(input('ต้องการแก้ไขข้อมูลนักเรียนลำดับที่ : '))
                self.update(od)
                os.system('pause')
            elif choice == 'd':
                od = int(input('ต้องการลบข้อมูลนักเรียนลำดับที่ : '))
                self.delete(od)
                os.system('pause')
            elif choice == 'x':
                self.exit_program()
            else:
                print('\nกรุณาเลือกรายการใหม่อีกครั้ง\n')
                continue


if __name__ == '__main__':
    db = StudentDatabase(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\student.db')
    db.main()
