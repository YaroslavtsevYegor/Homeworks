

def test_example_google_title(browser):
    browser.get('https://www.google.com/')
    assert 'Google' in browser.title


def test_example_yt_title(browser):
    browser.get('https://www.youtube.com/')
    assert 'YouTube' in browser.title
