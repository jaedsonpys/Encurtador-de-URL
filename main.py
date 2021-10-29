# Copyright © 2021 Jaedson Francisco da Silva 
# 
# Código principal #

from random import choice

class Shortener:
    def __init__(self, url: str) -> str:
        self.url = url
        print(self.__generate_key())


    def __generate_key(self) -> str:
        key = ''

        letters_lower = 'abcdefghijklmnopqrstuvwxyz'
        letter_upper = 'ABCDEFGHIJLKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'

        all_caracters = str(letter_upper + letters_lower + numbers)

        for i in range(6):
            key += f'{choice(all_caracters)}'

        return key

Shortener('www.google.com')