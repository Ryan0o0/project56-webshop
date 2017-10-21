from django.contrib.sessions.backends.db import SessionStore as DbSessionStore

class SessionStore(DbSessionStore):
    #TODO: Zorg dat er wel een nieuwe session komt naar dat de data (winkelwagentje e.d.) wordt overgezet. Nu wordt heel de session niet vervangen.

    def cycle_key(self):
        pass