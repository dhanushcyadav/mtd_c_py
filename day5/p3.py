import sys

def push_element(stack):
    try:
        element = input('Enter the element to be pushed: ')
        stack.insert(0, element)
        print(f'{element} has been pushed to the stack.')
    except Exception as e:
        print(f"Error pushing element: {e}")

def pop_element(stack):
    if len(stack) == 0:
        print('Stack is empty, nothing to pop.')
        return
    popped_element = stack.pop(0)
    print(f'Popped element is {popped_element}')

def list_stack(stack):
    if len(stack) == 0:
        print('Stack is empty')
        return
    print(f'The Stack is {stack}')

def top(stack):
    if len(stack) == 0:
        print('Stack is empty, no top element.')
        return
    print(f'The top element is {stack[0]}')

def exit_program(stack):
    print("Exiting the program.")
    sys.exit()

def invalid_choice(stack):
    print('Invalid choice entered. Please try again.')

def get_menu(choice, stack):
    menu = {
        1: push_element,
        2: pop_element,
        3: list_stack,
        4: top,
        5: exit_program
    }
    func = menu.get(choice)
    if func:
        func(stack)
    else:
        invalid_choice(stack)

def start_app(stack):
    while True:
        print('\nMenu:')
        print('1: Push')
        print('2: Pop')
        print('3: List Stack')
        print('4: Top')
        print('5: Exit')
        
        try:
            choice = int(input('Enter your choice: '))
            get_menu(choice, stack)
        except ValueError:
            print('Please enter a valid integer for your choice.')

stack = []  # This list works as Stack
start_app(stack)
