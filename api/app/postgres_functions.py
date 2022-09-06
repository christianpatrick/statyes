from alembic_utils.pg_function import PGFunction

updated_at_column_value = PGFunction(
    schema="public",
    signature="updated_at_column_value()",
    definition="""
    RETURNS TRIGGER AS $$
    BEGIN
       IF row(NEW.*) IS DISTINCT FROM row(OLD.*) THEN
          NEW.updated_at = now(); 
          RETURN NEW;
       ELSE
          RETURN OLD;
       END IF;
    END;
    $$ language 'plpgsql';
    """,
)
