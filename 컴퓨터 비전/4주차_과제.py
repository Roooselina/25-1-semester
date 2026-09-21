# 기본으로 사용하는 라이브러리이다.
# 아래 라이브러리들은 매 문제마다 반복해서 import 할 필요가 없으므로
# 여기에 import 하여 사용한다.
import cv2
import numpy as np
import matplotlib.pyplot as plt
# ##################################################
# #                       1번                      #
# ##################################################
# # 이미지 크기를 지정하여 흑백 이미지 행렬을 생성한다.
# # 이때 이미지의 크기는 세로 500px, 가로 600px이다.
# image = np.zeros((500, 600), np.uint8)

# # 이미지 행렬의 색상을 설정한다.
# # np.uint8 자료형은 0~255의 정수 값을 가지므로, 255는 흰색을 의미한다.
# # 따라서 전체 이미지가 흰색으로 채워진 500x600 크기의 흑백 이미지가 생성된다.
# image[:] = 255

# # 팝업 창의 이름을 "window"로 지정한다.
# title = "window"
 
# # 팝업 창의 속성을 설정한다.
# # cv2.WINDOW_NORMAL 옵션을 사용하면 사용자가 창의 크기를 자유롭게 조절할 수 있다.
# cv2.namedWindow(title, cv2.WINDOW_NORMAL)

# # 팝업 창이 화면에 나타나는 위치를 지정한다.
# # 화면 기준으로 왼쪽에서 100px, 위쪽에서 200px 떨어진 위치에 창이 생성된다.
# cv2.moveWindow(title, 100, 200)

# # 팝업 창을 띄우고, 해당 창에 이미지를 출력한다.
# cv2.imshow(title, image)

# # 키보드 입력을 대기한다.
# # 아무 키나 입력될 때까지 대기하며, 입력 시 아래의 destroyAllWindows()가 실행되어 창이 종료된다.
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ##################################################
# #                       2번                      #
# ##################################################
# # 1번 문제와 유사한 코드이다.
# # np.zeros() 메서드를 이용해 행렬을 생성해 이미지 크기를 지정하여 흑백 이미지 행렬을 생성한다.
# # 이때 이미지의 크기는 세로 256px, 가로 256px이다.
# image = np.zeros((256,256), dtype=np.uint8)

# # 이미지 행렬의 색상을 설정한다.
# # np.uint8 자료형은 0~255의 정수 값을 가지므로, 255는 흰색을 의미한다.
# # 따라서 전체 이미지가 흰색으로 채워진 256x256 크기의 흑백 이미지가 생성된다.
# image[:]=255

# # 팝업 창의 이름을 "results"로 지정한다.
# title="results"

# # 팝업 창을 띄우고, 해당 창에 이미지를 출력한다.
# cv2.imshow(title, image)

# # 키보드 입력을 대기한다.
# # 아무 키나 입력될 때까지 대기하며, 입력 시 아래의 destroyAllWindows()가 실행되어 창이 종료된다.
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ''' 1번 코드와 다른 점은 
#     cv2.namedWindow(title, cv2.WINDOW_NORMAL)
#     cv2.moveWindow(title, 100, 200)
#     코드를 지정하지 않는다. 하지만, OpenCV에서는 imshow() 메서드를 실행할 때 default로 cv2.WINDOW_AUTOSIZE 옵션을 가진다.
#     따라서 창 생성 시, 256X256의 흰 이미지가 있고, 창 조절이 불가능한 팝업이 생성된다.
    
#     moveWindow가 없을 시, 임의로 창 위치가 지정되어 창이 열리게 된다.

# '''

##################################################
#                     3-1번                      #
##################################################
# # np.zeros() 메서드를 이용해 행렬을 생성해 이미지 크기를 지정하여 컬러 이미지 행렬(3차원 행렬)을 생성한다.
# # 이때 이미지의 크기는 세로 300, 가로 400px이다.
# # 3은 B,G,R의 데이터를 나타내는 채널 역할을 한다.
# image = np.zeros((300, 400, 3), np.uint8)

