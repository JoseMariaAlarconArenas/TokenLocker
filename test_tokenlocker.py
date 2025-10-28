# test_tokenlocker.py
"""
Tests for TokenLocker module.
"""

import unittest
from tokenlocker import TokenLocker

class TestTokenLocker(unittest.TestCase):
    """Test cases for TokenLocker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenLocker()
        self.assertIsInstance(instance, TokenLocker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenLocker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
