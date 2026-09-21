/* Producer (producer.c) | 20234014 이은정 */
/* 메시지 큐 사용 + API 데이터 다운로드 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <unistd.h>
#include <curl/curl.h>

#define INPUT_FILE "rainfall.txt"  // 받아온 데이터 저장 파일
#define MSG_KEY 1234               // 메시지 큐 키값
#define MSG_TYPE 1                 // 메시지 타입
#define API_URL "https://apihub.kma.go.kr/api/typ01/url/gts_syn1.php?tm=202211301200&dtm=10&stn=47&help=1&authKey=njld-D40Rb25Xfg-NAW9hA"

typedef struct {
    float temperature;
    float humidity;
    float rainfall;
} SensorData;

typedef struct {
    long mtype; // 메시지 타입
    SensorData data;
} Message;

// 파일 다운로드 콜백 함수
size_t write_data(void* ptr, size_t size, size_t nmemb, FILE* stream) {
    size_t written = fwrite(ptr, size, nmemb, stream);
    return written;
}

int download_file(const char* url, const char* filename) {
    CURL* curl;
    FILE* fp;
    CURLcode res;

    curl = curl_easy_init();
    if (curl) {
        fp = fopen(filename, "wb");
        if (!fp) {
            perror("Failed to open file");
            return 1;
        }
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
            fclose(fp);
            curl_easy_cleanup(curl);
            return 1;
        }
        fclose(fp);
        curl_easy_cleanup(curl);
    }
    return 0;
}

int main() {
    int msgid;
    FILE* fp;
    char line[1024];
    float temp_temperature = -1, temp_humidity = -1, temp_rainfall = -1;

    // 1. API 데이터 다운로드
    if (download_file(API_URL, INPUT_FILE) != 0) {
        fprintf(stderr, "Failed to download API data\n");
        return 1;
    }

    // 2. 메시지 큐 생성
    msgid = msgget(MSG_KEY, IPC_CREAT | 0666);
    if (msgid == -1) {
        perror("msgget failed");
        return 1;
    }

    // 3. rainfall.txt 파일 열기
    fp = fopen(INPUT_FILE, "r");
    if (!fp) {
        perror("Failed to open rainfall.txt");
        return 1;
    }

    // 4. 파일 읽어서 데이터 추출
    while (fgets(line, sizeof(line), fp)) {
        if (strstr(line, "\"TA\"")) {
            char* p = strchr(line, ':');
            if (p) temp_temperature = atof(p + 1);
        }
        else if (strstr(line, "\"HM\"")) {
            char* p = strchr(line, ':');
            if (p) temp_humidity = atof(p + 1);
        }
        else if (strstr(line, "\"RN\"")) {
            char* p = strchr(line, ':');
            if (p) temp_rainfall = atof(p + 1);

            // 세 값이 다 모였을 때 메시지 큐로 전송
            Message msg;
            msg.mtype = MSG_TYPE;
            msg.data.temperature = temp_temperature;
            msg.data.humidity = temp_humidity;
            msg.data.rainfall = temp_rainfall;

            if (msgsnd(msgid, &msg, sizeof(SensorData), 0) == -1) {
                perror("msgsnd failed");
                fclose(fp);
                return 1;
            }

            printf("[Producer] Produced: Temperature=%.1fC, Humidity=%.1f%%, Rainfall=%.1fmm\n",
                temp_temperature, temp_humidity, temp_rainfall);

            sleep(1); // 1초 간격으로 전송
        }
    }

    fclose(fp);
    return 0;
}
