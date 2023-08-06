favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Looping Through All the Keys in a Dictionary
for name, language in favorite_languages.items():
 print(f"{name.title()}'s favorite language is {language.title()}.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# items(): take values and keys
# keys(): take keys
# values(): take values