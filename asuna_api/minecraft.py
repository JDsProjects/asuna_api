import datetime 

class HistoryConverter:
  _slots = (
      "name",
      "changedToAt",
      "timeChangedAt"
    )

  def __init__(self, data):
        self.name = data.get("name")
        self.changed_at = data.get("changedToAt")
        self.time_changed_at = data.get("timeChangedAt")

  def __str__(self):
      return self.name if self.name else None

class Minecraft:
    __slots__ = (
        "name",
        "uuid",
        "datetime_history"
    )

    def __init__(self, data):
        self.name = data.get("username")
        self.uuid = data.get("uuid")
        self.datetime_history = data.get("name_history")

    def __str__(self):
        return self.name if self.name else None

    @property
    def history(self):
      for json in self.datetime_history:
        changed_at = json["changedToAt"]
        if isinstance(changed_at, datetime.datetime):
          json["timeChangedAt"] = changed_at.strftime("%H:%M:%S")
          json["changedToAt"] = changed_at.strftime("%Y-%m-%d")

      return self.datetime_history

    @property
    def from_dict(self):
        datetime_history = self.datetime_history
        return [HistoryConverter(obj) for obj in datetime_history]

    @property
    def formatted_history(self):

        history = self.history

        formatted = ""
        for json in history:
            formatted += (
                f"{json['changedToAt'].replace('Origanal', 'Original')} >> {json['name']}\n"
            )

        return formatted

    @property
    def reversed_formatted_history(self):
        history = self.history

        formatted = ""
        for json in history[::-1]:
            formatted += (
                f"{json['changedToAt'].replace('Origanal', 'Original')} >> {json['name']}\n"
            )

        return formatted
