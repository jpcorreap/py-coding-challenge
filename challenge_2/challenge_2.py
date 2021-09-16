
def transpose(input: str) -> str:
    """ Transposes an input string matrix """
    # If there is no matrix then returns empty string
    # This evaluation has a complexity of O(1)
    if len(input) == 0:
        return ''

    # This split has a complexity of O(N)
    rows = input.split('\n')

    # Save max row len to know how to fit
    # This has a complexity of O(N) too
    max_row_len = max(len(row) for row in rows)

    # Fix incomplete rows adding spaces until it completes the max_row_len
    # It has also a complexity of O(N)
    fixed_rows = [row + ' ' * (max_row_len - len(row)) for row in rows]

    transposed_rows = []

    # Iterates rows, with X = len(rows) and Y = max_row_len
    # I recognize this is not the best approach since this is O(N^2), but
    # I tried to do it with zip() with no success...
    # I think zip internally does a similar action in O(N^2)
    for j in range(max_row_len):
        transposed_row = ''
        spaces = ''
        for i in range(len(rows)):
            # This space validation avoids adding spaces to right, it takes
            # advantage of the current iteration to avoid another innecesarly
            # O(N^2) iteration
            if fixed_rows[i][j] != ' ':
                transposed_row += spaces + fixed_rows[i][j]
                spaces = ''
            else:
                spaces += ' '

        transposed_rows.append(transposed_row)

    return '\n'.join(transposed_rows)
