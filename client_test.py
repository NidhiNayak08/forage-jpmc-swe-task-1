import unittest
from client3 import getRatio
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_when_price_b_is_nonzero(self):
    # Test when price_b is nonzero
    result = getRatio(10, 2)
    self.assertEqual(result, 5.0)  # Ensure that the ratio is calculated correctly


  def test_getRatio_when_price_b_is_zero(self):
    # Test when price_b is zero (edge case)
    result = getRatio(10, 0)
    self.assertIsNone(result)  # Ensure that the function returns None when price_b is zero

  def test_getRatio_when_both_prices_are_zero(self):
    # Test when both price_a and price_b are zero (edge case)
    result = getRatio(0, 0)
    self.assertIsNone(result)  # Ensure that the function returns None when both prices are zero

  def test_getRatio_when_price_a_is_zero(self):
    # Test when price_a is zero
    result = getRatio(0, 5)
    self.assertEqual(result, 0.0)  # Ensure that the ratio is calculated correctly

  def test_getRatio_when_price_a_and_price_b_are_negative(self):
    # Test when both price_a and price_b are negative
    result = getRatio(-5, -2)
    self.assertEqual(result, 2.5)  # Ensure that the ratio is calculated correctly


if __name__ == '__main__':
    unittest.main()
