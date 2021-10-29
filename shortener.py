# Copyright © 2021 Jaedson Francisco da Silva 
# 
# Código principal #

from random import choice
from sql.database import MySQL
from datetime import datetime

class Shortener:
    def new_url(self, url: str) -> str:
        self.url = url

        while True:
            key_url = self.__generate_key()
            db = MySQL().register_url(key_url, url)

            if not db:
                continue
            else:
                break
        
        return key_url

    def __generate_key(self) -> str:
        key = ''

        letters_lower = 'abcdefghijklmnopqrstuvwxyz'
        letter_upper = 'ABCDEFGHIJLKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'

        all_caracters = str(letter_upper + letters_lower + numbers)

        for i in range(6):
            key += f'{choice(all_caracters)}'

        return key


    def get_url(self, key_url) -> dict:
        db = MySQL().verify_key(key_url)

        if db is None:
            # não existe nenhuma URL registrada
            # com essa chave
            return False

        url_info = {
            'key_url': db[0],
            'url': db[1],
            'key_issue': db[2]
        }

        return url_info