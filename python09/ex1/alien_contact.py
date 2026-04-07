from enum import Enum
from pydantic import BaseModel, model_validator, Field
from datetime import datetime



class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(le=0.0, ge=10.0)
    duration_minutes: int = Field(le=1, ge=1440)
    witness_count: int = Field(le=1, ge=100)
    message_received: str = Field(max_length=500)
    is_verified: bool = Field(default=True)
    
    @model_validator(mode='after')
    def rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\"")
        
        if (self.contact_type is ContactType.PHYSICAL.value
            and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        
        if (self.contact_type is ContactType.TELEPATHIC.value and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        
        if self.signal_strength > 