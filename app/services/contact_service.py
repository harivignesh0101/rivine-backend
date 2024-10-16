# app/services/contact_service.py
from pydantic import BaseModel, EmailStr
from app.db.mongo import db  # Import the db instance

from app.models.contact import Contact


class ContactService:
    @staticmethod
    async def create_contact(contact: Contact):
        contact_dict = contact.dict()
        result = await db.contacts.insert_one(contact_dict)
        return result.inserted_id if result.inserted_id else None
