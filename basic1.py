product_name1 = "sugar"
product_name2 = "tee"
product_name3 = "book"
product_name4 = "pepar"
product_name5 = "pen"

quant1 = 2
quant2 = 5
quant3 = 8
quant4 = 9
quant5 = 12
price1 = 160
price2 = 2000
price3 = 3200
price4 = 50
price5 = 60
total_price1 = price1*quant1
total_price2 = price2*quant2
total_price3 = price3*quant3
total_price4 = price4*quant4
total_price5 = price5*quant5
discount = 10
total = total_price1 + total_price2 + total_price3 + total_price4 + total_price5
total_after_discount = total - (total*discount)/100
print("total product price is",total)
print("total 10% discount price is",total_after_discount)
