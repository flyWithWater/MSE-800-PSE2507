
from college_info_database import CollegeInfoDatabase
import sqlite3




#have at least three functionality such as add records, delete records and view records for different tables.
#  id:int
#     name:str
#     student_representative:str
#     classroom:str

class ClassDao:

    def add(self,name,student_representative, classroom):

        connection = CollegeInfoDatabase.create_connection()
        cursor = connection.cursor()
        try:
            insertSql = "insert into class(name, student_representative_id,classroom) VALUES(?, ?, ?)"
            params = [name,student_representative,classroom]
            cursor.execute(insertSql,params)
            connection.commit()
        except sqlite3.Error as errr:
            print(errr.sqlite_errorcode + errr.sqlite_errorname)
        
        cursor.close()
    


    def delete(self,id):
        connection = CollegeInfoDatabase.create_connection()
        cursor = connection.cursor()

        cursor.execute("delete from class where id = ?",[id])
        connection.commit()
        connection.close()





    def viewAll(self):
        connection = CollegeInfoDatabase.create_connection()
        cursor = connection.cursor()
        cursor.execute("select * from class")            
        rows = cursor.fetchall()

        connection.close()

        return rows
    
   