# # 이미지 행렬의 색상을 설정한다.
# # np.uint8 자료형은 0~255의 정수 값을 가지므로, 255는 흰색을 의미한다.
# # B,G,R 모두 255의 값을 가지므로, 전체 이미지가 흰색으로 채워진 256x256 크기의 컬러 이미지가 생성된다.
# image[:] = (255, 255, 255)

# # pt1, pt2의 좌표를 설정하는 행렬을 정의한다.
# # 각각의 점은 line을 그리기 위한 좌표로서 사용된다.
# pt1, pt2 = (50, 130), (200, 300)

# # line 그리려고 시도 시, 아래와 같은 오류가 발생한다.
# # OpenCV(4.11.0) :-1: error: (-5:Bad argument) in function 'line'
# #   > Overload resolution failed:
# #   >  - line() missing required argument 'color' (pos 4)
# #   >  - line() missing required argument 'color' (pos 4)
# # 즉슨 인수 4개가 전달되어야 하는데, 그 중 pt2를 담당하는 인수가 전달되지 않았다는 뜻이다.

# # line 메서드의 정의는 아래와 같다.
# ''' (function)
#     def line(
#         img: MatLike,
#         pt1: Point,
#         pt2: Point,
#         color: Scalar,
#         thickness: int = ...,
#         lineType: int = ...,
#         shift: int = ...
#     ) -> MatLike: ...
# '''
# # img, pt1, pt2, color은 필수로 전달되어야 하는 요소다.
# # # 따라서 아래 line 2개를 합쳐 pt1, pt2를 동시에 전달해주면 오류는 해결된다.
# # cv2.line(image, pt1, (100, 200))
# # cv2.line(image, pt2, (100, 100))

# # image : 300x400px(배경) | 색상: ffffff
# # pt1(시작점) : 50,130
# # pt2(끝나는 점) : 200,300
# # 선의 색상: 100,200,0 | R에 해당하는 값이 전달되지 않으면 0을 deafult  값으로 가진다.
# cv2.line(image, pt1, pt2, (100, 200))

# # rectangle() 메서드의 정의 또한 line() 메서드와 동일하다.
# # 따라서 이 코드는 오류가 발생하지 않는다.
# # image 데이터 위에서, pt1, pt2를 각 대각선 꼭짓점으로 가지는 2가지 색상의 rectangle을 그린다.
# # 2가지 동일한 크기의 사각형이 그려지나 (0,0,25) color 값을 가진 사각형이 더 나중에 그려지므로, R=255인 빨간 직사각형만 보인다.
# # 그 뒤에 R=255, B=255인 직사각형이 존재하나, 겹쳐서 보이지 않을 뿐이다.
# cv2.rectangle(image, pt1, pt2, (255, 0, 255))
# cv2.rectangle(image, pt1, pt2, (0, 0, 255))

# # title을 Line & Rectangle로 한 이후, 팝 업 창을 실행한다.
# # 창 배경은 image이다. 따라서, 그 배경 위에 위의 도형들이 그려지게 된다.
# title = "Line & Rectangle"
# cv2.namedWindow(title)
# cv2.imshow(title, image)

# #아무 키를 입력 하면 창을 종료한다.
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##################################################
#                     3-2번                      #
##################################################
# # 이 코드는 마우스를 클릭했을 때 이벤트를 처리 하는 함수이다.
# # mouseCallback 함수로 연결된 이 코드는, 왼쪽 마우스 오른쪽 마우스 클릭을 했을 때 각각의 동작을 정의하고 있다.
# def onMouse(event, x, y, flags, param):
#     global title, image

#     # 왼쪽 버튼을 누르는 이벤트가 발생했을 때 오류가 발생한다.
#     '''
#         Traceback (most recent call last):
#         File "C:\\Users\\kuroc\\OneDrive\\바탕 화면\\과제\\컴퓨터 비전\\4주차_실습.py", line 144, in onMouse
#             cv2.circle(image, pt=(x, y), radius=5, color=100, thickness=2)
#         cv2.error: OpenCV(4.11.0) :-1: error: (-5:Bad argument) in function 'circle'
#         > Overload resolution failed:
#         >  - circle() missing required argument 'center' (pos 2)
#         >  - circle() missing required argument 'center' (pos 2)
#     '''
#     # 위 오류는 circle()메서드에 필요한 인자가 전부 전달되지 않아 발생하느 오류이다.

