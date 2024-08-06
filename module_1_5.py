immutable_var=('string', 1, True, 4.5, None)
print(immutable_var)
#кортеж отлечается от списка тем, что он неизменяемый
mutable_list=['string', 1, True, 4.5, None]
mutable_list[0]= 'fafa'
print(mutable_list)
