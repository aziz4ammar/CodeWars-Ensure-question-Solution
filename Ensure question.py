def ensure_question(s):
    if not s:
        return '?'
    if s[-1] == '?':
        return s
    else:
        return s+"?"