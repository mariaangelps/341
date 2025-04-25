import re
def is_valid_expression_352(expr):
    # Check for invalid characters
    if not re.fullmatch(r'[0-9+\-*/().]*', expr):
        return False

    # Check for valid float/number patterns between operators
    tokens = re.findall(r'\d*\.\d+|\d+|[+\-*/()]', expr)
    if not tokens:
        return False

    # Basic parenthesis check
    stack = []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            if not stack or stack.pop() != '(':
                return False
    if stack:
        return False

    # Check syntax rules
    prev = ''
    for i, token in enumerate(tokens):
        if token in '+-*/':
            if prev in ('', '+', '-', '*', '/', '('):  # can't start with operator or follow another operator or '('
                return False
        elif token == ')':
            if prev in '+-*/(':
                return False
        elif token == '(':
            if prev not in ('', '+', '-', '*', '/', '('):
                return False
        prev = token

    if tokens[-1] in '+-*/(':
        return False

    return True

class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
        self.accepting_state = 'q_accept'

    def reset_352(self):
        self.stack = ['Zo']
        self.state = 'q0'

    def process_352(self, input_str):
        self.reset_352()
        i = 0
        n = len(input_str)
        k_count = 0

        if i < n and input_str[i] == 'a':
            self.stack.append('a')
            i += 1
        else:
            return False, "Does not start with 'a'"

        while i < n and input_str[i] == 'b':
            self.stack.append('b')
            k_count += 1
            i += 1

        if i < n and input_str[i] == 'a':
            self.stack.append('a')
            i += 1
        else:
            return False, "Missing second 'a' after ab^k"

        expr = ''
        while i < n and input_str[i] != 'a':
            expr += input_str[i]
            i += 1

        if not is_valid_expression_352(expr):
            return False, f"Invalid arithmetic expression: {expr}"

        if i < n and input_str[i] == 'a':
            i += 1
        else:
            return False, "Missing final 'a' before last b's"

        remaining_b = 0
        while i < n and input_str[i] == 'b':
            remaining_b += 1
            i += 1

        if remaining_b != k_count:
            return False, f"Mismatch in b counts: expected {k_count}, got {remaining_b}"

        if i < n and input_str[i] == 'a':
            i += 1
        else:
            return False, "Final 'a' missing at the end"

        if i != len(input_str):
            return False, "Extra characters found after expected pattern"

        self.state = self.accepting_state
        return True, ""

def main():
    strings = [
        "abbba43.51386abbba",
        "aa.78+27.-3.013/837.842+aa",
        "aa48622.+.41*1.2/00.1/521.23-.9+.53/7.aa",
        "abba382.89*14.2aba",
        "aba4.91-.*17.9aba",
        "aa44.88.6+3.208aa",
        "aba(1.2+(3.5-.9)/19).3aba",
        "abba(.4)64abba",
        "aba((824.23+(9.22-00.0)21.2))+((.2/7.))abba",
        "aba(())aba",
        "abba((14.252+(692.211(.39+492.1))/49.235)abba",
        "abba+6.5abba",
        "aa26.0*(.87/((4.+.2)/(23.1)-2.9)+6.)/(((823.*.333-57.*8.0)/.33))+.76aa",
        "abba.0*(32.922+.7-*9.))abba",
        "aba(4.+(.8-9.))/2.)*3.4+(5.21/34.2aba"
    ]

    pda = PDA()
    for s in strings:
        accepted, reason = pda.process_352(s)
        if accepted:
            print(f'✅ String "{s}" is ACCEPTED.')
        else:
            print(f'❌ String "{s}" is REJECTED. Reason: {reason}')

if __name__ == "__main__":
    main()
