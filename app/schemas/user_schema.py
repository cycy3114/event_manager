from pydantic import BaseModel, field_validator, constr
import re

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: str
    password: str
    
    @field_validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError("Username can only contain letters, numbers, and underscores")
        if v.lower() in ['admin', 'root', 'system']:
            raise ValueError("This username is not allowed")
        return v

class UserUpdate(BaseModel):
    username: constr(min_length=3, max_length=20) | None = None
    bio: str | None = None
    profile_picture_url: str | None = None
    
    @field_validator('username')
    def validate_username(cls, v):
        if v and not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError("Username can only contain letters, numbers, and underscores")
        return v
