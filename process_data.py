import pandas as pd
import os

def process_data(input_dir, output_file):
    ratings_file = os.path.join(input_dir, 'ml-100k/u.data')
    data = pd.read_csv(ratings_file, sep='\t', header=None, names=['user_id', 'movie_id', 'rating', 'timestamp'])
    data.to_csv(output_file, index=False)
    print(f'Data processed and saved to {output_file}.')

if __name__ == "__main__":
    process_data('ml-100k', 'ratings.csv')
