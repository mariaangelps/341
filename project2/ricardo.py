

from enum import IntEnum

class State(IntEnum):
    Q1 = 1
    Q2 = 2
    Q3 = 3
    Q4 = 4
    Q5 = 5
    Q6 = 6
    Q7 = 7
    Q8 = 8
    Q9 = 9
    QERROR = 10

def print_transition(state, char,stack_top, pop, push, next_state):
    if next_state == State.QERROR:
        print("ERROR")
        return
    else:
        print(f"Present State: q{state}")
        print(f"Current input symbol under R-head: {char}")
        print(f"Stack Top: {stack_top}")
        print(f"Symbol popped from Stack: {pop}")
        print(f"Symbols pushed onto Stack: {push}")
        print(f"Next state: q{next_state}\n")
def unmatched_parenthesis(paren):
    return paren < 0

def is_accepted(state, q2B, q8B, qA):
    return state == State.Q9 and q2B == q8B and qA == 0

def process_string(s):
    state, paren, q2B, qA, q8B = State.Q1, 0, 0, 0, 0
    stack, accept = [], False
    print(f"\nStart State: q{state}\n")

    for char in s:
        symbol = char
        stack_top = stack[-1] if stack else 'ε'

        pop = 'ε'
        push = 'ε'
        next_state = State.QERROR

        if symbol == '(':
            paren += 1
        elif symbol == ')':
            paren -= 1
            if unmatched_parenthesis(paren):
                print_transition(state, symbol,stack_top, pop, push, State.QERROR)
                break

        if state == State.Q1:
            if symbol == 'a':
                next_state = State.Q2
                push = 'a'
                stack.append('a')
                qA += 1
        elif state == State.Q2:
            if symbol == 'b':
                next_state = State.Q2
                push = 'b'
                stack.append('b')
                q2B += 1
            elif symbol == 'a':
                next_state = State.Q3
                push = 'a'
                stack.append('a')
                qA += 1
        elif state == State.Q3:
            if symbol.isdigit():
                next_state = State.Q4
                push = 'ε'
            elif symbol == '(':
                next_state = State.Q3
                push = '('
            elif symbol == '.':
                next_state = State.Q6
                push = 'ε'
            elif symbol == 'a':
                print_transition(state, symbol,stack_top, pop, 'ε', State.QERROR)
                accept = False
                break
            else:
                print_transition(state, symbol,stack_top, pop, 'ε', State.QERROR)
                accept = False
                break
            pop = 'ε'
        elif state == State.Q4:
            if symbol.isdigit():
                next_state = State.Q4
                push = 'ε'
                pop = 'ε'
            elif symbol == '.':
                next_state = State.Q5
                push = '.'
                pop = 'ε'
            elif symbol == ')':
                next_state = State.Q7
                if stack and stack[-1] == '(':
                    pop = stack.pop()
                else:
                    pop = 'ε'
                push = 'ε'
            elif symbol == 'a':
                if paren != 0:
                    next_state = State.Q10
                    accept = False
                    print("ERROR")
                    break
                else:
                    next_state = State.Q8
                    push = 'a'
                    stack.append('a')
                    qA -= 1
            elif symbol == 'b':
                next_state = State.Q8
                push = 'ε'
            else:
                print_transition(state, symbol,stack_top, pop, 'ε', 10)
                accept = False
                break
            pop = 'ε'
            push = 'ε'
        # State transitions of q5
        elif state == State.Q5:
            if symbol.isdigit():
                next_state = State.Q5
                push = 'ε'
                pop = 'ε'
            elif symbol in ['+', '-', '*', '/']:
                next_state = State.Q3
                push = 'ε'
                stack.append('ε')
                pop = 'ε'
            elif symbol == ')':
                next_state = State.Q7
                if stack and stack[-1] == '(':
                    pop = stack.pop()
                else:
                    pop = 'ε'
                push = 'ε'
            elif symbol == 'a':
                if paren != 0:
                    next_state = State.QERROR
                    accept = False
                    print("ERROR")
                    break
                else:
                    next_state = State.Q8
                    push = 'ε'
                    pop = 'ε'
                    stack.append('a')
                    qA -= 1
            elif symbol == 'b':
                next_state = State.Q8
                push = 'ε'
            else:
                print_transition(state, symbol,stack_top, pop, 'ε', State.QERROR)
                accept = False
                break
        # State transitions of q6
        elif state == State.Q6:
            if symbol.isdigit():
                next_state = State.Q5
                push = 'ε'
                pop = 'ε'
            elif symbol == ')':
                next_state = State.Q7
                if stack and stack[-1] == '(':
                    pop = stack.pop()
                else:
                    pop = 'ε'
                push = 'ε'
            elif symbol == 'a':
                if paren != 0:
                    next_state = State.QERROR
                    accept = False
                    print("ERROR")
                    break
                else:
                    next_state = State.Q8
                    push = 'a'
                    stack.append('a')
                    qA -= 1
            elif symbol == 'b':
                next_state = State.Q8
                push = 'ε'
            else:
                print_transition(state, symbol,stack_top, pop, 'ε', State.QERROR)
                accept = False
                break
        # State transitions of q7
        elif state == State.Q7:
            if symbol == 'b':
                next_state = State.Q8
                push = 'ε'
                pop = 'ε'
            elif symbol in ['+', '-', '*', '/']:
                next_state = State.Q3
                push = 'ε'
                stack.append('ε')
                pop = 'ε'
            elif symbol == 'a':
                if paren != 0:
                    next_state = State.QERROR
                    accept = False
                    print("ERROR")
                    break
                else:
                    next_state = State.Q8
                    push = 'a'
                    stack.append('a')
                    qA -= 1
            elif symbol == 'b':
                next_state = State.Q8
                push = 'ε'
            elif symbol == ')':
                next_state = State.Q7
                if stack and stack[-1] == '(':
                    pop = stack.pop()
                else:
                    pop = 'ε'
                push = 'ε'
            else:
                print_transition(state, symbol,stack_top, pop, 'ε', State.QERROR)
                accept = False
                break
        # State transitions of q8
        elif state == State.Q8:
            if symbol == 'b':
                next_state = State.Q8
                pop = 'b'
                q8B += 1
            elif symbol == 'a':
                if q2B != q8B:
                    next_state = State.QERROR
                else:
                    next_state = State.Q9
                    pop = 'a'
                    stack.append('a')
                    qA -= 1
            else:
                print_transition(state, symbol,stack_top, pop, 'ε', State.QERROR)
                accept = False
                break
            push = 'ε'
        # State transitions of q9
        elif state == State.Q9:
            if symbol == 'a':
                next_state = State.Q9
                pop = 'a'
                stack.append('a')
                qA -= 1
            else:
                print_transition(state, symbol,stack_top, pop, 'ε', State.QERROR)
                accept = False
                break
            push = 'ε'

        print_transition(state, symbol,stack_top, pop, push, next_state)
        if next_state == State.QERROR:
            break
        state = next_state

    if is_accepted(state, q2B, q8B, qA):
        accept = True

    print(f"\nString \"{s}\" is {'accepted' if accept else 'rejected'}.\n")

def main():
# CS 341 Project 2 information
    print("Project 2 for CS341")
    print("Section Number: 002")
    print("Semester: Spring 2025")
    print("Written by: Ricardo Mejia, ram227")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu")

    try:
        n = int(input("Enter the number of strings to be processed (number MUST be GREATER than 0): "))
        if n <= 0:
            print("You need to input a number GREATER than 0. Exiting program...")
            return
    except ValueError:
        print("Invalid input. Exiting program...")
        return

    for i in range(n):
        s = input(f"Enter string {i+1} of {n}: ")
        process_string(s)

    print("\nExiting program...")

if __name__ == "__main__":
    main()
