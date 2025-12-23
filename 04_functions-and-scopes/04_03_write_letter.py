# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, text):
    greeting = f"Dear {name},\n\n"
    goodbye = f"\n\nSincerely,\n{name}"
    letter = greeting + text + goodbye
    return letter

# Example usage:
letter_content = write_letter("Adama", "I hope this letter finds you well.")
print(letter_content)