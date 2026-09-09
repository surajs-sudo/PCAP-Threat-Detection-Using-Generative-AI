import pandas as pd
import os


# Automatically detect project folder
project_folder = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


data_folder = os.path.join(
    project_folder,
    "07_Source_Data"
)


files = [
    "traffic_segment_1.csv",
    "traffic_segment_2.csv",
    "traffic_segment_3.csv"
]


combined_data = []


for file in files:

    file_path = os.path.join(
        data_folder,
        file
    )

    print("Reading:", file_path)

    df = pd.read_csv(file_path)

    df["Source_File"] = file

    combined_data.append(df)


combined_df = pd.concat(
    combined_data,
    ignore_index=True
)


output_file = os.path.join(
    data_folder,
    "Combined_Traffic_Data.csv"
)


combined_df.to_csv(
    output_file,
    index=False
)


print("--------------------------------")
print("Combined dataset created")
print("Total records:", len(combined_df))
print("Saved:", output_file)
print("--------------------------------")