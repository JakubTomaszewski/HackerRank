import json
import os
from urllib import request
import gzip

url = 'https://s3.amazonaws.com/downloads.hackerrank.com/hacker_gdpr_data/jakub_k_tomasze1oWje7DgWmNoZ18HjJhYt_AoWje7DgWmNoZ18HjJhYt_AoWje7DgWmNoZ18HjJhYt_A.json.gz?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1580832734&Signature=pYjVk5LArNbzj54I7BiTOGe1anE%3D&response-content-disposition=attachment%3B%20filename%3Djakub_k_tomasze1_data.json.gz&response-content-type=application%2Foctet-stream'

response = request.urlopen(url)

with gzip.open(response, 'r') as zipfile:
    response_data = zipfile.read()
    json_data = json.loads(response_data)

subs = json_data['submissions']

for sub in subs:
    file = open('..\{}.py'.format(''.join(letter for letter in sub['challenge'] if letter.isalnum())), 'w') #moze zmienic mode na 'a' zeby się dopisywało
    file.write(sub['code'])
    file.close()

#changing directory
os.chdir('..')
print(os.system('dir'))

#pushing to git
os.system('git add *')
os.system('git commit -m "automatic commit"')
os.system('git push -u origin master')

# some sub names may be duplicates, due to many submissions(solutions) of one challenge
# thus, if the filename is the same, add the code to the existing file
# to finish





