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

    MACRON_LINE = ' ¯ ¯ ¯ '
    UNDERSCORE_LINE = ' _ _ _ '
    BLOCK_INDENT = ' ' * 8

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

    def _make_row_str(self, row):
        return '|' + '|'.join(row) + '|'

    def __str__(self):
        def make_indended_block_str(block, indent):
            block_str = ''.join([
                self.BLOCK_INDENT * indent, self.UNDERSCORE_LINE, '\n',
                self.BLOCK_INDENT * indent, self._make_row_str(block[0]), '\n',
                self.BLOCK_INDENT * indent, self._make_row_str(block[1]), '\n',
                self.BLOCK_INDENT * indent, self._make_row_str(block[2]), '\n',
                self.BLOCK_INDENT * indent, self.MACRON_LINE, '\n',
            ])
            return block_str

        middle_colors = ['Yellow', 'Red', 'White', 'Orange']
        middle_rows = [((self.UNDERSCORE_LINE + ' ') * (len(middle_colors)-1))
                       + self.UNDERSCORE_LINE]
        for i in range(3):
            row_list = [self._make_row_str(self.__getattribute__(color)[i])
                        for color in middle_colors]
            middle_rows.append(' '.join(row_list))
        middle_rows.append(((self.MACRON_LINE + ' ') * (len(middle_colors)-1))
                           + self.MACRON_LINE)

        top = make_indended_block_str(self.Green, 1)
        middle = '\n'.join(middle_rows)
        bottom = make_indended_block_str(self.Blue, 1)

        return ''.join([top, middle, '\n', bottom])

    def get_face_str(self, face_name):
        face = self.__getattribute__(face_name)
        middle_rows = [self._make_row_str(row) for row in face]
        face = self.UNDERSCORE_LINE + '\n' + \
            '\n'.join(middle_rows) + '\n' + \
            self.MACRON_LINE
        return face
