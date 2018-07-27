import unicodecsv as csv

COMMENT_CHAR = '#'

DEFAULT_DELIMITER = ';'
DEFAULT_LINETERMINATOR = '\n'


def strip_comments_and_empty_lines(lines):
    for line in lines:
        if not line.startswith(COMMENT_CHAR) and line.strip():
            yield line.strip()


def _read_csv(file_path, delimiter=DEFAULT_DELIMITER):
    return csv.reader(
        read_lines(file_path),
        delimiter=delimiter,
        encoding='utf-8'
    )


def _write_csv(
        file_path,
        data,
        delimiter=DEFAULT_DELIMITER,
        lineterminator=DEFAULT_LINETERMINATOR):
    with open(file_path, 'ab') as f:
        writer = csv.writer(
            f,
            delimiter=delimiter,
            lineterminator=lineterminator,
            encoding='utf-8'
        )
        writer.writerows(data)


def read_lines(file_path):
    with open(file_path, 'r') as f:
        for line in strip_comments_and_empty_lines(f):
            yield line.encode('utf-8')


read_map = _read_csv

write_map = _write_csv


def read_list(file_path):
    return [item[0] for item in _read_csv(file_path)]


def write_list(file_path, data):
    _write_csv(
        file_path,
        [[item] for item in data]
    )
