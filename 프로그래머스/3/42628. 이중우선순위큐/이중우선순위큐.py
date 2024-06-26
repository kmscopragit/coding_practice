def solution(operations):
    answer = [0,0]
    tree = {}
    for operation in operations:
        if operation[0] == 'I':   # 삽입 명령
            current = int(operation[2:])
            if tree:
                visit = root
                while visit:
                    idx = 0 if current < visit else 1   # 왼쪽(0) or 오른쪽(1)
                    if tree[visit][idx] == None:
                        tree[visit][idx] = current
                        tree[current] = [None, None]
                        break
                    else:
                        visit = tree[visit][idx]
            else:
                tree[current] = [None, None]
                root = current
        
        else:
            # 최대값 명령
            if operation.split()[-1] == "1" and tree:
                visit = root
                parent = False
                # 조회
                while True:
                    if tree[visit][1] == None:
                        break
                    else:
                        parent = visit
                        visit = tree[visit][1]
                # 삭제
                if parent == False:   # root node 삭제해야 한다면
                    if tree[visit][0] != None:
                        root = tree[visit][0]
                else:
                    tree[parent][1] = tree[visit][0]   # 자식 노드의 왼쪽 첫번째 노드 연결 없으면 None
                tree.pop(visit)
                        
            # 최소값 명령
            elif operation.split()[-1] == "-1" and tree:
                print('ok')
                visit = root
                parent = False
                # 조회
                while True:
                    if tree[visit][0] == None:
                        break
                    else:
                        parent = visit
                        visit = tree[visit][0]
                # 삭제
                if parent == False:   # root node 삭제해야 한다면
                    if tree[visit][1] != None:
                        root = tree[visit][1]
                else:
                    tree[parent][0] = tree[visit][1]   # 자식 노드의 우측 첫번째 노드 연결 없으면 None
                tree.pop(visit)
    if tree:
        answer = [max(tree), min(tree)] 
    return answer