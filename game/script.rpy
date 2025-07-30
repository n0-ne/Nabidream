image white = Solid("#fff")
transform half_size: 
    zoom 0.5

label splashscreen:
    scene black
    pause 1.0
    show cometorbit logo srcf at truecenter, half_size with dissolve
    # show commetorbit logo srcf:
    #     zoom 0.33
    #     xcenter 0.25
    #     ycenter 0.19
    #     rotate 0
    #     linear 5.0 align (-0.2, -0.4) knot (0.15, -0.3)
    pause 1.0
    hide cometorbit logo srcf with fade
    return


# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")


# 여기에서부터 게임이 시작합니다.
label start:

    e "새로운 렌파이 게임을 만들었군요."

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    "Korean with spacing test"

    "한글 간격 테스트"

    "한글간격테스트 한글간격테스트 한글간격테스트 한글간격테스트 한글간격테스트 한글간격테스트 한글간격테스트 한글간격테스트 한글간격테스트 "

    return
