# from faker import Faker
# import pandas as pd
# import random

# # Initialize Faker
# fake = Faker()

# # Parameters
# num_samples = 100  # Number of data points

# # Function to generate a dataset
# def generate_dataset(num_samples):
#     data = {
#         'cgpa': [],
#         'score': [],
#         'placed': []
#     }
    
#     for _ in range(num_samples):
#         cgpa = round(random.uniform(0, 10), 2)
#         score = round(random.uniform(0, 9), 2)
        
#         # Determine placement
#         placed = 1 if cgpa > 5.5 and score > 5.5 else 0
        
#         data['cgpa'].append(cgpa)
#         data['score'].append(score)
#         data['placed'].append(placed)
    
#     return pd.DataFrame(data)

# # Generate the dataset
# df = generate_dataset(num_samples)

# # Display the first few rows of the dataset
# print(df.head(10))

# df.to_csv("LogRe_FakeData.csv",index=False)


from faker import Faker
import pandas as pd
import random

# Initialize the Faker object
fake = Faker()

# Define the number of samples you want to generate
num_samples = 1000

# Generate the dataset
data = {
    'Age': [random.randint(18, 65) for _ in range(num_samples)],
    'EstimatedSalary': [random.randint(20000, 150000) for _ in range(num_samples)],
    'Purchased': [random.randint(0, 1) for _ in range(num_samples)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head(10))


df.to_csv("Purchase.csv",index=False)