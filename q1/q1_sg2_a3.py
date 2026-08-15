birthyear = int(input("Enter your birth year: "))
    
if birthyear < 1900:
    print("Invalid year. It should not be earlier than 1900.")
else:
    zodiac_num = (birthyear - 1900) % 12
    
    if zodiac_num == 0:
        print("Your Chinese Zodiac Sign is: Rat (鼠 / Shǔ)")                                           
    elif zodiac_num == 1:
        print("Your Chinese Zodiac Sign is: Ox (牛 / Niú)")
    elif zodiac_num == 2:
        print("Your Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")
    elif zodiac_num == 3:
        print("Your Chinese Zodiac Sign is: Rabbit (兔 / Tù)")
    elif zodiac_num == 4:
        print("Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
    elif zodiac_num == 5:
        print("Your Chinese Zodiac Sign is: Snake (蛇 / Shé)")
    elif zodiac_num == 6:
        print("Your Chinese Zodiac Sign is: Horse (马 / Mǎ)")
    elif zodiac_num == 7:
        print("Your Chinese Zodiac Sign is: Goat (羊 / Yáng)")
    elif zodiac_num == 8:
        print("Your Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
    elif zodiac_num == 9:
        print("Your Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
    elif zodiac_num == 10:
        print("Your Chinese Zodiac Sign is: Dog (狗 / Gǒu)")
    else:
        print("Your Chinese Zodiac Sign is: Pig (猪 / Zhū)")
    
