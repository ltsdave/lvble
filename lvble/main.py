import argparse

from sqlalchemy.orm import Session

from lvble.db import crud, engine, get_db, models

from .portals import Portal, ProtalBuilder
from .schemas import UserInput


def main(db: Session):
    parser = argparse.ArgumentParser(description="tenent portal data retriever")
    parser.add_argument("portal", type=str, help="portal of the tenent")
    parser.add_argument("username", type=str, help="username")
    parser.add_argument("password", type=str, help="password")
    args = parser.parse_args()

    user_input = UserInput(portal=args.portal, username=args.username, password=args.password)
    portal: Portal = ProtalBuilder(user_input)()
    tenant = portal.get_data()
    crud.create(db, tenant)


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    with get_db() as db:
        main(db)
