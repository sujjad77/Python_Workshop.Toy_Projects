def calc(amt,quality,num):
    tip = (amt*quality)/num
    return tip


billed_amount = int(input("Enter the total billed amount: "))
service_quality = (int(input("Rate the service quality in percentage: "))/100)
num_people = int(input("Enter the number of people who enjoyed the service: "))

total_tip = calc(billed_amount,service_quality,num_people)

print("The tip that needs to be provided is :{}".format(total_tip))