from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://exemplo.com/login")

# Preenche campos
driver.find_element("id", "email").send_keys("teste@email.com")
driver.find_element("id", "senha").send_keys("123456")
driver.find_element("id", "btn-login").click()

# Verifica se login foi bem-sucedido
assert "Bem-vindo" in driver.page_source
driver.quit()
