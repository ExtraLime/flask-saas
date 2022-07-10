from flask import url_for
import re

class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_faq_page(self, client):
        """ faq page should respond with a success 200. """
        response = client.get(url_for('page.faq'))
        assert response.status_code == 200 
    
    def test_valid_title(self, client):
        response = client.get(url_for('page.faq'))
        title_pattern = re.search(r'<title>(.*?)</title>',str(response.data))
        assert '<title>' in str(response.data)
        assert title_pattern
