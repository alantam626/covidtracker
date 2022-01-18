import psycopg
import pandas as pd
import datetime

try:
    connection = psycopg.connect(user="sungjunchoi", password="1234", host="127.0.0.1", port="8000", database="covidtracker")
    cursor = connection.cursor()
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    insert_query = """INSERT INTO covidtracker VALUES(1, 2, 'lat', 'long')"""


except (Exception) as error:
    print("Error while connecting to PostgreSQL", error)

# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")


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


#     for value in values:
#         name = value[0]
#         c = value[1]
#         d = value[2]
#         r = value[3]
#         da = year + '-' + month + '-' + day
#         print((name,da,c,d,r));
