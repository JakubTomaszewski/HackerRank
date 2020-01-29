import json
import os

with open('jakub_k_tomasze1_data.json', 'r') as json_file:
    json_data = json.load(json_file)

subs = json_data['submissions']

for sub in subs:
    file = open('..\HR\{}.py'.format(''.join(letter for letter in sub['challenge'] if letter.isalnum())), 'w') #moze zmienic mode na 'a'
    file.write(sub['code'])
    file.close()

#changing directory
os.chdir('..\HR')
print(os.system('dir'))

#pushing to git
os.system('git add *')
os.system('git commit -m "automatic commit"')
os.system('git push -u origin master')

# some sub names may be duplicates, due to many submissions(solutions) of one challenge
#thus, if the filename is the same, add the code to the existing file
#to finish



