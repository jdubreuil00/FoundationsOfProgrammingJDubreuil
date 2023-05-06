import unittest
from CoinCollector import CoinCollector

class CoinCollectorTests(unittest.TestCase):

    def test_parseChange_singleCoin(self):
        coins = 'P'
        expecteddepositAmount = 0.01

        result = CoinCollector.parseChange(coins)

        self.assertEqual(result, expecteddepositAmount)

    def test_parseChange_multipleCoins(self):
        coins = 'NDQ'
        expecteddepositAmount = 0.40

        result = CoinCollector.parseChange(coins)

        self.assertEqual(result, expecteddepositAmount)

    def test_parseChange_invalidCoin(self):
        coins = 'PXDQ'
        expecteddepositAmount = 0.36

        result = CoinCollector.parseChange(coins)

        self.assertEqual(result, expecteddepositAmount)

if __name__ == '__main__':
    unittest.main()
