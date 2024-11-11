# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str and captalize the first letter of each word
name = name.strip().title()

# Print hello and the inputted name
print(f"hello, {name}")