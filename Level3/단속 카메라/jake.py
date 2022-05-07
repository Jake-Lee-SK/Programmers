def solution(routes):
    # 나가는 순으로 정렬
    routes = sorted(routes, key = lambda x : (x[1]))
    camera = 0
    while routes:
        # 맨 처음 나가는 차량의 위치를 저장
        together = []
        together.append(routes[0])
        out = routes[0][1]
        # 카메라를 한 대 설치
        camera += 1
        # 그 카메라에 찍히는 녀석들을 제외
        for i in range(1, len(routes)):
            if routes[i][0] <= out <= routes[i][1]:
                together.append(routes[i])
                continue
        for car in together:
            routes.remove(car)
        # 그 후 반복
    return camera