import requests
from plotly.graph_objects import Bar
from plotly import offline

# Make an API call and store the response/value
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
header = {"Accept": "application/vnd.github.v4+json"}
r = requests.get(url, headers=header)
print(f"Status ocde : {r.status_code}")
response_dicts = r.json()

# Storing items in a variable and making an empty lists

item = response_dicts['items']
repo_links, stars, label = [], [], []

# Processing results through looping and searching for the items

for items in item:
    repo_name=items['name']
    repo_url=items['html_url']

    owner = items['owner'] ['login']
    description=items['description']

    stars.append(items['stargazers_count'])
    label.append(f'{owner}<br />{description}')
    repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")

# Making the visualization

data=[{'type': 'bar',
       'x': repo_links,
       'y': stars,
       'hovertext':label,
       'marker':{
           'color':'rgb(60,100,150)',
           'line': {
               'width': 1.5, 'color': 'rgb(25,25,25)'}
       },
       'opacity': 0.6,
       }]

my_layout = {'title': 'Most-Starred Python Projects on Github',
           'xaxis': {
               'title': 'Repositories',
           'titlefont': {'size': 24},
           'tickfont': {'size':14}
           },

           'yaxis': {'title':'Amount of stars',
                     'titlefont': {'size': 24},
                     'tickfont': {'size':14}
                     }
             }

# Running the graph and storing it 

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="Repositories.html")