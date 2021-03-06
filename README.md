# Sea Level Rising Project

Required Software :- Python3, Postman (API Call)

Libraries required:- Flask, Flask_restful, wget,Pandas, os, Webbrowser, Requests,sys


Rest Server API :- Representational state transfer (REST) is a software architectural style that was created to guide the design and development of the architecture for the World Wide Web. REST defines a set of constraints for how the architecture of an Internet-scale distributed hypermedia system, such as the Web, should behave. The REST architectural style emphasises the scalability of interactions between components, uniform interfaces, independent deployment of components, and the creation of a layered architecture to facilitate caching components to reduce user-perceived latency, enforce security, and encapsulate legacy systems 

What Does the server peform ?
The server downloads the requested data from the web and works on that datasets and gives the required output for the requested queries.

How to run the server?
1) Download all the necessary libarries mentioned above through command : pip3 install (library_name)
2) Download the Postman app(we need to download the app locally).
3) Open terminal where rest_api_final_submission.py file is located and run the python by command : python3 rest_api_final_submission.py    
4) After the step 2 you will see somenthing like this in the terminal, which means the server is up and running.
         * Serving Flask app 'rest_api_final_submission' (lazy loading)
         * Environment: production
           WARNING: This is a development server. Do not use it in a production deployment.
           Use a production WSGI server instead.
         * Debug mode: off
         * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

