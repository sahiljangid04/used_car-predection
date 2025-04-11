import pandas as pd
import matplotlib.pyplot as plt

# Data for the table (replace these values with your actual model results)
data = {
    "Model": ["Decision Tree", "Random Forest", "Linear Regression", "KNN", "SVM"],
    "Accuracy": ["78.21%", "81.56%", "80.22%", "79.89%", "83.12%"],
    "Precision": ["71.88%", "77.27%", "76.47%", "75.51%", "79.31%"],
    "Recall": ["65.85%", "69.51%", "67.07%", "66.67%", "71.95%"],
    "F1-Score": ["68.71%", "73.20%", "71.47%", "70.80%", "75.45%"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting the table
fig, ax = plt.subplots(figsize=(10, 2))  # Adjust size as needed
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.auto_set_column_width(col=list(range(len(df.columns))))

# Display the table
plt.show()