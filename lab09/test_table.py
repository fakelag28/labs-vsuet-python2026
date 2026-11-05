from table import column_sums, diagonal_pattern, row_sums, transform

matrix = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]
assert row_sums([]) == column_sums([]) == transform([]) == []
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]
source = [[-2, 0, 3], [4, -5, 6]]
result = transform(source)
assert result == [[0, 0, 3], [4, 0, 6]]
result[0][0] = 10
assert source == [[-2, 0, 3], [4, -5, 6]]
print("Проверки пройдены")
