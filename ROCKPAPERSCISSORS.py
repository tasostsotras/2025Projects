import random


print('To petra-psalidi-xarti paizetai os exis:\n'
      + "To xarti kerdaei tin petra. \n"
      + "I petra kerdaei to psalidi \n"
      + "To psalidi kerdaei to xarti \n")

while True:

    print("Vale tin epilogi sou \n 1 - Petra \n 2 - Xarti \n 3 - Psalidi \n")

   
    epilogi = int(input("Vale tin epilogi sou: "))

    # Elegxos orthis eisagogis
    while epilogi > 3 or epilogi < 1:
        epilogi = int(input('Vale egkyrh epilogh: '))

    
    if epilogi == 1:
        onoma = 'Petra'
    elif epilogi == 2:
        onoma = 'Xarti'
    else:
        onoma = 'Psalidi'

    
    print('O xristis epelexe', onoma)
    print("As doume ti epilegei o computer")

    
    epilogi_pc = random.randint(1, 3)

    
    if epilogi_pc == 1:
        comp_choice_name = 'Petra'
    elif epilogi_pc == 2:
        comp_choice_name = 'Xarti'
    else:
        comp_choice_name = 'Psalidi'

    print("Computer choice is:", comp_choice_name)
    print(onoma, 'vs', comp_choice_name)

    # Determine the winner
    if epilogi == epilogi_pc:
        result = "Isopalia"
    elif (epilogi == 1 and epilogi_pc == 2) or (epilogi_pc == 1 and epilogi == 2):
        result = 'Xarti'
    elif (epilogi == 1 and epilogi_pc == 3) or (epilogi_pc == 1 and epilogi == 3):
        result = 'Petra'
    elif (epilogi == 2 and epilogi_pc == 3) or (epilogi_pc == 2 and epilogi == 3):
        result = 'Psalidi'

    # Print the result
    if result == "Isopalia":
        print("<== ISOPALIA ==>")
    elif result == onoma:
        print("<== Kerdises esy ==>")
    else:
        print("<== Kerdise to pc ==>")

    # Ask if the user wants to play again
    print("Pame pali; (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

# After coming out of the while loop, print thanks for playing
print("Ela ton poulo")
