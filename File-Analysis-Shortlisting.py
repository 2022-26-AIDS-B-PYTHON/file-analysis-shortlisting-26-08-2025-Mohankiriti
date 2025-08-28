import pandas as pd

def marks_summary(marks_csv):
    df = pd.read_csv(marks_csv)
    df['Total'] = df.iloc[:, 1:].sum(axis=1)
    df = df.sort_values('Total', ascending=False)

    # Display full table
    print("\nFull Student Marks (Highest to Lowest):")
    print(df.to_string(index=False))

    # Top & bottom 10 by total
    print("\nTop 10 Students by Total Marks:")
    print(df.head(10).to_string(index=False))

    print("\nLeast 10 Students by Total Marks:")
    print(df.tail(10).to_string(index=False))

    # Ask user for threshold
    threshold = int(input("\nEnter a mark as threshold: "))

    # 10 nearest above
    above = df[df['Total'] > threshold].sort_values('Total').head(10)
    # 10 nearest below
    below = df[df['Total'] < threshold].sort_values('Total', ascending=False).head(10)

    print(f"\nTop 10 Students with Total Marks JUST ABOVE {threshold}:")
    print(above.sort_values('Total', ascending=False).to_string(index=False))

    print(f"\nTop 10 Students with Total Marks JUST BELOW {threshold}:")
    print(below.to_string(index=False))

if __name__ == "__main__":
    marks_summary('marks.csv')  