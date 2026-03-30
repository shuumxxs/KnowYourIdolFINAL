import json

try:
    filename = "q.json"
    with open(filename, 'r') as file:
        data = json.load(file)

    def menu():
        print("[0] START!")
        print("[1] INSTRUCTIONS!")
        print("[2] EXIT!")


    exo_pts = 0
    njz_pts = 0
    twc_pts = 0

    plv_pts = 0
    lsf_pts = 0
    tvq_pts = 0

    enh_pts = 0
    skz_pts = 0
    mtx_pts = 0


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

        ans = int(input("\nYour choice? (strings will end the program!) : "))
    
        while True:
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

            elif ans != int:
                print("\nNot a valid input!")
                ans = input("Your choice? ").upper()

            else:
                print("\nNot a valid input!")
                ans = input("Your choice? ").upper()


    def c1():
        print("words")


    print("*^-+" * 5)
    print("\n\nWelcome to Know your Idol! \n(Press Enter to continue.)")
    silly = input(": 3 ")
    print(silly)
    print("*^-+" * 5)



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

























except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
