import smtplib
from email.message import EmailMessage

from config import (
    EMAIL_CONTENT, EMAIL_SUBJECT, EMAIL_SENDER, EMAIL_HOST, EMAIL_PORT, EMAIL_PASSWORD,
    EMAIL_ERROR, SMS_MESSAGE
)
from database import Booking


class NotificationService:
    def send_email(self, booking: Booking):
        msg = EmailMessage()
        msg.set_content(
            EMAIL_CONTENT.format(booking.room_number, booking.start_time, booking.end_time)
        )
        msg["Subject"] = EMAIL_SUBJECT
        msg["From"] = EMAIL_SENDER
        msg["To"] = booking.email

        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            print(EMAIL_ERROR.format(e))

    def send_sms(self, booking: Booking):
        print(
            SMS_MESSAGE.format(
                booking.phone, booking.room_number, booking.start_time, booking.end_time
            )
        )
        # To be implemented
