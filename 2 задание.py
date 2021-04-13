my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

new_list = []
for idx, elem in enumerate(my_list):
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem):02}', '"'])
    else:
        new_list.append(elem)

out_info = ' '.join(new_list)
print(out_info)

#трудное задание. я понимаю код , но не понимаю как написать подобное или проще. Получается либо у меня не берется последнее число
#либо выдает ошибку. А сдавать задание с двумя заданиями не очень. 4 задание и то проще в понимание чем 2 