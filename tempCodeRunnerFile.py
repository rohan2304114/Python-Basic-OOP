def famousName(first ,last, **addition):
    name = f'{first} {last} '
    for key, value in addition.items():
        name+=f'{key}: {value} '
        return name
    
name=famousName(first="Asikur",last="Rahman",first_name="Rohan",last_name="Bhuiyan")