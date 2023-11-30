from pydantic import BaseModel


class CountryAlpha3(BaseModel):
    alpha3: str


class CountryOut(CountryAlpha3):
    alpha2: str
    name: str

    class Config:
        orm_mode = True
