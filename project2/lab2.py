# Project 2 for CS 341
# Section number: 002
# Semester: SPRING 2025
# Written by: Maria Angel Palacios Sarmiento, mp352
# Instructor: Arashdeep Kaur, ak3257@njit.edu

import re

def is_valid_expression_352(expr):
    allowed = set('0123456789+-*/().')

    if not all(c in allowed for c in expr):
        return False

    if expr[0] in '+*/' or expr[-1] in '+-*/':
        return False

    expr = expr.replace(" ", "")

    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False

    if re.search(r'\(\s*\)', expr):
        return False

    if re.search(r'(?<!^)(?<![\+\-\*/\(])\(', expr):
        return False

    if re.search(r'\)(?![\+\-\*/\)]|$)', expr):
        return False

    float_or_op = r'(\d+(\.\d*)?|\.\d+|\+|\-|\*|\/|\(|\))'
    valid_expr_pattern = f'^({float_or_op})+$'

    return re.match(valid_expr_pattern, expr) is not None


class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
        self.accepting_state = 'q_accept'

    def reset_352(self):
        self.stack = ['Zo']
        self.state = 'q0'
        print("PDA reset. Stack and state initialized.\nStart state: q0")

    def process_352(self, input_str):
        print(f"\nInput string: {input_str}")
        self.reset_352()

        i = 0
        n = len(input_str)
        k_count = 0

        if i < n and input_str[i] == 'a':
            self.stack.append('a')
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {self.stack[-2]}\nSymbols pushed onto Stack: a\nNext state: q0")
            i += 1
        else:
            return False, "Does not start with 'a'"

        while i < n and input_str[i] == 'b':
            self.stack.append('b')
            k_count += 1
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Symbol popped from Stack: {self.stack.pop()}")
            print(f"Stack Top: {self.stack[-1] if len(self.stack) > 0 else 'ε'}")
            self.stack.append('b')
            print(f"Symbol pushed onto Stack: b\nNext state: q0")
            i += 1

        if i < n and input_str[i] == 'a':
            self.stack.append('a')
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Symbol popped from Stack: {self.stack.pop()}")
            print(f"Stack Top: {self.stack[-1] if len(self.stack) > 0 else 'ε'}\nSymbols pushed onto Stack: a\nNext state: q0")
            i += 1
        else:
            return False, "Missing second 'a' after ab^k"

        # Step 4: Arithmetic Expression Parsing
        expr = ''
        self.state = 'q1'
        while i < n and input_str[i] != 'a':
            symbol = input_str[i]
            expr += symbol
            top = self.stack[-1] if self.stack else 'ε'

            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {symbol}")
            print(f"Stack Top: {top}")

            if symbol == '(':
                self.stack.append('(')
                print("Symbols pushed onto Stack: (")
            elif symbol == ')':
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                    print("Symbol popped from Stack: (")
                else:
                    return False, f"Unmatched ')' at position {i}"
            else:
                print(f"Symbols pushed onto Stack: {symbol}")

            print(f"Next state: {self.state}")
            i += 1

        if not is_valid_expression_352(expr):
            return False, f"Invalid arithmetic expression: {expr}"

        self.state = 'q2'
        if i < n and input_str[i] == 'a':
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {self.stack[-1] if self.stack else 'ε'}")
            print("Symbols pushed onto Stack: a\nNext state: q2")
            i += 1
        else:
            return False, "Missing final 'a' before last b's"

        self.state = 'q3'
        remaining_b = 0
        while i < n and input_str[i] == 'b':
            remaining_b += 1
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {self.stack[-1] if self.stack else 'ε'}")
            print("Symbol pushed onto Stack: b\nNext state: q3")
            i += 1

        if remaining_b != k_count:
            return False, f"Mismatch in b counts: expected {k_count}, got {remaining_b}"

        if i < n and input_str[i] == 'a':
            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {self.stack[-1] if self.stack else 'ε'}")
            print("Symbol pushed onto Stack: a\nNext state: q_accept")
            i += 1
        else:
            return False, "Final 'a' missing at the end"

        if i != len(input_str):
            return False, "Extra characters found after expected pattern"

        self.state = self.accepting_state
        print(f"\nFinal state reached: {self.state}")
        return True, ""


def main():
    print("Project 2 for CS 341")
    print("Section number: 002")
    print("Semester: SPRING 2025")
    print("Written by: Maria Angel Palacios Sarmiento, mp352")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu\n")

    pda = PDA()
    
    # Prompting the user to enter the number of strings
    n = int(input("Enter the number of input strings (n ≥ 0): "))
    print(f"\nYou entered: {n} strings to process.\n")

    if n == 0:
        print("Program terminates.")
        return

    # Loop for processing n strings
    for i in range(1, n + 1):
        user_input = input(f"Enter string {i} of {n}: ")
        
        accepted, reason = pda.process_352(user_input)
        if accepted:
            print(f'\nString w = "{user_input}" is ACCEPTABLE by the given PDA ✅.')
        else:
            print(f'\nString w = "{user_input}" is NOT acceptable by the given PDA because: \n{reason}')


if __name__ == "__main__":
    main()
