import pyperclip , re

dateRegex = re.compile (r'''(
    (\d{2})     #First two numbers for date (Day)
    (\s|\-|\\|\.|\/)      #Separator 
    (\d{2})     #Second two numbers for date (Month)
    (\s|\-|\\|\.|\/)      #Separator
    (\d{2,4})     #Last 2/4 numbers for date (Year)
    )''', re.VERBOSE)

#Find matches in clipboard text
text = str(pyperclip.paste())

#Reformats dates
matches = []
for groups in dateRegex.findall(text):
    dateNum = '/'.join([groups[1], groups[3], groups[5]])
    matches.append(dateNum)

#Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No dates found")
