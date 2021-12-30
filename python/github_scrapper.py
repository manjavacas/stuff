
import json
import requests
import pandas

from lxml import html

username = 'manjavacas'
token = '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'
headers = {'Authorization': f'token {token}'}
params = {
    'state': 'open',
}

file = open('repos.txt', 'r')
projects = file.readlines()

data = []

for project in projects:

    project_info = {}
    
    # Name and owner
    l = project.split('/')
    owner = l[0]
    repo = l[1].strip()

    project_info['name'] = repo
    project_info['creator'] = owner

    url_repo = f'https://github.com/{owner}/{repo}'
    url_api = f'https://api.github.com/repos/{owner}/{repo}'

    print('\nReading from: ' + url_api)
    
    # Stars, open issues and forks
    response = requests.get(url_api, headers=headers, params=params)
    json_data = json.loads(response.text)

    project_info['stars'] = json_data['stargazers_count']
    project_info['open_issues'] = json_data['open_issues_count']
    project_info['forks'] = json_data['forks_count']

    # Pull requests
    response = requests.get(url_repo, headers=headers, params=params)    
    content = html.fromstring(response.content)

    xpath_content = content.xpath('/html/body/div[4]/div/main/div[1]/nav/ul/li[3]/a/span[2]/@title')

    if len(xpath_content) > 0:
        project_info['pull_requests'] = xpath_content[0]
    else:
        project_info['pull_requests'] = 'NA'

    # Contributors
    xpath_content = content.xpath('/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[2]/div/div[5]/div/h2/a/span/@title')

    if len(xpath_content) > 0:
        project_info['contributors'] = xpath_content[0]
    else:
        project_info['contributors'] = 'NA'

    # Branches
    xpath_content = content.xpath('/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/a[1]/strong')
    
    if len(xpath_content) > 0:
        project_info['branches'] = xpath_content[0].text
    else:
        project_info['branches'] = 'NA'

    # Commits
    xpath_content = content.xpath('/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]/ul/li/a/span/strong')

    if len(xpath_content) > 0:
        project_info['commits'] = xpath_content[0].text
    else:
        project_info['commits'] = 'NA'

    # Save
    data.append(project_info)
    print(project_info)
    print(f'{repo}/{owner} saved!')


df = pandas.DataFrame(data)
print(df)

df.to_csv('table.csv')

