from fastapi import APIRouter, HTTPException
from app.models.contact import Contact
from app.services.contact_service import ContactService

router = APIRouter()

@router.post("/contact")
async def create_contact(contact: Contact):
    print(contact.email)
    contact_id = await ContactService.create_contact(contact)
    if contact_id:
        return {"message": "Contact created", "id": str(contact_id)}
    raise HTTPException(status_code=500, detail="Failed to create contact")
