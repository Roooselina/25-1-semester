#행렬과 벡터
import numpy as np

# 2차원 벡터 (3, 4)
# v2 = np.array([3, 4])
# print(v2)  # [3 4]
#
# v3 = np.array([1, 2, 3])
# print(v3)  # [3 4]

#####1. 기본 배열(array) ########
# import cv2
# path1 = r"Z:\open\Lenna.png"
#
# image = cv2.imread(path1, cv2.IMREAD_COLOR) #컬러 영상 처리
# if image is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리
#
# x_axis = cv2.flip(image, 0)                 # x축 기준 상하 뒤집기
# y_axis = cv2.flip(image, 1)                 # y축 기준 좌우 뒤집기
# xy_axis = cv2.flip(image, -1)                       # 양축 뒤집기
# rep_image   = cv2.repeat(image, 2, 2)       # 반복 복사
# trans_image = cv2.transpose(image)                  # 행렬 전치 (행과 열 교환)
#
# ## 각 행렬을 영상으로 표시
# titles = ['image', 'x_axis', 'y_axis','xy_axis','rep_image','trans_image']
# for title in titles:
#     cv2.imshow(title, eval(title))
# cv2.waitKey(0)

#####1-1. 기본 배열(array) ########
# import cv2
# path1 = r"Z:\open\Lenna.png"
#
# image = cv2.imread(path1, cv2.IMREAD_COLOR) #컬러 영상 처리
# if image is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리
# ch1 = np.ones((2, 4), np.uint8) * 20
#
# #h = cv2.hconcat(image,ch1)
# #v = cv2.vconcat(image,ch1)
# #h = np.hstack(image, ch1)
# #v = np.vstack([image, ch1])
#
# cv2.imshow("image", v)
# cv2.waitKey()

##### 2. 채널 분리 합성(array) ########
# import numpy as np
# import cv2
#
# # numpy array이용해 단일 채널 3개 생성
# ch0 = np.zeros((2, 4), np.uint8) + 10           # 0원소 행렬 선언 후 10 더하기
# ch1 = np.ones((2, 4), np.uint8) * 20            # 1원소 행렬 선언 후 20 곱하기
# ch2 = np.zeros((2, 4), np.uint8); ch2[:] = 30   # 0원소 행렬 선언 후 행렬원소값 30 지정
#
# list_bgr = [ch0, ch1, ch2]                      # 단일 채널들을 모아 리스트 구성
# merge_bgr = cv2.merge(list_bgr)                 # 채널 합성
# split_bgr = cv2.split(merge_bgr)                # 채널 분리: 컬러영상--> 3채널 분리
#
# print('split_bgr 행렬 형태 ', np.array(split_bgr).shape) #채널 행과 열 (채널 분리할 때는 이렇게)
# print('merge_bgr 행렬 형태', merge_bgr.shape)            #행과 열 채널
#
# # print("[ch0] = \n%s" % ch0)                     # 단일 채널 원소 출력
# # print("[ch1] = \n%s" % ch1)
# # print("[ch2] = \n%s" % ch2)
# print("[merge_bgr] = \n %s\n" % merge_bgr)       # 다중 채널 원소 출력
# #print(split_bgr)       # 다중 채널 원소 출력
#
# print("[split_bgr[0]] =\n%s " % split_bgr[0])
# print("[split_bgr[1]] =\n%s " % split_bgr[1])
# print("[split_bgr[2]] =\n%s " % split_bgr[2])

#####3. 커널 채널 분리 ########
# import cv2
# path1 = r"Z:\open\Lenna.png"
# image = cv2.imread(path1, cv2.IMREAD_COLOR)  # 영상 읽기
# if image is None: raise Exception("영상 파일 읽기 오류 발생")  # 예외 처리
# if image.ndim != 3: raise Exception("컬러 영상 아님")
#
# bgr = cv2.split(image)  # 채널 분리: 컬러영상--> 3채널 분리
# # blue, green, red = cv2.split(image)
#
# print(bgr)
# print("bgr 자료형:", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
# print("bgr 원소개수:", len(bgr))
#
# # 각 채널을 윈도우에 띄우기
# cv2.imshow("image", image)
# cv2.imshow("Blue channel", bgr[0])  # blue 채널
# cv2.imshow("Green channel", bgr[1])  # green 채널
# cv2.imshow("Red channel", bgr[2])  # red 채널
# # cv2.imshow("Blue channel" , image[:,:,0])         	# 넘파이 객체 인덱싱
# # cv2.imshow("Green channel", image[:,:,1])
# # cv2.imshow("Red channel"  , image[:,:,2])
# cv2.waitKey()

