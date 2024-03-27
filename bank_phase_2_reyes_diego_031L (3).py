#!/bin/python3

# Repeated symbol count for header messages
BORDER_CNT = 25

# Menu options
DEPOSIT_FUNDS = "1"
WITHDRAW_FUNDS = "2"
VIEW_BALANCE = "3"
CLOSE_ACCOUNT = "4"

print(
    "\n" + ("*" * BORDER_CNT) + "\n" + "Welcome to Banco Popular!\n" + ("*" * BORDER_CNT)
)

#
# Setup Account
#
print("\n" + ("-" * BORDER_CNT) + "\nAccount Setup\n" + ("-" * BORDER_CNT) + "\n")
name = input("Account name: ")

# Example of how to round a number:
x = True       #Condition remains true until the user inputs a valid response
while x == True:
 try:
     balance = input("Starting balance: $")
     _float = float(balance)     #float conversion in order to compare value againt the original string value
     if _float <= 0: #screen negative and empty balances, restarts loop
         continue
     _int = int(_float) #converts float to int in order to compare against the original string input, in order to allow inputs with no decinal places in their notation
     if balance == f'{_float:.2f}' or balance == str(_int): #Checks whether the string value is expressed to two decimal places, also checks for inputs with no decimal places in order stop te loop
         balance = round(_float,2) #Once the loop is closing, thhis line assigns the value for balance in order to use as a float for the remainder of the script.
         x = False #closes loop
     else:
         continue #restart, invalid floats
 except ValueError:
     continue #restart, invalid types




# Example of how to print variables more conveniently using formatted strings with multiple lines:
print(
    "\nWelcome new account member!\n"
    f"Account {name} created with starting balance: ${balance:.2f}"
)

#
# Main Account Menu
#
choice=True #placeholder choice value in order to initiate loop sequence, will be reasigned later
#accumulating values
deposits=0
withdrawals=0
penalties=0
withdrawn_amount=0
#stores initial balance
initial_balance=balance
# Example of how to show a multiline menu:
#checks for the account closing input for termination, also checks balance to provide closing option
while (choice !='4' or balance<0) and initial_balance>0:
 if balance>=0:
  choice = input(
    "\nSelect option:\n"
    "(1) Deposit funds\n"
    "(2) Withdraw funds\n"
    "(3) View bank account balance\n"
    "(4) Close account\n"
  )
 else: #negative balance menu
     choice = input(
         "\nSelect option:\n"
         "(1) Deposit funds\n"
         "(2) Withdraw funds\n"
         "(3) View bank account balance\n"
     )

# Conditional branching outcome=(1)
 if choice==DEPOSIT_FUNDS:
    print("\n" + ("-" * BORDER_CNT) + "\nDeposit Funds\n" + ("-" * BORDER_CNT) + "\n")
    #screening for valid deposit input, follow same principles as the previos try-except block
    try:
        amount_deposit = input('Amount to deposit: $')
        am_float = float(amount_deposit)
        am_int = int(am_float)
        if amount_deposit == f'{am_float:.2f}' or amount_deposit == str(am_int):
            amount_deposit = round(am_float,2)
        else:
            print('Transaction failed: Invalid deposit amount.	')
            continue

    except ValueError:
        print('Transaction failed: Invalid deposit amount.	')
        continue
    #Amount after deposit
    new_balance=round(balance + amount_deposit, 2)
    # Checks for 0 and negative values
    if amount_deposit>0:
        print(
            f'Account Name: {name}\n'
            f'Deposit Amount: ${amount_deposit:.2f}\n'
            f'New Balance: ${new_balance:.2f}'
        )
        #Add to deposit tally
        deposits+=1
        # Alters balance value outside of deposit instance
        balance+= amount_deposit
    # Invalid user input screening
    else:
        print('Transaction failed: Invalid deposit amount.')
