# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.
text = input("Entrez une phrase : ")
words = text.split()

# Trouver le mot le plus fréquent
most_common = None
max_count = 0
for word in set(words):
    count = words.count(word)
    if count > max_count:
        max_count = count
        most_common = word

print(f"Le mot le plus fréquent est : '{most_common}' (apparu {max_count} fois)")
