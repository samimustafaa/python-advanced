import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a table called a DataFrame
df = pd.read_csv("avgIQpercountry.csv")

# Keep only rows where the country is Albania
# .str.strip() removes spaces at the beginning and end
# .str.lower() converts text to lowercase
# This also matches values like "ALBANIA" or " Albania "
filtered_df = df[df["Country"].str.strip().str.lower() == "albania"]

# Display Albania's data in the terminal
print(filtered_df)

# Check whether Albania was found
if filtered_df.empty:
    print("Albania was not found in the CSV file.")
else:
    # Create a chart that is 7 inches wide and 6 inches tall
    plt.figure(figsize=(7, 6))

    # Draw a bar using the country name and its Average IQ value
    # Store the bars so we can add number labels later
    bars = plt.bar(
        filtered_df["Country"],
        filtered_df["Average IQ"],
        color="skyblue",
        width=0.4
    )

    # Set the chart title and axis labels
    plt.title("Average IQ in Albania (CSV data)", fontsize=16)
    plt.xlabel("Country", fontsize=14)
    plt.ylabel("Average IQ", fontsize=14)

    # Set the font size of the labels along both axes
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Put gridlines behind the bars
    plt.gca().set_axisbelow(True)

    # Add horizontal dashed gridlines
    # alpha=0.3 makes them partially transparent
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    # Display each bar's value above it
    plt.bar_label(
        bars,
        fmt="%.2f",       # Show exactly 2 decimal places
        fontsize=12,     # Size of the number labels
        color="black",   # Color of the number labels
        padding=5        # Distance from the bar, in points
    )

    # Add vertical space so the number labels fit
    plt.margins(y=0.15)

    # Adjust spacing to prevent labels from being cut off
    plt.tight_layout()

    # Open the chart window
    plt.show()