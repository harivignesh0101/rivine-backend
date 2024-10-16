from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

class Contact(BaseModel):
    email: EmailStr
    name: str
    message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)  # Automatically set to current time
