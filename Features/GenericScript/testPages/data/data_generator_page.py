import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

class DataGeneratorPage:
    def __init__(self, config_path='userinputs/config.xlsx', output_path='output/generated_data.csv'):
        self.config_path = config_path
        self.output_path = output_path
        self.fake = Faker()
        self.schema_df = pd.read_excel(self.config_path, sheet_name='Schema')

    def generate_value(self, row):
        dtype = row['Data Type']
        if dtype == 'int':
            return random.randint(int(row['Min']), int(row['Max']))
        elif dtype == 'name':
            return self.fake.name()
        elif dtype == 'email':
            return self.fake.email()
        elif dtype == 'date':
            start_date = datetime.now() - timedelta(days=5 * 365)
            return self.fake.date_between(start_date=start_date, end_date='today')
        elif dtype == 'choice':
            options = [opt.strip() for opt in str(row['Options']).split(',')]
            return random.choice(options)
        else:
            return 'N/A'

    def generate_data(self, num_rows=100):
        data = []
        for _ in range(num_rows):
            row_data = {}
            for _, row in self.schema_df.iterrows():
                column_name = row['Column Name']
                row_data[column_name] = self.generate_value(row)
            data.append(row_data)
        return pd.DataFrame(data)

    def save_data(self, df):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        df.to_csv(self.output_path, index=False)
        print(f"[INFO] Data saved to: {self.output_path}")
