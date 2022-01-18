import psycopg2
from psycopg2 import Error
import pandas as pd
import datetime

try:
    connection = psycopg2.connect(user="sungjunchoi", password="1234", host="127.0.0.1", port="8000", database="covidtracker")
    cursor = connection.cursor()
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


# for i in range(1,0,-1):
#     year = (datetime.datetime.now()- datetime.timedelta(days=i)).strftime("%Y")
#     month = (datetime.datetime.now()- datetime.timedelta(days=i)).strftime("%m")
#     day = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%d")

#     print(year + ' ' + month+ " " + day)
    
#     url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/" + month + '-' + day + '-' + year + ".csv"

#     df = pd.read_csv(url)
#     df = df.fillna('empty')
#     df = df[['Province_State', 'Confirmed', 'Deaths', 'Lat', 'Long_']]
#     df = df.astype({'Deaths': 'int'})


#     list = df.values.tolist()

#     print(list)

#     for elem in list:
#         pass


#     values = [['United States', 0, 0, 0], ['Canada', 0, 0, 0], ['Australia', 0, 0, 0], ['Diamond Princess', 0, 0, 0],
#     ['China', 0, 0, 0], ['World', 0, 0, 0], ['Denmark', 0, 0, 0], ['France', 0, 0, 0], ['Netherlands', 0, 0, 0], ['UK', 0, 0, 0], ['Italy', 0, 0, 0], ['Spain', 0, 0, 0], ['Germany', 0, 0, 0],
#     ['Mexico', 0, 0, 0], ['Chile', 0, 0, 0], ['Brazil', 0, 0, 0]]


#     for row in list:
#         values[5][1] += row[1]
#         values[5][2] += row[2]
#         values[5][3] += row[3]

#         if row[0] == 'US' or row[0] == 'USA' or row[0] == 'United States':
#             values[0][1] += row[1]
#             values[0][2] += row[2]
#             values[0][3] += row[3]

#         elif row[0] == 'Canada' or row[0] == 'CA':
#             values[1][1] += row[1]
#             values[1][2] += row[2]
#             values[1][3] += row[3]

#         elif row[0] == 'Australia':
#             values[2][1] += row[1]
#             values[2][2] += row[2]
#             values[2][3] += row[3]

#         elif row[0] == 'Others' or row[0] == 'Cruise Ship':
#             values[3][1] += row[1]
#             values[3][2] += row[2]
#             values[3][3] += row[3]

#         elif row[0] == 'Mainland China' or row[0] == 'China':
#                 values[4][1] += row[1]
#                 values[4][2] += row[2]
#                 values[4][3] += row[3]

#         # index 5 is world

#         elif row[0] == 'Denmark':
#             values[6][1] += row[1]
#             values[6][2] += row[2]
#             values[6][3] += row[3]

#         elif row[0] == 'France':
#             values[7][1] += row[1]
#             values[7][2] += row[2]
#             values[7][3] += row[3]

#         elif row[0] == "Netherlands":
#             values[8][1] += row[1]
#             values[8][2] += row[2]
#             values[8][3] += row[3]

#         elif row[0] == 'United Kingdom' or row[0] == 'UK':
#             values[9][1] += row[1]
#             values[9][2] += row[2]
#             values[9][3] += row[3]

#         elif row[0] == 'Italy':
#             values[10][1] += row[1]
#             values[10][2] += row[2]
#             values[10][3] += row[3]

#         elif row[0] == 'Spain':
#             values[11][1] += row[1]
#             values[11][2] += row[2]
#             values[11][3] += row[3]

#         elif row[0] == 'Germany':
#             values[12][1] += row[1]
#             values[12][2] += row[2]
#             values[12][3] += row[3]

#         elif row[0] == 'Mexico':
#             values[13][1] += row[1]
#             values[13][2] += row[2]
#             values[13][3] += row[3]

#         elif row[0] == 'Chile':
#             values[14][1] += row[1]
#             values[14][2] += row[2]
#             values[14][3] += row[3]

#         elif row[0] == 'Brazil':
#             values[15][1] += row[1]
#             values[15][2] += row[2]
#             values[15][3] += row[3]


#         elif row[0] == 'North Ireland':
#             values.append(['Ireland', row[1], row[2], row[3]])

#         elif row[0] == ' Azerbaijan':
#             values.append(['Azerbaijan', row[1], row[2], row[3]])

#         elif row[0] == 'United Arab Emirates':
#             values.append(['UAE', row[1], row[2], row[3]])

#         elif row[0] == 'Viet Nam':
#             values.append(['Vietnam', row[1], row[2], row[3]])

#         elif row[0] == 'Taipei and environs' or row[0] == 'Taiwan*':
#             values.append(['Taiwan', row[1], row[2], row[3]])

#         elif row[0] == 'Hong Kong SAR':
#             values.append(['Hong Kong', row[1], row[2], row[3]])

#         elif row[0] == 'Iran (Islamic Republic of)':
#             values.append(['Iran', row[1], row[2], row[3]])

#         elif row[0] == 'Republic of Korea' or row[0] == 'S. Korea' or row[0] == 'Korea, South':
#             values.append(['South Korea', row[1], row[2], row[3]])

#         elif row[0] == 'Republic of Ireland':
#             values.append(['Ireland', row[1], row[2], row[3]])

#         elif row[0] == 'Republic of Moldova':
#             values.append(['Moldova', row[1], row[2], row[3]])

#         elif row[0] == 'Macao' or row[0] == 'Macao SAR':
#             values.append(['Macau', row[1], row[2], row[3]])

#         elif row[0] == 'Congo (Kinshasa)':
#             values.append(['DRC', row[1], row[2], row[3]])

#         elif row[0] == '':
#             values.append(['Netherlands', row[1], row[2], row[3]])

#         else:
#             values.append([row[0], row[1], row[2], row[3]])



#     for value in values:
#         name = value[0]
#         c = value[1]
#         d = value[2]
#         r = value[3]
#         da = year + '-' + month + '-' + day
#         print((name,da,c,d,r));