# Conditional branching outcome=(2):Withdrawal
 elif choice==WITHDRAW_FUNDS:
    print("\n" + ("-" * BORDER_CNT) + "\nWithdraw Funds\n" + ("-" * BORDER_CNT) + "\n")
    # Value screener, same principles
    try:
        withdrawal = input('Amount to withdraw: $')
        w_float = float(withdrawal)
        w_int = int(w_float)
        if withdrawal == f'{w_float:.2f}' or withdrawal == str(w_int):
            withdrawal = round(w_float,2)
        else:
            print('Transaction failed: Invalid withdrawal amount.')
            continue
    except ValueError:
        print('Transaction failed: Invalid withdrawal amount.')
        continue
    #difference of balance and withdrawal
    new_balance = round(balance - withdrawal,2)
    #penalty accumulator
    penalty=0.
    # Non penalty input
    if 0 < withdrawal and new_balance >= -100:
        print(
            f'Account Name: {name}\n'
            f'Withdrawal Amount: ${withdrawal:.2f}\n'
            f'Penalties: ${penalty:.2f}\n'
            f'New Balance: ${new_balance:.2f}\n'
            f'Currency withdrawn:'
        )
        # Currency split
        _100 = int(withdrawal) // 100
        rem1 = int(withdrawal) % 100
        _50 = rem1 // 50
        rem2 = rem1 % 50
        _20 = rem2 // 20
        rem3 = rem2 % 20
        _10 = rem3 // 10
        rem4 = rem3 % 10
        _5 = rem4 // 5
        _1 = rem4 % 5
        cents = round(((withdrawal - int(withdrawal)) * 100))
        quarters = cents // 25
        crem1 = cents % 25
        dimes = crem1 // 10
        crem2 = crem1 % 10
        nickels = crem2 // 5
        pennies = crem2 % 5
        # Empty currency type screening
        if _100 > 0:
            print('$100s:', _100)
        if _50 > 0:
            print('$50s:', _50)
        if _20 > 0:
            print('$20s:', _20)
        if _10 > 0:
            print('$10s:', _10)
        if _5 > 0:
            print('$5s:', _5)
        if _1 > 0:
            print('$1s:', _1)
        if quarters > 0:
            print('quarters:', quarters)
        if dimes > 0:
            print('dimes:', dimes)
        if nickels > 0:
            print('nickels:', nickels)
        if pennies > 0:
            print('pennies:', pennies)
        #Accumulation
        withdrawals+=1
        balance-=withdrawal
    # 1% penalty input
    elif -1000 < new_balance < -100:
        penalty=withdrawal/100
        print(
            f'Withdrawal amount is greater than account balance. Overdraft penalty of 1% applied.\n'
            f'Account Name: {name}\n'
            f'Withdrawal Amount: ${withdrawal:.2f}\n'
            f'Penalties: ${penalty:.2f}\n'  
            f'New Balance: ${new_balance-penalty:.2f}\n'
            f'Currency withdrawn:'
        )
        _100 = int(withdrawal) // 100
        rem1 = int(withdrawal) % 100
        _50 = rem1 // 50
        rem2 = rem1 % 50
        _20 = rem2 // 20
        rem3 = rem2 % 20
        _10 = rem3 // 10
        rem4 = rem3 % 10
        _5 = rem4 // 5
        _1 = rem4 % 5
        cents = round(((withdrawal - int(withdrawal)) * 100))
        quarters = cents // 25
        crem1 = cents % 25
        dimes = crem1 // 10
        crem2 = crem1 % 10
        nickels = crem2 // 5
        pennies = crem2 % 5
        if _100 > 0:
            print('$100s:', _100)
        if _50 > 0:
            print('$50s:', _50)
        if _20 > 0:
            print('$20s:', _20)
        if _10 > 0:
            print('$10s:', _10)
        if _5 > 0:
            print('$5s:', _5)
        if _1 > 0:
            print('$1s:', _1)
        if quarters > 0:
            print('quarters:', quarters)
        if dimes > 0:
            print('dimes:', dimes)
        if nickels > 0:
            print('nickels:', nickels)
        if pennies > 0:
            print('pennies:', pennies)
        penalties+=1
        withdrawals+=1
        balance-=withdrawal+penalty
    # 3% penalty input
    elif-5000 < new_balance <= -1000:
        penalty = withdrawal*.03
        print(
            f'Withdrawal amount is greater than account balance. Overdraft penalty of 3% applied.\n'
            f'Account Name: {name}\n'
            f'Withdrawal Amount: ${withdrawal:.2f}\n'
            f'Penalties: ${penalty:.2f}\n'  
            f'New Balance: ${new_balance-penalty:.2f}\n'
            f'Currency withdrawn:'
        )
        _100 = int(withdrawal) // 100
        rem1 = int(withdrawal) % 100
        _50 = rem1 // 50
        rem2 = rem1 % 50
        _20 = rem2 // 20
        rem3 = rem2 % 20
        _10 = rem3 // 10
        rem4 = rem3 % 10
        _5 = rem4 // 5
        _1 = rem4 % 5
        cents = round(((withdrawal - int(withdrawal)) * 100))
        quarters = cents // 25
        crem1 = cents % 25
        dimes = crem1 // 10
        crem2 = crem1 % 10
        nickels = crem2 // 5
        pennies = crem2 % 5
        if _100 > 0:
            print('$100s:', _100)
        if _50 > 0:
            print('$50s:', _50)
        if _20 > 0:
            print('$20s:', _20)
        if _10 > 0:
            print('$10s:', _10)
        if _5 > 0:
            print('$5s:', _5)
        if _1 > 0:
            print('$1s:', _1)
        if quarters > 0:
            print('quarters:', quarters)
        if dimes > 0:
            print('dimes:', dimes)
        if nickels > 0:
            print('nickels:', nickels)
        if pennies > 0:
            print('pennies:', pennies)
        penalties+=1
        withdrawals+=1
        balance-=withdrawal+penalty
    # Input exceeds limit
    elif new_balance <= -5000:
        print('Transaction failed: withdrawal amount exceeds overdraft limit.')
    # Negative/invalid value screening
    else:
        print('Transaction failed: Invalid withdrawal amount.')
 elif choice == VIEW_BALANCE:
  print("\n" + ("-" * BORDER_CNT) + "\nAccount Balance\n" + ("-" * BORDER_CNT) + "\n"
          f'Account Name: {name}\n'
          f'Balance: ${balance:.2f}\n'
    )
