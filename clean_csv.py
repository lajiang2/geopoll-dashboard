import pandas as pd
from datetime import datetime as dt
import glob, os, sys

# Shows
AK = 'Akili and Me'
UK = 'Ubongo Kids'
UE = 'Umuhimu wa Elimu'
# Languages
EN = 'EN'
SW = 'SW'
ENSW = 'ENSW'
# Stations
AZAM_ONE = 'Azam One'
AZAM_TWO = 'Azam Two'
EATV = 'East Africa TV'
TBC_ONE = 'TBC1'
TBC_TWO = 'TBC2'
CITIZEN = 'Citizen'
NTV = 'NTV'
TV_THREE = 'TV3'
AIT = 'AIT'
NTA = 'NTA'
WAZOBIA = 'Wazobia TV'
RTV = 'Rwanda TV'
# Start Dates
TV_THREE_DATE = dt.strptime('2/1/2019', '%d/%m/%Y')
CITIZEN_DATE = dt.strptime('30/1/2019', '%d/%m/%Y')
AIT_DATE = dt.strptime('11/10/2018', '%d/%m/%Y')
NTA_DATE = dt.strptime('27/1/2018', '%d/%m/%Y')
RTV_DATE = dt.strptime('27/1/2018', '%d/%m/%Y')
WAZOBIA_DATE = dt.strptime('25/3/2019', '%d/%m/%Y')
TBC_ONE_DATE = dt.strptime('8/4/2016', '%d/%m/%Y')
EATV_DATE = dt.strptime('2/3/2018', '%d/%m/%Y')
AZAM_ONE_DATE = dt.strptime('29/12/2018', '%d/%m/%Y')
AZAM_TWO_DATE = dt.strptime('29/12/2018', '%d/%m/%Y')
NTV_DATE = dt.strptime('02/06/2018', '%d/%m/%Y')

frames = []

def filter_ghana(data):
    for i, row in data.iterrows():
        day = row['Day of Week']
        time = row['Time Block']
        station = row["Station"]
        date = dt.strptime(row['Date'], '%d/%m/%Y')
        show = 'None'
        language = 'None'
        if day == 'Wednesday':
            if time == '17:00':
                if station == TV_THREE and date >= TV_THREE_DATE:
                    show, language = UK, EN
            if time == '17:30':
                if station == TV_THREE and date >= TV_THREE_DATE:
                    show, language = UK, EN
        data.at[i, 'Show'] = show
        data.at[i, 'Language'] = language
        
    data = data[data['Show'] != 'None']
    data = data[data['Viewers'] != 0]

    return data

def filter_kenya(data):
    for i, row in data.iterrows():
        day = row['Day of Week']
        time = row['Time Block']
        station = row["Station"]
        date = dt.strptime(row['Date'], '%d/%m/%Y')
        show = 'None'
        language = 'None'
        if day == 'Saturday':
            if time == '09:00':
                if station == CITIZEN and date >= CITIZEN_DATE:
                    show, language = AK, EN
        elif day == 'Sunday':
            if time == '09:30':
                if station == CITIZEN and date >= CITIZEN_DATE:
                    show, language = UK, SW
        data.at[i, 'Show'] = show
        data.at[i, 'Language'] = language
        
    data = data[data['Show'] != 'None']
    data = data[data['Viewers'] != 0]

def filter_nigeria(data):
    for i, row in data.iterrows():
        day = row['Day of Week']
        time = row['Time Block']
        station = row['Station']
        date = dt.strptime(row['Date'], '%d/%m/%Y')
        show = 'None'
        language = 'None'
        if day == 'Monday':
            if time == '16:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '16:30':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '17:00':
                if station == NTA and date >= NTA_DATE:
                    show, language = UK, EN
                elif station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
        elif day == 'Tuesday':
            if time == '16:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '16:30':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
            elif time == '17:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
        elif day == 'Wednesday':
            if time == '16:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '16:30':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '17:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
            elif time == '17:30':
                if station == NTA and date >= AIT_DATE:
                    show, language = UK, EN
        elif day == 'Thursday':
            if time == '16:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '16:30':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
            elif time == '17:00':
                if station == AIT and date >= AIT_DATE:
                    show, language = AK, EN
                elif station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
        elif day == 'Friday':
            if time == '16:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '16:30':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '17:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
        elif day == 'Saturday':
            if time == '06:30':
                if station == AIT and date >= AIT_DATE:
                    show, language = AK, EN
                elif station == NTA and date >= NTA_DATE:
                    show, language = UK, EN
            elif time == '07:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '07:30':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '08:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
        elif day == 'Sunday':
            if time == '07:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = AK, EN
            elif time == '07:30':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
            elif time == '08:00':
                if station == WAZOBIA and date >= WAZOBIA_DATE:
                    show, language = UK, EN
        data.at[i, 'Show'] = show
        data.at[i, 'Language'] = language
        
    data = data[data['Show'] != 'None']
    data = data[data['Viewers'] != 0]

    return data