#     #circle() 메서드의 정의는 다음과 같다.
#     '''
#         def circle(
#         img: MatLike,
#         center: Point,
#         radius: int,
#         color: Scalar,
#         thickness: int = ...,
#         lineType: int = ...,
#         shift: int = ...
#         ) -> MatLike: ...
#     '''
#     # 아래 코드를 살펴보면 image, pt, radius, color, thickness 5개의 인자를 전달한다.
#     # 하지만 circledms center에 인자를 전달해야 한다.
#     # pt로 인자를 전달했으므로, center로 인자가 전달되지 않았던 것이다.
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # cv2.circle(image, pt=(x, y), radius=5, color=100, thickness=2)

#         # 이것 처럼, center로 제대로 데이터를 전달해주게 되면 오류 없이 코드가 제대로 실행되는 것을 확인할 수 있다.
#         cv2.circle(image, center=(x, y), radius=5, color=100, thickness=2)
#         cv2.imshow(title, image)

#     # 오른 쪽 버튼을 누르는 이벤트 처리는 오류 없이 제대로 작동한다.
#     # 마우스의 x, y를 왼쪽 위의 꼭짓점으로 하여 가로 세로 30px의 정사각형을 그린다.
#     # 100으로 scalar 값이 color 인자로 넘어가므로, 흑백의 밝기로 표현된다.
#     # 따라서 30px짜리 100의 밝기와 2px의 굵기를 가진 정사각형이 image에 그려진다.
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         cv2.rectangle(image, pt1=(x, y), pt2=(x+30, y+30), color=100, thickness=2)
#         cv2.imshow(title, image)

# # 모든 것의 배경이 되는 image를 정의한다.
# # 300, 300 사이즈의 1로 구성된 행렬에 255를 곱해줌으로써, 1줄로 300,300 크기의 흰 색 행렬 이미지를 구성할 수 있다.
# image = np.ones((300, 300), np.uint8) * 255
# title = "Draw Event"

# cv2.namedWindow(title)
# cv2.imshow(title, image)

# # 창을 실행하고 나서, 마우스 콜 백 함수를 정의한다.
# # 위의 마우스 처리 함수를 title이라는 이름을 가진 창에 연결해준다.
# cv2.setMouseCallback(title, onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##################################################
#                     4번                        #
##################################################
# # 3개의 배열을 정의 후, cv2를 사용해 창을 띄우는 문제이다.
# # 각 데이터 특징은 아래와 같다.
# '''
#     window 1 : ffffff | 0,0 위치
#     window 2 : ffffff | 300,300 위치
#     window 3 : 000000 | 600,0 위치
# '''
# # 즉슨 홀수 window는 y가 0, 짝수는 300이고, 1,2,3에서 각각 1을 뺀 수 *300 을 x값으로 가진다는 것이다.

# # 문제 조건은 3개의 행렬을 만들어, 제시된 이미지와 같이 창을 구성하는 것이다.
# # 따라서 위 조건을 만족하는 행렬을 만든다.
# # 각 image 중 1,2 만 np.ones((300,300), np.uint8) * 255 를 통해 흰 색을 구성하고, 3은 zeros를 통해 검은 색으로 두었다.
# image1 = np.ones((300, 300), np.uint8) * 255
# image2 = np.ones((300, 300), np.uint8) * 255
# image3 = np.zeros((300, 300), np.uint8)

# # window 3개를 for문을 사용해 참조할 것이므로 img라는 행렬에 위 행렬을 담는다.
# img = [image1, image2, image3]

# for i in range(1, 4):
#     # i는 1~3부터 출력된다. 따라서 title은 차례대로 window1, window2, window3으로 저장된다.
#     # 저장된 title을 for문을 통해 나타낼 창의 title로 지정한다.
#     title = "window"+str(i)
#     cv2.namedWindow(title)

