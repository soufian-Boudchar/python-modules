from enum import Enum
from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\"")

        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if (self.signal_strength > 7.0 and not self.message_received):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main(_contact_id_, _timestamp_, _location_, _contact_type_,
         _signal_strength_, _duration_minutes_, _witness_count_,
         _message_received_, _is_verified_) -> None:

    try:
        cna = AlienContact(contact_id=_contact_id_,
                           timestamp=_timestamp_,
                           location=_location_,
                           contact_type=_contact_type_,
                           signal_strength=_signal_strength_,
                           duration_minutes=_duration_minutes_,
                           witness_count=_witness_count_,
                           message_received=_message_received_,
                           is_verified=_is_verified_)
        print("Valid contact report:")
        print(f"ID: {cna.contact_id}")
        print(f"Type: {cna.contact_type.value}")
        print(f"Location: {cna.location}")
        print(f"Signal: {cna.signal_strength}/10")
        print(f"Duration: {cna.duration_minutes} minutes")
        print(f"Witnesses: {cna.witness_count}")
        print(f"Message: '{cna.message_received}'")

    except ValidationError as e:
        print(e.errors()[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    main(_contact_id_="AC_2024_001",
         _timestamp_=datetime(1999, 11, 11),
         _location_=" Area 51, Nevada",
         _contact_type_=ContactType.RADIO,
         _signal_strength_=8.5,
         _duration_minutes_=45,
         _witness_count_=5,
         _message_received_="Greetings from Zeta Reticuli",
         _is_verified_=True)
    print("\n======================================")
    print("Expected validation error:")

    main(_contact_id_="AC_2024_001",
         _timestamp_=datetime(1999, 11, 11),
         _location_="Area 51, Nevada",
         _contact_type_=ContactType.TELEPATHIC,
         _signal_strength_=8.5,
         _duration_minutes_=45,
         _witness_count_=1,
         _message_received_="Greetings from Zeta Reticuli",
         _is_verified_=True)
