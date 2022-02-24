import pandas as pd
import sqlite3
import json
from lxml import etree as ET

class Convoy:

    def __init__(self):
        self.file_name = None
        self.file_name_check = None
        self.count = []
        self.df = None
        self.df2 = None
        self.n = 0
        self.excel_file = None
        self.conn = None
        self.cur = None
        self.file_name_check_db = None
        self.fn_json = None
        self.score_list = []

    def choose_file(self):
        self.file_name = input('Input file name\n')
        if self.file_name.endswith('.s3db'):
            self.file_name_check_db = self.file_name
        elif self.file_name.endswith('[CHECKED].csv'):
            self.file_name_check = self.file_name
            self.setup_db()
            self.count_db_rows()
        else:
            if self.file_name.endswith('.xlsx'):
                self.xlsx_file()
                self.shape_(self.df)
                self.count_cells(self.df)
                self.remove_alpha(self.df)
                self.data_to_csv(self.df)
            elif self.file_name.endswith('.csv'):
                self.df = pd.read_csv(self.file_name)
                self.count_cells(self.df)
                self.remove_alpha(self.df)
                self.data_to_csv(self.df)
            self.setup_db()
            self.count_db_rows()
        self.sqlite_to_df()
        self.to_jsonfile()
        self.to_xmlfile()


    def create_connection(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def setup_db(self):
        self.df = pd.read_csv(self.file_name_check)
        self.scoring()
        self.df['score'] = self.score_list
        column_names = list(self.df.columns.values)
        file_name = self.file_name_check.split('[')[0]
        self.file_name_check_db = file_name + '.s3db'
        self.create_connection(self.file_name_check_db)

        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS convoy (
                                {column_names[0]} INTEGER PRIMARY KEY,
                                {column_names[1]} INTEGER NOT NULL,
                                {column_names[2]} INTEGER NOT NULL,
                                {column_names[3]} INTEGER NOT NULL,
                                {column_names[4]} INTEGER NOT NULL
                           );''')

        output = self.df.itertuples(index=False)
        data = tuple(output)
        insert_sql = f'INSERT OR REPLACE INTO convoy ({column_names[0]}, {column_names[1]}, {column_names[2]}, {column_names[3]}, {column_names[4]}) VALUES (?, ?, ?, ?, ?)'
        self.conn.executemany(insert_sql, data)
        self.conn.commit()

    def scoring(self):
        n = 0
        while n < self.df.shape[0]:
            a = self.df.loc[n, 'engine_capacity']
            b = self.df.loc[n, 'fuel_consumption']
            c = self.df.loc[n, 'maximum_load']
            score = 0
            check1 = 450 / (a / (b / 100))
            if check1 <= 1:
                score += 2
            elif 1 <= check1 <= 2:
                score += 1
            else:
                pass
            # check2
            if b <= 230:
                score += 2
            elif b > 230:
                score += 1
            # check3
            if c >= 20:
                score += 2
            self.score_list.append(score)
            n += 1
        return self.score_list

    def count_db_rows(self):
        self.cur.execute('SELECT COUNT(*) from convoy')
        cur_result = self.cur.fetchone()
        if max(cur_result) == 1:
            print(f"1 record was inserted into {self.file_name_check_db}")
        else:
            print(f"{max(cur_result)} records were inserted into {self.file_name_check_db}")

    def xlsx_file(self):
        self.df = pd.read_excel(self.file_name, sheet_name='Vehicles', dtype=str)
        file_name = self.file_name.split('.')[0]
        self.file_name = file_name + '.csv'
        self.df.to_csv(self.file_name, index=None, header=True)
        self.df = pd.read_csv(self.file_name)
        return self.df

    def remove_alpha(self, data_frame):
        for col in data_frame:
            data_frame[col] = data_frame[col].str.replace(r'([a-z._ ])', '', regex=True)

    def count_cells(self, data_frame):
        for col in data_frame:
            self.count.append(max(data_frame[data_frame[col].str.count('[a-z._ ]')>0].count()))
        self.count = sum(self.count)
        return self.count

    def data_to_csv(self, data_frame):
        fn = self.file_name.split('.')[0]
        self.file_name_check = fn + '[CHECKED].csv'
        data_frame.to_csv(self.file_name_check, index=None, header=True)
        print(f"{self.count} cells were corrected in {self.file_name_check}")
        return self.file_name_check

    def shape_(self, data_frame):
        if data_frame.shape[0] == 1:
            print(str(data_frame.shape[0]) + f" line was added to {self.file_name}")
        elif data_frame.shape[0] > 1:
            print(str(data_frame.shape[0]) + f" lines were added to {self.file_name}")

    def sqlite_to_df(self):
        self.create_connection(self.file_name_check_db)
        self.df = pd.read_sql("SELECT * FROM convoy WHERE score>3", con=self.conn)
        self.df.drop('score', axis=1, inplace=True)
        return self.df

    def to_jsonfile(self):
        file_name = self.file_name_check_db.split('.')[0]
        self.fn_json = file_name + '.json'
        self.df.to_json(self.fn_json, orient='records')
        with open(self.fn_json, 'r') as openfile:
            json_object = json.load(openfile)
        json_object2 = {"convoy":json_object}
        with open(self.fn_json, 'w') as outfile:
            json.dump(json_object2, outfile)
        x = len(json_object2["convoy"])
        if x == 1:
            print(f"1 vehicle was saved in {self.fn_json}")
        else:
            print(f"{x} vehicles were saved into {self.fn_json}")

    def to_xmlfile(self):
        file_name = self.file_name_check_db.split('.')[0]
        fn_xml = file_name + '.xml'
        self.df.to_xml(fn_xml, index=False, root_name='convoy', xml_declaration=False, row_name='vehicle') # attr_col=['vehicle_id', 'engine_capacity', 'fuel_consumption', 'maximum_load'])
        xml = ET.parse(fn_xml).getroot()
        count = []
        for item in xml.findall('vehicle'):
            count.append(item)
        if len(count) == 1:
            print(f"1 vehicle was saved into {fn_xml}")
        else:
            print(f"{len(count)} vehicles were saved into {fn_xml}")

current_convoy = Convoy()
current_convoy.choose_file()

