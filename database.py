import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Tuple, Optional

from config import DB_FILE


@dataclass
class Booking:
    room_number: int
    user_name: str
    email: str
    phone: str
    start_time: str
    end_time: str
    id: Optional[int] = None


class DatabaseManager:
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(DB_FILE)
        try:
            yield conn
        finally:
            conn.close()

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_number INTEGER,
                    user_name TEXT,
                    email TEXT,
                    phone TEXT,
                    start_time TEXT,
                    end_time TEXT
                )'''
            )
            conn.commit()

    def check_availability(self, room_number: int, start_time: str) -> Tuple[bool, Optional[Tuple]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT user_name, end_time FROM bookings
                WHERE room_number = ? AND ? < end_time''',
                (room_number, start_time)
            )
            return cursor.fetchone()

    def create_booking(self, booking: Booking):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO bookings (room_number, user_name, email, phone, start_time, end_time)
                VALUES (?, ?, ?, ?, ?, ?)''',
                    (booking.room_number, booking.user_name, booking.email,
                    booking.phone, booking.start_time, booking.end_time)
            )
            conn.commit()
