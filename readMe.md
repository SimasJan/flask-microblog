### Chapter 4 - Database

## Database Models
The data that will be stored in the database and will be represented by a collection of classes, usually called database models. The ORM layer within SQLAlchemy will do the translations required to map objects created from these classes into rows in the proper database tables.

## Database Migrations

- Generate a new database migration
> flask db migrate -m 'user table'

- Apply the newly generated migrations to the database
> flask db upgrade

- Allows Alembic to migrate the database to any point in the history, even to older versions, by using the downgrade path.
> flask db downgrade

### Manual Database Manipulation

1. Changes to a database are made in the context of a session, which can be accessed as `db.session`.
2. Multiple changes can be accumulated in a session and once all the changes have been registered write all the changes atomically `db.session.commit()`. **Changes are only written to the database using this command.**
3. If at any time while working on a session there is an error, a call to `db.session.rollback()` will abort the session and remove any changes stored in it.
