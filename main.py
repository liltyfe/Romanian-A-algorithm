from data import *
from mapclass import *


class Node:
    def __init__(self, name, father=None, g=0, h=0):
        self.name = name
        self.father = father
        self.g = g
        self.h = h
        self.f = self.g + self.h


def find_path(end_node):
    path = []
    while end_node.father is not None:
        path.append(end_node.name)
        end_node = end_node.father
    path.append(end_node.name)
    path.reverse()
    return path


def A_star_search(start, end, map_obj: my_Map):
    open_list = []  # 存储开启列表
    closed_list = []  # 存储关闭列表
    # 计算欧式距离
    map_obj.update_Euclidean_distance(end)
    # 加入开启列表
    first_node = Node(start, father=None, g=0, h=map_obj.Euclidean_distances[start])
    open_list.append(first_node)

    while True:
        if not open_list:
            return None
        current_node = open_list.pop(0)
        closed_list.append(current_node.name)
        if current_node.name == end:
            return current_node
        neighbour_list = map_obj.get_neighbours(current_node.name)
        neighbour_weight_list = map_obj.get_neighbour_weight(current_node.name)

        # 打印函数，调试使用
        # print("--------------------------------------")
        # print("current_node:", current_node.name)

        for i in range(len(neighbour_list)):
            # 打印函数，调试使用
            # print(neighbour_list[i])
            if neighbour_list[i] not in closed_list:
                g = current_node.g + neighbour_weight_list[i]
                neighbour_node = Node(neighbour_list[i], current_node, g=g, h=map_obj.Euclidean_distances[neighbour_list[i]])
                open_list.append(neighbour_node)
        # 重新排序
        open_list.sort(key=lambda x: x.f)
        # 打印函数，调试使用
        # for node in open_list:
        #     print(node.name, "f: ", node.f)


def main():
    # Load the data
    x_limit = 600
    y_limit = 600

    # get map
    map_obj = my_Map((20, 20), x_limit, y_limit)

    # 绘制原始图像图
    for node, value in romania_map_locations.items():
        map_obj.add_point(value[0], value[1], name=node)
    for neighbor in neighbormapWithweight:
        for node, weight in neighbormapWithweight[neighbor].items():
            map_obj.add_line(neighbor, node)

    # A*算法搜索路径
    # --- test 1
    # start = 'Arad'
    # end = 'Bucharest'
    # --- test 2
    # start = 'Arad'
    # end = 'Eforie'
    # --- test 3
    # start = 'Urziceni'
    # end = 'Mehadia'
    # --- test 4
    start = 'Vaslui'
    end = 'Timisoara'

    end_node = A_star_search(start, end, map_obj)
    cost = end_node.g
    if end_node is None:
        print("No path found")
        return
    # 回溯路径
    path= find_path(end_node)

    print("path:", path)
    print("cost:", cost)
    # 绘制路径
    map_obj.draw_path(path)
    # 显示图像
    map_obj.show_map(start, end)


if __name__ == '__main__':
    main()
