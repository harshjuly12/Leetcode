class Logger:
  def __init__(self):
    self.messageQueue = collections.deque()
    self.messageSet = set()

  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    while self.messageQueue:
      headTimestamp, headMessage = self.messageQueue[0]
      if timestamp < headTimestamp + 10:
        break
      self.messageQueue.popleft()
      self.messageSet.remove(headMessage)

    if message in self.messageSet:
      return False

    self.messageQueue.append((timestamp, message))
    self.messageSet.add(message)
    return True