#####4. 산술 연산 ########
# import numpy as np, cv2
#
# m1 = np.full((3, 6), 10, np.uint8)			# 단일 채널 생성 및 초기화
# m2 = np.full((3, 6), 50, np.uint8)
# m_mask = np.zeros(m1.shape, np.uint8)		# 마스크 생성
# m_mask[ :, 3: ] = 1							# 관심 영역을 지정한 후, 1을 할당
# print(m_mask)
# m_add1 = cv2.add(m1, m2)                    # 행렬 덧셈
# m_add2 = cv2.add(m1, m2, mask=m_mask)       # 관심 영역만 덧셈 수행
#
# # 행렬 나눗셈 수행
# m_div1 = cv2.divide(m1, m2)
# m1 = m1.astype(np.float32)                  # 형변환 - 소수 부분 보존
# m2 = np.float32(m2)
# m_div2 = cv2.divide(m1, m2)

# titles = ['m1', 'm2', 'm_mask','m_add1','m_add2','m_div1', 'm_div2']
# for title in titles:
#     print("[%s] = \n%s \n" % (title, eval(title)))

#####5. 산술 연산 ########
# import numpy as np
# import cv2
# m1 = np.full((3, 6), 10, np.uint8)			# 단일 채널 생성 및 초기화
# m2 = np.full((3, 6), 50, np.uint8)
# #실수
# scale = 2.0
# m1 = m1.astype(np.float32)
#
# #정수
# #scale = 2
# result_with_scale = cv2.divide(scale,m1)
#
# # 결과 출력
# print(result_with_scale)

#####6. addweighted ########
# import cv2
#
# path1 = r"Z:\open\Lenna.png"
# image1 = cv2.imread(path1, cv2.IMREAD_COLOR)
# image2 = cv2.imread(path1, cv2.IMREAD_COLOR)
#
# # cv2.addWeighted 함수 사용: alpha = 0.7, beta = 0.3, gamma = 0
# result_im = cv2.addWeighted(image1, 0.7, image2, 0.3, 0) #gamma 밝기 조절
#
# # 결과 이미지 출력
# # 결과 이미지 출력
# cv2.imshow('Blended Image', result_im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#####7. 지수 로그 ########
# import numpy as np, cv2
# # numpy array 생성 예시
# v1 = np.array([1, 2, 3], np.float32)          # 1차원 리스트로 생성- 행벡터
# v2 = np.array([[1], [2], [3]], np.float32)      # 2차원 리스트로(3행, 1열) - 행벡터
# v3 = np.array([[1, 2, 3]], np.float32)        	# 2차원 리스트로(1행, 3열) - 일반 행렬
#
# # OpenCV 산술 연산 함수는 numpy array만 가능함
# v1_exp = cv2.exp(v1)                             # 벡터에 대한
# v2_exp = cv2.exp(v2)                             # 행렬에 대한 지수 계산
# v3_exp = cv2.exp(v3)                             # 행렬에 대한 지수 계산
# log = cv2.log(v1)                             # 로그 계산
# sqrt= cv2.sqrt(v2)                            # 제곱근 계산
# pow = cv2.pow(v3, 3)                          # 3의 거듭제곱 계산
#
# # 결과 출력
# print("[v1] 형태: %s 원소: %s" % ( v1.shape, v1))
# print("[v2] 형태: %s 원소:\n%s" % ( v2.shape, v2))
# print("[v3] 형태: %s 원소: %s" % ( v3.shape, v3))
# print()
#
# # 행렬 정보 출력 - OpenCV 결과는 행렬로 반환됨 - 행벡터는 열벡터로 반환됨
# print("[v1_exp] 자료형: %s 형태: %s" % ( type(v1_exp), v1_exp.shape))  # 행벡터 인수의 결과
# print("[v2_exp] 자료형: %s 형태: %s" % ( type(v2_exp), v2_exp.shape))  # 행벡터 인수의 결과
# print("[v3_exp] 자료형: %s 형태: %s" % ( type(v3_exp), v3_exp.shape))  # 행벡터 인수의 결과
# print()
#
# # 열벡터를 1 행에 출력하는 예시 - 행벡터로 변환
# print("[log] =", log.T)            #다차원 배열을 1차원으로
# print("[sqrt] =", np.ravel(sqrt))  #다차원 배열을 1차원으로
# print("[pow] =", pow.flatten())    #다차원 배열을 1차원으로

#####8. magnitude  ########
import numpy as np, cv2

x = np.array([1, 2, 3, 5, 10], np.float32)            # 리스트를 numpy array로 변환
y = np.array([2, 5, 7, 2, 9]).astype("float32")

mag = cv2.magnitude(x, y)                   # 크기 계산
ang = cv2.phase(x, y)                       # 각도(방향) 계산
p_mag, p_ang  = cv2.cartToPolar(x, y)  # 극좌표로 변환
x2, y2 = cv2.polarToCart(p_mag, p_ang)  # 직교좌표로 변한

print("[x] 형태: %s 원소: %s" % ( x.shape, x))
print("[mag] 형태: %s 원소: %s" % ( mag.shape, mag))

print(">>>열벡터를 1행에 출력하는 방법")
print("[m_mag] = %s" % mag.T)
print("[p_mag] = %s" % np.ravel(p_mag))
print("[p_ang] = %s" % np.ravel(p_ang))
print("[x_mat2] = %s" % x2.flatten())
print("[y_mat2] = %s" % y2.flatten())