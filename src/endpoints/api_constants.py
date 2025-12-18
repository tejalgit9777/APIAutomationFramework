# API Constants - Class which contain all the endpoints
#  keep
# restfulbooker api, /booking, booking/id , /auth, /ping

class APIConstants:

    def base_url(self):
        return "https://restful-booker.herokuapp.com/"

    def get_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def get_booking_ID(self):
        return "https://restful-booker.herokuapp.com/booking"

    def create_booking(self):
        return "https://restful-booker.herokuapp.com/booking/1"

    # Update -> PUT, PATCH, DELETE - bookingId

    def put_patch_delete_booking(bookingID):
        return "https://restful-booker.herokuapp.com/booking/" + str(bookingID)

