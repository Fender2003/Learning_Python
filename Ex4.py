good_credit=True
Price=1000000
if good_credit:
    Price=0.1*Price

else:
    Price=0.2*Price

print(f"Down Payment is ${Price}")