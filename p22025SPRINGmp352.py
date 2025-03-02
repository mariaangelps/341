class EmailDFA:
    def __init__(self):
        self.states = {
            "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"
        }
        self.alphabet = {"psi", "pi", "phi"}  # 'psi' = letters, 'pi' = '.', 'phi' = '@'
        self.transitions = {
            "q0": {"psi": "q1"},  # Must start with a letter
            "q1": {"psi": "q1", "pi": "q2", "phi": "q3"},  # Local part (before @)
            "q2": {"psi": "q1"},  # Allow letters after a dot in local part

            "q3": {"psi": "q4"},  # Domain must start with a letter after '@'
            "q4": {"psi": "q4", "pi": "q5"},  # Main domain before first '.'
            "q5": {"psi": "q6"},  # First subdomain after '.'
            "q6": {"psi": "q6", "pi": "q7"},  # Allow multiple subdomains

            "q7": {"psi": "q8"},  # Last part of domain (gr/go/gov)
            "q8": {"psi": "q8", "pi": "q9"},  # Allow final dot before gov/gr
            "q9": {"psi": "q10"},  # Final domain part (gov/gr)

            # 🚀 NEW: Allow more subdomains after reaching .gov/.gr
            "q10": {"pi": "q7", "psi": "q10"}  # If another dot comes, restart subdomain parsing
        }
        self.accepting_states = {"q10"}  # The final domain must be in q10

    def process_string(self, string):
        state = "q0"  # Start state
        for char in string:
            symbol = self.get_symbol(char)
            if symbol not in self.alphabet or state not in self.transitions or symbol not in self.transitions[state]:
                return f"Rejected: Invalid transition from {state} on '{char}'"
            state = self.transitions[state][symbol]

        # Check if email ends in .gov or .gr
        valid_endings = [".gov", ".gr"]
        if any(string.endswith(suffix) for suffix in valid_endings):
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
