class Bucket:

    def __init__(self, goal: int, deadline: str):
        self._goal = goal
        self._deadline = deadline
        self._balance = 0
    
    # 
    @property
    def goal(self) -> int:
        return self._goal
    
    @goal.setter
    def goal(self, new_amount: int) -> None:
        self._goal = new_amount

    @property
    def deadline(self) -> str:
        return self._deadline
    
    @deadline.setter
    def deadline(self, new_deadline) -> None:
        self._deadline = new_deadline
    