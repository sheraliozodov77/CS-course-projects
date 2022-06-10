'''File: crcassonne_tile.py
   Author: Sherali Ozodov
   Purpose: This program creates a class called CarcassonneTile and
   define 12 tiles and represt with CarcassonneTile object. It has also
   several methods to implement the program such as edge_has_city(),get_edge(),
   edge_has_road(),has_crossroads(),road_get_connection(),city_connects(),
   rotate() and cities_sides_retval().
'''

class CarcassonneTile:
    '''
    The class CarcassonneTile stores several methods in it.
    '''

    def __init__(self,N,E,S,W,unconnected_city=''):
        '''
        The constructor takes four sides of tiles as parameteres
        (N-North,E-East,S-South,W-West,). it also  has default
        unconnected_city which helps to identifies connection of
        cities
        '''
        self._N = N
        self._E = E
        self._S = S
        self._W = W
        self._unconnected_city = unconnected_city
        self._sides = {N:0,E:1,S:2,W:3}
        self._array = [None,None,None,None]
        ## it creates an array and stores all information about tiles,
        # such as what are on the edges of the tiles
        self._array[0] = (self._N).split('+')
        self._array[1] = (self._E).split('+')
        self._array[2] = (self._S).split('+')
        self._array[3] =  (self._W).split('+')

    def edge_has_city(self, edge):
        '''
        This method checks if there is a city in the asked edge.
        if it has, it returns True, otherwise False
        '''
        if edge == 0:
            return 'city' in (self._N).split('+')
        elif edge == 1:
            return 'city' in (self._E).split('+')
        elif edge == 2:
            return 'city' in (self._S).split('+')
        elif edge == 3:
            return 'city' in (self._W).split('+')

    def get_edge(self, side):
        '''
        This method returns the what the asked side has on all four edges
        '''
        if side == 0:
            return (self._N)
        elif side == 1:
            return (self._E)
        elif side == 2:
            return (self._S)
        elif side == 3:
            return (self._W)

    def edge_has_road(self, side):
        '''
        This method checks if the asked side has road in it.
        '''
        if side == 0:
            return 'road' in (self._N).split('+')
        elif side == 1:
            return 'road' in (self._E).split('+')
        elif side == 2:
            return 'road' in (self._S).split('+')
        elif side == 3:
            return 'road' in (self._W).split('+')

    def has_crossroads(self):
        '''
        This method checks if a tile has a crossroad.
        To do it, it counts how many roads on the tile.
        If the number is more than 2, it finds crossroad and
        return True, otherwise False.
        '''
        count_road = 0
        for arr in self._array:
            if 'road' in arr:
                count_road+=1
        if count_road > 2:
            return True
        else:
            return False


    def road_get_connection(self, from_side):
        '''
        This method returns the side that a given road is connected to. If
        the road in question is connected to another edge, then return the
        integer for that edge. But if it is connected to a crossroads in
        the middle of the tile, return -1.
        '''
        self._arr_road = [None,None,None,None]
        self._keep_original = [None,None,None,None]
        ## it two identical arrays to store data about the tile
        self._arr_road[0] = (self._N).split('+')
        self._arr_road[1] = (self._E).split('+')
        self._arr_road[2] = (self._S).split('+')
        self._arr_road[3] =  (self._W).split('+')

        self._keep_original[0] = (self._N).split('+')
        self._keep_original[1] = (self._E).split('+')
        self._keep_original[2] = (self._S).split('+')
        self._keep_original[3] = (self._W).split('+')

        if 'road' in self._arr_road[from_side]:
            ## it gets the given side and checks other side if there is a road
            ## connection
            self._arr_road.pop(from_side)
            self._keep_original[from_side] = None
            for i in self._arr_road:
                if 'road' in i:
                    ## it finds a road connection
                    keep_orig_index =  self._keep_original.index(i)
                    array_pop = self._arr_road.index(i)
                    self._arr_road.pop(array_pop)
                    for b in self._arr_road:
                        ## then it checks other side again and if finds
                        # another road it return -1 for crossroad, other
                        # it just returns the side
                        if 'road' not in b:
                            return keep_orig_index
                        elif 'road' in b:
                            return -1


    def city_connects(self, sideA,sideB):
        '''
        This method checks if two sides are both cities and they are connected.
        If so, it returns True, otherwise False.
        '''
        if 'city' in self._array[sideA] and 'city' in self._array[sideB] and \
                self._unconnected_city != 'unconnected':
            return True
        elif sideA == sideB:
            return True
        else:
            return False

    def cities_sides_retval(self, side):
        '''
        the function should return a list.
        That list should contain the sides
        of the tile which are connected to
        to the side given as a parameter.
        '''
        self._cities_sides = []
        if side == 0:
            if self.city_connects(0, 1) == True:
                self._cities_sides.append(1)
            if self.city_connects(0, 2) == True:
                self._cities_sides.append(2)
            if self.city_connects(0, 3) == True:
                self._cities_sides.append(3)
        if side == 1:
            if self.city_connects(0, 1) == True:
                self._cities_sides.append(0)
            if self.city_connects(1, 2) == True:
                self._cities_sides.append(2)
            if self.city_connects(1, 3) == True:
                self._cities_sides.append(3)
        if side == 2:
            if self.city_connects(2, 0) == True:
                self._cities_sides.append(0)
            if self.city_connects(2, 1) == True:
                self._cities_sides.append(1)
            if self.city_connects(2, 3) == True:
                self._cities_sides.append(3)
        if side == 3:
            if self.city_connects(3, 0) == True:
                self._cities_sides.append(0)
            if self.city_connects(3, 1) == True:
                self._cities_sides.append(1)
            if self.city_connects(3, 2) == True:
                self._cities_sides.append(2)
        return self._cities_sides

    def rotate(self):
        '''
        This method returns a new object, which represents the same tile, but
        rotated clockwise by 90 degrees. It return a new object and does
        not modify  the original object.
        '''
        self._arr_rotate = [None,None,None,None]
        self._arr_rotate[0] = self._N
        self._arr_rotate[1] = self._E
        self._arr_rotate[2] = self._S
        self._arr_rotate[3] = self._W
        ## it creates an array and change the order of items in that array
        # with for loop

        for i in range(0, 3):
            first = self._arr_rotate[0]
            for j in range(0, len(self._arr_rotate) - 1):
                self._arr_rotate[j] = self._arr_rotate[j + 1]
            self._arr_rotate[len(self._arr_rotate) - 1] = first

        return CarcassonneTile(self._arr_rotate[0], self._arr_rotate[1],
                self._arr_rotate[2], self._arr_rotate[3],self._unconnected_city)



