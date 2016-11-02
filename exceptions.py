# -<USER INPUT EXCEPTIONS>-
class InputEmptyError('No information has been provided for "%s"' % element):
    """
    Nothing provided for required element.
    """
    def __init__(self, value):
        self.value=value
    def __str__(self, value):
        return repr(self.value)


class InputNotValidError('Validation failed for "%s"' % element):
    """
    Validation failed for an element.
    """
    def __init__(self, value):
        self.value=value
    def __str__(self):
        return repr(self.value)

class PasswordsNotMatchingError('The two attlempts to enter the password do not match.')
    """
    The two attlempts to enter the password do not match.
    """
    def __init__(self, value):
        self.value=value
    def __str__(self):
        return repr(self.value)
# -<UIE>-
