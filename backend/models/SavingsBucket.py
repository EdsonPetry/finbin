class SavingsBucket:

    def __init__(self, id: int, user_id: int, name: str, goal_amount: int, current_amount: int, target_date: str, icon):
        self._id = id
        self._user_id = user_id
        self._name = name
        self._goal_amount = goal_amount
        self._current_amount = current_amount
        self._target_date = target_date
        self._icon = icon
    
    @property
    def id(self):
        return self._id
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def goal_amount(self):
        return self._goal_amount
    
    @goal_amount.setter
    def goal_amount(self, new_goal_amount):
        self._goal_amount = new_goal_amount
    
    @property
    def current_amount(self):
        return self._current_amount
    
    @current_amount.setter
    def current_amount(self, new_current_amount):
        self._current_amount = new_current_amount

    @property
    def target_date(self):
        return self._target_date
    
    @target_date.setter
    def target_date(self, new_target_date):
        self._target_date = new_target_date
    
    @property
    def icon(self):
        return self._icon
    
    @icon.setter
    def icon(self, new_icon):
        self._icon = new_icon
    


    