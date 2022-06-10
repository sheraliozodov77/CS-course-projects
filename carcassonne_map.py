'''File: crcassonne_map.py
   Author: Sherali Ozodov
   Purpose: This program finishes to implement crcassonne game. In addition
   to previous versions of the game, the program creates some method, such as
   tracing road both forward and backward and tracing city. It is now
   comlete as it was required.
'''

import carcassonne_tile

class CarcassonneMap:

    def __init__(self):
        '''
        The constructor doesn't take any parameter (beside self). It
        creates some arrays and dictionary to store data.
        '''

        self._dic_map_array = []
        ##   self.dic_map_array is an array that store all coordinates in
        # which tiles are on the grid.
        self._dic_map_tiles = []
        ## self.dic_map_tiles_dictionary stores coordinates and tile on
        # the grid
        self._dic_map_border = []
        self._dic_map_tiles_dictionary = {}

        self._dic_map_array.append((0, 0))
        self._dic_map_tiles.append(carcassonne_tile.tile01)
        self._dic_map_tiles_dictionary = {(0, 0): carcassonne_tile.tile01}


    def dic_map_to_coord_side(self):
        '''
        This function takes the dictionary self._dic_map_tiles_dictionary
        which keys are (x,y) coordinates of the tile in the map and values
        and these tiles. It creates a new dictionary and returns (x,y)
        coordinates of the tile in the map and all four sides of the tiles.
        '''
        self._ret_coord_with_sides = {}
        for i in self._dic_map_tiles_dictionary:
            ## it calls get_edge method to get the sides of the tiles
            self._ret_coord_with_sides[(i[0],i[1])] = [self._dic_map_tiles_dictionary[i].get_edge(0),
                self._dic_map_tiles_dictionary[i].get_edge(1), self._dic_map_tiles_dictionary[i].get_edge(2),
                    self._dic_map_tiles_dictionary[i].get_edge(3),]
        return self._ret_coord_with_sides


    def get_border_city(self,x,y,side):
        '''
        This function takes two coordinates and side. If the two
        coordinates are in the dictionary,self._ret_coord_with_sides
        created above, it then checks connected sides of the tiles.
        It returns the given coordinates and the side that is connected
        with city.
        '''
        if side == 0:
            if (x,y+1) in self.dic_map_to_coord_side():
                if 'city' in self.dic_map_to_coord_side()[x,y+1][2]:
                    return ((x,y+1,2))
        elif side == 1:
            if (x+1,y) in self.dic_map_to_coord_side():
                if 'city' in self.dic_map_to_coord_side()[x+1,y][3]:
                    return ((x+1,y,3))
        elif side == 2:
            if (x,y-1) in self.dic_map_to_coord_side():
                if 'city' in self.dic_map_to_coord_side()[x,y-1][0]:
                    return ((x,y-1,0))
        elif side == 3:
            if (x - 1, y) in self.dic_map_to_coord_side():
                if 'city' in self.dic_map_to_coord_side()[x-1,y][1]:
                    return ((x-1,y,1))
        return []


    def reverse_road(self, lists):
        '''
        This function takes an array and reverse the order of
        item in the array. It changes the direction of road in the backwards
        '''
        if len(lists) == 0:
            return []
        reverse_road_temp = []
        for index in range(len(lists)):
            tuples = list(lists[len(lists) - index - 1])
            reverse_road_temp.append((tuples[0], tuples[1], tuples[3], tuples[2]))
        return reverse_road_temp

    def trace_road(self, x, y, side):
        '''
        This function traces the road in both directions: both moving forward
        and backward.
        '''
        temp_side = self.get(x,y).road_get_connection(side)
        traced_side = self.reverse_road(self.trace_road_one_direction(x,y,temp_side))+ \
               [(x, y, temp_side, side)] + self.trace_road_one_direction(x,y,side)
        return traced_side

    def get_all_coords(self):
        '''
        This method return all the coordinates in self.dic_map_array
        '''
        return set(self._dic_map_array)

    def find_map_border(self):
        '''
        This method every tile coordinate and checks border.
        If there is a border in which there is no tile, it will
        and to self.dic_map_border array.
        '''
        for i in self._dic_map_array:
            if (i[0]-1, i[1]) not in self._dic_map_array:
                self._dic_map_border.append((i[0]-1, i[1]))
            if (i[0], i[1]+1) not in self._dic_map_array:
                self._dic_map_border.append((i[0], i[1]+1))
            if (i[0], i[1]-1) not in self._dic_map_array:
                self._dic_map_border.append((i[0], i[1]-1))
            if (i[0]+1, i[1]) not in self._dic_map_array:
                self._dic_map_border.append((i[0]+1, i[1]))
        return set(self._dic_map_border)

    def get(self, x,y):
        '''
        This method returns returns the tile at the specified (x,y) location.
        If it does not exist, it return None.
        '''
        if (x, y) in self._dic_map_array:
            index = self._dic_map_array.index((x, y))
            return self._dic_map_tiles[index]


    def add(self, x, y, tile, confirm=True, tryOnly=False):
        '''
        This method adds a given tile, at the given x,y location.It returns True if
        True if returns True if it is possible to add the tile, or False if it is not.
        not. It has two defaults confirm and tryOnly. It does error checking based
        on that values as well.
        '''
        if confirm == True and tryOnly == False:
            ## (x,y) in the array which has all current coordinates, it checks
            ## (x-1,y) which is on the west of the tile aimed to be added.
            if (x, y) not in self._dic_map_array:
                if (int(x - 1), y) in self._dic_map_array:
                    current = (x, y)
                    comparable = (int(x - 1), y)
                    # after taking the tile aimed to be added and the one
                    # on the west of it, it does some error checking and
                    # return True if it is possible to add the given tile.
                    if abs(int(current[0] - comparable[0])) + \
                            abs(int(current[1] - comparable[1])) == 1:
                        last_tile = self._dic_map_tiles_dictionary[(x - 1), y]
                        if tile.get_edge(3) == last_tile.get_edge(1):
                            self._dic_map_array.append((x, y))
                            self._dic_map_tiles.append(tile)
                            self._dic_map_tiles_dictionary[(x, y)] = tile
                            return True
                        return False
                    return False

                elif (x, int(y - 1)) in self._dic_map_array:
                    ## (x,y-1) which is on the south of the tile aimed
                    # to be added.
                    current = (x, y)
                    comparable = (x, int(y - 1))
                    if abs(int(current[0] - comparable[0])) + \
                            abs(int(current[1] - comparable[1])) == 1:
                        last_tile = self._dic_map_tiles_dictionary[x, y - 1]
                        if tile.get_edge(S) == last_tile.get_edge(N):
                            self._dic_map_array.append((x, y))
                            self._dic_map_tiles.append(tile)
                            self._dic_map_tiles_dictionary[(x, y)] = tile
                            return True
                        return False
                    return False

                elif (int(x + 1), y) in self._dic_map_array:
                    ## (x+1,y) which is on the east of the tile aimed to be
                    # added.
                    current = (x, y)
                    comparable = (int(x + 1), y)
                    if abs(int(current[0] - comparable[0])) + \
                            abs(int(current[1] - comparable[1])) == 1:
                        last_tile = self._dic_map_tiles_dictionary[(x + 1), y]
                        if tile.get_edge(E) == last_tile.get_edge(W):
                            self._dic_map_tiles_dictionary[(x, y)] = tile
                            self._dic_map_array.append((x, y))
                            self._dic_map_tiles.append(tile)
                            return True
                        return False
                    return False

                elif (x, int(y + 1)) in self._dic_map_array:
                    ## (x,y+1) which is on the north of the tile aimed to be
                    # added.
                    current = (x, y)
                    comparable = (x, int(y + 1))
                    if abs(int(current[0] - comparable[0])) + \
                            abs(int(current[1] - comparable[1])) == 1:
                        last_tile = self._dic_map_tiles_dictionary[x, y + 1]
                        if tile.get_edge(N) == last_tile.get_edge(S):
                            self._dic_map_array.append((x, y))
                            self._dic_map_tiles.append(tile)
                            self._dic_map_tiles_dictionary[(x, y)] = tile
                            return True
                        return False
                    return False
                return False
            elif (x, y) in self._dic_map_array:
                ## if the given tile is already in the array, it return False
                return False


        elif confirm == True and tryOnly == True:
            ## this elif does the same thing except not adding to map. It only
            ## checks and return True if it is possbile to add the given tile.
            if (x, y) not in self._dic_map_array:
                if (int(x - 1), y) in self._dic_map_array:
                    current = (x, y)
                    comparable = (int(x - 1), y)
                    if abs(int(current[0] - comparable[0])) + \
                            abs(int(current[1] - comparable[1])) == 1:
                        last_tile = self._dic_map_tiles_dictionary[x-1,y]
                        if tile.get_edge(W) == last_tile.get_edge(E):
                            return True
                        return False
                    return False

                elif (x, int(y - 1)) in self._dic_map_array:
                    current = (x, y)
                    comparable = (x, int(y - 1))
                    if abs(int(current[0] - comparable[0])) + \
                            abs(int(current[1] - comparable[1])) == 1:
                        last_tile = self._dic_map_tiles_dictionary[x,y-1]
                        if tile.get_edge(S) == last_tile.get_edge(N):
                            return True
                        return False
                    return False

                elif (int(x + 1), y) in self._dic_map_array:
                    current = (x, y)
                    comparable = (int(x + 1), y)
                    if abs(int(current[0] - comparable[0])) + \
                            abs(int(current[1] - comparable[1])) == 1:
                        last_tile = self._dic_map_tiles_dictionary[x+1,y]
                        if tile.get_edge(E) == last_tile.get_edge(W):
                            return True
                        return False
                    return False


                elif (x, int(y + 1)) in self._dic_map_array:
                    current = (x, y)
                    comparable = (x, int(y + 1))
                    if abs(int(current[0] - comparable[0])) + \
                            abs(int(current[1] - comparable[1])) == 1:
                        last_tile = self._dic_map_tiles_dictionary[x,y+1]
                        if tile.get_edge(N) == last_tile.get_edge(S):
                            return True
                        return False
                    return False
                return False
            elif (x, y) in self._dic_map_array:
                return False

        elif confirm == False and tryOnly == True:
            ## it is an invalid combination. Therefore, it just
            ## returns False
            return False

        elif confirm == False and tryOnly == False:
            ## it just adds the given tile to the map without any
            # error-checking.
            self._dic_map_array.append((x, y))
            self._dic_map_tiles.append(tile)
            self._dic_map_tiles_dictionary[(x, y)] = tile
            return True

    def trace_road_one_direction(self, x, y, side, keep_x='', keep_y=''):
        '''
        This function takes two coordinates and side of tiles.
        It has two default parameters to detect loops.
        '''
        self._trace_array = []
        if keep_x == '':
            keep_x = x
            keep_y = y

        if side == 0:
            ## if the given side if North and there is a tile in
            # the north of it, and if it has no crossroad, it then appends
            ## the pssible tiles and their coordinates
            if (x, y + 1) in self._dic_map_tiles_dictionary:
                current_tile = self._dic_map_tiles_dictionary[(x, y + 1)]
                if 'road' in current_tile.get_edge(2) and \
                        current_tile.has_crossroads():
                    self._trace_array.append((x, y + 1, 2, -1))
                else:
                    tile_edge = current_tile.road_get_connection(2)
                    self._trace_array.append((x, y + 1, 2, tile_edge))
                    if (x, y + 1) != (keep_x, keep_y):
                        ## it does not detect a loop, it recurces and appends
                        ## the pssible tiles and their coordinates.
                        self._trace_array += self.trace_road_one_direction\
                            (x, y + 1, tile_edge, keep_x, keep_y)
        ## it then repeats checking with east, south and west.
        elif side == 1:
            if (x + 1, y) in self._dic_map_tiles_dictionary:
                current_tile = self._dic_map_tiles_dictionary[(x + 1, y)]
                if 'road' in current_tile.get_edge(3) and \
                        current_tile.has_crossroads():
                    self._trace_array.append((x + 1, y, 3, -1))
                else:
                    tile_edge = current_tile.road_get_connection(3)
                    self._trace_array.append((x + 1, y, 3, tile_edge))
                    if (x + 1, y) != (keep_x, keep_y):
                        self._trace_array += self.trace_road_one_direction\
                            (x + 1, y, tile_edge, keep_x, keep_y)

        elif side == 2:
            if (x, y - 1) in self._dic_map_tiles_dictionary:
                current_tile = self._dic_map_tiles_dictionary[(x, y - 1)]
                if 'road' in current_tile.get_edge(0) and \
                        current_tile.has_crossroads():
                        self._trace_array.append((x, y - 1, 0, -1))
                else:
                    tile_edge = current_tile.road_get_connection(0)
                    self._trace_array.append((x, y - 1, 0, tile_edge))
                    if (x, y - 1) != (keep_x, keep_y):
                        self._trace_array += self.trace_road_one_direction\
                            (x, y - 1, tile_edge, keep_x, keep_y)
        elif side == 3:
            if (x - 1, y) in self._dic_map_tiles_dictionary:
                current_tile = self._dic_map_tiles_dictionary[(x - 1, y)]
                if 'road' in current_tile.get_edge(1) and \
                        current_tile.has_crossroads():
                    self._trace_array.append((x - 1, y, 1, -1))
                else:
                    tile_edge = current_tile.road_get_connection(1)
                    self._trace_array.append((x - 1, y, 1, tile_edge))
                    if (x - 1, y) != (keep_x, keep_y):
                        self._trace_array += self.trace_road_one_direction\
                            (x - 1, y, tile_edge, keep_x, keep_y)
        return self._trace_array

    def trace_city_temp(self, x, y, side):
        '''
        This function takes two coordinates and a side. It searches from
        given coordinates and finds all of the parts of the city.
        '''
        temp_sets = set()
        temp_sets.add((x, y, side))
        keep_searching = True
        while keep_searching:
            keep_searching = False
            dup = list(temp_sets)
            ## it checks every location in the duplicate of the city
            for item in dup:
                item = list(item)
                if self.get(item[0], item[1]).cities_sides_retval(item[2]) != []:
                    temp = self.get(item[0], item[1]).cities_sides_retval(item[2])
                    for index in temp:
                        ## it also checks every other side of the same tile.
                        if (item[0], item[1], index) not in temp_sets:
                            ## If this other side is not in the city,
                            ## it then adds other side to the set
                            temp_sets.add((item[0], item[1], index))
                            keep_searching = True

                info = self.get_border_city(item[0], item[1], item[2])
                ## it then gets the neighbour sides of city
                ## if the list of neighbours is not an empty,
                ## it adds the side to the set
                if info != []:
                    if info not in temp_sets:
                        temp_sets.add(info)
                        keep_searching = True

        return temp_sets

    def trace_city(self,x,y,side):
        '''
        This function returns set of edges and a boolean which
        indicate the map is complete.
        '''
        sign = True
        for w in self.trace_city_temp(x,y,side):
            if w[2] == 0:
                if (w[0], w[1] + 1, 2) not in self.trace_city_temp(x,y,side):
                    sign = False
            if w[2] == 1:
                if (w[0] + 1, w[1], 3) not in self.trace_city_temp(x,y,side):
                    sign = False
            if w[2] == 2:
                if (w[0], w[1] - 1, 0) not in self.trace_city_temp(x,y,side):
                    sign = False
            if w[2] == 3:
                if (w[0] - 1, w[1], 1) not in self.trace_city_temp(x,y,side):
                    sign = False

        return (sign, self.trace_city_temp(x,y,side))

N = 0
E = 1
S = 2
W = 3