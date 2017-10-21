from django.contrib.sessions.backends.db import SessionStore as DbSessionStore
from .database.sessionOps import updateCartKeys

class SessionStore(DbSessionStore):
    #TODO: Zorg dat er wel een nieuwe session komt naar dat de data (winkelwagentje e.d.) wordt overgezet. Nu wordt heel de session niet vervangen.

    # def cycle_key(self):
    #     pass

    def cycle_key(self):
        print("Oude session key: " + str(self.session_key))
        oldkey = self.session_key
        super(SessionStore, self).cycle_key()
        self.save()
        print("Nieuwe session key: " + str(self.session_key))
        updateCartKeys(oldkey, self.session_key)
