# 1 добавление комментария
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
read_more_ruby = driver.find_element_by_css_selector(".col3-1.first.sub_column>.module>.woocommerce>.products>li>a:nth-child(2)")
read_more_ruby.click()
reviews_btn = driver.find_element_by_css_selector(".reviews_tab>a")
reviews_btn.click()
five_star_btn = driver.find_element_by_class_name("star-5")
five_star_btn.click()
review_field = driver.find_element_by_id("comment")
review_field.send_keys("Nice book!")
name_field = driver.find_element_by_id("author")
name_field.send_keys("Egor")
email_field = driver.find_element_by_id("email")
email_field.send_keys("betester@test.ru")
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
driver.quit()