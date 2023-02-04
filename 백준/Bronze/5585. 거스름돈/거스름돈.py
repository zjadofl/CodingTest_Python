thing = int(input())
remains = 1000 - thing
money_units = [500, 100, 50, 10, 5, 1]

quotient = 0
for money_unit in money_units:
    if remains >= money_unit:
        quotient += remains // money_unit
        remains = remains % money_unit
print(quotient)