UNI_B = False
CHAR_ = ""

def char_set (brow):
	global CHAR_
	brow_c = []
	for line in brow:
		brow_c.append (line.replace(" ",""))
		
	CHAR_ = brow_c[0][0]

def the_right_brow (file):
	global UNI_B
	with open (file) as rb:
		drbrow = rb.readlines ()
		
	crbrow = [] 
	
	for line in drbrow:
		crbrow.append (line.replace ("\n", ""))
	
	char_set (crbrow)
	
	if "/U" in crbrow:
		UNI_B = True
		return crbrow [0:crbrow.index("/U")]
		
	else:
		return crbrow

def groupe_letters (iter):
	f_str = ""
	for line in iter:
		fl_str = ""
		for char in line:
			fl_str += char
			
		f_str = f_str + (fl_str + "\n")
		
	return f_str
			

def the_left_brow (right_brow):
	left_brow = []
	
	for line in right_brow:
		lbr_str = ""
		line = list (line)
		line.reverse()
		for char in line:
			lbr_str += char
			
		left_brow.append (lbr_str)
	
	return left_brow
	
def groupe_brows (r_brow, l_brow):
	brows = []
	
	if UNI_B:
		for line in l_brow:
			if line [0] == " ":
				brows.append (line + (CHAR_ * 5) + r_brow[l_brow.index(line)])
			
			else:
				brows.append (line + (" " * 5) + r_brow[l_brow.index(line)])
	else :
		for line in l_brow:
			brows.append (line + (" " * 5) + r_brow[l_brow.index(line)])
	
	return brows
