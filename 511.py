input_data = open('input.txt', 'r') 

K = input_data.read() 

#--------------------------------------------------------------------
K= int(K)
Tm = 5
T1 = 0
if K >= 146:
     aut = str("NO")
else:
     TK = (Tm * K)-Tm    
     X = TK // 60
     Y = TK % 60
     X = str(X)
     Y = str(Y)
     aut = str(X + ' ' + Y)
#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write(aut)

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()
