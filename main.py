def greeting (name):
    print('hello'+ name.title()+'!')

    def greeting_2(name):
        print('hello {}!'.format(name.title()))
        print(f'helllo again{name.title()}!')
    
    greeting_2('Joel')



#python program to print first 100 odd numbers
start, end = 0, 101
#iterate each number in list
for num in range (start, end + 1):
#checking conditions
    if num % 2 != 0:
 # print(num, end = " ")




def max_num_in_list(a_list):
     max = a_list[0]
     #compare each number in list with max value.
     #largest number is then assigned value of "max"
     for x in a_list:
         if x > max:
             max = x
     #after going the list, return max value
     return max

#test code
a_list = [5,8,10,9,11]
print("largest integer is:", max_num_in_list(a_list))




def is_leap_year(a_year):
    if (a_year % 4 ==0) and (a_year % 100 != 0)  or (a_year % 400 == 0):
        return True
    else:
        return False
    return is_leap_year

#test code
a_year = 2004
if (is_leap_year(a_year)):
    print("true is a leap year")
else:
    print("false not a leap year")


def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

is_consecutive([1,2,3,4,5])

def welcome(marvel_character):
    print(f'Welcom to {marvel_character} Vision')

welcome('Wanda')