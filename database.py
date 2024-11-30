from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

# Initialize SQLite database
DATABASE_URL = "sqlite:///aasaas_product.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Companies table
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    contact_person = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    website = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Clients table
class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    name = Column(String, nullable=False)
    services_taken = Column(Text, nullable=True)
    why_with_us = Column(Text, nullable=True)
    website = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    company = relationship("Company", back_populates="clients")

# Recommendations table
class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    similar_company = Column(String, nullable=False)
    recommended_services = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    client = relationship("Client", back_populates="recommendations")

# Conversations table
class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True, nullable=False)
    user_input = Column(Text, nullable=False)
    agent_output = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Relationships
Company.clients = relationship("Client", back_populates="company")
Client.recommendations = relationship("Recommendation", back_populates="client")

# Create all tables
Base.metadata.create_all(bind=engine)
