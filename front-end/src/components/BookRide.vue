<template>
  <!-- Create a form asking for pickup location, dropoff location, pickup time and a checkbox for round trip-->
   <form @submit.prevent="bookRide">
        <div class="book-ride">
            <form>
                <!-- Pickup Location -->
               <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
                   <div class="form-group" style="width: 100%">
                        <label for="pickupLocation" class="form-label">Pickup Location</label>
                        <!-- <input type="text" class="form-control" id="pickupLocation" v-model="pickupLocation" placeholder="Enter pickup location"> -->
                        <input v-if="homePickup" type="text" class="form-control" id="pickupLocation" v-model="pickupLocation" placeholder="Enter pickup location" disabled>
                        <input v-else type="text" class="form-control" id="pickupLocation" v-model="pickupLocation" placeholder="Enter pickup location">
                    </div>
                    <div class="form-group">
                        <label for="homePickup" class="form-label">Home</label>
                        <input v-if="homeDropoff" type="checkbox" id="homePickup" v-model="homePickup" disabled>
                        <input v-else type="checkbox" id="homePickup" v-model="homePickup">
                    </div>
                </div> 
                <!-- Dropoff Location -->
                <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
                    <div class="form-group" style="width: 100%">
                        <label for="dropoffLocation" class="form-label">Dropoff Location</label>
                        <input v-if="homeDropoff" type="text" class="form-control" id="dropoffLocation" v-model="dropoffLocation" placeholder="Enter dropoff location" disabled>
                        <input v-else type="text" class="form-control" id="dropoffLocation" v-model="dropoffLocation" placeholder="Enter dropoff location">
                    </div>
                    <!-- checkbox for home -->
                    <div class="form-group">
                        <label for="homeDropoff" class="form-label">Home</label>
                        <input v-if="homePickup" type="checkbox" id="homeDropoff" v-model="homeDropoff" disabled>
                        <input v-else type="checkbox" id="homeDropoff" v-model="homeDropoff">
                    </div>
                </div>
                <!-- Pickup time -->
                <div class="form-group">
                    <label for="pickupTime" class="form-label">Pickup Time</label>
                    <input type="time" class="form-control" id="pickupTime" v-model="pickupTime" placeholder="Enter pickup time">
                </div>
                <!-- Round trip -->
                <div class="form-group round-trip-gp">
                    <label for="roundTrip" class="form-label">Round Trip
                        <span class="tooltiptext">By checking "Round Trip", you book a return trip that will take you from the dropoff location back to the pickup location at the selected time. </span>
                    </label>
                    <input type="checkbox" id="roundTrip" v-model="roundTrip">
                </div>
                <br>
                <!-- Round trip pickup time -->
                <div v-if="roundTrip" class="form-group">
                    <label style="display: flex; justify-content: center;" for="pickupTimeReturnTrip" class="form-label">Return Trip Pickup Time</label>
                    <input type="time" class="form-control" id="pickupTimeReturnTrip" v-model="pickupTimeReturnTrip" placeholder="Enter pickup time">
                </div>
                <br>
            </form>
        </div>
        <!-- Second Trip -->
        <p style="font-size: 30px; margin-top: 45px; font-weight: bold;">Book a Second Trip</p>
        <div class="book-ride">
            <form>
                <!-- Pickup Location -->
                <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
                   <div class="form-group" style="width: 100%">
                        <label for="pickupLocation2" class="form-label">Pickup Location</label>
                        <!-- <input type="text" class="form-control" id="pickupLocation" v-model="pickupLocation" placeholder="Enter pickup location"> -->
                        <input v-if="homePickup2" type="text" class="form-control" id="pickupLocation2" v-model="pickupLocation2" placeholder="Enter pickup location" disabled>
                        <input v-else type="text" class="form-control" id="pickupLocation2" v-model="pickupLocation2" placeholder="Enter pickup location">
                    </div>
                    <div class="form-group">
                        <label for="homePickup2" class="form-label">Home</label>
                        <input v-if="homeDropoff2" type="checkbox" id="homePickup2" v-model="homePickup2" disabled>
                        <input v-else type="checkbox" id="homePickup2" v-model="homePickup2">
                    </div>
                </div> 
                <!-- Dropoff Location -->
                <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
                    <div class="form-group" style="width: 100%">
                        <label for="dropoffLocation2" class="form-label">Dropoff Location</label>
                        <input v-if="homeDropoff2" type="text" class="form-control" id="dropoffLocation2" v-model="dropoffLocation2" placeholder="Enter dropoff location" disabled>
                        <input v-else type="text" class="form-control" id="dropoffLocation2" v-model="dropoffLocation2" placeholder="Enter dropoff location">
                    </div>
                    <!-- checkbox for home -->
                    <div class="form-group">
                        <label for="homeDropoff2" class="form-label">Home</label>
                        <input v-if="homePickup2" type="checkbox" id="homeDropoff2" v-model="homeDropoff2" disabled>
                        <input v-else type="checkbox" id="homeDropoff2" v-model="homeDropoff2">
                    </div>
                </div>
            <!-- <div class="form-group">
                <label for="pickupLocation2" class="form-label">Pickup Location</label>
                <input type="text" class="form-control" id="pickupLocation2" v-model="pickupLocation2" placeholder="Enter pickup location">
            </div>
                <div class="form-group">
                    <label for="dropoffLocation" class="form-label">Dropoff Location</label>
                    <input type="text" class="form-control" id="dropoffLocation2" v-model="dropoffLocation2" placeholder="Enter dropoff location">
                </div> -->
            <div class="form-group">
                <label for="pickupTime" class="form-label">Pickup Time</label>
                <input type="time" class="form-control" id="pickupTime2" v-model="pickupTime2" placeholder="Enter pickup time">
            </div>
            <div class="form-group round-trip-gp">
                <label for="roundTrip2" class="form-label">Round Trip
                    <span class="tooltiptext">By checking "Round Trip", you book a return trip that will take you from the dropoff location back to the pickup location at the selected time. </span>
                </label>
                <input type="checkbox" id="roundTrip2" v-model="roundTrip2">
            </div>
            <br>
            <div v-if="roundTrip2" class="form-group">
                <label style="display: flex; justify-content: center;" for="pickupTimeReturnTrip" class="form-label">Return Trip Pickup Time</label>
                <input type="time" class="form-control" id="pickupTimeReturnTrip" v-model="pickupTimeReturnTrip" placeholder="Enter pickup time">
            </div>
            <br>
            </form>
        </div>
        <div>
            <button style="margin-top: 10px;" type="submit" class="btn btn-primary">Submit</button>
        </div>
    </form>
