from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum

with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]
    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]
    for content in ["", "0 3\n", "1 2\n1\n", "1 2\n1 x\n", "1 1\n0\n1\n", "1 1\n0\n\n"]:
        path.write_text(content, encoding="utf-8")
        try:
            read_matrix(path)
        except ValueError as error:
            if content in ("1 2\n1\n", "1 2\n1 x\n"):
                assert "2" in str(error)
        else:
            assert False, "Ошибка не обнаружена"
    try:
        read_matrix(Path(directory) / "missing.txt")
    except FileNotFoundError:
        pass
    else:
        assert False, "Отсутствующий файл не обнаружен"
assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 8
assert selected_sum([[-1, 0]]) == 0
print("Проверки пройдены")
