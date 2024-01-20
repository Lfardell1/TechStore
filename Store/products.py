import pandas as pd
from models import StoreCategories , StoreProduct


def import_data(file_path):
    # Read Excel file into a DataFrame
    df = pd.read_csv(file_path)
    categories = StoreCategories.objects.all()
    # first iterate through the categories and create them
    for index, row in df.iterrows():
        if row['category'] not in categories:
                    categories = StoreCategories.objects.all()
                    
                    StoreCategories.objects.create(
                    Name=row['category']
                    )
        else:
            StoreCategories.objects.create(
                    Name=row['category']
                    )
    
    # Iterate through rows and create Django model objects
    for index, row in df.iterrows():
        StoreProduct.objects.create(
            Name=row['name'],
            Stock=row['stock'],
            Description=row['description'],
            CostPrice = 1/2 * row['price'],
            Image=row['image'],
            Sales=row['sales'],
            
            )
        print("adding: " + row['name'] , " to database and at index " , index)
   
print("Done")
            

# Usage example
import_data('../../TechStore/data/amazon.csv')