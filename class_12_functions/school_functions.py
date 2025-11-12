import statistics as st

def mode(grades):
    return st.mode(grades)

def mean(grades):
    return st.mean(grades)

def std_dev(grades):
    return st.stdev(grades)

def high_grade(grades):
    return max(grades)

def low_grade(grades):
    return min(grades)
