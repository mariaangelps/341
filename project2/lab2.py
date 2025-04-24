def is_operator(ch):
    return ch in ['+', '-', '*', '/']

def is_digit(ch):
    return ch.isdigit()

def is_valid_expression(expr):
    # Simple validation: ensure expression consists of digits, operators, and parentheses
    allowed = set('0123456789+-*/(). ')
    return all(c in allowed for c in expr)

class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
        self.accepting_state = 'q_accept'

    def reset(self):
        self.stack = ['Zo']
        self.state = 'q0'
        print("PDA reset. Stack and state initialized.\nStart state: q0")

    def process(self, input_str):
        print(f"\nInput string: {input_str}")
        self.reset()

        i = 0
        n = len(input_str)
        k_count = 0  # Count of b's in first ab^k

        # Step 1: Read a
        if i < n and input_str[i] == 'a':
            self.stack.append('a')
            print(f"\nPresent State: {self.state}\nCurrent input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {self.stack[-2]}\nSymbols pushed onto Stack: a\nNext state: q0")
            i += 1
        else:
            print("First symbol is not 'a'. Rejecting.")
            return False, "Does not start with 'a'"

        # Step 2: Read b's (ab^k)
        while i < n and input_str[i] == 'b':
            self.stack.append('b')
            k_count += 1
            print(f"\nPresent State: {self.state}\nCurrent input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {self.stack[-2]}\nSymbol pushed onto Stack: b\nNext state: q0")
            i += 1

        # Step 3: Read the next 'a' (completing ab^k a)
        if i < n and input_str[i] == 'a':
            self.stack.append('a')
            print(f"\nPresent State: {self.state}\nCurrent input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {self.stack[-2]}\nSymbols pushed onto Stack: a\nNext state: q0")
            i += 1

            # Special acceptance case for "ab^k a"
            if i == n:
                self.state = self.accepting_state
                print(f"\nFinal state reached: {self.state}")
                return True, ""

        elif k_count == 0 and i == 1 and input_str == "aa":
            # Special case for "aa"
            print(f"\nPresent State: {self.state}\nCurrent input symbol under R-head: {input_str[i]}")
            if self.stack[-1] == 'a':
                self.stack.pop()
                self.state = 'q_accept'
                print(f"Symbol popped from Stack: a\nNext state: {self.state}")
                return True, ""
            else:
                return False, "Expected 'a' on top of stack for 'aa' case"
        else:
            return False, "Missing second 'a' after ab^k"

        # Step 4: Read arithmetic expression until next 'a'
        expr = ''
        while i < n and input_str[i] != 'a':
            expr += input_str[i]
            i += 1

        if not is_valid_expression(expr):
            return False, f"Invalid arithmetic expression: {expr}"

        # Step 5: Read final a
        if i < n and input_str[i] == 'a':
            i += 1
        else:
            return False, "Missing final 'a' before last b's"

        # Step 6: Read b^k again
        remaining_b = 0
        while i < n and input_str[i] == 'b':
            remaining_b += 1
            i += 1

        # Step 7: Final 'a'
        if i < n and input_str[i] == 'a':
            i += 1
        else:
            return False, "Final 'a' missing at the end"

        # Step 8: Check if input fully consumed
        if i != len(input_str):
            return False, "Extra characters found after expected pattern"

        if remaining_b != k_count:
            return False, f"Mismatch in b counts: expected {k_count}, got {remaining_b}"

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
    try:
        n = int(input("Enter number of input strings to process (n >= 0): "))
        print(f"n = {n}")
        for idx in range(1, n + 1):
            user_input = input(f"\nEnter string {idx} of {n}: ").strip()
            accepted, reason = pda.process(user_input)
            if accepted:
                print(f'\nString w = "{user_input}" is ACCEPTABLE by the given PDA.')
            else:
                print(f'\nString w = "{user_input}" is NOT acceptable by the given PDA because: \n{reason}')
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