5) For dataset1:
     URL: http://127.0.0.1:5000/dataset1 
     
    ![Screenshot (44)](https://user-images.githubusercontent.com/78068339/168710112-6235494b-f0f0-4701-8f06-e53b04071e65.png)
    
    
    
    ![Screenshot (46)](https://user-images.githubusercontent.com/78068339/168706467-7d7c40de-6085-4cae-bda1-2c681c05ba76.png)
         If we pass the current city as "BOSTON" we get the output of Boston city.
     If we pass the lat-lon pair it finds the nearest city and the prints output of that two cities.
     
    
                
6) For Dataset 2:-
        I worked on 6queries for dataset2.
        
         Query 1: http://127.0.0.1:5000/Medianformonth
         
     ![Screenshot (47)](https://user-images.githubusercontent.com/78068339/168710867-a135a938-c776-4e1b-9cc5-f3eff5ca4c06.png)
     
      Query 2:- http://127.0.0.1:5000/Medianforyear
              
      ![Screenshot (48)](https://user-images.githubusercontent.com/78068339/168708175-cc766b28-7646-4801-a24f-446c9f29f8c4.png)
      
       Query3: http://127.0.0.1:5000/Absoluteriseinyear
                
      ![Screenshot (49)](https://user-images.githubusercontent.com/78068339/168708336-25a8a9d7-ccd6-4462-9653-9cb3f851ac28.png)
      
      Query4: http://127.0.0.1:5000/Percentaageabsoluteriseinyear
                
      ![Screenshot (50)](https://user-images.githubusercontent.com/78068339/168708482-2e4ccefc-e292-4d7d-928d-a0a2dff82a1d.png)
      
       Query5: http://127.0.0.1:5000/Avgofabsrisestarttoendyear
                
      ![Screenshot (51)](https://user-images.githubusercontent.com/78068339/168708714-2de9cbf8-1dee-4fd8-90bd-7e1129c112f8.png)
                
                
       Query6:- http://127.0.0.1:5000/Avgofperrisestarttoendyear
                
      ![Screenshot (52)](https://user-images.githubusercontent.com/78068339/168708930-367e8598-7c80-485a-8d04-db545c58b197.png)
                


     
    
Test Data for the Project:- 

For http://127.0.0.1:5000/dataset1  :- 
```
{
  "city":"boston",
  "lat":null,
   "lon":null
  
}
```                                    


For http://127.0.0.1:5000/dataset1  :- 
```
{
    "city":null,
    "lat":"40.7",
    "lon":"-74.01"
}
``` 


For http://127.0.0.1:5000/Medianformonth  :- 
```
{
    "input_year":"2013",
    "input_month":"11"
}
```  

For http://127.0.0.1:5000/Medianforyear  :- 
```
{
    "input_year":"2013"
}
``` 
For http://127.0.0.1:5000/Absoluteriseinyear  :- 
```
{
    "input_year":"2013"
}
``` 
For http://127.0.0.1:5000/Percentaageabsoluteriseinyear  :- 
```
{
    "input_year":"2013"
}
``` 
For http://127.0.0.1:5000/Avgofabsrisestarttoendyear  :- 
```
{
    "input_year":"2013",
    "end_year":"2014"
}
``` 

For http://127.0.0.1:5000/Avgofperrisestarttoendyear  :- 
```
{
    "input_year":"2013",
    "end_year":"2014"
}
``` 
The datasets I worked on :- 
1) Tides and Currents Nooa Gov. Dataset:- 
       Link for the dataset :- https://tidesandcurrents.noaa.gov/publications/techrpt083.csv
       Descriptions of Data Columns:																			
       A) Site: Site name, specified as Global Mean Sea Level (GMSL), as the name of specific tide gauge location, or as grid_lat_long for points on a gridded basis.				 B) PSMSL ID: for GMSL, 0; for tide gauge locations, the Permenant Service for Mean Sea Level (http://www.psmsl.org/) Tide Gauge Identification (ID) Number;  for          grid points, 109 + 105 * colatitude + longitude																			
       C) Latitude of location or grid																			
       D) Longitude of location or grid																			
       E) Scenario: For each of the six GMSL scenarios (identified by the height in meters in 2100), there is a low, medium and high sub-scenario, corresponding to the          17th, 50th, and 83rd percentile of the climate-related sea level projections consistent with the GMSL scenario. The scenario values are a summation of the                climate-related sea level with a linear non-climatic background relative sea level (RSL) trend applied (rate specified in column 'F')														 F) Background RSL rate (mm/yr): Applied as a constant linear trend. The mean estimate, mean estimate - 1 standard deviation, and mean estimate + 1 standard              deviation are respectively applied to the  medium, low and high sub-scenarios.																			
       G-T) Relative Sea level (RSL) rise: GMSL scenario rise amounts and associated RSL changes (both in cm) projected at tide gauge and grid locations by decade from          2000 to 2100 and also for years 2120, 2150 and 2200.																			



       Queries Performed For this Dataset:- 
       1) Average Rising Sea Level in (cms) for the particular city . (This query gives Average sea level Rise for the particular city in a span of year 2000 to year             2200 as given in the dataset . )
       2) Difference in rising Sea Level in for every 10 years from from 2000.( Based on the given input this query performs the difference in sea level rise for year         2020 minus the sea level rise in year 2010 and consecutively for other years).
 
       To reference a particular city, have your server accept the name of a city (e.g. ???Boston???) or a pair of latitude and logitude (e.g. ???42.31440581852247, -              71.03651997292752", this is a lat-lon for UMass Boston.). When it receives a city name, it will retrieve and return the SLR data for that city. (Return an error        or null if it cannot find the SLR data for that city.) When the server receives a lat-lon pair, it will find the geographically closest city from that. For            example, if it receives (42.31440581852247, -71.03651997292752), it will judge the lat-lon is closest to Boston ((42.35, -71.05) in the dataset) and return the        SLR data for Boston. You can use GeoPy or any other library to calculate the distance between two lat-lon pairs.
       
2) University Of Hauweii Dataset:- 
       Link For the Dataset:- http://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/daily/d741a.csv
       These is dataset for daily sea level Rise for all those years.
       Description Of the Data Columns:-
       A) Column 1 :- Denotes the Year 
       B) Column 2 :- Denotes the Month 
       C) Column 3 :- Denotes the Day
       D) Column 4 :- Denotes the Sea Level Rise 
       
       Queries Performed For this Dataset:- 
     1)  Median sea level in a particular month (Median of daily sea levels in a particular month).                                                                              - In this query when the client enter the "input_year" and "input_month". The server responds with the median sea level of the                                            particular month of that year.                                                                                                                                          For example if we pass:- {
                                            "input_year":"2013",
                                            "input_month":"11"
                                        }                                                                                                                                       The server will respond Median of 11/2013. (i.e. November 2013)                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      2)  Median sea level in a particular year (Median of daily sea levels in a particular year).                                                                                - In this query when the client enter the "input_year" . The server responds with the median sea level of that year.                                                    - For example If we pass :- {
                                            "input_year":"2013"
                                        }                                                                                                                                         The server will respond Median of year 2013.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
     3)  Yearly absolute rise in a particular year   (Median sea level in December) - (Median sea level in January).                                                           - In this query when the client enter the "input_year" . The server responds with the  Yearly absolute rise in a particular year .                                       - For example If we pass :- {
                                            "input_year":"2013"
                                        }                                                                                                                                           The server will respond   (Median sea level in December of year 2013)- (Median sea level in January of year 2013).                                                                                         
     4)  Yearly relative (percentage) rise in a particular year[(Median sea level in December) - (Median sea level in January)]/(Median sea level in January).                  - In this query when the client enter the "input_year" . The server responds with the  Yearly absolute rise in a particular year .                                       - For example If we pass :- {
                                            "input_year":"2013"
                                        }                                                                                                                                  The server will respond   [(Median sea level in December of year 2013)- (Median sea level in January of year 2013)]/(Median sea level in January of year 2013).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
     5)  Average of yearly absolute rises from a particular start year to end year
         e.g., If start yr = 2000 and end yr = 2001, compute [(yearly absolute rise in 2000)+(yearly absolute rise in 2001)]/2                                                  - In this query when the client enter the "input_year" and "end_year". The server responds with Average of yearly absolute rises from a particular start year            to end year.                                                                                                                                         
         For example if we pass:- {
                                            "input_year":"2013",
                                            "end_year":"2014"
                                        }                                                                                                                                       The server will respond  by computing  [(yearly absolute rise in 2013)+(yearly absolute rise in 2014)]/2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
     6) Average of yearly relative (percentage) rises from a particular start year to end year
        e.g., If start yr = 2000 and end yr = 2001, compute [(yearly relative rise in 2000)+(yearly relative rise in 2001)]/2
       


