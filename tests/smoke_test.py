import unittest


class SmokeTest(unittest.TestCase):
    def test_basic_functionality(self):
        """Test basic functionality works as expected."""
        from datamuse import Datamuse

        muse = Datamuse()
        synonyms = muse.synonyms("test")
        self.assertTrue(len(synonyms))

    def test_import_modules(self):
        """Test that all required modules can be imported."""
        try:
            import datamuse as datamuse
        except ImportError:
            raise

    def test_configuration(self):
        """Test that configuration is properly loaded."""
        from datamuse import Datamuse

        muse = Datamuse()
        self.assertEqual(muse._Datamuse__API_URL, "api.datamuse.com")  # pyright: ignore[reportAttributeAccessIssue]

    def test_error_handling(self):
        """Test error handling mechanisms."""
        from datamuse import Datamuse

        with self.assertRaises(TypeError):
            muse = Datamuse()
            muse.suggestions("why?")


if __name__ == "__main__":
    unittest.main()
