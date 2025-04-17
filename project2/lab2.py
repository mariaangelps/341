# Project 2 for CS 341
# Section number: [Enter your section]
# Semester: SPRING 2025
# Written by: [Your First and Last Name], [Your NJIT UCID]
# Instructor: Arashdeep Kaur, ak3257@njit.edu

import re

VALID_SYMBOLS = set("0123456789.+-*/()ab")

# Define PDA transition simulation
class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
        self.accept_state = 'q_accept'

    def reset(self):
        self.stack = ['Z']
        self.state = 'q0'

    def is_valid_symbol(self, string):
        return all(char in VALID_SYMBOLS for char in string)

    def run(self, input_string):
        self.reset()
        print(f"Starting state: {self.state}")
        index = 0

        # Simulate PDA transitions
        while index < len(input_string):
            current_char = input_string[index]
            stack_top = self.stack[-1] if self.stack else "ε"

            print(f"\nPresent State: {self.state}")
            print(f"Current input symbol under R-head: {current_char}")
            print(f"Stack Top: {stack_top}")

            # Handle 'a^k'
            if self.state == 'q0' and current_char == 'a':
                self.stack.append('a')
                print("Symbol popped from Stack: ε")
                print("Symbols pushed onto Stack: a")
                self.state = 'q0'
                print("Next state: q0")

            # Transition into middle expression (assumed)
            elif self.state == 'q0' and current_char == 'b':
                if self.stack[-1] == 'a':
                    self.stack.pop()
                    print("Symbol popped from Stack: a")
                    print("Symbols pushed onto Stack: b")
                    self.stack.append('b')
                    self.state = 'q1'
                    print("Next state: q1")
                else:
                    return self.reject(input_string, "Mismatch in 'a^k b^k' pattern")

            elif self.state == 'q1':
                # Continue processing midsection (arithmetic expression parser should go here)
                # For now, accept it as a placeholder
                print("Processing arithmetic section...")
                self.state = 'q2'
                print("Next state: q2")
                break

            else:
                return self.reject(input_string, f"No valid transition from state {self.state} on input '{current_char}'")

            index += 1

        # Simplified final check
        if self.state == 'q2':
            print(f"\nString w = \"{input_string}\" is accepted by the given PDA.")
        else:
            return self.reject(input_string, "Did not reach accepting state")

    def reject(self, input_string, reason):
        print(f"\nString w = \"{input_string}\" is not acceptable by the given PDA because {reason}.")
        return False


def main():
    print("Project 2 for CS 341")
    print("Section number: [Your Section]")
    print("Semester: SPRING 2025")
    print("Written by: [Your Full Name], [Your UCID]")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu\n")

    pda = PDA()

    try:
        n = int(input("Enter number of input strings to process (n >= 0): "))
        print(f"n = {n}")
    except ValueError:
        print("Invalid input for n. Must be an integer.")
        return

    if n == 0:
        return

    for i in range(1, n + 1):
        input_string = input(f"\nEnter string {i} of {n}: ")
        if not pda.is_valid_symbol(input_string):
            print("Entered string contains invalid input bits.")
        else:
            print(f"Input string: {input_string}")
            pda.run(input_string)


if __name__ == "__main__":
    main()
