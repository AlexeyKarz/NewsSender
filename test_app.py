import unittest
from news import NewsFeed


class TestNewsFeed(unittest.TestCase):
    def test_get(self):
        """Test that news fetching returns a non-empty string."""
        news_feed = NewsFeed(interest='nasa', from_date='2024-02-03', to_date='2024-02-04', language='en')
        result = news_feed.get()
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()