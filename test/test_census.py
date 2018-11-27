import unittest
import mock
from src import census


class TestRunner(unittest.TestCase):
    @mock.patch('requests.get')
    def testGetCityInformationThatHasCityTitle(self, mock_get):
        request_content = '''
        <div class="qf-titlebar">
        <div class="qf-learn">
        <a href="/quickfacts/fact/faq/brownsvillecitytexas,US/PST045217">
        What's New &amp; FAQs</a></div>
        <h1>QuickFacts</h1>
        <h2>Brownsville city, Texas; UNITED STATES</h2>
        <p>QuickFacts provides statistics for all states and counties,
        and for cities and towns with a
        <em><strong>population of 5,000 or more</strong></em>.</p>
        </div>
        '''
        mock_resp = mock.Mock()
        mock_resp.content = request_content
        mock_get.return_value = mock_resp
        city_information = census.get_city_information("brownsville", "texas")
        self.assertEqual(city_information.content, request_content)

    @mock.patch('requests.get')
    def testGetCityInformationStatusHasNoCityTitle(self, mock_get):
        request_content = '''
        <div class="qf-titlebar">
        <div class="qf-learn">
        <a href="/quickfacts/fact/faq/US/PST045217">What's New &amp; FAQs
        </a>
        </div>
        <h1>QuickFacts</h1>
        <h2>UNITED STATES</h2>
        <p>QuickFacts provides statistics for all states and counties,
        and for cities and towns with a
        <em><strong>population of 5,000 or more</strong></em>.</p>
        </div>
        '''
        mock_resp = mock.Mock()
        mock_resp.content = request_content
        mock_get.return_value = mock_resp
        with self.assertRaises(Exception):
            census.get_city_information("noWhere", "texas")

    @mock.patch('requests.get')
    def testGetCityInformationStatusHasNoHeaderTwoTag(self, mock_get):
        request_content = '''
        <div class="qf-titlebar">
        <div class="qf-learn">
        <a href="/quickfacts/fact/faq/US/PST045217">What's New &amp; FAQs
        </a>
        </div>
        <h1>QuickFacts</h1>
        <p>QuickFacts provides statistics for all states and counties,
        and for cities and towns with a
        <em><strong>population of 5,000 or more</strong></em>.</p>
        </div>
        '''
        mock_resp = mock.Mock()
        mock_resp.content = request_content
        mock_get.return_value = mock_resp
        with self.assertRaises(Exception):
            census.get_city_information("brownsville", "texas")


if __name__ == "__main__":
    unittest.main()
