#in flask shell:
from sqlalchemy import text
from app import db
db.session.execute(text('DELETE FROM User WHERE id = 5'))
db.session.commit()