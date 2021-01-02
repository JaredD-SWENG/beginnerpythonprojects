#3.22.2018
#Stock Trading Tool 2.0.0

'''Pseudocode: The program is designed to help the user with trading on the stock market. It does this by determining the appropriate selling price based on the user's
expences and how much money the user wants to earn. It first aks the user how many stocks do they want to process, if the answer is more than one the program will
reapet the following steps for each stock: asking the user for the cost per trade, number of trades done on the stock, and the price paid for the stock
to determine the user's expences on the stock; asking the user for how much money they would like to make on the stock. Finally the program displays
the best selling price for the stock.'''

numStocks = int(input("Number of stocks being proccesed: "))
print('\n')

def Sell_Price(current_amount_of_shares, trades_done, price_paid, money_wanted):
    '''(int, int, float, float) -> float

    Returns the appropriate selling price for a stock's shares when given the cost, amount of money wanted, number of trades done, price paid, and number of shares. 
    '''
    total_money_needed = (trades_done*cost) + money_wanted
    extra_price_per_stock = total_money_needed/current_amount_of_shares
    sell_price = extra_price_per_stock + price_paid
    return sell_price

cost = int(input("Cost per trade: "))
print('\n')

for stocks in range(1, numStocks+1):
    Current_Amount_Of_Shares = int(input("Current amount of shares on Stock "+str(stocks)+": "))
    Trades_Done = int(input("Number of trades done on Stock "+str(stocks)+": "))
    Price_Paid = float(input("Price paid for Stock "+str(stocks)+": "))
    Money_Wanted = float(input("Cash wanted on Stock "+str(stocks)+": "))
                
    print('Trade Stock '+str(stocks)+"'s shares at $"+str(Sell_Price(Current_Amount_Of_Shares, Trades_Done, Price_Paid, Money_Wanted)))
    print('\n')
