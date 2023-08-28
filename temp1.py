print('c or f or e')
user_input = input()

if user_input == 'c':
    print('Degree in celcius:')
    user_degree = input('Degrees:')
    user_degree_int = int(user_degree)
    result = (user_degree_int * 9/5) + 32
    print('Result is:', result)

if user_input == 'f':
   print('calculating for fahrenheit')
   user_fah = input('fahrenheit: ')

if user_input == 'e' :
   print('Exit')