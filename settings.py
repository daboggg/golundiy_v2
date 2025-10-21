from environs import Env
from dataclasses import dataclass


# @dataclass
# class Custom:
#     subscription_limit: int
#     subscription_privileged_limit: int

@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Database:
    database_name: str
    database_type: str


@dataclass
class Settings:
    bots: Bots
    db: Database
    # custom: Custom


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        # custom=Custom(
        #     subscription_limit=env.int("SUBSCRIPTION_LIMIT"),
        #     subscription_privileged_limit=env.int("SUBSCRIPTION_PRIVILEGED_LIMIT"),
        # ),
        bots=Bots(
            bot_token=env.str('BOT_TOKEN'),
            admin_id=env.int('ADMIN_ID')
        ),
        db=Database(
            database_name=env.str('DATABASE_NAME'),
            database_type=env.str('DATABASE_TYPE'),
        )
    )


settings = get_settings('.env')