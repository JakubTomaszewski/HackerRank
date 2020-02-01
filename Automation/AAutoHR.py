import json
import os
from urllib import request
import gzip

url = 'https://s3.amazonaws.com/downloads.hackerrank.com/hacker_gdpr_data/jakub_k_tomasze1oWje7DgWmNoZ18HjJhYt_AoWje7DgWmNoZ18HjJhYt_AoWje7DgWmNoZ18HjJhYt_A.json.gz?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1580832734&Signature=pYjVk5LArNbzj54I7BiTOGe1anE%3D&response-content-disposition=attachment%3B%20filename%3Djakub_k_tomasze1_data.json.gz&response-content-type=application%2Foctet-stream'
#getting response zip file
response = request.urlopen(url)

#opening zipfile and converting it into a dict using json.loads
with gzip.open(response, 'r') as zipfile:
    response_data = zipfile.read()
    json_data = json.loads(response_data)

subs = json_data['submissions']

#for every submission
for sub in subs:
    filename = ''.join(letter for letter in sub['challenge'] if letter.isalnum())

    #if file already exists add a comment and the next solution
    if os.path.exists('..\{}.py'.format(filename)):
        file = open('..\{}.py'.format(filename), 'a')
        file.write("\n\n\n'''#Next solution'''\n\n")
    else:
        file = open('..\{}.py'.format(filename), 'a')
    file.write(sub['code'])
    file.close()

#changing directory
os.chdir('..')
print(os.system('dir'))

#pushing to git
os.system('git add *')
os.system('git commit -m "automatic commit"')
os.system('git push -u origin master')

#Cleaning directory
# os.system('del /f *.py')
