import datetime 

class HistoryConverter:
  _slots = ("name", "changedToAt", "timeChangedAt")

  def __init__(self, data):
        self.name = data.get("name")
        self.changed_at = data.get("changedToAt")
        self.time_changed_at = data.get("timeChangedAt")

  def __str__(self):
      return self.name if self.name else None

class Minecraft:
    __slots__ = ("name", "uuid", "datetime_history")

    def __init__(self, data):
        self.name = data.get("username")
        self.uuid = data.get("uuid")
        self.datetime_history = data.get("name_history")

    def __str__(self):
        return self.name if self.name else None

    @property
    def history(self):
      for x in self.datetime_history:
        y = x["changedToAt"]
        if isinstance(y, datetime.datetime):
          x["timeChangedAt"] = y.strftime("%H:%M:%S")
          x["changedToAt"] = y.strftime("%Y-%m-%d")

      return self.datetime_history

    @property
    def from_dict(self):
        d = self.datetime_history
        return [HistoryConverter(obj) for obj in d]

    @property
    def formatted_history(self):

        d = self.history

        formatted = ""
        for x in d:
            formatted += (
                f"{x['changedToAt'].replace('Origanal', 'Original')} >> {x['name']}\n"
            )

        return formatted

    @property
    def reversed_formatted_history(self):
        d = self.history

        formatted = ""
        for x in d[::-1]:
            formatted += (
                f"{x['changedToAt'].replace('Origanal', 'Original')} >> {x['name']}\n"
            )

        return formatted
