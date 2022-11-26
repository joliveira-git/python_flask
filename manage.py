from os import environ

from flask.cli import FlaskGroup
from src import create_app, db

app = create_app(environ.get('FLASK_CONFIG'))

cli = FlaskGroup(create_app=create_app)

with app.app_context():
    db.create_all()

# TODO: Solve: Error: No such command 'recreate_db'.
@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()
