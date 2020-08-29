print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

hi = 100
low = 1
guess = (low + hi) // 2

while low <= hi:
    print(f"Is the number {guess}?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    if cmd == "h":
        hi = guess - 1
    elif cmd == "l":
        low = guess + 1
    elif cmd == "c":
        print("I AM VICTORIOUS")
        break
    elif cmd == "q":
        print("Quitter")
        break
    else:
        print(f"{cmd} is not among the recognized commands")
    guess = (low + hi) // 2

if hi < low:
    print("Tsk, tsk, don't try to cheat me")
