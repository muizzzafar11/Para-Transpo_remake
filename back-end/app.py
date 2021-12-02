from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Optional

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from fastapi import FastAPI
from selenium.webdriver.chrome.options import Options

class Booking(BaseModel):
    # Contact info
    regNum: str
    lastName: str
    firstName: str
    phoneNum: str
    email: str
    # Trip 1
    pickupLocation: str
    dropoffLocation: str
    pickupTime: str
    roundTrip: bool
    roundTripPickUpTime: str
    homePickup: bool
    homeDropoff: bool
    # Trip 2
    pickupLocation2: Optional[str] = None
    dropoffLocation2: Optional[str] = None
    pickupTime2: Optional[str] = None
    roundTrip2: Optional[bool] = None
    roundTripPickUpTime2: Optional[str] = None
    homePickup2: Optional[bool] = None
    homeDropoff2: Optional[bool] = None

origins = [
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/bookings/")
async def create_booking(booking: Booking):
    options = Options()
    options.headless = True
    web = webdriver.Chrome(options=options)
    web.get('https://www.octranspo.com/en/para-transpo/booking/reserve-a-trip')
    time.sleep(2)
    # Filling out the Contact Information Form
    web.switch_to.frame(web.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[1]/p[6]/iframe'))
    web.find_element(By.XPATH,'//*[@id="RegistrationNumber"]').send_keys(booking.regNum)
    web.find_element(By.XPATH,'//*[@id="FirstName"]').send_keys(booking.firstName)
    web.find_element(By.XPATH,'//*[@id="LastName"]').send_keys(booking.lastName)
    web.find_element(By.XPATH,'//*[@id="Email"]').send_keys(booking.email)
    web.find_element(By.XPATH,'//*[@id="Email"]').send_keys(webdriver.common.keys.Keys.TAB)
    web.find_element(By.XPATH,'//*[@id="Phone"]').send_keys(booking.phoneNum)
    web.find_element(By.XPATH, '//*[@id="ResAddTrip"]').click()
    # Filling out the Pickup and drop off information Information Form 1
    # Still need to time dropdown thing
    if(booking.homePickup):
        web.find_element(By.XPATH, '//*[@id="PickUpHome1"]').click()
    else:
        web.find_element(By.XPATH, '//*[@id="PickUpOtherAdd1"]').send_keys(booking.pickupLocation)
    if(booking.homeDropoff):
        web.find_element(By.XPATH, '//*[@id="DropOffHome1"]').click()
    else:
        web.find_element(By.XPATH, '//*[@id="DropOffOtherAdd1"]').send_keys(booking.dropoffLocation)
    # Filling out the Pickup and drop off information Information Form 2
    if(booking.homePickup2):
        web.find_element(By.XPATH, '//*[@id="PickUpHome2"]').click()
    else:
        web.find_element(By.XPATH, '//*[@id="PickUpOtherAdd2"]').send_keys(booking.pickupLocation2)
    if(booking.homeDropoff2):
        web.find_element(By.XPATH, '//*[@id="DropOffHome2"]').click()
    else:
        web.find_element(By.XPATH, '//*[@id="DropOffOtherAdd2"]').send_keys(booking.dropoffLocation2)
    # time.sleep(20)
    return (booking)
