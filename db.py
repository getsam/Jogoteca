import sqlite3

database = sqlite3.connect('jogoteca.db')
cursor = database.cursor()

cursor.execute('''CREATE TABLE `jogo` (
      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
      nome varchar(50) NOT NULL,
      categoria varchar(40) NOT NULL,
      console varchar(20) NOT NULL,
    )''')


'''cursor.executemany(
      'INSERT INTO jogo (id,  nome, categoria, console) VALUES (?,?, ?, ?)',
      [
            (1,'God of War 4', 'Acao', 'PS4'),
            (2,'NBA 2k18', 'Esporte', 'Xbox One'),
            (3,'Rayman Legends', 'Indie', 'PS4'),
            (4,'Super Mario RPG', 'RPG', 'SNES'),
            (5,'Super Mario Kart', 'Corrida', 'SNES'),
            (6,'Fire Emblem Echoes', 'Estrategia', '3DS'),
      ])'''

#cursor.execute("DROP TABLE jogo")
#cursor.execute("DROP TABLE USUARIO")
database.commit()

database.close()