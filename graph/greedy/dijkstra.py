# https://qiita.com/knhr__/items/cb3ce311508337128714

def dijkstra(nodes):
    start_node = nodes[0]
    routes_from_start = {n: math.inf for n in nodes}

    # 最初の頂点にゼロを設定
    routes_from_start[start_node] = 0

    minHeap = []

    # 最初の頂点を追加
    heappush(minHeap, (0, start_node))

    # ヒープがなくなるまで探索
    while minHeap:
        (cost, current_node) = heappop(minHeap)

        # priority keyは重複するのでここでチェックする
        if cost > routes_from_start[current_node]:
            continue

        for node in current_node.routes:
            price_info = current_node.routes[node]
            if routes_from_start[node] > price_info + routes_from_start[current_node]:
                routes_from_start[node] = price_info + routes_from_start[current_node]
                # 更新されたらpriorityに値を追加
                heappush(minHeap, (price_info + routes_from_start[current_node], node))

    return routes_from_start[nodes[-1]]


def dijkstra(nodes):
    start_node = nodes[0]
    routes_from_start = {n: math.inf for n in nodes}

    # 最初の頂点にゼロを設定
    routes_from_start[start_node] = 0

    minHeap = []


    # 最初の頂点を追加
    heappush(minHeap, (0, start_node))
    path = collections.defaultdict(Node)

    # ヒープがなくなるまで探索
    while minHeap:
        (cost, current_node) = heappop(minHeap)

        # priority keyは重複するのでここでチェックする
        if cost > routes_from_start[current_node]:
            continue

        for node in current_node.routes:
            price_info = current_node.routes[node]
            if routes_from_start[node] > price_info + routes_from_start[current_node]:
                routes_from_start[node] = price_info + routes_from_start[current_node]
                # 最短距離を更新するノードを記録する
                path[node.id] = current_node.id
                # 更新されたらpriorityに値を追加
                heappush(minHeap, (price_info + routes_from_start[current_node], node))

    current_node = nodes[-1].id
    path_array = []

    #最短距離を記録したノードをゴールからたどる
    while current_node:
        path_array.append(current_node)
        if current_node not in path:
            break
        current_node = path[current_node]

    return routes_from_start[nodes[-1]], path_array[::-1]