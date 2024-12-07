from funkyfuncs import *
from time import sleep
from os import system

def main ():
	try:
		while True:
			print ("\n\n\n" + groupe_letters(groupe_brows (the_right_brow("right_brow.txt"), the_left_brow (the_right_brow("right_brow.txt")))))
			sleep (0.2)
			system ("clear")
			
			print (groupe_letters(groupe_brows (the_right_brow("right_brow.txt"), the_left_brow (the_right_brow("right_brow.txt")))))
			sleep (0.2)
			system ("clear")
		
	except KeyboardInterrupt :
		print ("Them Brows :)")
		
main ()