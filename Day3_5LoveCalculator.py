print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

my_name = name1.lower()
his_name = name2.lower()
t_occurs = my_name.count("t") + his_name.count("t")
r_occurs = my_name.count("r") + his_name.count("r")
u_occurs = my_name.count("u") + his_name.count("u")
e_occurs = my_name.count("e") + his_name.count("e")
l_occurs = my_name.count("l") + his_name.count("l")
o_occurs = my_name.count("o") + his_name.count("o")
v_occurs = my_name.count("v") + his_name.count("v")
e_occurs_again = my_name.count("e") + his_name.count("e")

true_total = t_occurs + r_occurs + u_occurs + e_occurs
love_total = l_occurs + o_occurs + v_occurs + e_occurs_again

total = str(true_total) + str(love_total)
int_total = int(total)
if int_total < 10 or int_total > 90:
  print(f"Your score is {int_total}, you go together like coke and mentos.")
elif 40 < int_total < 50:
  print(f"Your score is {int_total}, you are alright together.")
else:
  print(f"Your score is {int_total}.")
