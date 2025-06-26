print('Welcome to Wura Bank!')
Pin = int(input('Enter your  4-digit pin here: '))
if Pin == 1234:
    print('Login successful!')
else:
    print('Invalid login details!')
    exit()
    
balance= 10000

while True:
    print('----Menu----')
    print('1. Check balance')
    print('2. Withdraw money')
    print('3. Deposit money')
    print('4. Exit')

    choice= int(input('Choose an option from (1-4): '))
    if choice == 1:
     print(f'Your balance is #{balance}')
    elif choice== 2:
       amount= int(input('Enter the amount you want to withdraw here: '))
       if amount <= balance:
          balance -= amount
          print(f'transaction is successful! New balance: #{balance}')
       else:
          print('Insufficient funds.')
    elif choice == 3:
       amount= int(input('Enter amount to deposit here: '))
       balance += amount 
       print(f'Deposit succesful! New balance: #{balance}')
    elif choice == 4:
       print('Thank you for banking with Wura Bank!')
       break
    else:
       print('Invalid option. Please choose (1-4)')
