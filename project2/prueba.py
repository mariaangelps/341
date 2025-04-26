
import re
import re

def is_valid_expression_352(expr):
    allowed = set('0123456789+-*/().')

    # Check if only allowed characters are present
    if not all(c in allowed for c in expr):
        return False

    # Check for invalid operator placement (no operator at start or end)
    if expr[0] in '+*/' or expr[-1] in '+-*/':
        return False

    # Remove spaces
    expr = expr.replace(" ", "")

    # Check for balanced parentheses
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

    # ❌ Reject empty parentheses like () or ( )
    if re.search(r'\(\s*\)', expr):
        return False

    # ❌ Reject if before ( is not operator or ( or start
    if re.search(r'(?<!^)(?<![\+\-\*/\(])\(', expr):
        return False

    # ❌ Reject if after ) is not operator or ) or end
    if re.search(r'\)(?![\+\-\*/\)]|$)', expr):
        return False

    # ✅ Check valid tokens
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
        k_count = 0  # Count of b's in first ab^k

        # Step 1: Read first 'a'
        if i < n and input_str[i] == 'a':
            self.stack.append('a')
            print(f"\nPresent State: {self.state}\nCurrent input symbol under R-head: {input_str[i]}")
            print(f"Stack Top: {self.stack[-2] if len(self.stack) > 1 else 'ε'}\nSymbols pushed onto Stack: a\nNext state: q0")
            i += 1
        else:
            return False, "Does not start with 'a'"

        # Step 2: Read b's (optional, can be k=0)
        while i < n and input_str[i] == 'b':
            self.stack.append('b')
            k_count += 1
            print(f"\nPresent State: {self.state}\nCurrent input symbol under R-head: {input_str[i]}")
            print(f"Symbol popped from Stack: {self.stack.pop() if self.stack else 'ε'}")
            print(f"Stack Top: {self.stack[-2] if len(self.stack) > 1 else 'ε'}\nSymbol pushed onto Stack: b\nNext state: q0")
            i += 1

        # Step 3: Second 'a'
        if i < n and input_str[i] == 'a':
            self.stack.append('a')
            print(f"\nPresent State: {self.state}\nCurrent input symbol under R-head: {input_str[i]}")
            print(f"Symbol popped from Stack: {self.stack.pop() if self.stack else 'ε'}")
            print(f"Stack Top: {self.stack[-2] if len(self.stack) > 1 else 'ε'}\nSymbols pushed onto Stack: a\nNext state: q0")
            i += 1
        else:
            return False, "Missing second 'a' after ab^k"

        # Step 4: Expression
        expr = ''
        while i < n and not (input_str[i] == 'a' and i + k_count + 1 < n and input_str[i + k_count + 1] == 'a'):
            expr += input_str[i]
            i += 1

        if not is_valid_expression_352(expr):
            return False, f"Invalid arithmetic expression: {expr}"

        # Step 5: Next 'a'
        if i < n and input_str[i] == 'a':
            i += 1
        else:
            return False, "Missing final 'a' before last b's"

        # Step 6: b^k again
        remaining_b = 0
        while i < n and input_str[i] == 'b':
            remaining_b += 1
            i += 1

        if remaining_b != k_count:
            return False, f"Mismatch in b counts: expected {k_count}, got {remaining_b}"

        # Step 7: Final 'a'
        if i < n and input_str[i] == 'a':
            i += 1
        else:
            return False, "Final 'a' missing at the end"

        # Step 8: Done?
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
    
    # Process the predefined strings
    test_strings = [
        "abbba43.51386abbba",
        "aa.78+27.-3.013/837.842+aa",
        "aa48622.+.41*1.2/00.1/521.23-.9+.53/7.aa",
        "abba382.89*14.2aba",
        "aba4.91-.*17.9aba aa44.88.6+3.208aa",
        "aba(1.2+(3.5-.9)/19).3aba",
        "abba(.4)64abba",
        "aba((824.23+(9.22-00.0)*21.2))+((.2/7.))abba",
        "aba(())aba",
        "abba((14.252+(692.211*(.39+492.1))/49.235)abba",
        "abba+6.5abba",
        "aa26.0*(.87/((4.+.2)/(23.1)-2.9)+6.)/(((823.*.333-57.*8.0)/.33))+.76aa",
        "abba.0*(32.922+.7-*9.))abba",
        "aba(4.+(.8-9.))/2.)*3.4+(5.21/34.2ab"
    ]
    
    for idx, user_input in enumerate(test_strings, 1):
        accepted, reason = pda.process_352(user_input)
        if accepted:
            print(f'\nString w = "{user_input}" is ACCEPTABLE by the given PDA ✅.')
        else:
            print(f'\nString w = "{user_input}" is NOT acceptable by the given PDA because: \n{reason}')

if __name__ == "__main__":
    main()
