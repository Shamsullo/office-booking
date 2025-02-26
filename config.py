# Constants
DB_FILE = "office_booking.db"
EMAIL_HOST = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_password"

# Messages
ROOM_OCCUPIED = "Кабинет {} занят пользователем {} до {}"
ROOM_AVAILABLE = "Кабинет {} свободен"
ROOM_BOOKED = "Кабинет {} успешно забронирован с {} до {}"
BOOKING_ERROR = "Ошибка: Для бронирования укажите имя, email, телефон, время начала и окончания"
EMAIL_ERROR = "Ошибка отправки email: {}"
SMS_MESSAGE = "Отправка SMS на {}: Вы забронировали кабинет {} с {} до {}."
EMAIL_SUBJECT = "Подтверждение бронирования"
EMAIL_CONTENT = "Вы забронировали кабинет {} с {} до {}."
