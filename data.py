neighbor_map = {'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
                'Bucharest': ['Urziceni', 'Pitesti', 'Giurgiu', 'Fagaras'],
                'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
                'Drobeta': ['Mehadia'],
                'Eforie': ['Hirsova'],
                'Fagaras': ['Sibiu'],
                'Hirsova': ['Urziceni'],
                'Iasi': ['Vaslui', 'Neamt'],
                'Lugoj': ['Timisoara', 'Mehadia'],
                'Oradea': ['Zerind', 'Sibiu'],
                'Pitesti': ['Rimnicu'],
                'Rimnicu': ['Sibiu'],
                'Urziceni': ['Vaslui']}

# 这里的权重参数有问题，和实际距离有差距，实际项目中重新计算了欧式距离作为新的权重
neighbormapWithweight = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
                         'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
                         'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
                         'Drobeta': {'Mehadia': 75},
                         'Eforie': {'Hirsova': 86},
                         'Fagaras': {'Sibiu': 99},
                         'Hirsova': {'Urziceni': 98},
                         'Iasi': {'Vaslui': 92, 'Neamt': 87},
                         'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
                         'Oradea': {'Zerind': 71, 'Sibiu': 151},
                         'Pitesti': {'Rimnicu': 97},
                         'Rimnicu': {'Sibiu': 80},
                         'Urziceni': {'Vaslui': 142}
                         }

# 坐标位置
romania_map_locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

straight_line_distance_to_Bucharest = dict(
    Arad=366, Bucharest=0, Craiova=160,
    Drobeta=242, Eforie=161, Fagaras=178,
    Giurgiu=77, Hirsova=151, Iasi=266,
    Lugoj=244, Mehadia=241, Neamt=234,
    Oradea=380, Pitesti=98, Rimnicu=193,
    Sibiu=253, Timisoara=329, Urziceni=80,
    Vaslui=199, Zerind=374)
