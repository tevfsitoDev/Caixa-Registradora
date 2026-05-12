import sqlite3
pytosql = sqlite3.connect("gastos.db")
cursor = pytosql.cursor()
#conexāo python a sql

cursor.execute("""
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preço_und REAL NOT NULL,
    total REAL NOT NULL,
    data DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
pytosql.commit()

def leide(i,c,p,t):
 cursor.execute("INSERT INTO compras (item,quantidade,preço_und,total) VALUES(?,?,?,?)",
 (i,c,p,t))
 pytosql.commit()
def historico():
 print("\n--Historico De Compras--")
 cursor.execute("SELECT * FROM compras")
 datos = cursor.fetchall()
 for fila in datos:
  print(f"#{fila[0]}  - {fila[1]} | Total: {fila[4]} | Fecha: {fila[5]}")     

while True:
 print ("Bem-Vindo A Caixa Registradora\n")
 print ("Seleccione uma opçāo\n")
 print ("""
 1.Registrar Vendas
 2.Historico
 3.Sair""")

 opcion = int(input(""))
 if opcion == 1:
  while True:
   item = input("Item: ")
   cantidad = int(input("Quantidade: "))
   precio = float(input("Preço unidade: "))
   total = cantidad * precio
   print("Total: ", total)
   leide(item,cantidad,precio,total)
   print("Sucesso!\n")
   print("1.Nova compra 2.sair")
   opcion2 = int(input(""))
   if opcion2 == 2:
    print("saindo...")
    break
   else:
    print("Nova Compra")
 elif opcion == 2:
  historico()
  input('Presione "Enter" Para Voltar Ao Inicio\n')

 
 elif opcion == 3:
  print("Saindo...")
  break
