import unittest
from unittest.mock import MagicMock
from strategy import Compressor, Strategy, BitmapStrategy, RunLengthStrategy


class Compressortest(unittest.TestCase):

    def test_compress(self):
        bitmap_compressor = BitmapStrategy()
        runlength_compressor = RunLengthStrategy()
        bitmap_compressor.algorithm_interface = MagicMock(return_value=True)
        runlength_compressor.algorithm_interface = MagicMock(return_value=True)

        compressor = Compressor(runlength_compressor, bitmap_compressor)
        compressor.compress('Ce ttttttexttttt eeeeeeeeeeeeeeest rrrrrrrrrrrrrrrrrrepppppppppetttttttttttti')

        bitmap_compressor.algorithm_interface.assert_called_with('Ce ttttttexttttt eeeeeeeeeeeeeeest rrrrrrrrrrrrrrrrrrepppppppppetttttttttttti')



if __name__ == "__main__":
    unittest.main()