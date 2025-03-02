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
        self.states = {
            "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"
        }
        self.alphabet = {"psi", "pi", "phi"}  # 'psi' = letters, 'pi' = '.', 'phi' = '@'
        self.transitions = {
            "q0": {"psi": "q1", "pi": "q_trap", "phi": "q_trap"},
            "q1": {"psi": "q1", "pi": "q2", "phi": "q3"},
            "q2": {"psi": "q1"},  
            "q3": {"psi": "q4"},  
            "q4": {"psi": "q4", "pi": "q5"},  
            "q5": {"psi": "q6"},  
            "q6": {"psi": "q6", "pi": "q7"},  
            "q7": {"psi": "q8"},  
            "q8": {"psi": "q8", "pi": "q9"},  # Sigue aceptando letras y puntos
            "q9": {"psi": "q10", "pi": "q7"},  # Permite más puntos después
            "q10": {"psi": "q10", "pi": "q9"}  # Asegura que los dominios largos se procesen
 
        }
        self.accepting_states = {"q6","q10"}

    def process_string_352(self, string):
        state = "q0"  
        print(f"Starting DFA processing in state: {state}")

        for char in string:
            symbol = self.get_symbol_352(char)
            
            if symbol not in self.alphabet:
                print("Entered string contains invalid input bits")
                return  

            if state not in self.transitions or symbol not in self.transitions[state]:
                print(f"String w= \"{string}\" is not acceptable by the given DFA because of an invalid transition from {state} on '{char}'.")
                return  

            next_state = self.transitions[state][symbol]
            print(f"Present State: {state}")
            print(f"Current input symbol: {char}")
            print(f"Next State: {next_state}\n")
            state = next_state  
        print(f"Final State: {state}")  # Verifica en qué estado termina la cadena


        if state in self.accepting_states and (string.endswith(".gov") or string.endswith(".gr")):
            print(f"String w= \"{string}\" is accepted.")
        else:
            print(f"String w= \"{string}\" is not acceptable by the given DFA because it does not end in '.gov' or '.gr'.")

    def get_symbol_352(self, char):
        if char.islower():
            return "psi"
        elif char == ".":
            return "pi"
        elif char == "@":
            return "phi"
        else:
            return "invalid"

dfa = EmailDFA_352()

# Input handling
n = int(input("Enter number of strings, they have to be greater than 0: "))
print(f"Number of strings to be processed: {n}")

if n == 0:
    print("No input to process. Try a valid number")
else:
    for i in range(1, n + 1):
        email = input(f"Enter string {i} of {n}: ")
        dfa.process_string_352(email)
