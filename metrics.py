import pandas as pd
from jiwer import wer

ground_truth = pd.read_csv("ground_truth.csv")
predictions = pd.read_csv("output/whisper_output.csv")


df = pd.merge(
    ground_truth,
    predictions,
    on="filename"
)


for index, row in df.iterrows():

    actual = row["ground_truth"]
    predicted = row["transcript"]

    error = wer(actual, predicted)

    print("\nFile:", row["filename"])
    print("Actual:", actual)
    print("Predicted:", predicted)
    print("WER:", round(error, 2))