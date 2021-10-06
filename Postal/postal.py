# Решение задачи для вычисления кратчайшего пути для почтальона для курса "Основы Python" от Y_Lab
# заданы координаты точек
post_office = (0, 2)
griboedov_street = (2, 5)
baker_street = (5, 2)
bolshaya_sadovaya_street = (6, 6)
evergreen_alley = (8, 3)

# создается словарь из переменных этих координат, который в дальнейшем будет использоваться в вычислениях
value_dict = {}

def create_dict(**kwargs):
    for key, value in kwargs.items():
        value_dict[key]=value           

create_dict(post_office=post_office, griboedov_street=griboedov_street, baker_street=baker_street,bolshaya_sadovaya_street=bolshaya_sadovaya_street,evergreen_alley=evergreen_alley)

# в этой функции вычисляется первый шаг
def first_step_forward(val):
    list_keys = []
    list_values = []
    result_list = []
    for key, value in val.items():
        list_keys.append(key)
        list_values.append(value)
    for n in range(len(list_values)-1,-1,-1):
        result_list.append(((list_values[n][0] - list_values[0][0]) ** 2 + (list_values[n][1] - list_values[0][1]) ** 2) ** 0.5)
    final_dict=dict(zip(list_keys,list(reversed(result_list))))
    sorted_final_dict = {}
    sorted_final_dict_keys = sorted(final_dict, key=final_dict.get)
    for w in sorted_final_dict_keys:
        sorted_final_dict[w] = final_dict[w]
    first_key = list_keys[0]
    del(sorted_final_dict[first_key])
    return sorted_final_dict
first_step_forward(value_dict)

# записывается результат в переменную для первого шага
first_step_dict = first_step_forward(value_dict)

# функция для вычисления последующих шагов вперед к другим точкам.
def another_step_forward(val, value_dict):
    var_dict_1 = value_dict
    del_key=""
    for i in var_dict_1:
        if i not in val:
            del_key = i
    del(var_dict_1[del_key])
    new_var_dict_1 = {}
    sorted_var_dict_1 = sorted(var_dict_1, key=val.get)
    for k in sorted_var_dict_1:
        new_var_dict_1[k] = var_dict_1[k]
    list_keys = []
    list_values = []
    result_list = []
    for key, value in new_var_dict_1.items():
        list_keys.append(key)
        list_values.append(value)
    for n in range(len(list_values)-1,-1,-1):
        result_list.append(((list_values[n][0] - list_values[0][0]) ** 2 + (list_values[n][1] - list_values[0][1]) ** 2) ** 0.5)
    final_dict = dict(zip(list_keys,list(reversed(result_list))))
    sorted_final_dict = {}
    sorted_final_dict_keys = sorted(final_dict, key=final_dict.get)
    for w in sorted_final_dict_keys:
        sorted_final_dict[w] = final_dict[w]
    first_key = list_keys[0]
    del(sorted_final_dict[first_key])
    return sorted_final_dict
# используя функцию выше получаем значения для последующих шагов к другим точкам
second_step_dict = another_step_forward(first_step_dict,value_dict)
third_step_dict = another_step_forward(second_step_dict,value_dict)
fourth_step_dict = another_step_forward(third_step_dict,value_dict)
#функция для вычисления пути из последней точки маршрута к стартовой: Почтовое отделение – (0, 2)
def step_backward(val, value_dict):
    # снова запускается функция по созданию словаря с координатами точек
    create_dict(post_office=post_office, griboedov_street=griboedov_street, baker_street=baker_street,bolshaya_sadovaya_street=bolshaya_sadovaya_street,evergreen_alley=evergreen_alley)
    var_dict_1 = {} 
    for n in val:
        var_dict_1[n] = val[n]
    var_dict_2 = value_dict
    for w in var_dict_2:
        var_dict_1[w] = var_dict_2[w]
    list_keys = []
    list_values = []
    result_list = []
    for key, value in var_dict_1.items():
        list_keys.append(key)
        list_values.append(value)
    for n in range(len(list_values)-1,-1,-1):
        result_list.append(((list_values[n][0] - list_values[0][0]) ** 2 + (list_values[n][1] - list_values[0][1]) ** 2) ** 0.5)
    final_dict = dict(zip(list_keys,list(reversed(result_list))))
    start_point = {'post_office':0}
    for k in final_dict:
        if k in start_point:
            start_point[k] = final_dict[k]
    return start_point

# записываем возврат к стартовой точке в переменную.
last_backward_step_dict = step_backward(fourth_step_dict, value_dict)
# функция для оформления всего пути в соотвествии с ТЗ
def show_result():
    txt_result = "(0, 2)"
    result_sum = 0
    list_steps = [first_step_dict, second_step_dict, third_step_dict, fourth_step_dict, last_backward_step_dict]
    for i in list_steps:
        keys_step_lst = list(i.keys())
        values_step_lst  = list(i.values())
        for key, value in value_dict.items():
            if keys_step_lst[0] == key:
                result_sum += values_step_lst[0]
                txt_result += " -> " + str(value) + "[" + str(result_sum) + "]"
    txt_result += " = " + str(result_sum)           
    return txt_result
# записываем результат и отображаем его
result = show_result()
print(result)

