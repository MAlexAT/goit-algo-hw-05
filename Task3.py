import timeit

# Реалізація алгоритму Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return 0, 0
    
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    skip = [skip.get(c, m) for c in text]
    
    i = m - 1
    count = 0
    while i < n:
        count += 1
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i, count
            i -= 1
            j -= 1
        i += skip[i] if skip[i] > m - j else m - j
    return -1, count

# Реалізація алгоритму Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    lps = [0] * m
    j = 0
    i = 1
    count = 0

    while i < m:
        count += 1
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    i = j = 0
    while i < n:
        count += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j, count
        elif i < n and pattern[j] != text[i]:
            j = lps[j - 1] if j != 0 else 0
    return -1, count

# Реалізація алгоритму Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    count = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        count += 1
        if p == t:
            if text[i:i + m] == pattern:
                return i, count
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1, count

# Функція для вимірювання часу виконання кожного алгоритму
def time_algorithm(algorithm, text, pattern):
    start_time = timeit.default_timer()
    position, iterations = algorithm(text, pattern)
    end_time = timeit.default_timer()
    time_taken = end_time - start_time
    return position, iterations, time_taken

with open('стаття 1.txt', 'r', encoding='utf-8', errors='ignore') as file:
    text1 = file.read()

with open('стаття 2.txt', 'r', encoding='utf-8', errors='ignore') as file:
    text2 = file.read()

# Вибір підрядків для пошуку
pattern_existing = "алгоритм"
pattern_nonexistent = "випадковий рядок"

# Виконання пошуку та порівняння алгоритмів на обох текстах
results = {}
for text, label in zip([text1, text2], ["стаття 1", "стаття 2"]):
    results[label] = {}
    for algorithm, name in zip([boyer_moore, kmp_search, rabin_karp],
                               ["Boyer-Moore", "Knuth-Morris-Pratt", "Rabin-Karp"]):
        # Тест із наявним підрядком
        pos, iter_count, time_taken = time_algorithm(algorithm, text, pattern_existing)
        results[label][f"{name} (existing)"] = (pos, iter_count, time_taken)
        
        # Тест із неіснуючим підрядком
        pos, iter_count, time_taken = time_algorithm(algorithm, text, pattern_nonexistent)
        results[label][f"{name} (non-existent)"] = (pos, iter_count, time_taken)

# Виведення результатів на екран
print("# Результати порівняння алгоритмів пошуку підрядка\n")
for label, timings in results.items():
    print(f"## Результати для {label}")
    for test_case, (pos, iter_count, time_taken) in timings.items():
        print(f"- **{test_case}**: Позиція: {pos}, Ітерації: {iter_count}, Час: {time_taken:.6f} секунд")
    print()
print("## Висновки\n")
print("На основі результатів зроблено наступні спостереження:")
print("- У кожному випадку швидкість кожного алгоритму залежить від типу пошуку.")
