import mysql.connector


def customers():
    mydb=mysql.connector.connect(host="localhost",user="Sanchit",passwd="jajwuth@2",database="fourplus")
    mycursor=mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS customers(Name text,Address text,PhoneNumber text,GSTIN text,State text,StateCode text)")
    mydb.commit()
    mydb.close()
    
def register(name,address,phno,gstin,state,statecode):
    mydb=mysql.connector.connect(host="localhost",user="Sanchit",passwd="jajwuth@2",database="fourplus")
    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO customers VALUES(%s,%s,%s,%s,%s,%s)",(name,address,phno,gstin,state,statecode))
    mydb.commit()
    mydb.close()

def update(name,address,phno,gstin,state,statecode):
    mydb=mysql.connector.connect(host="localhost",user="Sanchit",passwd="jajwuth@2",database="fourplus")
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE customers SET Address=%s OR PhoneNumber=%s OR GSTIN=%s OR State=%s OR StateCode=%s WHERE Name=%s",(address,phno,gstin,state,statecode,name))
    mydb.commit()
    mydb.close()

def delete(name):
    mydb=mysql.connector.connect(host="localhost",user="Sanchit",passwd="jajwuth@2",database="fourplus")
    mycursor=mydb.cursor()
    mycursor.execute("DELETE FROM customers WHERE Name=%s",(name,))
    mydb.commit()
    mydb.close()

def view():
    mydb=mysql.connector.connect(host="localhost",user="Sanchit",passwd="jajwuth@2",database="fourplus")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    rows=mycursor.fetchall()
    mydb.close()
    return rows

customers()