#     # 창이 홀수인지, 아니면 짝수인지에 따라 창의 x, y 좌표가 달라지므로, 짝수-홀수를 검사한다.
#     # 만약 홀수일 경우, y가 0이다.
#     # 따라서 (i-1)*300, 0으로 pt를 지정한다.
#     if (i%2 == 1):
#         pt= ((i-1)*300,0)
    
#     # 짝수 일 경우, y는 300이다.
#     # 따라서 (i-1)*300, 300으로 pt를 지정한다.
#     else:
#         pt= ((i-1)*300,300)
    
#     # 위 과정을 통해 pt를 지정했으므로, 창의 위치를 지정한다.
#     # 현재 창의 이름을 인수로 넘겨 객체를 지정하고, x, y 데이터를 넘기기 위해 pt의 각 데이터를 인수로 넘긴다.
#     cv2.moveWindow(title, pt[0], pt[1])

#     # 배경 이미지는 img에서 0,1,2 순으로 저장되어 있다. 따라서 i-1의 인덱스를 배경으로 하여 창을 생성한다.
#     cv2.imshow(title, img[i-1])

# cv2.waitKey(0)
# cv2.destroyAllWindows()        
##################################################
#                     5번                        #
##################################################
# # 이미지 데이터를 읽어온다.
# # cv2에서 보이는 이미지는 BGR 형태로, 정상적으로 보인다.
# image = cv2.imread('ocean.jpeg')

# # 2개의 이미지를 동시에 보여주어야 하므로 subplot을 사용한다. 
# # subplot은 다음과 같이 정의된다.
# '''
#     plt.subplot(nrows, ncols, index)
#     nrows : subplot 전체 행
#     ncols : subplot 전체 열
#     index : 현재 위치 인덱스
# '''
# # index는 왼쪽 위를 기준으로 1로 간주되며, 자동으로 1씩 번호가 매겨진다.
# # plt를 사용해 bgr 이미지를 출력한다.
# # plt는 rgb를 사용하고 있으므로 이상한 결과가 출력된다.
# plt.subplot(1, 2, 1)
# plt.imshow(image)
# plt.title('bgr color')

# # 2번 인덱스에서는 text 작성 및 rgb로 채널 전환을 한다.
# plt.subplot(1, 2, 2)

# # 이미지에 아래와 같은 속성을 가진 텍스트를 작성한다.
# cv2.putText(
#     image, "OpencvPython", 
#     (10, 120),                         # 위치 (x=10, y=50)
#     cv2.FONT_HERSHEY_DUPLEX,        # 폰트
#     5,                              # 크기
#     (255, 0, 0),                      # 색상 (파란색 in BGR)
#     3,                                # 두께
#     cv2.LINE_AA                      # 안티알리아싱
# )

# # 이후, cv2.cvtColor(image, cv2.COLOR_BGR2RGB)를 통해 rgb로 채널 순서를 전환한다.
# # 이로서, plt에서 정상적으로 처리하는 이미지 형태가 되었다.
# image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # 아래와 같이 이름을 붙이고, 창을 띄운다.
# plt.imshow(image_2)
# plt.title('rgb color')

# # 모든 subplot에 대한 이름을 붙이고, 창을 출력한다.
# plt.suptitle("BGR-RGB")
# plt.tight_layout()
# plt.show()

#########################
#          6번          #
#########################
# # onchange()에서 imshow()에서 사용하는 객체들이다.
# # 'Trackerbar Event' 이름을 가진 500x500px 크기의 검은색 배경이다.
# title ='Trackerbar Event'
# base_image = np.zeros((500, 500), np.uint8)

# # 교과서의 예제 코드는 다음과 같았다
# '''
#     # 윈도우 생성
#     title ='Trackerbar Event'
#     image = np.zeros((300,300), np.uint8)

#     def onChange(value):
#         global image, title

#         add_value = value - int(image[0][0])
#         image = image + add_value
#         cv2.imshow(title, image)
# '''
# # 위 메서드 사용 후, 코드 실행 시 밝아지는 것은 잘 되지만, 어두워 지는 것은 제대로 되지 않는다.
# # 그 이유는 image 데이터가 밝아진 데이터로 업데이트 되었기 때문이다. 
# # image[0][0] 데이터는 계속 변화한다. 따라서, 연속 계산 시 오류가 발생할 수 있다.

