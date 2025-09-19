class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26 # Columns A to Z
        self.grid = [[0] * self.cols for _ in range(rows)]

    def _parse_cell(self,cell: str):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return row, col    
    
    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parse_cell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._parse_cell(cell)
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        def get_operand_value(operand):
            if operand[0].isalpha():
                row, col = self._parse_cell(operand)
                return self.grid[row][col]
            else:
                return int(operand)

        if formula.startswith('='):
            formula = formula[1:]

        x, y = formula.split('+')
        return get_operand_value(x) + get_operand_value(y)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)