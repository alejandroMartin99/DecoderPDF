import os
import camelot
import pandas as pd
import fitz 

def compare_and_save_tables(tables):

    combined_tables = [pd.concat(df_list, axis=1) for df_list in tables]
    combined_tables = pd.concat(combined_tables, axis=1)

    print(combined_tables)
    
    combined_tables.columns = [f'{col}_X' if i < len(combined_tables.columns)//2 else f'{col}_Y' for i, col in enumerate(combined_tables.columns)]
    
    exclude_columns = ['Name_PDF']
    relevant_columns = [col for col in combined_tables.columns if not any(exclude_col in col for exclude_col in exclude_columns)]

    combined_tables['Change'] = 'check'
    combined_tables['Evidence'] = ''

    for column in relevant_columns:
        base_column_name = column[:-2]
        condition = combined_tables[f'{base_column_name}_X'] != combined_tables[f'{base_column_name}_Y']
        Condition2 = combined_tables[base_column_name + '_X'] == combined_tables[column]

        combined_tables.loc[condition, 'Change'] = True
        combined_tables.loc[condition & Condition2, 'Evidence'] += f'{base_column_name}-'

    return combined_tables