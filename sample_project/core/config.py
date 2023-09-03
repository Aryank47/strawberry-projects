from typing import Any, Dict, Optional

from pydantic import validator
from pydantic.networks import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "sample_project"

    # Database configuration
    POSTGRES_SERVER: str
    POSTGRES_PORT: Optional[int] = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        # print(
        #     "DB URL -->",
        #     PostgresDsn.build(
        #         scheme="postgresql",
        #         hosts=None,
        #         username=str(values.get("POSTGRES_USER")),
        #         password=str(values.get("POSTGRES_PASSWORD")),
        #         host=str(values.get("POSTGRES_SERVER")),
        #         port=values.get("POSTGRES_PORT", 5432),
        #         path=f"{values.get('POSTGRES_DB') or ''}",
        #     ),
        # )
        return str(
            PostgresDsn.build(
                scheme="postgresql",
                hosts=None,
                username=str(values.get("POSTGRES_USER")),
                password=str(values.get("POSTGRES_PASSWORD")),
                host=str(values.get("POSTGRES_SERVER")),
                port=int(values.get("POSTGRES_PORT", 5432)),
                path=f"{values.get('POSTGRES_DB') or ''}",
            )
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
