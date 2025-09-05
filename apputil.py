

# add code below ...
# Exercise 1
import string

def palindrome(word):
    # Remove spaces and punctuation, and convert to lowercase
    cleaned = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned == cleaned[::-1]

print(palindrome('racecar'))                   
print(palindrome('Nurses Run'))                
print(palindrome('Sit on a potato pan, Otis.'))



#Exercise 2
def parentheses(sequence):
    stack = []
    mapping = {')': '('}
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != mapping[char]:
                return False
    return stack == []

print(parentheses('((blah)()()())'))
print(parentheses('(((())blee))'))
print(parentheses('(()hello((())()))'))
print(parentheses('((((((())'))
print(parentheses('()))'))