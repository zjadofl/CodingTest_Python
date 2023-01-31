a, b = input().split()
convert_five_a = int(a.replace('6', '5'))
convert_five_b = int(b.replace('6', '5'))
convert_six_a = int(a.replace('5', '6'))
convert_six_b = int(b.replace('5', '6'))

print(convert_five_a + convert_five_b, 
      convert_six_a + convert_six_b, end=' ')