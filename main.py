import argparse

from booking import BookingService
from config import BOOKING_ERROR
from database import Booking


def main():
    booking_service = BookingService()
    booking_service.db_manager.init_db()

    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["check", "book"],
                        help="Действие: check - проверить, book - забронировать")
    parser.add_argument("room_number", type=int, help="Номер кабинета")
    parser.add_argument("--user", help="Имя пользователя (для бронирования)")
    parser.add_argument("--email", help="Email пользователя (для бронирования)")
    parser.add_argument("--phone", help="Телефон пользователя (для бронирования)")
    parser.add_argument("--start", help="Время начала (YYYY-MM-DD HH:MM)")
    parser.add_argument("--end", help="Время окончания (YYYY-MM-DD HH:MM)")

    args = parser.parse_args()

    if args.command == "check":
        print(booking_service.check_availability(args.room_number, args.start))
    elif args.command == "book":
        if not all([args.user, args.email, args.phone, args.start, args.end]):
            print(BOOKING_ERROR)
        else:
            booking = Booking(
                args.room_number, args.user, args.email,
                args.phone, args.start, args.end
            )
            print(booking_service.book_room(booking))


if __name__ == "__main__":
    main()