from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('template.html')

data = {
    'band_info': {
        'name': 'とあるBand',
        'genre': 'Rock',
        'members': ['a', 'abc', 'あああ'],
    },
    'news': [
        {
            'title': 'New Album Release',
            'date': '2023-09-01',
            'content': 'Our band has released a new album. Check it out!',
        },
        {
            'title': 'Upcoming...',
            'date': '2023-09-10',
            'content': 'Don\'t miss our upcoming concert on June 10th.',
        },
    ],
}

# data = {
#     'title': 'Jinja2 Example',
#     'name': 'exampleName',
#     'content': 'This is an example of data integration with Jinja2.',
# }

output = template.render(data)

# with open('./band.html', 'w') as f:
#     f.write(output)

print(output)
