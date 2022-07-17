import pandas as pd


if __name__ == '__main__':
    main_df = pd.read_excel(r'data/main_df.xlsx')
    meta_data = pd.read_csv(r"data/titles.test.csv")
    merged_df = pd.merge(main_df, meta_data, left_on=main_df.iloc[:, 0], right_on=meta_data.iloc[:, 0])
    merged_df = merged_df.drop(columns=['key_0', 'Unnamed: 0_x', 'Unnamed: 0_y'])
    merged_df.to_excel('data/merged_df.xlsx')
    merged_df = merged_df.drop_duplicates(subset=['conceptUri'])
    merged_df.to_excel('data/unique_merged_df.xlsx')