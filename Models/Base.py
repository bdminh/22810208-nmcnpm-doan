
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass


