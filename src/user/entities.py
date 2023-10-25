from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class User:
    id: Optional[int]
    username: str
    mobile: str
    hashed_password: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    registration_date: date

    @classmethod
    def create(cls, **kwargs) -> "User":
        return cls(
            id=None,
            username=kwargs["username"],
            mobile=kwargs["mobile"],
            hashed_password=kwargs["hashed_password"],
            first_name=kwargs.get("first_name") or None,
            last_name=kwargs.get("last_name") or None,
            email=kwargs.get("email") or None,
            registration_date=date.today(),
        )
