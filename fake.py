from faker import Faker
import pandas as pd

fake=Faker()

name=[]
phone=[]
age=[]

num_records=100


for _ in range(num_records):
    name.append(fake.name())
    phone.append(fake.numerify('##########'))
    age.append(fake.random_int(min=18,max=45))

df=pd.DataFrame({
    'Name':name,
    'Phone':phone,
    'Age':age
})

print(df.head(10))