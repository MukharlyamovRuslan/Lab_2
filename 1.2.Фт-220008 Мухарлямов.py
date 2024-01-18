name = input('Введите ваше имя: ')
age = input('Введите ваш возраст: ')
country = input('Введите страну проживания: ')
city = input('Введите город проживания: ')
year = str(2023 - int(age))

print('\nУважаемый ' + str(name) + '!\n')
print('На сегодняшний день Вы проживаете в стране ' +
      str(country) + ',\nв городе ' + str(city) +
      ',\nи вы родились в ' + year + '.')