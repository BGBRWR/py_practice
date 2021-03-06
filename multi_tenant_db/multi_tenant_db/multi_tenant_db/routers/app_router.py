class AppRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'snippets':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'snippets':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the snippets app is involved.
        """
        print(obj1)
        print(obj2)
        if obj1._meta.app_label == 'snippets' or \
           obj2._meta.app_label == 'snippets':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the snippets app only appears in the 'auth_db'
        database.
        """
        # print(db)
        if app_label == 'snippets':
            return db == 'default'
        return None
