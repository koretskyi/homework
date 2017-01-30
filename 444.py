from selenium import webdriver

wiki = webdriver.Chrome()

wiki.get('https://ru.wikipedia.org')

wiki.maximize_window()

search_form = wiki.find_element_by_xpath('//*[@id = "searchInput"]').send_keys('список римских пап')

search_button = wiki.find_element_by_xpath('//*[@id = "searchButton"]').click()

anaklet_pic = wiki.find_element_by_xpath('//*[@id="mw-content-text"]/table[2]//tr[3]//a/img').click()