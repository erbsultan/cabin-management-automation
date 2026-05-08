from sqlalchemy import select

from app.database import SessionLocal
from app.models.cabin import Cabin


def seed_cabins() -> None:
    db = SessionLocal()

    try:
        for number in range(1, 10):
            existing_cabin = db.scalar(
                select(Cabin).where(Cabin.number == number)
            )

            if existing_cabin:
                continue

            cabin = Cabin(
                number=number,
                name=f"Cabin {number}",
                is_active=True,
            )
            db.add(cabin)

        db.commit()
        print("Cabins seed completed successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_cabins()
