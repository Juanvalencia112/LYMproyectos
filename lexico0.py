import ply.lex as lex
import re
import codecs
import os
import sys


tokens = ['ASSIGN', 'WALKn', 'JUMP', 'JUMPTO', 'VEER' 
        , 'LOOK', 'DROP', 'GRAB', 'GET', 'FREE', 'POP'
        , 'WALKdn', 'WALKon', 'M','R' , 'C', 'B'
        , 'c', 'b', 'P', 'JN', 'Gxy']


reservadas = {'ifelse':'IFELSE'
        ,'if':'IF', 'while':'WHILE', 'repeat':'REPEAT'
        ,'prog':'PROG', 'gorp':'GORP', 'var':'VAR'
        , 'proc':'PROC', 'corp':'CORP' } 



tokens = tokens + list(reservadas.values())

t_ASSIGN = r'='
t_