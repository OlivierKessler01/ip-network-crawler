import unittest
from unittest.mock import MagicMock, patch
from strategy import Compressor, Strategy, BitmapStrategy, RunLengthStrategy

class Compressortest(unittest.TestCase):

    @patch('strategy.BitmapStrategy')
    @patch('strategy.RunLengthStrategy')
    def test_compress(self, bitmap_compressor, runlength_compressor):
        compressor = Compressor(bitmap_compressor=bitmap_compressor, runlength_compressor=runlength_compressor)
        compressor.compress('tti')
        bitmap_compressor.algorithm_interface.assert_called_with('tti')
    
    @patch('strategy.BitmapStrategy')
    @patch('strategy.RunLengthStrategy')
    def test_compress_runlength(self, bitmap_compressor, runlength_compressor):
        compressor = Compressor(bitmap_compressor=bitmap_compressor, runlength_compressor=runlength_compressor)
        compressor.compress('tti', 1)
        runlength_compressor.algorithm_interface.assert_called_with('tti')
        

if __name__ == "__main__":
    unittest.main()