def filter_rwanda(data):
    for i, row in data.iterrows():
        day = row['Day of Week']
        time = row['Time Block']
        station = row['Station']
        date = dt.strptime(row['Date'], '%d/%m/%Y')
        show = 'None'
        language = 'None'
        if day == 'Monday':
            if time == '16:30':
                if station == RTV and date >= RTV_DATE:
                    show, language = AK, EN
        elif day == 'Tuesday':
            if time == '16:30':
                if station == RTV and date >= RTV_DATE:
                    show, language = AK, EN
        elif day == 'Wednesday':
            if time == '16:30':
                if station == RTV and date >= RTV_DATE:
                    show, language = AK, EN
        elif day == 'Thursday':
            if time == '16:30':
                if station == RTV and date >= RTV_DATE:
                    show, language = UK, EN
        elif day == 'Friday':
            if time == '16:30':
                if station == RTV and date >= RTV_DATE:
                    show, language = UK, EN
        data.at[i, 'Show'] = show
        data.at[i, 'Language'] = language

    data = data[data['Show'] != 'None']
    data = data[data['Viewers'] != 0]

    return data

def filter_tanzania(data):
    for i, row in data.iterrows():
        day = row['Day of Week']
        time = row['Time Block']
        station = row['Station']
        date = dt.strptime(row['Date'], '%d/%m/%Y')
        show = 'None'
        language = 'None'
        if day == 'Monday':
            if time == '08:00':
                if station == AZAM_ONE and date >= AZAM_ONE_DATE:
                    show, language = AK, EN
            elif time == '14:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = AK, SW
            elif time == '16:30':
                if station == EATV and date >= EATV_DATE:
                    show, language = AK, SW
                elif station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = UE, SW
            elif time == '17:30':
                if station == AZAM_TWO and date >= AZAM_TWO_DATE:
                    show, language = AK, SW
        elif day == 'Tuesday':
            if time == '08:00':
                if station == AZAM_ONE and date >= AZAM_ONE_DATE:
                    show, language = UK, EN
            elif time == '14:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = AK, SW
            elif time == '16:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = UE, SW
            elif time == '17:30':
                if station == AZAM_TWO and date >= AZAM_TWO_DATE:
                    show, language = UK, SW
        elif day == 'Wednesday':
            if time == '08:00':
                if station == AZAM_ONE and date >= AZAM_ONE_DATE:
                    show, language = AK, EN
            elif time == '14:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = AK, SW
            elif time == '16:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = UE, SW
            elif time == '17:30':
                if station == AZAM_TWO and date >= AZAM_TWO_DATE:
                    show, language = AK, SW
        elif day == 'Thursday':
            if time == '08:00':
                if station == AZAM_ONE and date >= AZAM_ONE_DATE:
                    show, language = UK, EN
            elif time == '14:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = AK, SW
            elif time == '16:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = UE, SW
                elif station == EATV and date >= EATV_DATE:
                    show, language = AK, SW
            elif time == '17:30':
                if station == AZAM_TWO:
                    show, language = UK, SW
        elif day == 'Friday':
            if time == '08:00':
                if station == AZAM_ONE and date >= AZAM_ONE_DATE:
                    show, language = AK, EN
            elif time == '14:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = AK, SW
            elif time == '15:00':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = AK, SW
            elif time == '16:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = UE, SW
            elif time == '17:30':
                if station == AZAM_TWO and date >= AZAM_TWO_DATE:
                    show, language = AK, SW
        elif day == 'Saturday':
            if time == '06:30':
                if station == EATV and date >= EATV_DATE:
                    show, language = AK, SW
            elif time == '07:00':
                if station == EATV and date >= EATV_DATE:
                    show, language = UK, SW
            elif time == '09:00':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = AK, SW
            elif time == '09:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = UK, SW
                elif station == AZAM_TWO and date >= AZAM_TWO_DATE:
                    show, language = AK, SW
        elif day == 'Sunday':
            if time == '08:00':
                if station == AZAM_ONE and date >= AZAM_ONE_DATE:
                    show, language = UK, EN
            elif time == '08:30':
                if station == AZAM_ONE and date >= AZAM_ONE_DATE:
                    show, language = AK, EN
            elif time == '09:00':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = AK, ENSW
            elif time == '09:30':
                if station == TBC_ONE and date >= TBC_ONE_DATE:
                    show, language = UK, EN
                elif station == AZAM_TWO and date >= AZAM_TWO_DATE:
                    show, language = UK, SW
        data.at[i, 'Show'] = show
        data.at[i, 'Language'] = language

    data = data[data['Show'] != 'None']
    data = data[data['Viewers'] != 0]

    return data

