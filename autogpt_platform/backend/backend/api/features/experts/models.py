from pydantic import BaseModel, Field, field_validator

AI_DISCLOSURE_RULE = "The expert discloses that it is AI when acting externally."
EXTERNAL_ACTION_APPROVAL_RULE = "External actions require approval."
PROTECTED_SOUL_RULES = (AI_DISCLOSURE_RULE, EXTERNAL_ACTION_APPROVAL_RULE)


class ExpertWorkflowRef(BaseModel):
    id: str
    store_listing_version_id: str | None
    library_agent_id: str | None
    graph_id: str | None
    name: str | None
    description: str | None


class Expert(BaseModel):
    id: str
    name: str
    avatar_url: str | None
    role: str
    tagline: str | None
    bio: str | None
    skills: list[str]
    identity: str
    voice_preferences: str
    boundaries: str
    protected_soul_rules: list[str]
    is_template: bool
    source_template_id: str | None
    is_archived: bool
    workflows: list[ExpertWorkflowRef]


class HireResult(BaseModel):
    expert: Expert
    failed_preloads: list[str]


class ExpertSoulUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    identity: str = Field(min_length=1, max_length=10_000)
    voice_preferences: str = Field(max_length=4_000)
    boundaries: str = Field(max_length=4_000)

    @field_validator("name", "identity")
    @classmethod
    def strip_required_fields(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped:
            raise ValueError("Field must not be blank")
        return stripped
