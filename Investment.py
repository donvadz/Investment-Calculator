def investment(Years):
    total_return = 0
    
    
    while True:
        try:
            initial_investment = int(input('What is your initial investment? £'))
            break
        except:
            print('Invalid input! Try again.')

    while True:
        try:
            annual_return = int(input('What is your investments annual return? Answer as a percentage: '))
            break
        except:
            print('Invalid input! Try again.')         
    
    
    while True:
        yearly_investment = input('Do you wish to invest your initial investment annually? Answer Y or N or Yes or No: ')
        yearly_investment.lower()
        if yearly_investment == 'y' or yearly_investment == 'n' or yearly_investment == 'yes' or yearly_investment == 'no':
            print('Thanks for letting us know')
            break
        else:
            print('Please input the available options')
   
    
    
    
    
    
    if annual_return >= 0:
        annual_return = (annual_return/100) + 1
    else:
        annual_return = 1 - (annual_return/100)
    
    
    
    if yearly_investment == 'n' or yearly_investment == 'no':
        total_return = initial_investment * (annual_return ** Years)
        
        return 'The value of your fund will be £{:.2f} in {} years'.format(total_return, Years)    
    else:
        while True:
            increase_investment_yearly = input('Do you wish to increase your yearly investment? Answer Y or N or Yes or No: ')
            increase_investment_yearly.lower()
            if increase_investment_yearly == 'y' or increase_investment_yearly == 'n' or increase_investment_yearly == 'yes' or increase_investment_yearly == 'no':
                print('Thanks for letting us know')
                break
            else:
                print('Please input the available options')
        if increase_investment_yearly == 'n' or increase_investment_yearly == 'no':
            total_return = 0
            for year in range(Years):
                total_return = total_return + initial_investment
                total_return = total_return * annual_return
            return 'The value of your fund will be £{:.2f} in {} years'.format(total_return, Years)   
        else:
            while True:
                try:
                    investment_increase = int(input('How much do you want to increase your annual investment every year?: £'))
                    break
                except:
                    print('Invalid input! Try again.')
        
            yearly_investment = initial_investment
            total_return = 0
            for year in range(Years):
                total_return = total_return + yearly_investment
                total_return = total_return * annual_return
                yearly_investment = yearly_investment + investment_increase
            return 'The value of your fund will be £{:.2f} in {} years'.format(total_return, Years)       
