# Maria Angel Palacios Sarmiento
# mp352
# CS 341-002
# Spring 2025

# Printing Information 
def header_info():
    print("Project 1 for CS 341")
    print("Section number: 002")
    print("Written by: Maria Angel Palacios Sarmiento, mp352")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu")

header_info()

class EmailDFA:
    def __init__(self):
        self.states = {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"}
        self.alphabet = {"psi", "pi", "phi"}  # 'psi' = letters a-z, 'pi' = '.', 'phi' = '@'
        self.transitions = {
            "q0": {"psi": "q1"},  # El email debe comenzar con una letra
            "q1": {"psi": "q1", "phi": "q2", "pi": "q7"},  # Usuario antes de @
            "q2": {"psi": "q3"},  # Debe haber al menos una letra después del @
            "q3": {"psi": "q3", "pi": "q4"},  # Dominio antes del punto
            "q4": {"psi": "q5"},  # Debe haber letras después del punto
            "q5": {"psi": "q5"},  # Dominio válido
        }
        self.accepting_states = {"q5"}  # Solo q5 es final

    def process_string(self, string):
        state = "q0"  # Estado inicial corregido
        for char in string:
            symbol = self.get_symbol(char)
            if symbol not in self.alphabet or state not in self.transitions or symbol not in self.transitions[state]:
                return f"Rejected: Invalid transition from {state} on '{char}'"
            state = self.transitions[state][symbol]
        return "Accepted" if state in self.accepting_states else f"Rejected: Did not reach accepting state (Ended at {state})"

    def get_symbol(self, char):
        if char.islower():
            return "psi"
        elif char == ".":
            return "pi"
        elif char == "@":
            return "phi"
        else:
            return "invalid"

dfa = EmailDFA()
n = int(input("Enter number of strings: "))
for _ in range(n):
    email = input("Enter email string: ")
    print(dfa.process_string(email))