# # 위 문제를 해결하기 위해 기준 데이터가 필요하다.
# # 위 데이터 중, base 이미지를 지정하고, 현재 밝기에 대한 데이터를 매번 업데이트 해주는 것이 좋다.
# # value를 통해 계속해서 param 데이터 값은 들어오고 있으니 0 + param 데이터로 image를 업데이트 한다.
# # 이 때, 원 본 값 손실이 발생해서는 안되므로, 함수 내에서만 사용하는 지역 변수 image를 지정한다.

# def onChange(value):
#     # 함수 내로 들어와서 계속해서 사용해야 하므로 global 함수로 지정한다.
#     global base_image, title

#     # 0에서 param 데이터 값을 더한 밝기를 cv2로 내보낸다.
#     # 이 방식을 통해 밝기 오류를 해결할 수 있다.
#     image = base_image + value
#     cv2.imshow(title, image)

# # 가장 초기 창을 생성한다. 이 때에는 base_image를 사용한다.
# # 추후 함수를 통해 새로운 image가 배경으로 업데이트 된다.
# cv2.namedWindow(title)
# cv2.imshow(title, base_image)

# # 트랙바를 생성한다.
# # 트랙바 정의는 아래와 같다.
# '''
#     (function) def createTrackbar(
#         trackbarName: str,
#         windowName: str,
#         value: int,
#         count: int,
#         onChange: (int) -> None
#     ) -> None
# '''
# # 따라서 트랙바 명, window 창 이름(str; 행렬 값을 받지 않음), 최소 값, 최대 값, 콜 백 함수를 연결한다.
# # 트랙바를 움직이면 항상 onChange에 트랙바가 가리키는 데이터가 자동으로 전달된다.
# cv2.createTrackbar('Brightness', title, 0, 255, onChange)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#########################
#          7번          #
#########################
# # Lenna 이미지 로드
# # matplotlib로 데이터를 표현해야 하기 때문에 BGR2RGB로 이미지를 BGR에서 RGB 배열로 바꿔준다.
# img = cv2.imread('Lenna.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # 보간 기법 리스트를 지정한다.
# methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36']

# # plt 크기 지정 후, 시각화한다.
# plt.figure(figsize=(12, 8))

# # methods에 나오는 보간법을 Lenna.jpg에 적용한다. 
# for i, method in enumerate(methods):
#     # 각 위치, method를 적용해 이미지에 보간법을 적용 시, 총 6개의 보간법이 적용된 이미지가 표현된다.
#     plt.subplot(2, 3, i + 1)
#     plt.imshow(img, interpolation=method)
#     plt.title(method)

# # 창을 이미지에 맞게 재조정한다.
# plt.tight_layout()

# # 비동기 식으로, 이미지를 창에 계속 띄운다.
# # 이후, 아무 키를 입력하게 될 때까지 기다렸다 입력을 받고 나면 close() 메서드를 통해 창을 닫는다.
# plt.show(block=False)
# plt.waitforbuttonpress(0)
# plt.close()

#########################
#          8번          #
#########################
# import os

# # Lenna 이미지 로드
# # matplotlib로 데이터를 표현해야 하기 때문에 BGR2RGB로 이미지를 BGR에서 RGB 배열로 바꿔준다.
# img = cv2.imread('Lenna.jpg')
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # 보간 기법 리스트를 지정한다.
# methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36']

# # 저장 폴더 지정
# # 원래는 '4th_Img_save_Folder' 라는 현재 폴더 디렉토리에 저장하려 했으나 jpg, bmp 파일을 저장하지 못하는 오류가 발생했다.
# # 따라서 이 문제를 해결하기 위해, c에 데이터를 저장했다.
# save_dir = r'C:\4th_Img_save_Folder'

# # 각각 이미지에 대해 저장 옵션을 설정한다.
# # 문제 조건에 맞게 각 이미지를 조절한다.
# params_jpg = [cv2.IMWRITE_JPEG_QUALITY, 90]       # JPEG: 퀄리티 90 이상
# params_png = [cv2.IMWRITE_PNG_COMPRESSION, 5]     # PNG: 압축 레벨 5 이상

