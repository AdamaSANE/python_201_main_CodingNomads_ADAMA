# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(name):
    return f"Dear {name},\n"

def write_letter(name, body):
    greeting = greet(name)
    return f"{greeting}{body}\nSincerely,\nYour Friend"

# Example usage:
letter = write_letter("Adama", "I hope this letter finds you well.")