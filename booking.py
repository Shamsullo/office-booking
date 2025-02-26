from config import ROOM_OCCUPIED, ROOM_AVAILABLE, ROOM_BOOKED
from database import DatabaseManager, Booking
from notification import NotificationService


class BookingService:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.notification_service = NotificationService()

    def check_availability(self, room_number: int, start_time: str) -> str:
        booking = self.db_manager.check_availability(room_number, start_time)
        if booking:
            return ROOM_OCCUPIED.format(room_number, booking[0], booking[1])
        return ROOM_AVAILABLE.format(room_number)

    def book_room(self, booking: Booking) -> str:
        self.db_manager.create_booking(booking)
        self.notification_service.send_email(booking)
        self.notification_service.send_sms(booking)
        return ROOM_BOOKED.format(booking.room_number, booking.start_time, booking.end_time)
