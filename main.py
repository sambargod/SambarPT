
import openai
import time

# Use Your API Key HERE!
openai.api_key = "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"

print("""<----Welcome to SambarPT---->
prefix !! to edit model parameters
prefix && to change output options

""")

m = "text-davinci-003"
t = 1
tok = 3_000
top = 0.5
fp = 0
pp = 0

# mode 1, 2, 3, 4= console output mode, txt, html, python
mode = 1

while True:
    p = str(input("[Sambar]: "))
    if p[0:2] == "!!":
        if p == "!!":
            print('''<---Model Parameter Options--->
      !!1. View Current Settings
      !!2. Edit Parameters
      ''')
        elif p == "!!1":
            print(
                f"Current Parameters:\n"
                f"Model:\t\t{m}\n"
                f"Temperature:\t\t{t}\n"
                f"Max Tokens:\t\t{tok}\n"
                f"Top P:\t\t{top}\n"
                f"Frequency Penalty:\t\t{fp}\n"
                f"Presence Penalty:\t\t{pp}\n\n"

            )
            pass
        elif p == "!!2":
            selection = input(
                f"\nWhich Parameter would you like to edit?\n"
                f"1. Model:\n"
                f"2. Temperature:\n"
                f"3. Max Tokens:\n"
                f"4. Top P:\n"
                f"5. Frequency Penalty:\n"
                f"6. Presence Penalty:\n"
            )
            if not selection.isdigit():
                print("Invalid!")
            elif selection == "1":
                new_val = input("Enter new value")
                m = new_val
            elif selection == "2":
                new_val = input("Enter new value")
                if not new_val.isdigit():
                    print("Invalid!")
                else:
                    t = float(new_val)
            elif selection == "3":
                new_val = input("Enter new value")
                if not new_val.isdigit():
                    print("Invalid!")
                else:
                    tok = int(new_val)
            elif selection == "4":
                new_val = input("Enter new value")
                if not new_val.isdigit():
                    print("Invalid!")
                else:
                    top = float(new_val)
            elif selection == "5":
                new_val = input("Enter new value")
                if not new_val.isdigit():
                    print("Invalid!")
                else:
                    fp = float(new_val)
            elif selection == "6":
                new_val = input("Enter new value")
                if not new_val.isdigit():
                    print("Invalid!")
                else:
                    pp = float(new_val)
    elif p[0:2] == "&&":
        if p == "&&":
            print(''' <---Output Options--->
      &&1. Console Output Mode
      &&2. Text File
      &&3. HTML File
      &&4. Python File
      ''')
        elif p == "&&1":
            mode = 0
        elif p == "&&2":
            mode = 1
        elif p == "&&3":
            mode = 2
        elif p == "&&4":
            mode = 3
    else:

        response = openai.Completion.create(
            model=m,
            prompt=p,
            temperature=t,
            max_tokens=tok,
            top_p=top,
            frequency_penalty=fp,
            presence_penalty=pp
        )
        # print(mode)
        if mode == 1:
            print(response["choices"][0]["text"], '\n')
        elif mode ==2:
            pass
        elif mode == 3:
            pass
        else:
            pass
