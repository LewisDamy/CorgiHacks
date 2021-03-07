from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.akc.org/dog-breeds/american-staffordshire-terrier/")

print(driver.title)

search = driver.find_element_by_class_name("breed-hero__footer")
Height = driver.find_element_by_xpath("/html/body/div[5]/section[1]/div/div/div[1]/div/div[1]/div/div/div[1]/ul/li[3]/span[2]")
print(f"Height: {Height.text}")


Weight = driver.find_element_by_xpath("/html/body/div[5]/section[1]/div/div/div[1]/div/div[1]/div/div/div[1]/ul/li[4]/span[2]")
print(f"Weight: {Weight.text}")


#TODO Take the Photo from the dog

#screenshot = driver.find_element_by_class_name("img.media-wrap__image lozad")
#print(screenshot)
#with open("american-staffordshire-terrier.png", "wb") as file:
 #   file.write(driver.find_element_by_xpath("/html/body/div[5]/section[1]/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/img".screenshot_as_png))

#TODO Life Expatation not working

#LifeExpect = driver.find_element_by_xpath("/html/body/div[5]/section[1]/div/div/div[1]/div/div[1]/div/div/div[1]/ul/li[5]/span[1]")
#printf(f"Life Expectation: {LifeExpect}")


driver.quit()


dogs = {
    "american-staffordshire-terrier" : 1,
    "chihuahua" : 2,
    "australian-terrier" : 3,
    "barbet" : 4,
    "belgian-sheepdog" : 5,
    "basset-hound" : 6,
    "beagle" : 7,
    "bearded-collie" : 8,
    "beauceron" : 9,
    "bernese-mountain-dog" : 10,
    "boerboel" : 11,
    "border-collie" : 12,
    "boston-terrier" : 13,
    "boxer" : 13,
    "bulldog" : 14,
    "collie" : 15,
    "danish-swedish-farmdog" : 16,
    "doberman-pinscher" : 17,
    "english-cocker-spaniel" : 18,
    "english-foxhound" : 19,
    "german-shepherd-dog" : 20
}