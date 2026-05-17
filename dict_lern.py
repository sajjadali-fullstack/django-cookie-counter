# Session management by using Cookies
# ----------------------------------------------------------------------

# TO ADD COOKIES TO THE RESPONSE:
# response.set_cookie(cookie_name, value)

# TO GET COOKIES SEND BY CLIENT:
'''
    request.COOKIES[cookiename]
    reqest.COOKIES.get(cookieName)
    request.COOKIES.get(cookieName, defaultValue)
'''

# FOX EG:

D={101: "Apple"}
print(D[101])

# print(D[102])  # KeyError

# '''
# Traceback (most recent call last):
#   File "D:\Django 2025-26\NavidSir\Project 29 COOKIES Count Project\pageCountProject\dict_lern.py", line 19, in <module>
#     print(D[102])  # KeyError
#           ~^^^^^
# KeyError: 102
# '''

print(D.get(101))  # Apple

print(D.get(102))  # None

print(D.get(101, "Key is Not available"))

print(D.get(102, "Key is Not available"))

# run in terminal : py dict_lern.py