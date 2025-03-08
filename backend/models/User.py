class User:

    def __init__(self, id: int, username: str, email: str, password_hash: str, created_at: str, preferences):
        self._id = id
        self._username = username
        self._email = email
        self._password_hash = password_hash
        self._created_at = created_at
        self._prefrences = preferences

    # ID GETTER
    @property
    def id(self) -> int:
        return self._id
    
    # USERNAME GETTER
    @property
    def username(self) -> str:
        return self._username
    
    # USERNAME SETTER
    @username.setter
    def username(self, new_username) -> None:
        self._username = new_username

    # EMAIL GETTER
    @property
    def email(self) -> str:
        return self._email
    
    # PASSWORD HASH GETTER??????????????
    # idk if we would want that to check the password or something lol

    # DATE CREATED GETTer
    @property
    def created_at(self) -> str:
        return self._created_at
    
    # PREFRENCES GETTER
    @property
    def preferences(self):
        return self._prefrences
    
    # PREFERENCES SETTER
    @preferences.setter
    def prefereences(self, updated_prefs):
        self._prefrences = updated_prefs

    
    
