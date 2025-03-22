from datetime import datetime
subtotal = float(input("Please enter the subtotal:"))


#Call now() method to get date and time from operating system
current_date_and_time = datetime.now()
#Call the weekday()method to get the day of the week
#from the current_date_and_time object. 
day_of_the_week = current_date_and_time.weekday()
#store day of the week and give discount if applicable

if (day_of_the_week == 1 or day_of_the_week == 2) and subtotal >= 50:
    discount = subtotal*(10/100)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount
taxes = subtotal * (6/100)
total = subtotal + taxes
print(f'Sales tax amount: {taxes:.2f}')
print(f'Total: {total:.2f}')

