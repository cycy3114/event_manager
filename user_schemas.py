from pydantic import BaseModel, validator

class UserBase(BaseModel):
    username: str

    @validator("username")
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        if len(value) < 3 or len(value) > 20:
            raise ValueError("Username must be between 3 and 20 characters")
        return value

