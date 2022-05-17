from flask import Flask, request
from flask_restful import Resource, Api
from flask.json import jsonify
import webbrowser
import wget
import os
import sys
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import requests

app = Flask(__name__)

def dist(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371* c
    return km

def find_nearest(lat, long, members):
    lat = float(lat)
    long = float(long)
    distances = members.apply(
        lambda row: dist(lat, long, row['Latitude'], row['Longitude']),
        axis=1)
    return members.loc[distances.idxmin(), 'Site']

def city_data(current_city):
    data_current_city = []
    d1='techrpt083.csv'
    l1='https://tidesandcurrents.noaa.gov/publications/techrpt083.csv'
    local_file=d1
    f_name = pd.read_csv(local_file, header = 15)
    for index, row in f_name.iterrows():
        if row["Site"] == current_city:
            data_current_city.append(row.tolist())
    return data_current_city

@app.route("/dataset1", methods=['POST'])
def dataset1():
    d1='techrpt083.csv'
    l1='https://tidesandcurrents.noaa.gov/publications/techrpt083.csv'
    local_file=d1
    slrRemoteLink =l1
    r=requests.get(slrRemoteLink)
    with open("r.text","w") as f:
                f.write(r.text)
                read_file = pd.read_csv('r.text')
    read_file.to_csv(local_file, index = None)
    text='hi'
   # wget.download(slrRemoteLink, local_file)
    membersa = pd.read_csv(local_file, header = 15)
    membersa['Latitude'] = membersa['Latitude'].fillna(0)
    membersa['Longitude'] = membersa['Longitude'].fillna(0)
    members=membersa[['Site','Latitude','Longitude']]
    members=members.drop_duplicates()
    req = request.get_json(force=True)
    print(req)
    current_city = req.get('city',None)
    if current_city :
        current_city = current_city.upper()
    print(current_city)
    lat = req.get('lat',None)
    lon = req.get('lon',None)
    if current_city:
        data_current_city = city_data(current_city)

    if lat and lon:
        current_city=find_nearest(lat, lon, members)
        print(current_city)
        if current_city:
            data_current_city = city_data(current_city)
        else:
            return {'Error':'Data not found'}

    sum_RSL = 0
    diff = []
    count = 0
    alldata=data_current_city
    #print(data_current_city)
    curr_city_RSL = data_current_city[-1][6:]#take the most recent one
    print("HELLLo",curr_city_RSL)
    print("Every 10year rise in sea level of a particular city:")
    for i in range(0, len(curr_city_RSL)):
        sum_RSL += curr_city_RSL[i]
        count+=1

    avg_RSL = sum_RSL/count

    for i in range(1, len(curr_city_RSL)):
        diff.append(curr_city_RSL[i] - curr_city_RSL[i-1])

    print("difference: ", diff)
    print("AVG RSL: ", avg_RSL, "(cm)")
    os.remove(local_file)
    return {
        "All the data of the current city":alldata,
        "Difference in rising Sea Level in for every 10 years from from 2000": diff,
        "Average Rising Sea Level in (cms) for the particular city": avg_RSL
    }

@app.route("/Medianformonth", methods=['POST'])
def Medianformonth():
    d1='d740a.csv'
    l1='http://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/daily/d740a.csv'
    local_file=d1
    slrRemoteLink =l1
    r=requests.get(slrRemoteLink)
    with open("r.text","w") as f:
                f.write(r.text)
                read_file = pd.read_csv('r.text')
    read_file.to_csv(local_file, index = None)
    #####
    req = request.get_json(force=True)
    input_year=req.get('input_year',None)
    input_month=req.get('input_month',None)

    filename = pd.read_csv(local_file)
    filename.columns =['Year', 'Month', 'Day', 'SeaLevel Rise']
    filename['Date']=pd.to_datetime(filename[['Year', 'Month', 'Day']])
    filename1=filename[['Date','SeaLevel Rise']]
    filenamemonth=filename1.groupby(pd.PeriodIndex(filename1['Date'], freq="M"))['SeaLevel Rise'].median().reset_index()
    search_str=input_year+"-"+input_month
    medianformonth =filenamemonth.loc[filenamemonth['Date'].astype(str).str.contains(search_str, case=False)]
    mfm=medianformonth['SeaLevel Rise'].to_string(index=False)
    return{
        "Median sea level in a particular month of that year ":mfm
        }

@app.route("/Medianforyear", methods=['POST'])
def Medianforyear():
    d1='d740a.csv'
    l1='http://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/daily/d740a.csv'
    local_file=d1
    slrRemoteLink =l1
    r=requests.get(slrRemoteLink)
    with open("r.text","w") as f:
                f.write(r.text)
                read_file = pd.read_csv('r.text')
    read_file.to_csv(local_file, index = None)

    req = request.get_json(force=True)
    input_year=req.get('input_year',None)


    filename = pd.read_csv(local_file)
    filename.columns =['Year', 'Month', 'Day', 'SeaLevel Rise']
    filename['Date']=pd.to_datetime(filename[['Year', 'Month', 'Day']])
    filename1=filename[['Date','SeaLevel Rise']]
    filenameyear=filename1.groupby(pd.PeriodIndex(filename1['Date'], freq="Y"))['SeaLevel Rise'].median().reset_index()
    medianforyear = filenameyear.loc[filenameyear['Date'].astype(str).str.contains(input_year, case=False)]
    mfy=medianforyear['SeaLevel Rise'].to_string(index=False)
    return{
        "Median sea level in that particular year ":mfy
        }

@app.route("/Absoluteriseinyear", methods=['POST'])
def Absoluteriseinyear():
    d1='d740a.csv'
    l1='http://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/daily/d740a.csv'
    local_file=d1
    slrRemoteLink =l1
    r=requests.get(slrRemoteLink)
    with open("r.text","w") as f:
                f.write(r.text)
                read_file = pd.read_csv('r.text')
    read_file.to_csv(local_file, index = None)

    req = request.get_json(force=True)
    input_year=req.get('input_year',None)


    filename = pd.read_csv(local_file)
    filename.columns =['Year', 'Month', 'Day', 'SeaLevel Rise']
    filename['Date']=pd.to_datetime(filename[['Year', 'Month', 'Day']])
    filename1=filename[['Date','SeaLevel Rise']]
    fm=filename1.groupby(pd.PeriodIndex(filename1['Date'], freq="M"))['SeaLevel Rise'].median()
    fm = fm.to_dict()
    start = pd.Period(input_year+'-01-01', freq='M')
    end = pd.Period(input_year+'-12-01', freq='M')


    absoluteriseinyear=0
    absoluteriseinendyear=0
    percentageabsoluteriseinyear=0
    percentageabsoluteriseinendyear=0
    if start in fm and end in fm:
        absoluteriseinyear=fm[end] - fm[start]
        absiy=absoluteriseinyear


    return{
        "Yearly absolute rise in a particular year":absiy
        }

@app.route("/Percentaageabsoluteriseinyear", methods=['POST'])
def Percentaageabsoluteriseinyear():
    d1='d740a.csv'
    l1='http://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/daily/d740a.csv'
    local_file=d1
    slrRemoteLink =l1
    r=requests.get(slrRemoteLink)
    with open("r.text","w") as f:
                f.write(r.text)
                read_file = pd.read_csv('r.text')
    read_file.to_csv(local_file, index = None)

    req = request.get_json(force=True)
    input_year=req.get('input_year',None)


    filename = pd.read_csv(local_file)
    filename.columns =['Year', 'Month', 'Day', 'SeaLevel Rise']
    filename['Date']=pd.to_datetime(filename[['Year', 'Month', 'Day']])
    filename1=filename[['Date','SeaLevel Rise']]
    fm=filename1.groupby(pd.PeriodIndex(filename1['Date'], freq="M"))['SeaLevel Rise'].median()
    fm = fm.to_dict()
    start = pd.Period(input_year+'-01-01', freq='M')
    end = pd.Period(input_year+'-12-01', freq='M')


    absoluteriseinyear=0
    absoluteriseinendyear=0
    percentageabsoluteriseinyear=0
    percentageabsoluteriseinendyear=0
    if start in fm and end in fm:
        percentageabsoluteriseinyear=((fm[end] - fm[start])/ fm[start])*100
        pabsiy=percentageabsoluteriseinyear


    return{
        "Percenteage Yearly absolute rise in a particular year":pabsiy
        }
@app.route("/Avgofabsrisestarttoendyear", methods=['POST'])
def Avgofabsrisestarttoendyear():
    d1='d740a.csv'
    l1='http://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/daily/d740a.csv'
    local_file=d1
    slrRemoteLink =l1
    r=requests.get(slrRemoteLink)
    with open("r.text","w") as f:
                f.write(r.text)
                read_file = pd.read_csv('r.text')
    read_file.to_csv(local_file, index = None)

    req = request.get_json(force=True)
    input_year=req.get('input_year',None)
    end_year=req.get('end_year',None)


    filename = pd.read_csv(local_file)
    filename.columns =['Year', 'Month', 'Day', 'SeaLevel Rise']
    filename['Date']=pd.to_datetime(filename[['Year', 'Month', 'Day']])
    filename1=filename[['Date','SeaLevel Rise']]
    fm=filename1.groupby(pd.PeriodIndex(filename1['Date'], freq="M"))['SeaLevel Rise'].median()
    fm = fm.to_dict()
    start = pd.Period(input_year+'-01-01', freq='M')
    end = pd.Period(input_year+'-12-01', freq='M')
    start_end=pd.Period(end_year+'-01-01', freq='M')
    end_end=pd.Period(end_year+'-12-01', freq='M')
    absoluteriseinyear=0
    absoluteriseinendyear=0
    percentageabsoluteriseinyear=0
    percentageabsoluteriseinendyear=0
    if start in fm and end in fm:
        absoluteriseinyear=fm[end] - fm[start]

    if start_end in fm and end_end in fm:
        absoluteriseinendyear=fm[end_end] - fm[start_end]


    averageofyearlyabsoluterises=(absoluteriseinyear+absoluteriseinendyear)/2
    avgoyabs=averageofyearlyabsoluterises

    return{
        "Average of yearly absolute rises from a particular start year to end year":avgoyabs
        }


@app.route("/Avgofperrisestarttoendyear", methods=['POST'])
def Avgofperrisestarttoendyear():
    d1='d740a.csv'
    l1='http://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/daily/d740a.csv'
    local_file=d1
    slrRemoteLink =l1
    r=requests.get(slrRemoteLink)
    with open("r.text","w") as f:
                f.write(r.text)
                read_file = pd.read_csv('r.text')
    read_file.to_csv(local_file, index = None)

    req = request.get_json(force=True)
    input_year=req.get('input_year',None)
    end_year=req.get('end_year',None)


    filename = pd.read_csv(local_file)
    filename.columns =['Year', 'Month', 'Day', 'SeaLevel Rise']
    filename['Date']=pd.to_datetime(filename[['Year', 'Month', 'Day']])
    filename1=filename[['Date','SeaLevel Rise']]
    fm=filename1.groupby(pd.PeriodIndex(filename1['Date'], freq="M"))['SeaLevel Rise'].median()
    fm = fm.to_dict()
    start = pd.Period(input_year+'-01-01', freq='M')
    end = pd.Period(input_year+'-12-01', freq='M')
    start_end=pd.Period(end_year+'-01-01', freq='M')
    end_end=pd.Period(end_year+'-12-01', freq='M')
    absoluteriseinyear=0
    absoluteriseinendyear=0
    percentageabsoluteriseinyear=0
    percentageabsoluteriseinendyear=0
    if start in fm and end in fm:
        percentageabsoluteriseinyear=((fm[end] - fm[start])/ fm[start])*100
    if start_end in fm and end_end in fm:
        percentageabsoluteriseinendyear=((fm[end_end] - fm[start_end])/ fm[start_end])*100
    averageofyearlyrelativepercentagerises= (percentageabsoluteriseinyear+percentageabsoluteriseinendyear)/2
    avg2=averageofyearlyrelativepercentagerises



    return{
        "Average of yearly relative (percentage) rises from a particular start year to end year":avg2
        }




if __name__ == '__main__':
    app.run()
