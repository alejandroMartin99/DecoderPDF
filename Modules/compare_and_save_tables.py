import pandas as pd

def compare_and_save_tables(tables):

    combined_tables = [pd.concat(df_list, axis=1) for df_list in tables]
    combined_tables = pd.concat(combined_tables, axis=1)
    combined_tables.columns = [f'{col}_X' if i < len(combined_tables.columns)//2 else f'{col}_Y' for i, col in enumerate(combined_tables.columns)]

    exclude_columns = [col for col in combined_tables.columns if col.startswith('Name_PDF')]
    other_columns = [col for col in combined_tables.columns if col not in exclude_columns]
    other_columns.sort()
    ordered_columns = exclude_columns + other_columns
    combined_tables = combined_tables[ordered_columns]
    combined_tables = combined_tables.astype(str)

    for col_x in other_columns:
        if col_x.endswith('_X'):
            col_y = col_x[:-2] + '_Y'
            comparison_col_name = f'{col_x[:-2]}__Check'
            if col_y in combined_tables.columns:
                comparison_result = (combined_tables[col_x] == combined_tables[col_y]).astype(str).replace({'True': 'Y', 'False': 'X'})
                combined_tables[comparison_col_name] = comparison_result

    exclude_columns = [col for col in combined_tables.columns if col.startswith('Name_PDF')]
    other_columns = [col for col in combined_tables.columns if col not in exclude_columns]
    other_columns.sort()
    ordered_columns = exclude_columns + other_columns
    combined_tables = combined_tables[ordered_columns]

    return combined_tables


