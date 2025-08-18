import sqlite3


from database import create_connection




class StudentManager():

    @staticmethod
    def add_student(stu_name, stu_address):
        """
            add a student into the table. 
            stuid, stu_name, stu_address cannot be null.
        """

        connection = create_connection()
        cursor = connection.cursor()

        try:
            sql = "INSERT INTO students(stu_name, stu_address) VALUES(?, ?)"
                
            values = [stu_name, stu_address]
            cursor.execute(sql, values)
            connection.commit()
            connection.close()
            print("This Student already Added!")
        except sqlite3.Error as error:
            print(f"ERROR: {error.message()}")

        connection.close()

    @staticmethod
    def delete_student(stu_id):
        """
            delete a student each time. to specific the student by stu_id
        """
        connection = create_connection()
        cursor = connection.cursor()       
        sql = "delete from students where stu_id = ?"
        cursor.execute(sql, [stuid])
        connection.commit()
        connection.close()
     

    @staticmethod
    def search_student(stu_id)->list[any]:
        """
        search student through his/her stu_id;
        """
        con = create_connection()
        cursor = con.cursor()
        sql = "select * from students where stu_id = ?"
        cursor.execute(sql,[stu_id])
        rows = cursor.fetchone()
        con.close()   
        return rows
             

    @staticmethod
    def view_all_students()->list[any]:
        """
        search and return all the students in the table.
        """
        con = create_connection()
        cursor = con.cursor()
        sql = "select * from students " 
        cursor.execute(sql)
        rows = cursor.fetchall()
        con.close()
        return rows