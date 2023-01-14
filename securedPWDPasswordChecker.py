import requests
import hashlib
import sys

#Check the data
def request_apiData(queryHash):
    url = 'https://api.pwnedpasswords.com/range/' + queryHash
    res = requests.get(url)
    if res.status_code != 200:
        raise  RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def password_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,k in hashes:
        if h == hash_to_check:
            return k
    return 0

#Convert password to SHA1
#Returns the time of the leak
def pwnedAPI_check(password):
    #check password exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_apiData(first5_char)
    return password_leaks(response, tail)

def main(args):
    for password in args:
        count = pwnedAPI_check(password)
        if count:
            print(f"{password} was found {count} times...Change your password")
        else:
            print(f"{password} was NOT found! Great job!")

        return 'done'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