tile01 = CarcassonneTile('city',(f"grass+road"),'grass',(f"grass+road"))
tile02 = CarcassonneTile('city','city','grass','city')
tile03 = CarcassonneTile((f"grass+road"),(f"grass+road"),(f"grass+road"),
                         (f"grass+road"))
tile04 = CarcassonneTile('city',(f"grass+road"),(f"grass+road"),'grass')
tile05 = CarcassonneTile('city','city','city','city')
tile06 = CarcassonneTile((f"grass+road"),'grass',(f"grass+road"),'grass')
tile07 = CarcassonneTile('grass','city','grass','city','unconnected')
tile08 = CarcassonneTile('grass','city','grass','city',)
tile09 = CarcassonneTile('city','city','grass','grass',)
tile10 = CarcassonneTile('grass',(f"grass+road"),(f"grass+road"),
                         (f"grass+road"))
tile11 = CarcassonneTile('city',(f"grass+road"),(f"grass+road"),'city')
tile12 = CarcassonneTile('city','grass',(f"grass+road"),(f"grass+road"))
tile13 = CarcassonneTile('city',(f"grass+road"),(f"grass+road"),
                         (f"grass+road"))
tile14 = CarcassonneTile('city','city','grass','grass','unconnected')
tile15 = CarcassonneTile('grass','grass',(f"grass+road"),(f"grass+road"))
tile16 = CarcassonneTile('city','grass','grass','grass',)

N = 0
E = 1
S = 2
W = 3