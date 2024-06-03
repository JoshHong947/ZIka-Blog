import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

# 读取数据
file_path = '/Users/Meraki/Desktop/shetuan.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1 (2)')
data.columns = ['id', 'st', 'room']

# 创建无向图
G = nx.Graph()

# 添加节点和边
for idx, row in data.iterrows():
    G.add_node(row['id'], bipartite=0)
    G.add_node(row['st'], bipartite=1)
    G.add_edge(row['id'], row['st'], room=row['room'])

# 设置节点属性
top_nodes = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}
bottom_nodes = set(G) - top_nodes

# 设置节点颜色和形状
color_map = []
shape_map = []
for node in G:
    if node in top_nodes:
        color_map.append('red')
        shape_map.append('o')  # circle
    else:
        color_map.append('green')
        shape_map.append('s')  # square

# 绘制双向图
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=color_map, node_shape='o', edge_color='black')
plt.show()

# 获取二分图的关联矩阵
incidence_matrix = nx.bipartite.matrix.biadjacency_matrix(G, row_order=top_nodes, column_order=bottom_nodes).toarray()

# 学生关系
student_adj = incidence_matrix.dot(incidence_matrix.T)
student_adj[student_adj > 0] = 1

# 创建学生关系图
student_G = nx.from_numpy_matrix(student_adj)
student_G = nx.relabel_nodes(student_G, {i: list(top_nodes)[i] for i in range(len(top_nodes))})
nx.draw(student_G, with_labels=False, node_size=[200 * nx.degree(student_G)[n] for n in student_G], node_color='green', node_shape='s', layout=nx.spring_layout(student_G))
plt.show()

# 度分布
degree_sequence = [d for n, d in student_G.degree()]
plt.hist(degree_sequence, bins=range(max(degree_sequence) + 1))
plt.show()

# 社团关系
club_adj = incidence_matrix.T.dot(incidence_matrix)
club_adj[club_adj > 0] = 1

# 创建社团关系图
club_G = nx.from_numpy_matrix(club_adj)
club_G = nx.relabel_nodes(club_G, {i: list(bottom_nodes)[i] for i in range(len(bottom_nodes))})
nx.draw(club_G, with_labels=False, node_size=[200 * nx.degree(club_G)[n] for n in club_G], node_color='green', node_shape='s', layout=nx.spring_layout(club_G))
plt.show()

# 度分布
degree_sequence = [d for n, d in club_G.degree()]
plt.hist(degree_sequence, bins=range(max(degree_sequence) + 1))
plt.show()
