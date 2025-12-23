print("SCRIPT STARTED")
import pandas as pd
import matplotlib as plt
df = pd.read_csv("data/students.csv",sep="\t")
print("DATA LOADED")
print("Columns in CSV:", df.columns)
print(df.head())
# Average score per subject
print("\nAverage scores per subject:")
print(df.mean(numeric_only=True))
# Highest scorer per subject
print("\nHighest scorer per subject:")
print(df.loc[df[['math','science','english']].idxmax()])
# Students below 70 in any subject
print("\nStudents scoring below 70 in any subject:")
print(df[(df['math'] < 70) | (df['science'] < 70) | (df['english'] < 70)])
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV (tab or comma separated, depending on your file)
df = pd.read_csv("data/students.csv", sep='\t')  # change sep=',' if CSV is proper comma-separated
print("Dataset loaded:\n", df)

# Average score per subject
avg_scores = df[['math','science','english']].mean()
print("\nAverage scores per subject:\n", avg_scores)

# Highest scorer per subject
top_scorers = df.loc[df[['math','science','english']].idxmax()]
print("\nHighest scorer per subject:\n", top_scorers)

# Students below 70 in any subject
below_70 = df[(df['math']<70) | (df['science']<70) | (df['english']<70)]
print("\nStudents scoring below 70 in any subject:\n", below_70)


# 1️⃣ Average scores bar chart
avg_scores.plot(kind='bar', title='Average Scores per Subject')
plt.ylabel('Score')
plt.show()

# 2️⃣ Top score per subject bar chart
top_scores_values = df[['math','science','english']].max()
top_scores_values.plot(kind='bar', title='Top Score per Subject', color='green')
plt.ylabel('Score')
plt.show()

# 3️⃣ Number of students below 70 per subject
bad_counts = {
    'math': (df['math']<70).sum(),
    'science': (df['science']<70).sum(),
    'english': (df['english']<70).sum()
}
plt.bar(bad_counts.keys(), bad_counts.values(), color='red')
plt.title('Number of Students Below 70 per Subject')
plt.ylabel('Count')
plt.show()
