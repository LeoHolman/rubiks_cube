import unittest
import rubiks_cube


class StrTest(unittest.TestCase):
    """
    Test string represenations
    """

    def test_str_ouput(self):
        """
        Test that an unmodified cube outputs the correct str representation
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

    def test_face_str(self):
        """
        Test that it correctly outputs a single face as a string
        """
        rubix = rubiks_cube.RubiksCube()
        orange_face = rubix.get_face_str('Orange')
        target_str = """ _ _ _ 
|O|O|O|
|O|O|O|
|O|O|O|
 ¯ ¯ ¯ """  # noqa W291
        self.assertEqual(orange_face, target_str)


if __name__ == '__main__':
    unittest.main()
