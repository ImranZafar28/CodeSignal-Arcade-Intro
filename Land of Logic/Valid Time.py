# Valid Time
'''
Check if the given string is a correct time representation of the 24-hour clock.
'''

# Example
'''
For time = "13:58", the output should be solution(time) = true;

For time = "25:51", the output should be solution(time) = false;

For time = "02:76", the output should be solution(time) = false.
'''

def solution(time):
    hr = int(time[:2])
    mn = int(time[3:])
    if 0 <= hr <= 23 and 0 <= mn <= 59:
        return True
    else:
        return False

time = "13:58"
print(solution(time))

time = "25:51"
print(solution(time))

time = "02:76"
print(solution(time))