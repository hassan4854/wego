from selenium import webdriver
from time import sleep
url = 'https://bahman.iranecar.com/'
driver = webdriver.Chrome()

driver.get(url)
driver.fullscreen_window()
driver.find_element('xpath', "//ul[@class='sale-type-items sale-type-items-1']//li").click()

sleep(1) # essential
driver.find_element('tag name', "i").click()

driver.find_element('xpath', "//li[@index='1']//i[1]").click()

# driver.find_element('class name', "recaptcha-checkbox-border").click()
# sleep(2)
# sleep(2)
driver.execute_script("window.scrollTo(0, 2800)")
driver.find_element('id', "agreement").click()
sleep(8)
driver.find_element('class name', "go-next").click()

driver.execute_script("window.scrollTo(0, 2800)")

#name
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[1]/input").send_keys('علی')


#family
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[2]/input").send_keys('حسینی')


#father_name
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[3]/input").send_keys('رضا')
# sleep(2)


driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[4]/input").send_keys('6000028490')
# sleep(2)

driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[5]/input").send_keys('1234')
# sleep(2)

#man
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[6]/select/option[3]").click()
# sleep(2)

#woman
# driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[6]/select/option[2]").click()
# sleep(2)

#serial shenasname
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[7]/input").send_keys('123456')
# sleep(2)

# birthday
driver.find_element('xpath', "/html/body/div[1]/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[8]/span/span/input").send_keys('1365/03/02')
# sleep(2)

# date sodoor shenasname
driver.find_element('xpath', "/html/body/div[1]/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[9]/span/span/input").send_keys('1366/05/03')
# sleep(2)

#ostan mehal sodoor shenasname
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[10]/select/option[9]").click()
# sleep(2)
sleep(1)
#shahr mehal sodoor shenasname
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[11]/select/option[14]").click()
# sleep(2)

# ostan tavalod
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[12]/select/option[9]").click()
# sleep(2)
sleep(1)
#shahr tavalod
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[13]/select/option[14]").click()
# sleep(2)

#shoghl
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[14]/select/option[2]").click()
# sleep(2)

#nahve ashnaee
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[15]/select/option[8]").click()
# sleep(2)

# type pelak
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[2]/div[16]/select/option[3]").click()
# sleep(2)

# address ostan
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[4]/div[1]/select/option[9]").click()
# sleep(2)

sleep(1)
# address shahr
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[4]/div[2]/select/option[14]").click()
# sleep(2)

# major ave
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[4]/div[3]/input").send_keys('خیابان ازادی')
# sleep(2)

# minor ave
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[4]/div[4]/input").send_keys('مرتضوی')
# sleep(2)

# alley
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[4]/div[5]/input").send_keys('موسوی')
# sleep(2)

#pelak
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[4]/div[6]/input").send_keys('6')
# sleep(2)

# mantaghe shahrdari
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[4]/div[7]/input").send_keys('2')
# sleep(2)

# code posti
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[4]/div[8]/input").send_keys('1234567891')

#bank
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[5]/div[1]/input").send_keys('ملت')
# sleep(2)

#shaba
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[5]/div[2]/input").send_keys('123123123132')
# sleep(2)

#taeed
driver.find_element('xpath', "//*[@id='has_certficate_number']").click()
# sleep(2)

#shomare govahi
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[6]/div[2]/input").send_keys('123123123132')
# sleep(2)

#mobile
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[7]/div[1]/input").send_keys('09121234322')
# sleep(2)

#telephone
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[7]/div[2]/input").send_keys('02199083787')
# sleep(2)

#email
driver.find_element('xpath', "//*[@id='app']/div/div[2]/div[5]/div/div/div/div/div/div/div[1]/div[7]/div[3]/input").send_keys('admin@admin.com')
# sleep(2)
driver.execute_script("window.scrollTo(0, 4000)")
sleep(1)
driver.close()

