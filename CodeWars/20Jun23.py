from re import search,match,findall

# Breaking search bad | 6 Kyu

def search(titles, term): 
    return [title for title in titles if term.lower() in title.lower()]

titles = ['Rocky 1', 'Rocky 2', 'My Little Poney']
print(search(titles, 'ock'))