def get_reply_keyboard(replies):
    """
    Formats replies keyboard according
    to the telegrams specification
    """
    return [[{"text": reply} for reply in replies]]
