from operator import itemgetter


def travelling_salesman_problem(graph, s, V, cities_list):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    dist = []
    while True:
        temp_dict = {}
        current_pathweight = 0

        k = s
        st = ''
        for i in range(len(vertex)):
            st = st + cities_list[k] + ' -> '
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        st = st + cities_list[k] + ' -> '
        st = st + cities_list[s]
        current_pathweight += graph[k][s]

        temp_dict['dist'] = current_pathweight
        temp_dict['path'] = st
        dist.append(temp_dict)
        if not next_permutation(vertex):
            break

    newlist = sorted(dist, key=itemgetter('dist'), reverse=True)
    print(newlist)
    return newlist


def next_permutation(L):
    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True


def get_paths(dep, dests):
    print(dests)
    cities = {
        'Nursultan': [0, 968, 992, 271, 1005, 857, 1484, 798, 922, 1388, 190, 578, 829, 1728, 250, 442, 908, 623],
        'Almaty': [968, 0, 604, 1240, 1683, 223, 1994, 857, 451, 2101, 783, 1473, 926, 2064, 994, 1408, 699, 839],
        'Shymkent': [992, 604, 0, 1216, 1298, 764, 1492, 1307, 156, 1694, 876, 1288, 433, 1500, 1233, 1399, 154, 1208],
        'Kokshetau': [271, 1240, 1216, 0, 900, 1126, 1413, 982, 1164, 1237, 461, 382, 977, 1705, 527, 183, 1112, 809],
        'Aktobe': [1005, 1683, 1298, 900, 0, 1685, 523, 1802, 1357, 414, 1135, 548, 867, 866, 1393, 956, 1144, 1627],
        'Taldykorgan': [857, 223, 764, 1126, 1685, 0, 2045, 634, 607, 2102, 667, 1404, 1012, 2155, 810, 1281, 828, 615],
        'Atyrau': [1484, 1994, 1492, 1413, 523, 2045, 0, 2264, 1596, 460, 1586, 1071, 1078, 390, 1883, 1478, 1346,
                   2093],
        'Ust-Kamenagorsk': [798, 857, 1307, 982, 1802, 634, 2264, 0, 1162, 2186, 678, 1355, 1401, 2468, 463, 1061, 1317,
                            175],
        'Taraz': [922, 451, 156, 1164, 1357, 607, 1596, 1162, 0, 1765, 784, 1283, 519, 1630, 1122, 1347, 257, 1072],
        'Uralsk': [1388, 2101, 1694, 1237, 417, 2102, 460, 2186, 1765, 0, 1533, 856, 1260, 846, 1756, 1247, 1540, 2010],
        'Karaganda': [190, 783, 876, 461, 1135, 667, 1586, 678, 784, 1533, 0, 755, 796, 1796, 382, 624, 815, 510],
        'Kostanay': [578, 1473, 1288, 382, 548, 1404, 1071, 1355, 1283, 856, 755, 0, 939, 1399, 908, 407, 1153, 1180],
        'Kyzylorda': [829, 926, 433, 977, 867, 1012, 1078, 1401, 519, 1260, 796, 939, 0, 1143, 1178, 1148, 280, 1260],
        'Aktau': [1728, 2064, 1500, 1705, 866, 2155, 390, 2468, 1630, 846, 1796, 1399, 1143, 0, 2131, 1796, 1373, 2305],
        'Pavlodar': [250, 994, 1233, 527, 1393, 810, 1883, 463, 1122, 1756, 382, 908, 1178, 2131, 0, 598, 1189, 301],
        'Petropavlovsk': [442, 1408, 1399, 183, 956, 1281, 1478, 1061, 1347, 1247, 624, 407, 1148, 1796, 598, 0, 1293,
                          897],
        'Turkestan': [908, 699, 154, 1112, 1144, 828, 1346, 1317, 257, 1540, 815, 1153, 280, 1373, 1189, 1293, 0, 1201],
        'Semey': [623, 829, 1208, 809, 1627, 615, 2093, 175, 1072, 2010, 510, 1180, 1260, 2305, 301, 897, 1201, 0]
    }
    distances = []
    sq = 0
    for idx, city in enumerate(dests):
        if city == dep:
            sq = idx
        distances.append(cities[city])
    return travelling_salesman_problem(distances, sq, len(distances), dests)
