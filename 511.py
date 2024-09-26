input_data = open('input.txt', 'r') 

K = input_data.read() 

#--------------------------------------------------------------------
K= int(K)
Tm = 5
T1 = 0
if K >= 250:
     TK = str("NO")
else:
     TK = (Tm * K)-Tm
X=TK // 60
Y=TK % 60
X = str(X)
Y = str(Y)
#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write(str(X + ' ' + Y))

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()
