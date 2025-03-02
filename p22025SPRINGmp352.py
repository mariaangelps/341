# Maria Angel Palacios Sarmiento
# mp352
# CS 341-002
# Spring 2024

# Printing Information 
def header_info_352():
    print("Project 1 for CS 341")
    print("Section number: 002")
    print("Semester: Spring 2024")
    print("Written by: Maria Angel Palacios Sarmiento, mp352")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu")

header_info_352()

class EmailDFA_352:
    def __init__(self):
        #stating states involved in the DFA
        self.states = {
            "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"
        }
        self.alphabet = {"psi", "pi", "phi"}  # 'psi' = letters, 'pi' = '.', 'phi' = '@'
        self.transitions = {
            "q0": {"psi": "q1", "pi": "q_trap", "phi": "q_trap"}, #q0 when input is letter, goes to q1, "." or "@" to trap state 
            "q1": {"psi": "q1", "pi": "q2", "phi": "q3"}, #when input is letter and Machine is on q1 iterates over itself, "." -> q2 , "@" -> q3
            "q2": {"psi": "q1"},  # letter on q2 -> goes to q1
            "q3": {"psi": "q4"},  # letter on q3 -> goes to q4
            "q4": {"psi": "q4", "pi": "q5"},   #letter on q4-> iterates over itself, "." ->q5
            "q5": {"psi": "q6"},  # q5 when letter input, transitions to q6
            "q6": {"psi": "q6", "pi": "q7"},  # letter input on q6, iterates over itself, "." ->q7
            "q7": {"psi": "q8"},  # letter input on q7 -> q8
            "q8": {"psi": "q8", "pi": "q9"},  #letter input on q8 iterates over itself, "." -> transitions to q9 
            "q9": {"psi": "q10", "pi": "q7"},   #letter input on q9 -> transitions to q10, "." -> transitions to q7
            "q10": {"psi": "q10", "pi": "q9"}  #letter input on q10, iterates over itself, "." -> transitions to q9 
        }
        self.accepting_states = {"q6","q10","q8"}

    def process_string_352(self, string):
        #start on q0
        state = "q0"  
        print(f"Starting DFA processing in state: {state}")

        #for loop that iterates through each char of the string entered from the user
        for char in string:
            #by using get method, we convert each char to symbol so the Machine can identify wisely
            symbol = self.get_symbol_352(char)
            
            #if not in alphabet-> error message
            if symbol not in self.alphabet:
                print("Entered string contains invalid input bits")
                return  

            #if no transition for the state-> error
            if state not in self.transitions or symbol not in self.transitions[state]:
                print(f"String w= \"{string}\" is not acceptable by the given DFA because of an invalid transition from {state} on '{char}'.")
                return  
            #assign next state and update each transitions
            next_state = self.transitions[state][symbol]
            print(f"Present State: {state}")
            print(f"Current input symbol: {char}")
            print(f"Next State: {next_state}\n")
            state = next_state  
            #debugging
        print(f"Final State: {state}")  

        #check terminations, either ends with both vo and gr or with each one
        if state in self.accepting_states and (
            string.endswith(".gov.gr") or string.endswith(".gov") or string.endswith(".gr")):
            print(f"String w= \"{string}\" is accepted.")
        else:
            print(f"String w= \"{string}\" is not acceptable by the given DFA because it does not end in '.gov.gr', '.gov', or '.gr'.")

    #definition of get method used above
    def get_symbol_352(self, char):
        if char.islower():
            return "psi"
        elif char == ".":
            return "pi"
        elif char == "@":
            return "phi"
        else:
            return "invalid"
#instance
dfa = EmailDFA_352()

# String eq 0-> exit program
n = int(input("Enter number of strings, they have to be greater than 0: "))
print(f"Number of strings to be processed: {n}")

if n == 0:
    print("No input to process. Try a valid number")
else:
    for i in range(1, n + 1):
        email = input(f"Enter string {i} of {n}: ")
        dfa.process_string_352(email)
