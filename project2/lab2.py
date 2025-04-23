# Project 2 for CS 341
# Section number: 002
# Semester: SPRING 2025
# Written by: Maria Angel Palacios Sarmiento, mp352
# Instructor: Arashdeep Kaur, ak3257@njit.edu

import re

terminal_symbols = set("0123456789.+-*/()ab")

# PDA class with transitions and processing
class PDA_mp352:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
        self.accept_state = 'q_accept'

    def reset(self):
        self.stack = ['Zo']
        self.state = 'q0'

    # Is valid symbol (only checks if all symbols are in the terminal set)
    def is_valid_symbol(self, string):
        return all(char in terminal_symbols for char in string)

    def run(self, input_s):
        self.reset()
        print(f"Start state: {self.state}")
        index = 0
        error_occurred = False

        # goes through each char in input
        while index < len(input_s):
            current_char = input_s[index]
            stack_top = self.stack[-1] if self.stack else "epsilon"

            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {current_char}")
            print(f"Stack Top: {stack_top}")

            # Handle 'a^k'
            if self.state == 'q0' and current_char == 'a':
                self.stack.append('a')
                print("Symbol popped from Stack: Epsilon")
                print("Symbols pushed onto Stack: a")
                self.state = 'q0'
                print("Next state: q0")

            # Transition into middle expression (b section)
            elif self.state == 'q0' and current_char == 'b':
                if self.stack[-1] == 'a':
                    self.stack.pop()
                    print("Symbol popped from Stack: a")
                    print("Symbols pushed onto Stack: b")
                    self.stack.append('b')
                    self.state = 'q1'
                    print("Next state: q1")
                else:
                    error_occurred = True
                    print(f"No valid transition from state {self.state} on input '{current_char}'")

            # Process the arithmetic section (state q1)
            elif self.state == 'q1' and current_char in "0123456789.+-*/()":
                print(f"Processing arithmetic section: {current_char}")
                self.state = 'q1'  # Stay in q1 as we're processing the middle part
                print("Next state: q1")
                
            # Transition to final state after arithmetic processing
            elif self.state == 'q1' and current_char == 'a':
                if self.stack[-1] == 'b':
                    self.stack.pop()
                    print("Symbol popped from Stack: b")
                    print("Symbols pushed onto Stack: a")
                    self.stack.append('a')
                    self.state = 'q2'
                    print("Next state: q2")
                else:
                    error_occurred = True
                    print(f"No valid transition from state {self.state} on input '{current_char}'")

            # Reject if no valid transition is found
            else:
                error_occurred = True
                print(f"No valid transition from state {self.state} on input '{current_char}'")

            index += 1

        # Final check for accepting state
        if not error_occurred and self.state == 'q2' and not self.stack:
            print(f"\nString w = \"{input_s}\" is accepted by the given PDA.")
        else:
            print(f"\nString w = \"{input_s}\" is not acceptable by the given PDA.")
            return False

def main():
    print("Project 2 for CS 341")
    print("Section number: 002")
    print("Semester: SPRING 2025")
    print("Written by: Maria Angel Palacios Sarmiento, mp352")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu\n")

    pda = PDA_mp352()

    try:
        n = int(input("Enter number of input strings to process (n >= 0): "))
        print(f"n = {n}")
    except ValueError:
        print("Invalid input for n. Must be an integer.")
        return

    if n == 0:
        return

    # Loop to process each input string
    for i in range(1, n + 1):
        input_s = input(f"\nEnter string {i} of {n}: ")
        if not pda.is_valid_symbol(input_s):
            print("Entered string contains invalid input bits.")
        else:
            print(f"Input string: {input_s}")
            pda.run(input_s)

if __name__ == "__main__":
    main()
