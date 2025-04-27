# Project 2 for CS 341
# Section number: 002
# Semester: SPRING 2025
# Written by: Maria Angel Palacios Sarmiento, mp352
# Instructor: Arashdeep Kaur, ak3257@njit.edu

import re

def is_valid_expression_352(expr):
    # Strip leading/trailing 'a'
    core = re.sub(r'^a+', '', expr)
    core = re.sub(r'a+$', '', core)

    if not core:
        return False

    # Allowed characters in full expr
    allowed = set('0123456789+-*/().a')

    if not all(c in allowed for c in expr):
        return False

    # Core can't start or end with operator
    if core[0] in '+*/' or core[-1] in '+-*/':
        return False

    # Balanced parentheses in core
    stack = []
    for ch in core:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False

    # No empty parentheses
    if re.search(r'\(\s*\)', core):
        return False
    
    # No operator-dot-operator
    if re.search(r'[+\-*/]\.[+\-*/]', core):
        return False

    # No multiple dots in a number (covers leading-dot and others)
    if re.search(r'\.\d*\.', core):
        return False
    
    # No permitir punto o dígito inmediatamente después de ')'
    if re.search(r'\)[\d\.]', core):
        return False


    # token pattern for regex
    token_pattern = re.compile(r'^(?:\d+\.\d*|\.\d+|\d+|\(|\)|[+\-*/])+$')
    if not token_pattern.match(core):
        return False

    return True


class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q'
        self.accepting_state = 'q_accept'

    def reset_352(self):
        self.stack = ['ϵ']
        self.state = 'q'
        print("Start state: q")
        print(f"\nPresent State: {self.state}")
        print("Current input symbol under R-head: ε")
        print("Stack Top: ϵ")
        print("Symbol popped from Stack: ϵ")
        print("Symbols pushed onto Stack: z0")
        print("Next state: q0")
        
        # Now actually do the transition
        self.stack.pop()
        self.stack.append('z0')
        self.state = 'q0'

    def process_352(self, input_str):
        print(f"\nInput string: {input_str}")
        self.reset_352()
        
        i = 0
        n = len(input_str)
        k_count = 0


        if i < n and input_str[i] == 'a':
            top = self.stack[-1] if self.stack else 'ϵ'
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {top}")
            print("Symbols pushed onto Stack: a")
            print("Next state: q1")
            self.stack.append('a')
            self.state = 'q1'
            i += 1
        else:
            return False, "Does not start with 'a'"

        while i < n and input_str[i] == 'b':
            top = self.stack[-1] if self.stack else 'ϵ'
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {top}")
            print("Symbol popped from Stack: ε")
            print("Symbol pushed onto Stack: b")
            print("Next state: q1")
            self.stack.append('b')
            k_count += 1
            i += 1

        if i < n and input_str[i] == 'a':
            top = self.stack[-1] if self.stack else 'ϵ'
            print(f"\nPresent State: q1")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {top}")
            print("Symbol popped from Stack: ε")
            print("Symbols pushed onto Stack: a")
            print("Next state: q2")
            self.stack.append('a')
            self.state = 'q2'
            i += 1
        else:
            return False, "Missing second 'a' after ab^k"

        expr = ''
        while i < n and input_str[i] != 'a':
            symbol = input_str[i]
            expr += symbol
            top = self.stack[-1] if self.stack else 'ϵ'

            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {symbol}")
            print(f"Stack Top: {top}")

            if symbol == '(':
                print("Symbols pushed onto Stack: (")
                self.stack.append('(')
            elif symbol == ')':
                if self.stack and self.stack[-1] == '(':
                    print("Symbol popped from Stack: (")
                    self.stack.pop()
                else:
                    return False, f"Unmatched ')' at position {i}"
            else:
                print("Symbol popped from Stack: ε pop")
                print("Symbols pushed onto Stack: none ")

            print(f"Next state: {self.state}")
            i += 1

        if not is_valid_expression_352(expr):
            return False, f"Entered string contains invalid input bits: {expr}"

        if i < n and input_str[i] == 'a':
            top = self.stack[-1] if self.stack else 'ϵ'
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {top}")
            print("Symbol popped from Stack: ε pop")
            print("Symbols pushed onto Stack: none ")
            print("Next state: q3")
            self.stack.append('a')
            self.state = 'q3'
            i += 1
        else:
            return False, "Missing final 'a' before last b's"

        remaining_b = 0
        while i < n and input_str[i] == 'b':
            top = self.stack[-1] if self.stack else 'ϵ'
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {top}")
            print("Symbol popped from Stack: ε pop")
            print("Symbols pushed onto Stack: none ")
            print("Next state: q3")
            self.stack.append('b')
            remaining_b += 1
            i += 1

        if remaining_b != k_count:
            return False, f"Mismatch in b counts: expected {k_count}, got {remaining_b}"

        if i < n and input_str[i] == 'a':
            top = self.stack[-1] if self.stack else 'ϵ'
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {top}")
            print("Symbol popped from Stack: ε pop")
            print("Symbols pushed onto Stack: none ")
            print("Next state: q_accept")
            self.stack.append('a')
            self.state = self.accepting_state
            i += 1
        else:
            return False, "Final 'a' missing at the end"

        if i != len(input_str):
            return False, "Extra characters found after expected pattern"

        print(f"\nFinal state reached: {self.state}")
        return True, ""

      



def main():
    print("Project 2 for CS 341")
    print("Section number: 002")
    print("Semester: SPRING 2025")
    print("Written by: Maria Angel Palacios Sarmiento, mp352")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu\n")

    pda = PDA()
    
    n = int(input("Enter the number of input strings (n ≥ 0): "))
    print(f"\nYou entered: {n} strings to process.\n")

    if n == 0:
        print("Program terminates.")
        return

    for i in range(1, n + 1):
        user_input = input(f"Enter string {i} of {n}: ")
        accepted, reason = pda.process_352(user_input)

        if accepted:
            print(f'\nString w = "{user_input}" is ACCEPTABLE by the given PDA.')
        else:
            print(f'\nString w = "{user_input}" is NOT acceptable by the given PDA because:\n{reason}')

if __name__ == "__main__":
    main()