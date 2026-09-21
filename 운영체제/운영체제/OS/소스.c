#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX 512

struct msg_buffer {
    long msg_type;
    char msg_text[MAX];
};

int main() {
    key_t key;
    int msgid;
    struct msg_buffer message;

    // key를 생성한다.
    key = ftok("msgprod.c", 65);

    // 메시지 큐 생성
    msgid = msgget(key, 0666 | IPC_CREAT);create unique key
    // 키 생성 실패시 오류 처리
    if (msgid == -1) {
        perror("msgget failed");
        exit(1);
    }

    // 전달할 메시지 작성
    message.msg_type = 1;
    snprintf(message.msg_text, MAX, "Hello Soonchunhyang Computer Engineering and Science!\n");

    // 메시지 송신 오류 처리
    if (msgsnd(msgid, &message, strlen(message.msg_text) + 1, 0) == -1) {
        perror("msgsnd failed");
        exit(1);
    }

    printf("Message succesfully sent!\ncontent: %s\n", message.msg_text);
    return 0;
}
