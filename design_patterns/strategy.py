from abc import ABC, abstractmethod

class Strategy(ABC):
    '''
        The Strategy design pattern is a behavioral pattern. Which means it mostly
        manages how a system behaves.
        It allows the selection of a particular algorythm at runtime.

        Let's say you have multiple compression algorythms, a bitmap on and a run-length one.
        At runtime, depending on the IO latency, the strategy patterns let's you choose which one is more appropriate.
    '''

    @abstractmethod
    def algorithm_interface(self, to_compress:str):
        pass


class BitmapStrategy(Strategy):
    def algorithm_interface(self, to_compress:str):
        return "0101010"

class RunLengthStrategy(Strategy):
    def algorithm_interface(self, to_compress:str):
        return "030303"


class Compressor:
    def __init__(self, bitmap_compressor: Strategy, runlength_compressor: Strategy):
        self.bitmapCompressor = bitmap_compressor
        self.runlength_compressor = runlength_compressor

    def compress(self, str_to_compress, flag=0):
        if(flag == 1):
            return self.runlength_compressor.algorithm_interface(str_to_compress)
        else:
            return self.bitmapCompressor.algorithm_interface(str_to_compress)



