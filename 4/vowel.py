n=input("Enter the word :")
vo="aeiou"
for ch in n:
    if ch not in vo:
        continue
    print(ch)
    