# # plt 크기 지정 후, 시각화한다.
# plt.figure(figsize=(12, 8))

# # methods에 나오는 보간법을 Lenna.jpg에 적용한다.
# # 따라서 i에는 0부터 5까지의 숫자가, method에는 보간법 이름이 전달된다.
# for i, method in enumerate(methods):
#     # 각 위치, method를 적용해 이미지에 보간법을 적용 시, 총 6개의 보간법이 적용된 이미지가 표현된다.
#     plt.subplot(2, 3, i + 1)
#     plt.imshow(img_rgb, interpolation=method)
#     plt.title(method)

#     if method == 'none':
#         continue

#     filename = f"image_{method}"
#     filepath = os.path.join(save_dir, filename)

#     # 저장 시에는 반드시 BGR 이미지 사용한다.(cv2 사용해서)
#     # 위에 지정해둔 위치에 파일들을 저장한다.
#     if method == 'spline16':
#         cv2.imwrite(filepath + '.jpg', img, params_jpg)
#     elif method == 'spline36':
#         cv2.imwrite(filepath + '.bmp', img)
#     else:
#         cv2.imwrite(filepath + '.png', img, params_png)

# # 창을 이미지에 맞게 재조정한다.
# plt.tight_layout()

# # 비동기 식으로, 이미지를 창에 계속 띄운다.
# # 이후, 아무 키를 입력하게 될 때까지 기다렸다 입력을 받고 나면 close() 메서드를 통해 창을 닫는다.
# plt.show(block=False)
# plt.waitforbuttonpress(0)
# plt.close()

#########################
#          9번          #
#########################
# # Lenna 이미지를 로드한다.
# image = cv2.imread('Lenna.jpg')

# # 마우스를 떼고 나면 그린 사각형이 사라진다.
# # 따라서 원본 이미지를 가지고 있어야 원본 이미지를 복구할 수 있다.
# original = image.copy()
# window = "Draw Event"

# # 마우스가 눌렸는지를 검사한다.
# # 마우스 눌렸는지 여부, x, y 값을 저장할 변수들이다.
# mouse_down = False
# mouse_x, mouse_y = 0, 0

# # 마우스 이벤트를 처리한다.
# # 마우스가 눌렀을 때, 아래와 같이 x, y 데이터를 저장한다.
# # 해당 값은 함수 외에서도 사용해야 하므로 global을 사용해 전역 변수로 지정해준다.
# def mouse_event(event, x, y, flags, param):
#     global mouse_down, mouse_x, mouse_y

#     if event == cv2.EVENT_LBUTTONDOWN:
#         mouse_down = True
#         mouse_x, mouse_y = x, y
#     elif event == cv2.EVENT_LBUTTONUP:
#         mouse_down = False

# # Draw Event 창에서 해당 콜 백 함수를 사용할 수 있도록 윈도우 생성 후 및 콜백 함수를 등록한다.
# cv2.namedWindow(window)
# cv2.setMouseCallback(window, mouse_event)

# # 이는 종료 전까지 계속 반복해서 사용되야 한다.
# # 따라서 while문을 사용해 무한 루프를 구성한다.
# while True:
#     # 이전의 데이터가 남아있으면 안되기 때문에, 새 이미지로 초기화한다.
#     screen = original.copy()

#     # 왼쪽 버튼 누르고 있을 때만 사각형 그림을 그리는 메서드이다.
#     # 만약 누르는 경우, 마우스의 위치에 검정 사각형을 그린다.
#     if mouse_down:
#         pt1 = (mouse_x, mouse_y)
#         pt2 = (mouse_x + 20, mouse_y + 20)
#         cv2.rectangle(screen, pt1, pt2, (0, 0, 0), thickness=-1)

#     # 이후, 그림을 그린 화면을 띄운다.
#     cv2.imshow(window, screen)

#     key = cv2.waitKey(10)
#     if key != -1:   # 아무 키나 누르면 while을 종료한다.
#         break       # 따라서 프로그램이 그대로 종료된다.

