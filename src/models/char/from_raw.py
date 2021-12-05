class FromRaw(object):


  checked_dot = "☒"
  unchecked_dot = "☐"

  def bool_to_dot( self, val: bool):
    return self.checked_dot if val else self.unchecked_dot
