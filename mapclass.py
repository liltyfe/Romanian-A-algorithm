import matplotlib.pyplot as plt


class my_Map:
    def __init__(self, fig_size=(20, 20), ax_xlimit=200, ax_ylimit=200):
        self.nodes = {}
        """
        {name1: (x, y), name2: (x, y),...}
        """
        self.weights = {}
        """
        {name1: {name2: weight, name3: weight}, 
         name4: {name5: weight},
         ...}
        """
        self.ax_ylimit = ax_ylimit
        self.ax_xlimit = ax_xlimit
        self.fig, self.ax = plt.subplots(figsize=fig_size)
        self.Euclidean_distances = {}
        """
        {name1: distance, name2: distance, name3: distance,...}
        """

    def add_point(self, x, y, color='red', marker='o', name=None, show_name=True):
        node = (x, y)
        self.weights[name] = {}
        self.nodes[name] = node
        if 0 <= x <= self.ax_xlimit and 0 <= y <= self.ax_ylimit:
            self.ax.scatter(x, y, color=color, marker=marker, )
            self.ax.text(x, y+1, name if show_name else '')
        else:
            print("Point is outside the map")

    def add_line(self, name1=None, name2=None, color='black', linestyle='--', linewidth=1, update_weight=True):
        if name1 is None or name2 is None:
            print("Please enter the names of the two nodes")
        else:
            if name1 in self.nodes and name2 in self.nodes:
                x1, y1 = self.nodes[name1]
                x2, y2 = self.nodes[name2]
                weight = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                self.ax.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle, linewidth=linewidth)
                if update_weight:
                    self.weights[name1][name2] = weight

    def update_Euclidean_distance(self, EndNode=None):
        if EndNode is None:
            print("Please enter the names of the two nodes")
        else:
            if EndNode in self.nodes:
                x_end, y1_end = self.nodes[EndNode]
                for name1, node1 in self.nodes.items():
                    x1, y1 = node1
                    distance = ((x1 - x_end) ** 2 + (y1 - y1_end) ** 2) ** 0.5
                    self.Euclidean_distances[name1] = distance

    def get_neighbours(self, name):
        if name in self.nodes:
            neighbours_list = list(self.weights[name].keys())
            for node, value in self.weights.items():
                if name in list(value.keys()):
                    neighbours_list.append(node)
            return neighbours_list
        else:
            print("Node not found")
            return None

    def get_neighbour_weight(self, name):
        if name in self.nodes:
            neighbour_weight_list = list(self.weights[name].values())
            for node, value in self.weights.items():
                if name in list(value.keys()):
                    neighbour_weight_list.append(value[name])
            return neighbour_weight_list
        else:
            print("Node not found")
            return None

    def draw_path(self, path, color='blue', linewidth=3, linestyle='-'):
        if len(path) > 1:
            x_list = []
            y_list = []
            for name in path:
                x, y = self.nodes[name]
                x_list.append(x)
                y_list.append(y)
            self.ax.plot(x_list, y_list, color=color, linewidth=linewidth, linestyle=linestyle)
        else:
            print("Path should have at least two nodes")

    def show_map(self, start_node=None, end_node=None):
        self.ax.set_title(f"{start_node}->{end_node}")
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        plt.show()


# test the code
def main():
    my_map = my_Map((10, 10), 100, 100)
    my_map.add_point(0, 0, name='A')
    my_map.add_point(100, 100, name='B')
    my_map.add_point(50, 50, name='C')
    my_map.add_line(name1='A', name2='B', weigth=5)
    my_map.add_line(name1='A', name2='C', weigth=10)
    my_map.show_map()

if __name__ == '__main__':
    main()