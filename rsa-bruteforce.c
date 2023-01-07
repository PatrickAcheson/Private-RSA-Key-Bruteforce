#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 128

int try_password(const char *password) {
  char command[BUFFER_SIZE];
  sprintf(command, "openssl rsa -in private.pem -out out.key -passin pass:%s", password);
  int result = system(command);
  return result == 0;
}

int main(int argc, char *argv[]) {
  FILE *fp = fopen("rockyou.txt", "r");
  if (fp == NULL) {
    perror("Error opening file");
    return 1;
  }

  char password[BUFFER_SIZE];
  int count = 0;
  while (fgets(password, BUFFER_SIZE, fp) != NULL) {
    // Strip the newline character from the password
    password[strcspn(password, "\n")] = '\0';
    if (try_password(password)) {
      printf("Found password: %s\n", password);
      break;
    } else {
      count++;
      printf("Incorrect password: %s\n", password);
    }
  }

  fclose(fp);
  return 0;
}
