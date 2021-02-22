# MHRPDJ
MAPPING HIGH RESOLUTION POPULATION DISTRUBUTION OF JAPAN

## Declaration

This is a repository of the Bacholar Degree Thesis written by the author. 

This branch is aimed at better algrithm/database management design. 

Foreseeing greatly improved performance and searching time.

* By the way, it is still under construction.


## Design

### Search Algorithm

Geographic/spatial referenced data is constitution of location identifier and its attribute. If the space is 2 dimensional which we can assign a set of coordinate (y,x) to it, the data will be in 2+n dimension.

Meanwhile, as foremensioned, location can act as an identifier, such that (y,x) will become a single entity like y_x. For instance, a grid system consist of 800\*800 cells, the cell which y=651 and x=452 will be identified as 651_452, or 651452 if underscore is removed. Thus, reduced one dimension to 2 dimensional dataset.

Let say landuse data. A single data record will be like this:

      [651452,'foest']

For such data, linear search is not efficient enough. Let say we are searching for one particular cell in a grid system consisting 800\*800 cells, in the worse case, we will have to look for all cells in order to find our target. 800^2 = 640,000 cells are there waiting for us. Considering a nation-wide geographic information database, 1 billion identifiers are possible.

To tackle this problem, binary search algorithm maybe considered to be introduced. However, search algorithm has to be alongside with sorted data and geographic/spatial referenced data is not sorted and cannot be sorted in many situation. Here, the data structure must be construced well in order to enhence quicker search.

First, unique identifier must be assigned to every location.

Second, search algoritm is launched solely upon those unique identifier as we can refer to other database to grap the population or else later.

### Data Structure

Since our purpose is to analysis relationship between locations and create alternative subset containing interested locations, attributes other than geographical ones can be omitted during processing. Also geographic/spatial information is inherent in its unique identifier, we can process the data straightly.

      Regional Agglomeration = subset of Local Agglomeration which share mutual border/edge
      Local Agglomeration = the smallest spatial unit of aggregated human settlement data

Their relationships are referred in a nested list, namely, a 3 dimensional list:
      
      [
      regional1 [ local1, local2, local3 ]
      regional2 [ local4, local5, local6 ]
      regional3 [ local7, local8, local9 ]
      ]

So as we execute some code to search for one specific item, executing speed will be immense:

      Regional_Agglomerations = [ regional1 [ local1, local2, local3 ]
                                  regional2 [ local4, local5, local6 ]
                                  regional3 [ local7, local8, local9 ] ]
      
      for each_RegAgg in Reginoal_Agglomeration:
            if local5 in each_RegAgg:
                  p = each_RegAgg.index(local5)
                  q = Regional_Agglomerations.index(each_RegAgg)
                  print('local5 is contained in Regional_Agglomerations[{}][{}]'.format(q,p)
                  
                  
