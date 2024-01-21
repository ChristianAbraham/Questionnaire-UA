from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given("I am on SignIn Page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://qa.unair.ac.id/")

@when("i fill in username field with username")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="userid"]').send_keys("ganti dengan nim anda")

@when("i fill in password field with password")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("ganti dengan password anda")

@when("i press SignIn button")
def step_impl(context):
    context.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[4]/button').click()

@Then("i should be on home")
def step_impl(context):
    assert "SIM Kuesioner" in context.browser.page_source

@when("i press SIM Kuesioner")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="navigation"]/li').click()

@when("i press Mahasiswa S1")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="kuesioner"]/div/div').click()

@then("i should be on https://qa.unair.ac.id/qa/kuesioner/dashboard")
def step_impl(context):
    assert "https://qa.unair.ac.id/qa/kuesioner/dashboard" in context.browser.current_url

@when("i press Kinerja Tim Dosen")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//html/body/div/div[2]/div[2]/div/div/a[1]/div/div').click()

@when("i press mata kuliah")
def step_impl(context):
    context.browser.find_element(By.XPATH, ' //*[@id="idmk"]').click()

@when("i press DI PRAK")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="idmk"]/option[2]').click()

@when("i fill form with 10")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="jawaban_715_39_134"]').click()
    context.browser.find_element(By.XPATH, '//*[@id="jawaban_716_39_134"]').click()
    context.browser.find_element(By.XPATH, '//*[@id="jawaban_717_39_134"]').click()
    context.browser.find_element(By.XPATH, '//*[@id="jawaban_718_39_134"]').click()
    context.browser.find_element(By.XPATH, '//*[@id="jawaban_719_39_134"]').click()
    context.browser.find_element(By.XPATH, '//*[@id="jawaban_720_39_134"]').click()

@when("i press dosen")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="dosen"]').click()

@when("i chose dosen")
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="dosen"]/option[2]').click()

@when("i press button simpan")
def step_impl(context):
    context.browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/form/div[17]/button').click()

@when("i press OK")
def step_impl(context):
    alert = context.browser.switch_to.alert
    alert.accept()

@then("i should see Pengisian Kuesioner Berhasil")
def step_impl(context):
    assert "Pengisian Kuesioner Berhasil" in context.browser.page_source