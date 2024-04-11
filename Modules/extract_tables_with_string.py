import os
import camelot
import pandas as pd
import fitz 


def extract_tables_with_string(pdf_path, string, index_offset=0, header_change=False, column_names=None):
    """
    Extract tables from PDF containing a specific string and perform operations on them.

    Parameters:
        pdf_path (str): Path to the PDF file.
        string (str): String to search for in the tables.
        index_offset (int): Offset for row index slicing.
        header_change (bool): Flag to indicate whether to change the header of the table.
        column_names (list): List of column names for renaming.

    Returns:
        list: List of DataFrames containing tables with the specified string.
    """
    tables_with_string = []
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    tables = camelot.read_pdf(pdf_path, flavor='stream', table_areas=['0,780,1000,1'], pages='all')

    for table in tables:

        # print(table.df.head(4))
        
        if any(string in cell for row in table.data for cell in row):

            # print(f'\nTabla en bruto')
            # print(table.df.head(15))
            table.df = table.df[~table.df.apply(lambda row: any('BARCELONA/Josep' in str(cell) for cell in row), axis=1)]
            table.df = table.df.iloc[index_offset:].reset_index(drop=True)
            # print(f'\nTabla con reseteo de idx y cabecera')
            # print(table.df.head(5))

            if header_change:
                table.df.columns = table.df.iloc[0]
                table.df = table.df.iloc[1:].reset_index(drop=True)
                table.df = table.df[table.df['WPT'].apply(lambda x: len(str(x)) <= 6)].reset_index(drop=True)
                table.df = table.df[table.df['COORD'].str.contains('º')].reset_index(drop=True)

            elif column_names:
                table.df = table.df[~table.df.apply(lambda row: any('TABULAR' in str(cell) for cell in row), axis=1)]
                table.df = table.df[~table.df.apply(lambda row: any('DESCRIPTION' in str(cell) for cell in row), axis=1)]
                columns_to_drop = table.df.iloc[:5].apply(lambda col: all(col == ''), axis=0)
                table.df = table.df.loc[:, ~columns_to_drop]
                table.df.columns = column_names

                # print(f'\nTabla con PROCEDIMIENTO tras procesado')
                # print(table.df.head(5))

            table.df.insert(0, 'Name_PDF', pdf_name)
            tables_with_string.append(table.df)

            



    return tables_with_string