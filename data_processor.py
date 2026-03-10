import pandas as pd

def convert_board_to_df(board):

    rows = []

    for item in board["items_page"]["items"]:

        row = {"Item Name": item["name"]}

        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]

        rows.append(row)

    df = pd.DataFrame(rows)

    return df