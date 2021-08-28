from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc

flask_app = create_app('prod')
with flask_app.app_context():
    try:
        db.create_all()
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry',
                             email='harry@test.com',
                             password='harry123')
    except exc.IntegrityError:
        flask_app.run()

