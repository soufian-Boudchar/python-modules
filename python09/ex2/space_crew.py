from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def format_validator(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")

        valid = False
        experienced = 0
        active = True
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                valid = True
            if member.years_experience >= 5:
                experienced += 1
            if not member.is_active:
                active = False
        if not valid:
            raise ValueError("Must have at least one Commander or Captain")

        if not active:
            raise ValueError("All crew members must be active")

        if self.duration_days > 365:
            if experienced < (len(self.crew) / 2):
                raise ValueError("Long missions (> 365 days) need "
                                 "50% experienced crew (5+ years)")
        return self


def mission_creator(
    _mission_id_: str,
    _mission_name_: str,
    _destination_: str,
    _launch_date_: datetime,
    _duration_days_: int,
    _crew_: list[CrewMember],
    _mission_status_: str,
    _budget_millions_: float,
) -> None:
    try:
        spm = SpaceMission(mission_id=_mission_id_,
                           mission_name=_mission_name_,
                           destination=_destination_,
                           launch_date=_launch_date_,
                           duration_days=_duration_days_,
                           crew=_crew_,
                           mission_status=_mission_status_,
                           budget_millions=_budget_millions_)
        print("Valid mission created:")
        print(f"Mission: {spm.mission_name}")
        print(f"ID: {spm.mission_id}")
        print(f"Destination: {spm.destination}")
        print(f"Duration: {spm.duration_days} days")
        print(f"Budget: ${spm.budget_millions}M")
        print(f"Crew size: {len(spm.crew)}")
        print("Crew members:")
        for member in spm.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")
    except ValidationError as e:
        print(e.errors()[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    member1 = CrewMember(member_id="CM001",
                         name="Sarah Connor",
                         rank=Rank.COMMANDER,
                         age=43,
                         specialization="Mission Command",
                         years_experience=19,
                         is_active=True)
    member2 = CrewMember(member_id="CM002",
                         name="John Smith",
                         rank=Rank.LIEUTENANT,
                         age=43,
                         specialization="Navigation",
                         years_experience=30,
                         is_active=True)
    member3 = CrewMember(member_id="CM003",
                         name="Alice Johnson",
                         rank=Rank.OFFICER,
                         age=35,
                         specialization="Engineering",
                         years_experience=15,
                         is_active=True)
    members = [member1, member2, member3]
    print("Space Mission Crew Validation")
    print("=========================================")
    mission_creator(_mission_id_="M2024_MARS",
                    _mission_name_="Mars Colony Establishment",
                    _destination_="Mars",
                    _launch_date_=datetime(2024, 3, 30),
                    _duration_days_=900,
                    _crew_=members,
                    _mission_status_="planned",
                    _budget_millions_=2500.0)
    print("\n=========================================")
    print("Expected validation error:")
    memberz = CrewMember(member_id="CM008",
                         name="sboudcha",
                         rank=Rank.LIEUTENANT,
                         age=35,
                         specialization="Engineering",
                         years_experience=15,
                         is_active=True)

    mission_creator(_mission_id_="M2024_MARS",
                    _mission_name_="Mars Colony",
                    _destination_="Mars",
                    _launch_date_=datetime(2024, 3, 30),
                    _duration_days_=900,
                    _crew_=[memberz],
                    _mission_status_="planned",
                    _budget_millions_=2500.0)
