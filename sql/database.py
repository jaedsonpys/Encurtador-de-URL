import pymysql
from datetime import datetime

conn = pymysql.connect(
    password='firlastdatabase',
    user='root'
)

sql = conn.cursor()

sql.execute('create database if not exists FirlastShortener')
sql.execute('use FirlastShortener')

sql.execute('''create table if not exists URLs(
    key_url varchar(6) primary key, original_url varchar(256), key_issue datetime not null)
''')


class MySQL:
    def register_url(self, key, url) -> bool:
        has_exist_key = self.verify_key(key)

        if has_exist_key is not None:
            # a chave já está em uso, logo, retorne um "aviso"
            # para que outra chave seja gerada.
            return False


        key_issue = str(datetime.utcnow())
        sql.execute('insert into URLs values(%s, %s, %s)', (key, url, key_issue, ))
        conn.commit()
        
        return True


    def verify_key(self, key_url) -> bool:
        # Essa função é encarregada de realizar 
        # a verificação para ver se a url já está registrada
        # e também para obter a url original quando um usuário
        # solicitar. #
        
        sql.execute('select * from URLs where key_url = %s', (key_url, ))
        original_url = sql.fetchone()

        return original_url

#app = MySQL()

#for i in range(10):
#    print(app.register_url(f'7Hjk{i}T', 'www.google.com'))
#    print(app.verify_key('7Hjk2T'))
#    print()