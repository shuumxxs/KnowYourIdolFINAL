import json

try:
    filename = "questions.json"
    with open(filename, 'r') as file:
        data = json.load(file)

    def menu():
        print("[0] START!")
        print("[1] INSTRUCTIONS!")
        print("[2] CREDITS!")
        print("[3] EXIT!")


    def c0():
        global exo_pts
        global njz_pts
        global twc_pts
        global plv_pts
        global lsf_pts
        global tvq_pts
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
        print("[7] WIP")
        print()
        print("[8] WIP")
        print()
        print("[9] WIP")
        print()

        ans = int(input("\nYour choice? : "))
    
        while True:
            if ans == 1:

                for q in data:
                    if q["group"] == "":
                        print(q[""])
                        print(q[""])
                        print(q[""])
                        print(q[""])
                        ans = input("Your choice?").upper()
                        if ans == q["correct"]:
                            _pts =+ 1
                    
                
            elif ans == 2:
                
            elif ans == 3:
                
            elif ans == 4:

            elif ans == 5:

            elif ans == 6:

    exo_pts = 0
    njz_pts = 0
    twc_pts = 0


    plv_pts = 0
    lsf_pts = 0
    tvq_pts = 0

    print("✧･ﾟ: *✧･ﾟ:*:･ﾟ✧*:･ﾟ✧" * 5)
    print("\n\nWelcome to Know your Idol! \n(Press Enter to continue.)")
    silly = input(print("\n\n : 3 "))
    print("✧･ﾟ: *✧･ﾟ:*:･ﾟ✧*:･ﾟ✧" * 5)
    print("\n\n ")


    menu()

    ans = int(input("\nYour choice? : "))

    while True:
        if ans == 0:
            c0()
        elif ans == 1:
            c1()
        elif ans == 2:
            c2()
        elif ans == 3:
            print("are you sure? y/n : ")
            while True:
                leave = str(input("your choice:"))
                if leave == "y":
                    print("Awh man!! okay..")
                    break
                elif leave == "n":
                    print("oh, nevermind!")
                else:
                    print("invalid input :,(")
                break

        else:
            print("invalid input.")
            print("")
        start_menu()
        ans = int(input("Your choice? "))

























except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
