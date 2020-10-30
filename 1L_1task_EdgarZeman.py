numb_int = 0
string = ''
numb_float = 0.0
type_none = None
is_true = False
# что-нибудь поделаем с переменными)
string = input("Как Вас зовут? ")
numb_int = int(input("Сколько вам лет? "))
# по градации ВОЗ 90+ это долголетие
# узнаем является ли пользователь долгожителем
if numb_int >= 90:
    print('Вы долгожитель')
    is_true = True
else:
    print('Вам еще %d лет (года) до долголетия' %(90 - numb_int))
    numb_float = (numb_int / 90) * 100
    print('Или вы уже успели прожить %2.f процент возраста долголетия' %(numb_float))