print (" Welcome to Tonia's LEC Estimator!")
print("Let's calculate your LEC units.")

my_cash = float(input("Enter how much money  you  have: "))
my_money_type = (input("Enter currency (USD or LRD)"))
usd_rate = float (input("Enter exchange rate (USD or LRD , enter 1 if LRD) : "))
price_per_kwh = float(input("Enter price for kWh (LRD) : "))
lec_charge = float(input("Enter LEC service charge (LRD) : "))

print("Thank you! You entered :")
print(" My cash :", my_cash, my_money_type)
print(" USD Rate :", usd_rate)
print(" Price per kWh :", price_per_kwh)
print(" LEC Charge :", lec_charge)

# part 1 - H0w many units will i get?
total_in_lrd = my_cash * usd_rate
cash_for_power = total_in_lrd - lec_charge
units_i_get = cash_for_power / price_per_kwh

print(" --- Your Result ---")
print(" Total in LRD  :", total_in_lrd)
print(" Cash left for units :", cash_for_power)
print(" You will get :", round  (units_i_get ,2 ),"kwh")

#part 2 - How much will i pay for units i want?
print(" --- Bill Estimator ---")
units_i_want = float(input(" How many kwh do you want? : "))
bill_in_lrd = units_i_want * price_per_kwh + lec_charge
bill_in_usd = bill_in_lrd / usd_rate

print(" To get :", units_i_want, " kwh" )
print(" You need to pay :", bill_in_lrd, "LRD")
print(" This is :", round (bill_in_usd, 2) ,"USD")

#part 3 Your unique feature - How many days will it last?
daily_kwh = float(input(" How many kwh do you use per day? :"))
days_it_will_last = units_i_want / daily_kwh
print(" Your:", units_i_want, "kwh will last you about ",round (days_it_will_last, 1) ,"days")
print("Thank you for using Tonia's LEC Estimator! ")




