# database.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


# Pass the Base class to SQLAlchemy - this is the correct pattern for flask_sqlalchemy 3.x
db = SQLAlchemy(model_class=Base)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))


class University(db.Model):
    __tablename__ = "universities"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    logo_url: Mapped[str] = mapped_column(String(255), nullable=True)
    picture_url: Mapped[str] = mapped_column(String(255), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    uni_off_page_url: Mapped[str] = mapped_column(String(255), nullable=True)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    language_of_education: Mapped[str] = mapped_column(String(50), nullable=True)
    prep_school: Mapped[str] = mapped_column(String(255), nullable=True)
    study_programs_link: Mapped[str] = mapped_column(String(255), nullable=True)
    application_deadline: Mapped[str] = mapped_column(String(50), nullable=True)
    application_fee: Mapped[str] = mapped_column(String(50), nullable=True)
    tuition_fee: Mapped[str] = mapped_column(String(50), nullable=True)
    tuition_fee_link: Mapped[str] = mapped_column(String(255), nullable=True)
    requirements: Mapped[str] = mapped_column(Text, nullable=True)
    scholarship_available: Mapped[str] = mapped_column(String(255), nullable=True)
    country: Mapped[str] = mapped_column(String(50), nullable=False)