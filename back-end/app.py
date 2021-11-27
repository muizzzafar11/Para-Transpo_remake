from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Optional

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from fastapi import FastAPI

class Booking(BaseModel):
    regNum: str
    lastName: str
    firstName: str
    phoneNum: str
    email: str
    pickupLocation: str
    dropoffLocation: str
    pickupTime: str
    roundTrip: bool
    pickupLocation2: Optional[str] = None
    dropoffLocation2: Optional[str] = None
    pickupTime2: Optional[str] = None
    roundTrip2: Optional[str] = None

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
    web = webdriver.Chrome()
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
    time.sleep(20)
    return (booking)
