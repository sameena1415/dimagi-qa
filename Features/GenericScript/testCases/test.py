import unittest
import os
from pages.data_generator_page import DataGeneratorPage

class TestDataGeneratorPage(unittest.TestCase):

    def setUp(self):
        self.generator = DataGeneratorPage()
        self.num_rows = 100

    def test_data_generation_length(self):
        df = self.generator.generate_data(self.num_rows)
        self.assertEqual(len(df), self.num_rows, "Row count mismatch")

    def test_column_names_match(self):
        df = self.generator.generate_data(self.num_rows)
        expected_columns = list(self.generator.schema_df['Column Name'])
        self.assertEqual(list(df.columns), expected_columns, "Columns do not match schema")

    def test_data_file_creation(self):
        df = self.generator.generate_data(self.num_rows)
        self.generator.save_data(df)
        self.assertTrue(os.path.exists(self.generator.output_path), "Output file not created")

if __name__ == '__main__':
    unittest.main()