# cv2.destroyAllWindows()

#########################
#          10번          #
#########################  
# Lenna 이미지를 로드한다.
# image = cv2.imread('Lenna.jpg')

# # 마우스를 떼고 나면 그린 사각형이 사라진다.
# # 따라서 원본 이미지를 가지고 있어야 원본 이미지를 복구할 수 있다.
# original = image.copy()
# window = "Draw Event"

# # 마우스가 눌렸는지를 검사한다.
# # 마우스 눌렸는지 여부, x, y 값을 저장할 변수들이다.
# mouse_down = False
# mouse_x, mouse_y = 0, 0

# # 마우스 이벤트를 처리한다.
# # 마우스가 눌렀을 때, 아래와 같이 x, y 데이터를 저장한다.
# # 해당 값은 함수 외에서도 사용해야 하므로 global을 사용해 전역 변수로 지정해준다.
# def mouse_event(event, x, y, flags, param):
#     global mouse_down, mouse_x, mouse_y

#     if event == cv2.EVENT_RBUTTONDOWN:
#         mouse_down = True
#         mouse_x, mouse_y = x, y
#     elif event == cv2.EVENT_RBUTTONUP:
#         mouse_down = False

# # Draw Event 창에서 해당 콜 백 함수를 사용할 수 있도록 윈도우 생성 후 및 콜백 함수를 등록한다.
# cv2.namedWindow(window)
# cv2.setMouseCallback(window, mouse_event)

# # 이는 종료 전까지 계속 반복해서 사용되야 한다.
# # 따라서 while문을 사용해 무한 루프를 구성한다.
# while True:
#     # 이전의 데이터가 남아있으면 안되기 때문에, 새 이미지로 초기화한다.
#     screen = original.copy()

#     # 왼쪽 버튼 누르고 있을 때만 사각형 그림을 그리는 메서드이다.
#     # 만약 누르는 경우, 마우스의 위치에 검정 사각형을 그린다.
#     if mouse_down:
#         '''(function)
#             def circle(
#                 img: MatLike,
#                 center: Point,
#                 radius: int,
#                 color: Scalar,
#                 thickness: int = ...,
#                 lineType: int = ...,
#                 shift: int = ...
#             ) -> MatLike: ...
#         '''
#         # circle의 함수는 위와 같다. 위의 조건에 맞춰 변수를 설정한다.
#         pt1 = (mouse_x, mouse_y)
#         cv2.circle(screen, pt1, 5, (0, 255, 0), thickness=-1)

#     # 이후, 그림을 그린 화면을 띄운다.
#     cv2.imshow(window, screen)

#     key = cv2.waitKey(10)
#     if key != -1:   # 아무 키나 누르면 while을 종료한다.
#         break       # 따라서 프로그램이 그대로 종료된다.

# cv2.destroyAllWindows()


def onChange(value):  # 트랙바 콜백 함수: 밝기 업데이트
    pass

def onMouse(event, x, y, flags, param):  # 마우스 클릭 이벤트 처리
    global image, bar_name, title, value
    value = cv2.getTrackbarPos(bar_name, title)

    if event == cv2.EVENT_RBUTTONDOWN:
        if value < 245:
            value += 10
            cv2.setTrackbarPos(bar_name, title, value)  # 트랙바 위치 변경 → onChange 자동 호출

    elif event == cv2.EVENT_LBUTTONDOWN:
        if value > 10:
            value -= 10
            cv2.setTrackbarPos(bar_name, title, value)  # 트랙바 위치 변경 → onChange 자동 호출
    
    image[:] = value                             # 이미지 전체 밝기를 value로 설정
    cv2.imshow(title, image)

# 초기 이미지 생성
image = np.zeros((300, 500), np.uint8)
title = "Trackbar & Mouse Event"
bar_name = "Brightness"
cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)  # 트랙바 생성
cv2.setMouseCallback(title, onMouse)  # 마우스 이벤트 콜백 등록
cv2.imshow(title, image)

cv2.waitKey(0)
cv2.destroyAllWindows()