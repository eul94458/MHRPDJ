# MHRPDJ
MAPPING HIGH RESOLUTION POPULATION DISTRUBUTION OF JAPAN

## Declaration

This is a repository of the Bacholar Degree Thesis written by the author. 

This branch is aimed at better algrithm/database management design. 

Foreseeing greatly improved performance and searching time.


## Design

### Dadabase Design

Geographic/spatial referenced data is basically 2 dimensional data which at least contains longitude and latitude code. Or inversely, attributes are assigned to each of these locations indentified by longitude and latitude code. There we have 1) attribute and 2) location data combined to form a 3 dimensional dataset. 

Location data itself is a compond data like (y_x). Let say there is a grid system constitute 800\*800 cells. We are searching for (a_b). The first method to do this is to search the exact coordinate (a_b) in a linear search fashion. As there are 800\*\*2 combinations of x and y, therefore for the worse case which if the target is (799_799), search time is 800\*\*2. 

So the second method is to design a database struture enhence faster searching inherently. Instead of storing the location as a single entity like (y_x), it would be better if it is stored as seperated entities (y),(x). Thus we search for the first entity, and then the second. Seching time is only the double of 800 even though we are using linear search.

Therefore, each attribute should be stored as the following:
list = \[\[y_coordinate_1, y_coordinate_2, y_coordinate_3, ... , y_coordinate_n]
      \[x_coordinate_1, x_coordinate_2, x_coordinate_3, ... , x_coordinate_n]
      \[attribute_1, attribute_2, attribute_3, ... , attribute_n]].

And the duo layer search algrithm is made for faster searching:
if a in list\[0]: # see if the target is in the list by looking for existence of certain y-coordinate
  if b in list\[1]: # see if the target is in the list by looking for existence of certain x-coordinate
    for y,i in enumerate(list\[0]): # locating the target column
      if i == a: # matching target's y-coordinate
        if list\[1]\[y] == b: # matching target's x-coordinate
          return list\[3]\[y] # reture attribute

