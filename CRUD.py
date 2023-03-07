import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password = 'srjfrAP6!',
    database = 'bdyoutube'
)

cursor = conexao.cursor()


#CREATE
nome_produto = 'Toddynho'
valor = 3
comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})' #importante inserir aspas no elemento de texto para o python enviar "Toddynho" ou inves de Toddynho
cursor.execute(comando)
conexao.commit() #edita o banco de dados
resultado = cursor.fetchall ()#lê o banco de dados

#READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall ()
print(resultado)

#UPDATE
nome_produto = 'Toddynho'
valor = 6
comando = f'UPDATE vendas SET valor = {valor}  WHERE nome_produto = "{nome_produto}" ' #importante inserir aspas no elemento de texto para o python enviar "Toddynho" ou invés de Toddynho
cursor.execute(comando)
conexao.commit()

#DELETE
nome_produto ="Toddynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" '
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()