from tests import *

increase = driver.find_element_by_id("increase")


for i in range(100):
    increase.click()