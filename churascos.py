import os 
os.system("cls")

churrascoN = int(input("Cuantos churrascos desea llevar?: "))
completo = int(input("Cuantos completos desea llevar?: "))
veget = int(input("Cuantos vegetarianos desea llevar?: "))
barroL = int(input("Cuantos barros luco desea llevar?: "))

total1 = churrascoN * 1500
total2 = completo * 1000
total3 = veget * 2000
total4 = barroL* 3000
total5 = total1 + total2 + total3 + total4 

input("Tiene cupon de descuento [Si/No]?")
cupdesc = total5 / 10 
print(f"El total a pagar es: {total5-cupdesc} ")