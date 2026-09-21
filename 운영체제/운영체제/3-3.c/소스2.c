/* Consumer (consumer.c) | 20234014 이은정 */
/* 메시지 큐 사용 */
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <unistd.h>

#define MSG_KEY 1234  // 메시지 큐 키값
#define MSG_TYPE 1    // 메시지 타입

// 송신할 데이터 목록
typedef struct {
    float temperature;
    float humidity;
    float rainfall;
} SensorData;

// 메시지 큐 구조
typedef struct {
    long mtype; // 메시지 타입
    SensorData data;
} Message;

int main() {
    int msgid;
    Message msg;

    // 메시지 큐 열기
    msgid = msgget(MSG_KEY, 0666);
    if (msgid == -1) {
        perror("msgget failed");
        exit(1);
    }

    while (1) {
        // 메시지 수신
        if (msgrcv(msgid, &msg, sizeof(SensorData), MSG_TYPE, 0) == -1) {
            perror("msgrcv failed");
            exit(1);
        }

        SensorData data = msg.data;
        // 각 데이터 불러와서 출력
        printf("[Consumer] Consumed: Temperature=%.1fC, Humidity=%.1f%%, Rainfall=%.1fmm\n",
            data.temperature, data.humidity, data.rainfall);

        // 각 데이터 별 인식 기능을 하는지 여부를 검토
        if (data.temperature > 30.0)
            printf("[Warning] High Temperature Alert!\n");

        if (data.humidity > 80.0)
            printf("[Warning] High Humidity Alert!\n");

        if (data.rainfall > 30.0)
            printf("[Warning] Heavy Rainfall Alert!\n");

        sleep(2); // 2초 간격으로 소비(여유시간 주기)
    }

    return 0;
}
