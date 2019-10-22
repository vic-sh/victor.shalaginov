for number in list(''.join(MAC.split(':'))): 
 #print(bin(int(number,16))) 
 string_1 = bin(int(number,16)) + string_1 
 print(string_1.replace('0b',''))
