import json

#Open the JSON file that contains the quiz questions & answers for each group
try:
    filename = "q.json"
    with open(filename, 'r') as file:
        data = json.load(file)

#Display the options menu for the user to choose
    def menu():
        print("[0] START!")
        print("[1] INSTRUCTIONS!")
        print("[2] EXIT!")

#Score counter for each group quiz 
    exo_pts = 0
    njz_pts = 0
    twc_pts = 0

    plv_pts = 0
    lsf_pts = 0
    tvq_pts = 0

    enh_pts = 0
    skz_pts = 0
    mtx_pts = 0


#Main quiz game function
    def c0():
        global exo_pts
        global njz_pts
        global twc_pts
        global plv_pts
        global lsf_pts
        global tvq_pts
        global enh_pts
        global skz_pts
        global mtx_pts
        print()
        print("CHOOSE A GROUP!")
        print()
        print()
        print("[1] EXO")
        print()
        print("[2] NEWJEANS")
        print()
        print("[3] TWICE")
        print()
        print("[4] PLAVE")
        print()
        print("[5] LE SSERAFIM")
        print()
        print("[6] TVXQ!")
        print()
        print("[7] ENHYPEN")
        print()
        print("[8] STRAY KIDS")
        print()
        print("[9] MONSTA X")
        print()

#Get user k-pop group choice
        ans = int(input("\nYour choice? (strings will end the program!) : "))

#Code for the quiz group questions and answer gameplay
        while True:
        #Quiz for EXO
            if ans == 1:

                for q in data:
                    if q["group"] == "exo":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()
                        while True:
                            if ans == q["correct"]:
                                exo_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            elif ans != str:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {exo_pts}/5!")
                break

                            
            elif ans == 2:
                #Quiz for NEWJEANS
                for q in data:
                    if q["group"] == "njz":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()
                        while True:
                            if ans == q["correct"]:
                                njz_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            elif ans != str:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {njz_pts}/5!")
                break



            elif ans == 3:
                #Quiz for TWICE 
                for q in data:
                    if q["group"] == "twc":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()
                        while True:
                            if ans == q["correct"]:
                                twc_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            elif ans != str:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {twc_pts}/5!")
                break


            elif ans == 4:
                #Quiz for PLAVE
                for q in data:
                    if q["group"] == "plv":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()

                        while True:
                            if ans == q["correct"]:
                                plv_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            elif ans != str:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {plv_pts}/5!")
                break



            elif ans == 5:
                #Quiz for LE SSERAFIM 
                for q in data:
                    if q["group"] == "lsf":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()
                        while True:
                            if ans == q["correct"]:
                                lsf_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            elif ans != str:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {lsf_pts}/5!")
                break

            elif ans == 6:
                #Quiz for TVXQ!
                for q in data:
                    if q["group"] == "tvq":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()
                        while True:
                            if ans == q["correct"]:
                                tvq_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            elif ans != str:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {tvq_pts}/5!")
                break

            elif ans == 7:
                #Quiz for ENHYPEN 
                for q in data:
                    if q["group"] == "enh":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()
                        while True:
                            if ans == q["correct"]:
                                enh_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            elif ans != str:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {enh_pts}/5!")
                break

            elif ans == 8:
                #Quiz for STRAY KIDS
                for q in data:
                    if q["group"] == "skz":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()
                        while True:
                            if ans == q["correct"]:
                                skz_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            elif ans != str:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {skz_pts}/5!")
                break

            elif ans == 9:
                #Quiz for MONSTA X
                for q in data:
                    if q["group"] == "mtx":
                        print(q["q"])
                        print(f"[A] {q["A"]}")
                        print(f"[B] {q["B"]}")
                        print(f"[C] {q["C"]}")
                        print(f"[D] {q["D"]}")
                        ans = input("Your choice? ").upper()
                        while True:
                            if ans == q["correct"]:
                                mtx_pts += 1
                                print("\nCorrect!")
                                break
                            elif ans != q["correct"]:
                                print("\nIncorrect!")
                                break
                            else:
                                print("\nNot a valid input!")
                                ans = input("Your choice? ").upper()
                print(f"\n                Score: {mtx_pts}/5!")
                break

#Checking in case of invalid user inputs
            elif ans != int:
                print("\nNot a valid input!")
                ans = input("Your choice? ").upper()

            else:
                print("\nNot a valid input!")
                ans = input("Your choice? ").upper()

#Show the instructions for the quiz game
    def c1():
        print(" ")
        print("INSTRUCTIONS")
        print("*^-+" * 5)
        print(" ")
        print("Guidelines")
        print("*^-+" * 5)
        print(" ")
        print("1.Always pick from only the numbered choices, for example is if the choices are from the numbers 1-9,")
        print("  avoid picking number like 0, 10 and so on.")
        print("2.Refrain from putting malicious inputs like swear words, racist jokes and so on.")
        print("3.When playing alongside friends, always to remember that it's just a quiz game, NOT WW3.")
        print("4.Don't use strings for integer input or else the game goes BOOM!")
        print("5.And lastly, don't forget to HAVE FUN!!")
        print(" ")
        print("How to Play")
        print("*^-+" * 5)
        print(" ")
        print("1. Once you start the game, you will be shown 9 choices of the creators' favourite k-pop groups")
        print("2. When you choose a group, you'll be given 5 questions that will show how well you know your k-pop idol.")
        print("3. After that, the points will be tallied and displayed in the ?/5 format. ")
        print("4. In the end it will bring you back to the menu and let you repeat the process or just leave. ")
        print("BONUS: It's always better if you play it with the people that make you laugh, so invite your friends to play too!")
        print(" ")

#Quiz game welcome screen 
    print("*^-+" * 5)
    print("\n\nWelcome to Know your Idol! \n(Press Enter to continue.)")
    silly = input(": 3 ")
    print(silly)
    print("*^-+" * 5)


#Main quiz game loop
    while True:
        menu()

        ans = int(input("\nYour choice? (strings will end the program!): "))

        if ans == 0:
            c0()
        elif ans == 1:
            c1()
        elif ans == 2:
            print("are you sure? y/n")
            leave = str(input("your choice : ")).lower()
            while True:

                if leave == "y":
                    print("Awh man!! okay..")
                    break
                elif leave == "n":
                    print("oh, nevermind!")
                else:
                    print("invalid input :,(")
                    leave = input("your choice:")


        else:
            print("\nNot a valid input!")
            ans = int(input("Your choice? : "))
























#Raised if in case of any JSON file errors
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
