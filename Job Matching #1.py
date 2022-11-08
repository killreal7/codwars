def match(candidate, job):
    try:
        if candidate['min_salary'] * 0.9 <= job['max_salary']:
            return True
        else:
            return False
    except:
        return 'Error'