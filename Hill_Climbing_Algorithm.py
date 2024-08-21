#HILL CLIMBING ALGORITHM
#TO FIND THE SHORTEST PATH TO TRAVEL THROUGH CITIES

import numpy as np
import random
      
def algo_dijkstras(metrx):    #finding the shortest dist between two cities and return shortest dist metrx
    n = len(metrx)
    dists = np.copy(metrx)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]

    return dists.tolist()

def randm_seq(shotest_dis_metrx):   #generate random sequence of all the cities
    n = len(shotest_dis_metrx)
    randm_routs =[]
    for i in range(1000):
        new_randm_generted_rout = random.sample(range(1,n), n-1)
        if new_randm_generted_rout not in randm_routs:
            randm_routs.append(new_randm_generted_rout)
    return randm_routs

def dist_of_truck_traversl_paths(orderOfCities, shortest_dis_metrx):   #return the dist tavelled by a truck from source to destination
    n = len(orderOfCities)
    distBetweenPaths = 0
    for i in range(n-1):
        distBetweenPaths += shortest_dis_metrx[orderOfCities[i]][orderOfCities[i+1]]
    return distBetweenPaths + shortest_dis_metrx[0][orderOfCities[0]]

def HillClimbingfunction(truk_capcity,randm_routs,shortest_dis_metrx):    #hill climbing algorithm
    bst_rout = []
    shortst_dist = float('inf')
    for i in range (len(randm_routs)):
        tot_dist = 0
        for j in range(len(truk_capcity)):
            siz = truk_capcity[j]
            truk_path = randm_routs[i][0:siz]
            dist = dist_of_truck_traversl_paths(truk_path,shortest_dis_metrx)
            tot_dist += dist
            randm_routs[i]=randm_routs[i][siz:]
        if tot_dist < shortst_dist:
            bst_rout_index = i
            shortst_dist = tot_dist
            
    return bst_rout_index,shortst_dist


def main():
    with open("input.txt", "r") as givn_inpt_file:     #reading the input file
        lines = givn_inpt_file.readlines()
        for line in lines[:2]:
            n = len(line.strip().split(','))  
        CityOrdr = [list(map(lambda x: int(x) if x != "N" else float("inf"), line.strip().split(','))) for line in lines[:n]]

    
    truks = []   # Parse truck information to a list
    for line in lines[n :]:
        components = line.strip().split('#')
        truk_no = components[0]
        capacity = int(components[1])
        truks.append([truk_no, capacity])
        
    
    
    truk_capcity = []  #list of truck capacities
    for i in range(len(truks)):
        truk_capcity.append(truks[i][1])
    
    shortst_dists = algo_dijkstras(CityOrdr)
    randm_routs = randm_seq(shortst_dists)
    path_copy = randm_routs.copy()
    index, dist = HillClimbingfunction(truk_capcity, path_copy, shortst_dists)
    
    path = randm_routs[index]
    
    with open("210382H.txt", 'w') as output_file:
        #formatting the output
        for i in range (len(truk_capcity)):
            rng = truk_capcity[i]
            city_list = path[0:rng]
            city_string = ''
            for j in range(len(city_list)):
                city_string += chr(ord('a') + city_list[j])+' '
            output_file.write('truck_'+str(i+1)+'#' + city_string +'\n')
            
            path = path[rng:]
        output_file.write(str(int(dist)))
if __name__=="__main__":
    main()
