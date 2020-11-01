class Clock:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._normalize()

    def str_update(self, new_value: str):
        hours, minutes, seconds = new_value.split(":")
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)
        self._normalize()

    def _normalize(self):
        carry_minutes, seconds = divmod(self.seconds, 60)
        self.seconds = seconds
        self.minutes += carry_minutes
        carry_hours, minutes = divmod(self.minutes, 60)
        self.minutes = minutes
        self.hours += carry_hours
        self.hours = self.hours % 24

    def __str__(self) -> str:
        return f"{self.hours} hours, {self.minutes} minutes and {self.seconds} seconds"

    def add_clocks(self, other: "Clock") -> "Clock":
        return Clock(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
