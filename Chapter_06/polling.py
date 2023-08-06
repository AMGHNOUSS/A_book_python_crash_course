favorite_languages = {'adam': 'python',
                      'harry': 'c',
                      'edward': 'rust',
                      'phil': 'python',
                      'john': 'ruby',
                      'nike': 'java'
                      }
languages_poll = ['jen', 'edward', 'john']
for key in favorite_languages.keys():
    if key in languages_poll:
        print(f"Mr. {key.title()} I would like to thank you for responding")
    else:
        print(f"Mr. {key.title()} I would like to invite you to take the poll.")