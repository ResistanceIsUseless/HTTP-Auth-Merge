# /usr/bin/python3
# TODO: Fix output to file
import argparse
import base64


parser = argparse.ArgumentParser()
parser.add_argument('-u', "--usernames", help="username list")
parser.add_argument('-p', "--passwords", help="password list")
parser.add_argument('-o', "--out", help="output file")
parser.add_argument('-b', "--base64", help="base 64 encode output", action ='store_true')
args = parser.parse_args()

usernames = open(args.usernames, 'r')
passwords = open(args.passwords, 'r')
output = [...]
usernames = ['joe']
with open(args.usernames, 'r') as username_file:
    for user in username_file:
        user = user.strip('\n', )
        usernames.append(user)
for user in usernames:
    # print(user)
    for p in passwords:
        Pass = p.strip('\n', )
        User = user.strip('\n', )
        output = str(User) + ":" + str(Pass)
        if args.base64:
            b_output = base64.b64encode(output.encode())
            print(b_output.decode("utf-8"))
            if args.out:
                file = open(args.out, "w")
                for o in b_output:
                    file.write(str(o))
                    file.write("\n")
                file.close()
        else:
            print(output)
            if args.out:
                file = open(args.out, "w")
                for o in output:
                    file.write(str(o))
                    file.write("\n")
                file.close()

    passwords.seek(0)
