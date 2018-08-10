import unittest
import census


class TestRunner(unittest.TestCase):
    def setUp(self):
        pass

    def testGetCityInformationStatusCodeGood(self):
        city_information = census.get_city_information("brownsville", "texas")
        self.assertNotEqual(city_information, None)

    def testGetCityInformationStatusCodeBad(self):
        city_information = census.get_city_information("noWhere", "texas")
        self.assertEqual(city_information, None)


if __name__ == "__main__":
    unittest.main()
