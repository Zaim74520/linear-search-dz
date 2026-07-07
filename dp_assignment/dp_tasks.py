def knapsack(weights, values, W):
    n = len(weights)
    # dp[i][w] = макс. стоимость первых i предметов при вместимости w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wi = weights[i - 1]
        vi = values[i - 1]
        for w in range(W + 1):
            # не берём предмет
            dp[i][w] = dp[i - 1][w]
            # берём, если влезает
            if wi <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)

    return dp[n][W]


def lcs_length(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def count_partitions(n):
    # dp[x] = количество способов получить сумму x
    dp = [0] * (n + 1)
    dp[0] = 1  # один способ получить 0: ничего не брать

    # перебираем слагаемые от 1 до n
    for num in range(1, n + 1):
        for x in range(num, n + 1):
            dp[x] += dp[x - num]

    return dp[n]


def floyd_warshall(dist):
    n = len(dist)
    # делаем копию, чтобы не менять исходную матрицу
    d = [row[:] for row in dist]

    for k in range(n):  # промежуточная вершина
        for i in range(n):  # начало
            for j in range(n):  # конец
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d


if __name__ == "__main__":
    # 01. Рюкзак
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    W = 8
    print("01. Knapsack max value:", knapsack(weights, values, W))

    # 02. LCS
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    print("02. LCS length:", lcs_length(s1, s2))

    # 03. Разбиение числа
    n = 5
    print("03. Partitions of", n, ":", count_partitions(n))

    # 04. Флойд-Уоршелл
    INF = float("inf")
    dist = [[0, 3, INF, 7], [8, 0, 2, INF], [5, INF, 0, 1], [2, INF, INF, 0]]
    result = floyd_warshall(dist)
    print("04. Floyd-Warshall result:")
    for row in result:
        print(row)
