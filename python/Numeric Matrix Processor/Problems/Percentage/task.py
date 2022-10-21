def get_percentage(p, round_digits=None):
    if round_digits is None:
        return str(round(p * 100)) + '%'
    else:
        return str(round(p * 100, round_digits)) + '%'