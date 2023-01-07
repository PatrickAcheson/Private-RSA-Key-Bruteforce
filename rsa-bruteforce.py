import subprocess
import codecs
import sys

def cmdline(command) -> bytes:
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
    (out, err) = proc.communicate()
    return err

def main() -> None:
    # Assume that the rockyou.txt file is encoded using koi8_u
    with codecs.open('rockyou.txt', 'r', encoding='koi8_u') as f:
        # Read all the lines from the file and strip the leading/trailing whitespace
        words = [line.strip() for line in f]
    count = 0
    # Iterate through the list of words and try each one as the password
    for w in words:
        # command for cli
        strcmd = ("openssl rsa -in private.pem -out out.key -passin pass:" + w)
        res = cmdline(strcmd)
        count +=1
        if res.startswith(b"writing"):
            # working password is printed
            print("\nThe key is: " + w)
            sys.exit()
        else:
            print(f"{count} : {w}")
    print("Finished Wordlist")

if __name__ == '__main__':
    main()
