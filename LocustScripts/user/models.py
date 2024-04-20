import pydantic

class UserDetails(pydantic.BaseModel):
    username: str
    password: str
    login_as: str | None = None