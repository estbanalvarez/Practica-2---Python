GAMES = 25
WEIGHT_GOALS=1.5
WEIGHT_GOALS_AVOIDED=1.25
WEIGHT_ASSIST=1

def  generate_structure(names,goals,goals_avoided,assists):
    """Esta funcion retorna una sola estructura de datos 
        que es una secuencia de tuplas, donde cada una de estas contiene el elemento que corresponde 
        de cada una de  la estructuras que recibio
        """
    return list(zip(names,goals,goals_avoided,assists))


def goal_scorer(players):
    """Esta funcion retorna en una tupla el nombre del goleador o 
        goleadora y su cantidad de goles"""
    
    return max(players, key=lambda player: player[1])[:2]

def promedio_ponderado(goles, goles_salvados, asist):
    """Esta funcionte retorna un promedio ponderado"""
    
    return goles*WEIGHT_GOALS + goles_salvados*WEIGHT_GOALS_AVOIDED + asist * WEIGHT_ASSIST


def influential_player(players):
    """ Esta funcion  retorna el nombre del jugador mas influyente"""
    
    list_influential= [(player[0],promedio_ponderado(player[1],player[2],player[3])) for player in players]
    
    return max(list_influential, key = lambda player: player[1])[0]

def goals_average(players):
    """Esta funcion  retorna el promedio de gol del equipo en general"""
    
    return sum(player[1] for player in players) /GAMES

def striker_average(players):
    """Esta funcion retorna el promedio de goles por partido del goleador o goleadora del equipo"""
    
    return goal_scorer(players)[1]/GAMES