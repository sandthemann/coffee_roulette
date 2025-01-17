from faker import Faker
import pandas as pd
import random

def employees(number=50, seed = 100):

    fake = Faker()
    Faker.seed(seed)
    random.seed(seed)

    teams = {'Eagles':['Bald', 'Great', 'Golden'], 'Bears':['Polar', 'Black', 'Grizzly']}
    
    def random_group(team):
        return fake.random_element(teams[team])

    data = []
    for _ in range(number):
        data.append({
            'name': fake.name(),
            'email': fake.email(),
            'job': fake.job().split(',')[0],
            'team': fake.random_element(teams.keys())
        })

    df = pd.DataFrame(data)

    

    df['group'] = df['team'].apply(random_group)
    df['active'] = pd.Series([random.randint(1,10) for i in range(len(df))]).apply(lambda x: 0 if x >= 9 else 1)
    df.insert(0, 'id', df.index + 1)
    return df