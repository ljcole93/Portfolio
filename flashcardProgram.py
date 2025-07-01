# Logan Cole ljcole93
# COP2002.0M1
# 26Apr25
# Project Part 2
# A program that uses arrays and functions to quiz a user on port numbers and protocols.

import random

# Quiz 1 function: given a port number, identify a protocol

def quiz1(quiz1_list):

    # Printing header for quiz 1
    print("\nQuiz 1: Identify the port's PROTOCOL.")
    print("-" * 40)

    continueQuiz = True
    # While loop that prompts user for protocol based on random port
    while continueQuiz:
        port, protocol = random.choice(quiz1_list)                                 # Randomly selects from list
        prompt = f"What is the protocol for port {port} (m=Main Menu)?  "   # Prompts the user for an answer
        userInput = input(prompt).strip()                                   # Receives user input and removes whitespace

        # If loop to allow user to return to main menu and compare user input to stored value
        if userInput == "m":
            continueQuiz = False
        else:
            if userInput == protocol:
                print("Correct Answer!")
            else:
                print(f"Incorrect. The correct answer is {protocol}")

# Quiz 2 function: given a protocol, identify valid port numbers

def quiz2(quiz2_list):

    # Printing header for quiz 2
    print("\nQuiz 2: Identify the protocol's NUMBER")
    print("-" * 40)

    continueQuiz = True
    # While loop that prompts user for port based on random protocol
    while continueQuiz:
        protocol, ports = random.choice(quiz2_list)                                        # Randomly selects from list
        prompt = f"What is the number for protocol {protocol} (m=Main Menu)?  "     # Prompts the user for an answer
        userInput = input(prompt).strip()                                           # Receives user input and removes whitespace

        # If loop to allow user to return to main menu and compare user input to stored value
        if userInput == "m":
            continueQuiz = False

        # The rest of this loop determines if the user input matches stored data and, in the case of a wrong answer, will check 
        # To see how many valid ports exist for that item.
        else:
            if userInput in ports:
                print("Correct Answer!")
            else:
                if len(ports) == 1:
                    print(f"Incorrect. The correct answer is {ports[0]}")               
                else:
                    answer = "Incorrect. The correct answers are: "
                    for x in ports:
                        answer += x + " "
                    print(answer)

# Main function, displays the main menu for the user and navigates between quizzes. 

def main():

# Quiz 1 array with each tuple listed as (port, protocol) as (integer, string) and passed into quiz1

    quiz1_list = [
    (20, "FTP"),
    (21, "FTP"),
    (22, "SSH"),
    (23, "Telnet"),
    (25, "SMTP"),
    (53, "DNS"),
    (67, "DHCP"),
    (68, "DHCP"),
    (80, "HTTP"),
    (110, "POP3"),
    (137, "NetBIOS"),
    (139, "NetBIOS"),
    (143, "IMAP"),
    (161, "SNMP"),
    (162, "SNMP"),
    (389, "LDAP"),
    (443, "HTTPS"),
    (445, "SMB"),
    (3389, "RDP")
]

# Quiz 2 array with each tuple listed as (protocol, port) as (string, list of integers) and passed into quiz2

    quiz2_list = [
    ("FTP", ["20", "21"]),
    ("SSH", ["22"]),
    ("TELNET", ["23"]),
    ("SMTP", ["25"]),
    ("DNS", ["53"]),
    ("DHCP", ["67", "68"]),
    ("HTTP", ["80"]),
    ("POP3", ["110"]),
    ("NetBIOS", ["137", "139"]),
    ("IMAP", ["143"]),
    ("SNMP", ["161", "162"]),
    ("LDAP", ["389"]),
    ("HTTPS", ["443"]),
    ("SMB", ["445"]),
    ("RDP", ["3389"])
]

    # Turning on the loop
    running = True
    while running:
        # Printing all of the menu options
        print("\nMain Menu:")
        print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
        print("2. Given a port protocol, identify a port NUMBER.")
        print("3. Exit\n")

        # Retrieving user input for menu choice and running the related function
        choice = input("Choice: ").strip()
        if choice == "1":
            quiz1(quiz1_list)
        elif choice == "2":
            quiz2(quiz2_list)
        elif choice == "3":
            print("\nProgram Complete. I hope this has helped in studying for the CompTIA A+ certification")  
            running = False # Exiting main loop
        else:
            print("Invalid option. Please choose 1, 2, or 3.") 

if __name__ == "__main__":
        main()
    