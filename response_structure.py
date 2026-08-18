from pydantic import BaseModel


class Experience(BaseModel):
    company: str | None
    role: str | None
    start_date: str | None
    end_date: str | None
    place: str | None
    description: list[str]


class Education(BaseModel):
    institution: str | None
    degree: str | None
    field: str | None
    start_year: int | None
    end_year: int | None


class Resume(BaseModel):
    name: str | None
    email: str | None
    phone: str | None
    summary: str | None
    strengths: list[str] | None
    weakness: list[str] | None
    experience: list[Experience] | None
    skills: list[str]
    education: list[Education]