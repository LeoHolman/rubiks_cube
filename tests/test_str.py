import unittest
import rubiks_cube


class StrTest(unittest.TestCase):
    """
    Test string represenations
    """

    def test_str_ouput(self):
        """
        Test that an unmodified cube outputs the correct representation with
        __str__
        """
        rubix_str = str(rubiks_cube.RubiksCube())
        target_str = """         _ _ _ 
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

        self.assertEqual(rubix_str, target_str)


if __name__ == '__main__':
    unittest.main()
