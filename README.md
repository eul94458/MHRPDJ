# MHRPDJ
MAPPING HIGH RESOLUTION POPULATION DISTRUBUTION OF JAPAN

## Declaration

This is a repository of the Bacholar Degree Thesis written by the author. 

This branch is aimed at better algrithm/database management design. 

Foreseeing greatly improved performance and searching time.


## Design

### Search Algorithm

Geographic/spatial referenced data is constitution of location identifier and its attribute. If the space is 2 dimensional which we can assign a set of coordinate (y,x) to it, the data will be in 2+n dimension.

Meanwhile, as foremensioned, location can act as an identifier, such that (y,x) will become a single entity like y_x. For instance, a grid system consist of 800\*800 cells, the cell which y=651 and x=452 will be identified as 651_452, or 651452 if underscore is removed. Thus, reduced one dimension to 2 dimensional dataset.

Let say landuse data. A single data record will be like this:

      [651452,'foest']

For such data, linear search is not efficient enough. Let say we are searching for one particular cell in a grid system consisting 800\*800 cells, in the worse case, we will have to look for all cells in order to find our target. 800^2 = 640,000 cells are there waiting for us. Considering a nation-wide geographic information database, 1 billion identifiers are possible.

To tackle this problem, logorithmic search algorithm must be introduced. An example is presented as the following.

      def search_LogInList(k,q,a,b):
            # k is the target
            # q is dataset that may contain the target
            # a is lower bound of search range
            # b is upper bound of search range
            
            limit = (b+a)//2
            interval = b-a
            #print(interval)
            if interval > 2:
                  if q[limit] > k: # left
                        b = limit
                        search_LogInList(k,q,a,b)
                  elif q[limit] < k: # right
                      a = limit
                       search_LogInList(k,q,a,b)
                  else:
                     print(q[limit])
            else:
                  if q[limit+1] == k:
                        print(q[limit+1])
                  elif q[limit-1] == k:
                        print(q[limit-1])
                  elif q[limit] == k:
                        print(q[limit])            
                  else:
                        print('None')

      templist = []
      for j in range(500000):
            num = j+1
            templist.append(num)

      while True:
            query = input("input a value : ")

            target = int(query)

            LowerBound = 0
            UpperBound = len(templist)-1

            search_LogInList(target,templist,LowerBound,UpperBound)

The search algorithm is written into a function. It can be modified to fit different usage such as returning boolean or returing target identifier.