</template>

<script>
import axios from "axios";
export default {
    name: 'BookRide',
    data() {
        return {
            pickupLocation: '',
            dropoffLocation: '',
            pickupTime: '',
            roundTrip: false,
            roundTripPickUpTime: '',
            homePickup: false,
            homeDropoff: false,
            pickupLocation2: '',
            dropoffLocation2: '',
            pickupTime2: '',
            roundTrip2: false,
            roundTripPickUpTime2: '',
            homePickup2: false,
            homeDropoff2: false,
        }
    },
    methods: {
        bookRide() {
            axios.post('http://localhost:8000/api/bookings', {
                regNum: localStorage.getItem('regNum'),
                lastName: localStorage.getItem('lastName'),
                firstName: localStorage.getItem('firstName'),
                phoneNum: localStorage.getItem('phoneNum'),
                email: localStorage.getItem('email'),
                pickupLocation: this.pickupLocation,
                dropoffLocation: this.dropoffLocation,
                pickupTime: this.pickupTime,
                roundTrip: this.roundTrip,
                roundTripPickUpTime: this.roundTripPickUpTime,
                homePickup: this.homePickup,
                homeDropoff: this.homeDropoff,
                pickupLocation2: this.pickupLocation2,
                dropoffLocation2: this.dropoffLocation2,
                pickupTime2: this.pickupTime2,
                roundTrip2: this.roundTrip2,
                roundTripPickUpTime2: this.roundTripPickUpTime2,
                homePickup2: this.homePickup2,
                homeDropoff2: this.homeDropoff2,
            })
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error);
            })
        }
    }

}
</script>

<style>
.book-ride {
    border-radius: 20px;
    border: 3px solid #f1f1f1;
    width: 60vw;
    margin: auto;
    padding: 20px;
    font-size: 20px;
}
.form-group input[type="text"], input[type="time"]{
    height: 50px;
    margin-bottom: 20px;
    border-radius: 30px;
}
.form-group input[type="checkbox"]{
    margin-left: 10px;
}
.round-trip-gp{
    float: left;
}
.form-label{
    font-weight: bold;
}

.tooltiptext {
  visibility: hidden;
  width: 500px;
  background-color: black;
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;
  position: absolute;
  z-index: 1;
}

.form-label:hover .tooltiptext {
  visibility: visible;
}
</style>