french = set(map(int, input().split()))
swimmers = set(map(int, input().split()))
pianists = set(map(int, input().split()))

swimmers_pianists = swimmers & pianists

# Исключаем тех, кто шарит за французский
result = swimmers_pianists - french

# Пример из задачи
# french = 1 2 5 7 8 9
# swimmers = 3 4 8 2 10
# pianists = 10 3 2 8 5

print(' '.join(map(str, sorted(result))))
