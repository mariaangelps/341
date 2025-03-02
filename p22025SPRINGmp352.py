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
        self.states = {
            "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"
        }
        self.alphabet = {"psi", "pi", "phi"}  # 'psi' = letras, 'pi' = '.', 'phi' = '@'
        self.transitions = {
            "q0": {"psi": "q1"},  # Debe comenzar con una letra
            "q1": {"psi": "q1", "pi": "q2", "phi": "q3"},  # Local part (usuario)
            "q2": {"psi": "q1"},  # Permite letras después de un punto en usuario
            "q3": {"psi": "q4"},  # Dominio debe comenzar con una letra después del '@'
            "q4": {"psi": "q4", "pi": "q5"},  # Dominio principal antes del primer '.'
            "q5": {"psi": "q6"},  # Subdominio después del primer '.'
            "q6": {"psi": "q6", "pi": "q7"},  # Permite más subdominios
            "q7": {"psi": "q8"},  # Última parte del dominio después del último '.'
            "q8": {"psi": "q8"},  # Permite continuar con letras en el dominio final
        }
        self.accepting_states = {"q7", "q8"}  # Ahora q7 y q8 son estados de aceptación

    def process_string(self, string):
        state = "q0"  # Estado inicial
        for char in string:
            symbol = self.get_symbol(char)
            if symbol not in self.alphabet or state not in self.transitions or symbol not in self.transitions[state]:
                return f"Rejected: Invalid transition from {state} on '{char}'"
            state = self.transitions[state][symbol]

        # Verificación final para asegurar que termine en .gov o .gr
        if string.endswith(".gov") or string.endswith(".gr"):
            return "Accepted"
        else:
            return f"Rejected: Email must end in '.gov' or '.gr'"

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
