import numpy as np

x = np.array([1, 2, 3])
print(x)

print(x[0])

x[2] = 100
print(x)


# 要素ごとの算術演算
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)
print(x - y)
print(x * y)
print(x / y)


# スカラー演算（ブロードキャスト）
x = np.array([1, 2, 3, 4, 5], dtype= np.float)

print(x + 10)
print(x - 1)
print(x * 10)
print(x / 2)

# 割った結果の整数部分
print(x // 2)
# 剰余
print(x % 2)


x = np.array([1, 2, 3, 4, 5], dtype= np.float)

print(np.power(x, 2))
print(x ** 2)

print(np.sqrt(x))


# 最小、最大、平均、分散
x = np.array([35, 40, 45, 50, 55, 60], dtype= np.float)
print(np.max(x))
print(np.min(x))
print(np.mean(x))
print(np.var(x))
print(np.std(x))


vec1 = np.array([10, 20, 30])
vec2 = np.array([40, 50, 60])

print(vec1 + vec2)
print(vec1 - vec2)
print(vec1 / vec2)  # ブロードキャストによる要素ごとの演算

print(vec1 * vec2)  # アダマール積


# 内積
vec1 = np.array([2, 3])
vec2 = np.array([4, 5])

print(np.dot(vec1, vec2))


# 行列
mtx = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]],
                dtype= np.float
                )

# 行列のスカラー演算
print(mtx + 10)
print(mtx - 10)
print(mtx * 2)
print(mtx / 2)
print(mtx % 2)


# 行列のアクセス
print(mtx.dtype)  # データの型確認

# 1行目全て
print(mtx[0])
print(mtx[0, ])
print(mtx[0, :])

# 1列目すべて
print(mtx[:, 0])
print(mtx[1, 1])  # 2行2列目の要素
print(mtx[0:2, 0:2])  # 1行、2行、1列、2列の要素を抜き出し


# 行列の足し算、引き算
a = np.array([[1, 2],
            [3, 4]]
            )

b = np.array([[4, 3],
            [2, 1]]
            )

print(a + b)
print(a - b)


# 行列の積
print(np.dot(a, b))


# 行列の転置
mtx = np.array([[1, 2, 3],
                [4, 5, 6]],
                dtype= np.float
                )

print(np.transpose(mtx))
