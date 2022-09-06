from alembic_utils.pg_trigger import PGTrigger

updated_at_column_events = PGTrigger(
    schema="public",
    signature="updated_at_column_events",
    on_entity="public.events",
    definition="""
    	BEFORE UPDATE ON events
    	FOR EACH ROW EXECUTE FUNCTION updated_at_column_value()
    """,
)

updated_at_column_updates = PGTrigger(
    schema="public",
    signature="updated_at_column_updates",
    on_entity="public.updates",
    definition="""
    	BEFORE UPDATE ON updates
    	FOR EACH ROW EXECUTE FUNCTION updated_at_column_value()
    """,
)
