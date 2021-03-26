class Mock:
  def __init__(self, mock_id=""):
    self.mock_id = mock_id

  def __eq__(self, other):
    return self.mock_id == other.mock_id
