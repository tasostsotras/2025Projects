ypsos=float(input("Ypsos se ekatosta: "))
varos=float(input("Varos se kila: "))
ypsos = ypsos/100
BMI=varos/(ypsos*ypsos)
print("O deiktis mazas somatos: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("exete sovari elleipsi varous")
	elif(BMI<=18.5):
		print("exete elleipsi varous")
	elif(BMI<=25):
		print("eiste se fysiologika epipeda")
	elif(BMI<=30):
		print("eiste ypervaros")
	else: print("eiste paxysarkos")
else:("eisagete egkyra dedomena")
