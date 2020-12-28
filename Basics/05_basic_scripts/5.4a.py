num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

number = input('Enter a number: ')
word = input('Enter a word: ')

lenght_num = len(num_list)
num_list.reverse()
position_rev_num = num_list.index(int(number))
position_num = lenght_num - position_rev_num - 1

lenght_word = len(word_list)
word_list.reverse()
position_rev_word = word_list.index(word)
position_word = lenght_word - position_rev_word - 1

print(position_num)
print(position_word)





#num_list_rev1.index(number)
#print(num_list_rev1.index(number))


#num_str = ''.join(str(num_list))
#num_str_replaced = num_str.replace('[','').replace(']','')

#print(num_str_replaced)
#print(num_str_replaced.count(number))

#print(num_list.index(int(number)))
#print(word_list.index(word))

