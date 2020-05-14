class RubiksCube():
    """
    A representation of a Rubix Cube
    This cube is red-centric, the absolute representation is as follows:
             _ _ _ 
            |G|G|G|
            |G|G|G|
            |G|G|G|
             ¯ ¯ ¯ 
     _ _ _   _ _ _   _ _ _   _ _ _ 
    |Y|Y|Y| |R|R|R| |W|W|W| |O|O|O|
    |Y|Y|Y| |R|R|R| |W|W|W| |O|O|O|
    |Y|Y|Y| |R|R|R| |W|W|W| |O|O|O|
     ¯ ¯ ¯   ¯ ¯ ¯   ¯ ¯ ¯   ¯ ¯ ¯ 
             _ _ _
            |B|B|B|
            |B|B|B|
            |B|B|B|
             ¯ ¯ ¯ 
    """  # noqa W291

    def __init__(self):
        self.Red = [['R', 'R', 'R'],
                    ['R', 'R', 'R'],
                    ['R', 'R', 'R']]

        self.Yellow = [['Y', 'Y', 'Y'],
                       ['Y', 'Y', 'Y'],
                       ['Y', 'Y', 'Y']]

        self.Green = [['G', 'G', 'G'],
                      ['G', 'G', 'G'],
                      ['G', 'G', 'G']]

        self.White = [['W', 'W', 'W'],
                      ['W', 'W', 'W'],
                      ['W', 'W', 'W']]

        self.Blue = [['B', 'B', 'B'],
                     ['B', 'B', 'B'],
                     ['B', 'B', 'B']]

        self.Orange = [['O', 'O', 'O'],
                       ['O', 'O', 'O'],
                       ['O', 'O', 'O']]

    def __str__(self):
        macron_line = ' ¯ ¯ ¯ '
        underscore_line = ' _ _ _ '
        block_indent = ' ' * 8

        def make_row_str(row):
            return '|' + '|'.join(row) + '|'

        def make_indended_block_str(block, indent_level):
            block_str = ''.join([
                block_indent * indent_level, underscore_line, '\n',
                block_indent * indent_level, make_row_str(block[0]), '\n',
                block_indent * indent_level, make_row_str(block[1]), '\n',
                block_indent * indent_level, make_row_str(block[2]), '\n',
                block_indent * indent_level, macron_line, '\n',
            ])
            return block_str

        middle_colors = ['Yellow', 'Red', 'White', 'Orange']
        middle_rows = [((underscore_line + ' ') * (len(middle_colors) - 1))
                       + underscore_line]
        for i in range(3):
            row_list = [make_row_str(self.__getattribute__(color)[i])
                        for color in middle_colors]
            middle_rows.append(' '.join(row_list))
        middle_rows.append(((macron_line + ' ') * (len(middle_colors) - 1))
                           + macron_line)

        top = make_indended_block_str(self.Green, 1)
        middle = '\n'.join(middle_rows)
        bottom = make_indended_block_str(self.Blue, 1)

        return ''.join([top, middle, '\n', bottom])
