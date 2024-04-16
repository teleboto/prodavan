
import json

class Action:

  def __init__(
      self,
      type,
      payload
    ):
    self.type = type
    self.payload = payload

  @classmethod
  def from_dict(cls, data):
    return cls(data["type"], data["payload"])

  def to_dict(self):
    return {
      "type": self.type,
      "payload": self.payload
    }

  def to_json(self):
    return json.dumps(self.to_dict())
