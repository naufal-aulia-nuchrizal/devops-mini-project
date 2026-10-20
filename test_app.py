import unittest
from unittest.mock import MagicMock
from app import get_hit_count

class TestDevOpsApp(unittest.TestCase):
    def test_get_hit_count_sukses(self):
        mock_redis = MagicMock()
        mock_redis.incr.return_value = 5
        
        hasil = get_hit_count(mock_redis)
        self.assertEqual(hasil, 5)
        
if __name__ == '__main__':
    unittest.main()