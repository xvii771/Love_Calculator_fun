# Greeting and taking names through input finction 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# fetching the strings and convering into a final score "fscr"
string1 = str.lower(name1) + str.lower(name2)
string1 = string1.replace(" ", "")
true_num = string1.count("t") + string1.count("r") + string1.count(
    "u") + string1.count("e")
love_num = string1.count("l") + string1.count("o") + string1.count(
    "v") + string1.count("e")
fscr = true_num*10 + love_num

#Formatting the output
if (fscr<10) and (fscr>90):
  print(f"Your score is {fscr}, you go together like coke and mentos. ")
elif (fscr<50) and (fscr>40):
  print(f"Your score is {fscr}, you are alright together.")
else:
  print(f"Your score is {fscr}, you both are made for each other..")
