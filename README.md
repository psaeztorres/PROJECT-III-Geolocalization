# PROJECT-III-Geolocalization

## 1- INFORMATION WE HAVE 

A- OUR WORKING FORCE
_____________________

    - 20 Designers
    - 5 UI/UX Engineers
    - 10 Frontend Developers
    - 15 Data Engineers
    - 5 Backend Developers
    - 20 Account Managers
    - 1 Maintenance guy that loves basketball
    - 10 Executives
    - 1 CEO/President.
   
B- THEIR PREFERENCES
______________________
      
    1- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
    2- 30% of the company staff have at least 1 child.
    3- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
    4- Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
    5- Account managers need to travel a lot.
    6- Everyone in the company is between 25 and 40, give them some place to go party.
    7- The CEO is vegan.
    8- If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
    9- The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.

      
## 2- OUR APPROACH

    STARTUP: will be considered those companys with less than 5 years from its fundation. As the latest fundation year in the "companies"
    database is 2013 it will be considered startup any company founded after 2007.
    DESIGN CATEGORY will not be taking into account as it is understood as "fashon design" or "forniture design" etc..but not tech 
    design which it is understood what it means in the first point of the worker's preferences.
      
      1-search for top cities that:
          a- have more game_video startups
          b- have more web startups 
        and get TOP 10
             
      2- searh for the cities where there are most game and web companies 
      3- join answers to the two previous research to find the cities were we have the best conditions to  satisfy worker's preferences 1&3
      4- search for number of design companies ( web, game) companies in those cities so we will fullfield number 
         and 3 of the requierements
      4-choose the best point to search in those cities for the rest of the requirements
      5-based on this location search for the rest of the requirements determining the distance from our proposal location
      6-based on the distance and services available choose the best city
      
      
## 3- EXECUTION.
     
     1- EXECUTING APPROACH POINT 1
         1.1 Create a function ("nongo_search") that takes as arguments as many conditions as we want and returns:
             - company name
             - fundation year
             -number of workers
             -cities where it is
             - coordinates of its locations (up to two locations)
          1.2- Create a function ("merge_and_get_top10_cities) that returns the top10 cities with more startups which have raised >1M$
          
          Now we are sure that by choosing one of this 10 cities we are satisfying requeriment num. 4 in workers's preferences
          
     2- EXECUTING APPROACH POINT 2  
         Do the same as in previous research but without the condition of year or money to get the top 10 companies that hold the
             highest number of web and game design companies. 
        
    3- EXECUTING APPROACH POINT 3
        
        Create cleaning function "merge_cities" that joins the result of point 1 and point 2.1 and returns the cities that are in the 
            top 10 of both researchs.
            
     4- EXECUTING APPROACH POINT 4
     
         In order to settle the best place were to locate our company we will see the average coordinates (avg(lon) and avg(len) of 
         all the companies we have found for each city. This will give us a starting point.
         
         After realizing there are outter values of lon and lat values in the table it has been crated a function ("clean_coord") that
         removes those companies that are more than 75km from the city centre.
         
     5- FIRST MAPS: with all the info above we plot a map of each city to see where our situation would be and where are 
         the startups and web/game companies
         
     6-SEARCHING FOR THE REST OF THE WORKER'S WISHES:
         It has been stablished 3 levels of search:
         1-what should be in a radious of 500m sorted by distance. The venues searched are :Starbucks,vegan restaurant,school, 
         Pet Grooming, bar,karaoke and the function used is 'queries_for_a_city' . After this query the dataframe returned is
         transformed into a df of number of services and distance by using the function 'distance_venue_city'.
         2-what should be in a radius of 10km which is the basketball stadium and  and in a distance of 50km which is an
         International Aeroport. To make this queries it has been used the function requests_for_foursquare_relevance by 
         changing the radius argument .
         
     7- With all the results obtained until now a city is chosen an a map with the different requirements plot by using
         the function 'city_map'.
         
         
     
     
         
         
         
         
         
         
         
         
         
         
         
         
         
      
   
         