# Conditional branching outcome=(3)
 elif choice == CLOSE_ACCOUNT:
    #Catches '4' input before its able to terminate loop when not allowed
    if balance<0:
        continue
    else:
        # Percentage delta operation
        percentage=((round(balance,2)-initial_balance)/initial_balance)*100
        #Formats positive percentages and 0 with '+'
        if percentage>=0:

            percentage_print=f'+{percentage:.2f}'
        #Assigns negative percentage to the same output variable as the >=0 percentages
        else:
            percentage_print = f'{percentage:.2f}'
        print("\n" + ("*" * BORDER_CNT) + "\nClosing Account\n" + ("*" * BORDER_CNT) + "\n" + "\n" +
              ("-" * BORDER_CNT) + "\nFinal Account Statement\n" + ("-" * BORDER_CNT) + "\n" )
        print(
            f'Account name: {name}\n'
            f'Initial balance: ${initial_balance:.2f}\n'
            f'Final balance: ${balance:.2f} ({percentage_print}%)\n'
            f'Deposit count: {deposits}\n'
            f'Withdrawal count: {withdrawals}\n'
            f'Overdraft penalty count: {penalties}'

        )
# Invalid user input screening
 else:
     continue





#
# Deposit
#

# TODO: Implement the logic for the deposit action here

#
# Withdrawal
#

# TODO: Implement the logic for the withdrawal action here

#
# View balance
#

# TODO: Implement the logic for the view balance action here

#
# Close account
#

# TODO: Implement the logic for the close account action here


print("\nThank you for banking with Banco Popular!")
