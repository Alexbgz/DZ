from mysql import connector
#connection = connector.connect(user='root', password='root', host='127.0.0.1', database='1db')
class Connection():
   def __init__(self,user,password,host,database):
      self.user=user
      self.password = password
      self.host = host
      self.database = database
      self._connection=None
   @property
   def connection(self):
      return self._connection
   def __enter__(self):
      self.connect()
   def __exit__(self, exc_type, exc_val, exc_tb):
      self.disconnect()
   def connect(self):
      if not self._connection:
         self._connection = connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
   def disconnect(self):
      if self._connection:
         self._connection.close()

class Catalog:
   def __init__(self,db_connection, product, category, price, quantity, foto):
       self.db_connection=db_connection
       self.product=product
       self.category = category
       self.price = price
       self.quantity = quantity
       self.foto = foto

   def save(self):
      c = self.db_connection.cursor()
      c.execute("INSERT INTO user (product, category, price, quantity, foto) VALUES (%s,%s,%s,%s,%s)", (self.product, self.category, self.price, self.quantity, self.foto))
      self.db_connection.commit()
      c.close()

   def spisok(self):
      c = self.db_connection.cursor()
      c.execute("SELECT * FROM catalog")
      takeall=c.fetchall()
      arr = []
      for e in takeall:
         arr.append(Catalog(self.db_connection, e[1], e[2], e[3], e[4], e[5]))
      return arr

conn=Connection('alex','177','127.0.0.1','shope')
with conn:
   prod=Catalog(conn.connection,'роза', 'розы', '100', '7', 'http://file.mobilmusic.ru/8e/93/2f/1330096.jpg')
   #man.save()
   a = prod.spisok()
   print(a[0].foto)