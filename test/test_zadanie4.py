import unittest
from zadanie4 import XmasSong


class XmasSongTest(unittest.TestCase):
    song = [
        'On the first day of Christmas my true love gave to me: a Partridge '
        'in a Pear Tree.',
        'On the second day of Christmas my true love gave to me: two Turtle '
        'Doves, and a Partridge in a Pear Tree.',
        'On the third day of Christmas my true love gave to me: three French '
        'Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        'On the fourth day of Christmas my true love gave to me: four Calling '
        'Birds, three French Hens, two Turtle Doves, and a Partridge in a '
        'Pear Tree.',
        'On the fifth day of Christmas my true love gave to me: five Gold '
        'Rings, four Calling Birds, three French Hens, two Turtle Doves, '
        'and a Partridge in a Pear Tree.',
        'On the sixth day of Christmas my true love gave to me: '
        'six Geese-a-Laying, five Gold Rings, four Calling Birds, '
        'three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        'On the seventh day of Christmas my true love gave to me: '
        'seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, '
        'four Calling Birds, three French Hens, two Turtle Doves, '
        'and a Partridge in a Pear Tree.',
        'On the eighth day of Christmas my true love gave to me: '
        'eight Maids-a-Milking, seven Swans-a-Swimming, six '
        'Geese-a-Laying, five Gold Rings, four Calling Birds, '
        'three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        'On the ninth day of Christmas my true love gave to me: '
        'nine Ladies Dancing, eight Maids-a-Milking, '
        'seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, '
        'four Calling Birds, three French Hens, two Turtle Doves, '
        'and a Partridge in a Pear Tree.',
        'On the tenth day of Christmas my true love gave to me: '
        'ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, '
        'seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, '
        'four Calling Birds, three French Hens, two Turtle Doves, and a'
        ' Partridge in a Pear Tree.',
        'On the eleventh day of Christmas my true love gave to me: '
        'eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, '
        'eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, '
        'five Gold Rings, four Calling Birds, three French Hens, '
        'two Turtle Doves, and a Partridge in a Pear Tree.',
        'On the twelfth day of Christmas my true love gave to me: '
        'twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, '
        'nine Ladies Dancing, eight Maids-a-Milking, '
        'seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, '
        'four Calling Birds, three French Hens, two Turtle Doves, and a '
        'Partridge in a Pear Tree.'
    ]

    def test_get_all(self):
        self.assertEqual(self.xmas_song.get_all(), '\n\n'.join(self.song))

    def test_line_1(self):
        self.assertEqual(self.xmas_song.get_line(1), self.song[0])

    def test_line_2(self):
        self.assertEqual(self.xmas_song.get_line(2), self.song[1])

    def test_line_3(self):
        self.assertEqual(self.xmas_song.get_line(3), self.song[2])

    def test_line_4(self):
        self.assertEqual(self.xmas_song.get_line(4), self.song[3])

    def test_line_5(self):
        self.assertEqual(self.xmas_song.get_line(5), self.song[4])

    def test_line_6(self):
        self.assertEqual(self.xmas_song.get_line(6), self.song[5])

    def test_line_7(self):
        self.assertEqual(self.xmas_song.get_line(7), self.song[6])

    def test_line_8(self):
        self.assertEqual(self.xmas_song.get_line(8), self.song[7])

    def test_line_9(self):
        self.assertEqual(self.xmas_song.get_line(9), self.song[8])

    def test_line_10(self):
        self.assertEqual(self.xmas_song.get_line(10), self.song[9])

    def test_line_11(self):
        self.assertEqual(self.xmas_song.get_line(11), self.song[10])

    def test_line_12(self):
        self.assertEqual(self.xmas_song.get_line(12), self.song[11])

    def test_line_1_3(self):
        self.assertEqual(self.xmas_song.get_range(1, 3),
                         '\n\n'.join(self.song[0:3]))

    def test_line_8_10(self):
        self.assertEqual(self.xmas_song.get_range(8, 10),
                         '\n\n'.join(self.song[7:10]))

    def test_line_7_8(self):
        self.assertEqual(self.xmas_song.get_range(7, 8),
                         '\n\n'.join(self.song[6:8]))

    def test_line_3_4(self):
        self.assertEqual(self.xmas_song.get_range(3, 4),
                         '\n\n'.join(self.song[2:4]))

    def test_line_7_11(self):
        self.assertEqual(self.xmas_song.get_range(7, 11),
                         '\n\n'.join(self.song[6:11]))

    def test_line_7_9(self):
        self.assertEqual(self.xmas_song.get_range(7, 9),
                         '\n\n'.join(self.song[6:9]))

    def test_line_1_9(self):
        self.assertEqual(self.xmas_song.get_range(1, 9),
                         '\n\n'.join(self.song[0:9]))

    def test_line_9_11(self):
        self.assertEqual(self.xmas_song.get_range(9, 11),
                         '\n\n'.join(self.song[8:11]))

    def test_line_5_7(self):
        self.assertEqual(self.xmas_song.get_range(5, 7),
                         '\n\n'.join(self.song[4:7]))

    def test_line_2_4(self):
        self.assertEqual(self.xmas_song.get_range(2, 4),
                         '\n\n'.join(self.song[1:4]))

    def test_line_6_11(self):
        self.assertEqual(self.xmas_song.get_range(6, 11),
                         '\n\n'.join(self.song[5:11]))

    def test_not_int(self):
        with self.assertRaises(ValueError):
            self.xmas_song.get_line("D")

    def test_int_out_of_range_15(self):
        with self.assertRaises(ValueError):
            self.xmas_song.get_line(15)

    def test_int_out_of_range_0(self):
        with self.assertRaises(ValueError):
            print(self.xmas_song.get_line(0))

    def test_range_not_int_1_arg(self):
        with self.assertRaises(TypeError):
            self.xmas_song.get_range("", 9)

    def test_range_not_int_2_arg(self):
        with self.assertRaises(TypeError):
            self.xmas_song.get_range(1, "")

    def test_range_1_arg_gt_2_arg(self):
        with self.assertRaises(ValueError):
            self.xmas_song.get_range(8, 4)

    def test_range_1_arg_lt_1(self):
        with self.assertRaises(ValueError):
            self.xmas_song.get_range(-1, 4)

    def test_range_2_arg_gt_12(self):
        with self.assertRaises(ValueError):
            self.xmas_song.get_range(1, 44)

    def test_range_all_out_of_range(self):
        with self.assertRaises(ValueError):
            self.xmas_song.get_range(20, 44)

    def setUp(self):
        self.xmas_song = XmasSong()

    def setDown(self):
        self.xmas_song = null
