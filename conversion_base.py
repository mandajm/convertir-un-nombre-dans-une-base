# -*- coding: utf-8 -*-
import sys
import re
regex_n,regex_o = r"[0-9]", r"[a-zA-Z]"

def carre(new_value):
	line = " "
	for i in range(0,10):
		if i == 5:
			longueur = int(len(new_value))
			j = int(14 - longueur) // 4
			print(" {} {} {} ".format("* "* j, new_value ,"* " * j))
		else:
			if i % 2 == 0: 
				line += "*  "
			else:
				line+= " *  "
			print(line)


def demarche_calcul(number,base):
	value = []
	rest,base = int(number),int(base)
	big = int(number)
	while big != 0:
		rest = rest // base
		value += "{}".format(big - rest * base)
		big = rest
	new_value = ""
	for i in range(0,len(value)):
		old_value = len(value) - 1
		new_value += "{}".format(value[old_value - i])
	return carre(new_value)

def veuiller_confirmer(base,number):	
	status = input("veuiller confirmer si vous vouler convertir [y/n]: ")
	if re.search(regex_o, status) is not None:	
		if status == "y" or status == "Y":
			return demarche_calcul(number,base)
		elif status == "n" or status == "N":
			print("Voullez_vous vous vraiment quitter [y/n]....")
			choix = input(">> ")
			if choix == "y" or choix == "Y":
				pass
			elif choix == "n" or choix == "N":
				return get_base()
			else:
				print ("choix inconnus.....")
		else:
			print("Je ne comprend pas votre choix, veuiller repeter","\n {}".format("="*60))
			veuiller_confirmer(base,number)
	else:
		print("vous devez entrer une lettre")
		return veuiller_confirmer(base,number)

def get_number(base):
	number = input("Entrer le nombre à convertir: ")
	if re.search(regex_n, number) is None:
		print("Vous devez entrer un nombre")
		return get_number(base)
	else:
		print("\n >> vous aller convertir {} en base {}".format(number,base))
		return veuiller_confirmer(base,number)
		

def get_base():
	base = input("Entrer le base dans lequel vous aller convertit votre nombre: ")
	if re.search(regex_n, base) is None:
		print("Vous devez entrer un nombre")
		return get_base()
	else:
		if int(base) <= 10:			
			return get_number(base)
		else:
			print("Vous devez choisir une valeur inférieur à 10")
			return get_base()
		
get_base()