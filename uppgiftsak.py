poäng = input("Vad fick du för poäng? ")
poäng = int(poäng)

if poäng >= 25 and poäng <= 30:
    print(f"Du fick {poäng} poäng, vilket är betyget E.")

elif poäng >= 30 and poäng <= 35:
    print(f"Du fick {poäng} poäng, vilket är betyget D.")
elif poäng >= 35 and poäng <=40:
    print(f"Du fick {poäng} poäng, vilket är betyget C.")
elif poäng >= 40 and poäng <=49:
    print(f"Du fick {poäng} poäng, vilket är betyget A.")
elif poäng == 50:
    print(f"Du fick {poäng} poäng, vilket är max poäng!")