# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 

#crea la estructura de datos
def create_data_structure(string):
    string=string.split('.')#el string se divide en frases separadas por un punto 
    users={}#diccionario para almacenar los usarios,sus conexiones y sus juegos
    nString=len(string)-1# la longitud del string(el cual ahora es una lista de frases)
    
    for frase in range(0, nString):
        nombre=string[frase][:string[frase].find(" ")]    #string[i] frase del string
        #print nombre
        if nombre not in users:
            connections=string[frase][string[frase].find('to')+3:]
            users[nombre]=[ connections.split(', '),[]]
            
        elif nombre in users and  users[nombre][1]==[]:# si esta el user pero no hay likes 
            games=string[frase][string[frase].find('play')+5:]#devuelve un string con todos los juegos
            users[nombre][1]+=(games.split(', '))
    return users
# ----------------------------------------------------------------------------- 
#Obtiene las conexiones de un usuario
def get_connections(network, user):
    if user not in network.keys():
        return None
    else:    
	    return network[user][0]

# ----------------------------------------------------------------------------- 
#Obtiene los juegos de un usuario
def get_games_liked(network,user):
    if user not in network.keys():
        return None
    else:    
	    return network[user][1]

# ----------------------------------------------------------------------------- 
#agrega una nueva conexion a un usuario
def add_connection(network, userA, userB):
    if userA not in network.keys() or userB not in network.keys():#si los users no estan entre las keys
        return False
    elif userB in network[userA][0]:#si el userB esta en las conexiones del userA
        return network
    else:
        network[userA][0].append(userB)
        
    return network

# ----------------------------------------------------------------------------- 
#agrega un nuevo user
def add_new_user(network, user, games):
    if user in network.keys():
        return network
    else:
        network[user]=[[],games]
        
    return network
		
# ----------------------------------------------------------------------------- 
#obtiene las conexiones de las conexiones
def get_secondary_connections(network, user):
    connectionList=[]
    if user not in network.keys():
        return None
    elif network[user][0]==[]:
        return []
    else:
        for connection in get_connections(network, user) :
                connectionList += get_connections(network, connection)
              #eliminar duplicados
                for item in connectionList:
                    if connectionList.count(item) >=2:
                        connectionList.remove(item)   
  
            
    return connectionList    
            

# ----------------------------------------------------------------------------- 	
#obtiene la cantidad de conexiones en comun
def count_common_connections(network, userA, userB):
    if userA not in network.keys() or userB not in network.keys():#si los users no estan entre las keys
        return False
   
    else:
        counter=0
        for connection in get_connections(network, userA):
            #print connection
            if connection in get_connections(network, userB):
                counter+=1
                 
             
    return counter

# ----------------------------------------------------------------------------- 
#encuentra el camino hacia un amigo
def find_path_to_friend(network, userA, userB, visited = None):
    print visited
    if visited == None: 
        visited = []
    if userA not in network or userB not in network: 
        return None
        
    connections = get_connections(network, userA)
    visited.append(userA)
    if userB in connections:
        path = [userA, userB] #path es la lista que se va a retornar
        visited.append(userB)
        return path
        
    for user in connections:
        if user in visited: 
            continue
        path = find_path_to_friend(network, user, userB, visited)
        if userB in visited:
            path.insert(0, userA) #mueve el user al frente de la lista
            return path
    return None
            
            
	    

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
#elimina un user
def removeUser(network, user):
    if user in network.keys():
        del network[user]
        return network
    else:
        return 'User no in network'
    

net = create_data_structure(example_input)
#print net

#print removeUser(net,'John')
#print get_connections(net, "Debra")
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_secondary_connections(net, "Mercedes")
#print count_common_connections(net, "Mercedes", "John")
#print find_path_to_friend(net, "John", "Ollie")
print find_path_to_friend(net, 'John', 'Levi')
