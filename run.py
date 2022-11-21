from flask.cli import FlaskGroup

from src.main.configs import create_app
from src.main.midlewares.extensions import db


app = create_app()

cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()

# if __name__ == "__main__":
#     app = app.create_app()
#     app.run(host="0.0.0.0", port=5000)