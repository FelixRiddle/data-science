from dataset import load_dataset


def main():
    """Run example 1"""
    df = load_dataset("Titanic-Dataset.csv")

    if df is not None:
        print("\n--- Dataset Preview ---")
        print(df.head())  # Shows first 5 rows

        print("\n--- Column Info ---")
        print(df.info())  # Shows data types and non-null counts
