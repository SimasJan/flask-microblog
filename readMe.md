### Chapter 4 - Database

## Database Models
The data that will be stored in the database and will be represented by a collection of classes, usually called database models. The ORM layer within SQLAlchemy will do the translations required to map objects created from these classes into rows in the proper database tables.

## Database Migrations

- Create a database migration sub-command
> flask db migrate -m 'user table'

> flask db upgrade()
- downgrade()

ou will find that it has two functions called upgrade() and downgrade(). The upgrade() function applies the migration, and the downgrade() function removes it. This allows Alembic to migrate the database to any point in the history, even to older versions, by using the downgrade path.