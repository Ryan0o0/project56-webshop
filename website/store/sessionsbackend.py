from django.contrib.sessions.backends.db import SessionStore as DbSessionStore
from .database.sessionOps import updateCartKeys

class SessionStore(DbSessionStore):
    def cycle_key(self):
        oldkey = self.session_key
        super(SessionStore, self).cycle_key()
        self.save()
        updateCartKeys(oldkey, self.session_key)
