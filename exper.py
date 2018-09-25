#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import inferences
from inferences import solve

from pprint import pprint

def is_printing(char):
	i = "qertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM".find(char)
	if i == -1:
		return 0
	return 1

def is_tabu(string):
	for i in string:
		if i != '\t' and i != ' ':
			return 0
	return 1

def is_space(string):
	for i in string:
		if i != ' ':
			return 0
	return 1

def init_table():
	table = []
	try:
		oui = sys.argv[1]
	except:
		print "file"
		sys.exit()

	text = open(sys.argv[1], "r")
	text = text.read()
	text = text.replace("\t","")
	text = text.split('\n')

	count = 0
	for i in text:
		try:
			sharp = i.index("#")
			i = i[:sharp]
			if len(i) == 0 and is_tabu(i):
				continue
			i = ' '.join(i.split())
			table.append(i)
		except:
			if len(i) != 0 and is_tabu(i) == 0:
				i = ' '.join(i.split())
				table.append(i)
		count += 1
	return table

def set_true_value(table):
	true_value = []
	count = 0;
	for i in table:
		if i[0] == '=':
			table.remove(i)
			i = i [ 1:]
			if(i == ''):
				print "error = "
				sys.exit()
			i = i.split(',');
			for val in i:
				if('!' in val or '(' in val or ')' in val or '+' in val or '^' in val or '|' in val or ' ' in val or len(val) == 0):
					print 'error ='
					sys.exit()
				if((val in true_value) == False):
					true_value.append(val)
			count = 1;
	if count == 0:
		print "erreur = not found"
		sys.exit()
	return true_value

def set_chr_value(table):
	true_value = []
	count = 0;
	for i in table:
		if i[0] == '?':
			table.remove(i)
			i = i [ 1:]
			if(i == ''):
				print "error ? "
				sys.exit()
			i = i.split(',');
			for val in i:
				if('!' in val or '(' in val or ')' in val or '+' in val or '^' in val or '|' in val or ' ' in val or len(val) == 0):
					print 'error ?'
					sys.exit()
				if((val in true_value) == False):
					true_value.append(val)
			count = 1;
	if count == 0:
		print "erreur ? not found"
		sys.exit()
	return true_value

def parsing_corp(table, true_value):
	false_value = []
	for i in table:
		split = i.split("=>")
		if len(split) == 1:
			print "erreur parsing =>"
			sys.exit()
		split[0] = ' '.join(split[0].split())
		condition = split[0].split(' ');

		#condition.remove('')

		count = 0
		#print condition;
		for verif in condition:
			if(',' in verif):
				print 'erreur parsing'
				sys.exit()
			if verif == '':
				continue

			if(count % 2 == 0):
				while(verif[0] == '!' or verif[0] == '('):
					verif = verif [ 1:]
					if(len(verif) == 0):
						print "error parsing"
						sys.exit()
				if(len(verif) >= 1 and verif[len(verif) - 1] == ')'):
					verif = verif [:len(verif)-1]


				


				if (verif in true_value) == False  and (verif in false_value) == False :
					if('(' in verif or ')' in verif or '+' in verif or '^' in verif or '|' in verif or ' ' in verif or len(verif) == 0):
						print 'error var'
						sys.exit()
					false_value.append(verif)

			else:
				if verif != '+' and verif != '|' and verif != '^' and verif != '':
					print "erreur parsing"
					sys.exit()
			count += 1
	return (false_value);





def braket(tab):
	for var in tab:
		var = var.split("=>")
		if(var[0].count('(') != var[0].count(')') or var[1].count('(') != var[1].count(')')):
			print "error braket"
			sys.exit()



def false_char_in_chr(chr_value, false_value,true_value):
	for i in chr_value:
		if ((i in false_value) == False and (i in true_value) == False):
			false_value.append(i)
	return(false_value)


def format(tab):
	i = 0
	while(i < len(tab)):
		tab[i] = tab[i].replace("!", " ! ")
		tab[i] = tab[i].replace("(", " ( ")
		tab[i] = tab[i].replace(")", " ) ")
		tab[i] = ' '.join(tab[i].split())
		print tab[i]
		i += 1
	return(tab)


if ( __name__ == "__main__"):
	table = init_table()
	true_value = set_true_value(table)
	chr_value = set_chr_value(table)
	false_char = parsing_corp(table, true_value)
	false_char = false_char_in_chr(chr_value, false_char, true_value)
	braket(table)
	table = format(table)

	#print text
	print true_value     #valeur vrais
	print false_char 	 #valeur fause
	print chr_value 	 #les valeur qu'on cherche
	print table 		 #les ligne a executer au fur est a mesur, elle sont tout vrais !
	#solve()