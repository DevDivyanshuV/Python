# format specifiers


price1=45.816
price2=-4864.46
price3=116515312.4651351

print(f"1. Price1 is ₹ {price1:.2f}")          # 2 decimal places
print(f"2. price2 is ₹ {price2:12}")           # 12 space store the value
print(f"3. price2 is ₹ {price2:012}")          # 12 space store the value with 0 padded
print(f"4. price2 is ₹ {price2:>12}")          # 12 space store the value rightward align
print(f"5. price2 is ₹ {price2:<12}")          # 12 space store the value leftward align
print(f"6. price1 is ₹ {price1:^12}")          # 12 space store the value centerly aligned
print(f"7. price3 is ₹ {price3:+}")            # positive signs before the value
print(f"8. price2 is ₹ {price2:+}")            
print(f"9. price1 is ₹ {price1: }")            
print(f"10. price2 is ₹ {price2: }")
print(f"11. price3 is ₹ {price3:+,.3f}")    # combination of flags