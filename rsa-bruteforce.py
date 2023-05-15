import subprocess
import sys

def cmdline(command) -> bytes:
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
    (out, err) = proc.communicate()
    return err

def main(file) -> None:
    count = 0
    # Iterate through the lines in the file and try each one as the password
    with open('rockyou.txt', 'r', encoding='koi8_u') as f:
        for w in f:
            w = w.strip()  # strip the leading/trailing whitespace
            # command for cli
            strcmd = f"openssl rsa -in {file} -out out.key -passin pass:{w}"
            res = cmdline(strcmd)
            count += 1
            if res.startswith(b"writing"):
                # working password is printed
                print("\nThe key is: " + w)
                sys.exit()
            else:
                print(f"{count} : {w}")
    print("Finished Wordlist")

if __name__ == '__main__':
    file = "private.pem"
    main(file)
