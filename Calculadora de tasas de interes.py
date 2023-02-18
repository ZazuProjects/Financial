#!/usr/bin/env python
# coding: utf-8

# Where:
# A = the total payment amount (Principal + Interest)
# P = the principal amount
# r = the annual interest rate
# n = the number of times the interest is compounded per year
# t = the number of years

# In[110]:


#Debt / investment calculator by ZazuDev

import numpy_financial as npf
import numpy as np
from decimal import Decimal

# User inputs
principal = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the interest rate (as a decimal): "))
years = float(input("Enter the loan duration in years: "))
cap_period = int(input("Enter the number of months between capitalizations: "))



# Convert years to months for monthly calculations
n = 12 / cap_period
t = int(years*12 / cap_period)

tax_type= input("Is the interest rate compound (c) or simple (s)? ") #User input should be either c or s
if tax_type == 'c':
    
    amount = Decimal(int(principal)) * ((1 + Decimal(int(interest_rate)/n))**(Decimal(n*t))) #Decimal to avoid overflow, int to avoid numpy.int32 conversion error
    print("Initial value: $" + str(amount))
    
else:
    
    amount = principal * (1 + interest_rate* t)
    print("Initial value: $" + str(amount))

monthly_rate = interest_rate/12
loan_amount = principal
monthly_payment = (npf.pmt(monthly_rate, t, loan_amount)) * -1 
print("Monthly Installment Amount (Principal + Interest): $" + str(monthly_payment ))


per = np.arange(t) + 1


interest_paids = npf.ipmt(monthly_rate, per, t, loan_amount)
principal_paids = npf.ppmt(monthly_rate, per, t, loan_amount)



fmt1 = '{0:s} {1:s} {2:s} {3:s} '
fmt2 = '{0:2d} {1:12.2f} {2:15.2f} {3:15.2f} '
fmt3 = '{0:2d} {1:12.2f} {2:15.2f} {3:15.2f} '

fv = npf.fv(interest_rate,t,0,principal)    #npf.fv(rate=rate, nper=nper, pmt=pmt, pv=pv)
print("\033[1;31mFinal Value: ${:,.2f}\033[0m".format(fv*-1))

print("----"*10)

print("\033[1;31mTable for debts - does not apply for investments:\033[0m")

print(fmt1.format('Term', 'Principal Paid', 'Interest Paid', 'Remaining Principal'))
print(fmt2.format(0, 0, 0, loan_amount))

total_paid = 0


for n in per:
    i = n - 1
    principal = principal + principal_paids[i]
    interest_paid = interest_paids[i]
    principal_paid = principal_paids[i]
    print(fmt3.format(n, principal_paid, interest_paid, principal))
    


# In[ ]:





# In[ ]:





# In[108]:


a = 46 + 30000
a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[109]:


#simplified calculator

import numpy as np
principal = 30000
interest_rate = 0.02
t = 12 * 4

fv = principal * ((1 + interest_rate)**t)
print(fv)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