def filter_uganda(data):
    for i, row in data.iterrows():
        day = row['Day of Week']
        time = row['Time Block']
        station = row['Station']
        date = dt.strptime(row['Date'], '%d/%m/%Y')
        show = 'None'
        language = 'None'
        if day == 'Friday':
            if time == '16:00':
                if station == NTV and date >= NTV_DATE:
                    show, language = AK, EN
        elif day == 'Saturday':
            if time == '09:30':
                if station == NTV and date >= NTV_DATE:
                    show, language = UK, EN
            if time == '10:30':
                if station == NTV and date >= NTV_DATE:
                    show, language = AK, EN
        elif day == 'Sunday':
            if time == '07:00':
                if station == NTV and date >= NTV_DATE:
                    show, language = AK, EN
            elif time == '07:30':
                if station == NTV and date >= NTV_DATE:
                    show, language = UK, EN
        data.at[i, 'Show'] = show
        data.at[i, 'Language'] = language

    data = data[data['Show'] != 'None']
    data = data[data['Viewers'] != 0]

    return data

if sys.argv[1] == "init":
    data_path = "./data/upToMay2019/"
    # os.chdir("./data/upToMay2019")
elif sys.argv[1] == "update":
    data_path = "./data/update/"
else:
    print("invalid parameter: use 'init' or 'update'")

for file in glob.glob(data_path + "*.csv"):
    file_name = file.split("/")[-1]
    
    if sys.argv[1] == "init":
        country_name = file_name[:-8]
    elif sys.argv[1] == "update":
        country_name = file_name[:-12]
        print(country_name)

    # read file
    df = pd.read_csv(file)
    print(file + " read")

    # drop unnecessary columns
    drop_columns = [col for col in df.columns.tolist() if len(col) == 1 or col == 'Total']
    df = df.drop(columns=drop_columns)

    # format date string
    split_date = pd.DataFrame(df['Day'].str.split('-',1).tolist(), columns = ['Date', 'Day of Week'])
    df = pd.concat([split_date, df], axis=1)
    df['Date'] = df['Date'].str[:-1]
    df['Day of Week'] = df['Day of Week'].str[1:]
    df = df.drop(columns=['Day'])

    # format time block
    df['Time Block'] = df['Time Block'].str[:5]
    
    # reformat table, create station column
    df = df.melt(id_vars=['Date', 'Day of Week', 'Time Block', 'Sample Size'], var_name = 'Station', value_name = 'Viewers')
    
    # filter out stations with missing data
    df['Viewers'] = df['Viewers'].astype(str)
    df.loc[df['Viewers'] == '**', 'Viewers'] = 0
    df['Viewers'] = df['Viewers'].astype(int)

    # set default column values
    df['Show'] = 'None'
    df['Language'] = 'None'
    df['Country'] = country_name

    # filter out time blocks based on country
    if country_name == 'ghana':
        filtered_df = filter_ghana(df)
    elif country_name == 'kenya':
        filtered_df = filter_kenya(df)
    elif country_name == 'nigeria':
        filtered_df = filter_nigeria(df)
    elif country_name == 'rwanda':
        filtered_df = filter_rwanda(df)
    elif country_name == 'tanzania':
        filtered_df = filter_tanzania(df)
    elif country_name == 'uganda':
        filtered_df = filter_uganda(df)
    else:
        print("file name error: country not found")
        break
    frames.append(filtered_df)

result = pd.concat(frames)

# reformat dates for google data studio
result['Date'] = pd.to_datetime(result['Date'], dayfirst=True).dt.strftime('%Y-%m-%d')

# create output directory
if not os.path.exists(data_path + "output"):
    os.mkdir(data_path + "output")

# write csv
result.to_csv(data_path + "output/" + sys.argv[1] + ".csv", index=False, header=False)



