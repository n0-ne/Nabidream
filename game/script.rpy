image white = Solid("#fff")
transform half_size: 
    zoom 0.5

label splashscreen:
    scene white
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
#define e = Character('아이린', color="#c8ffc8")
define j = Character("정원우", color="#c8ffc8")
define n = Character("나비연", color="#c8ffc8")
define h = Character("홍성영", color="#c8ffc8")
define s = Character("성유진", color="#c8ffc8")

# 여기에서부터 게임이 시작합니다.
label start:
    
    j "나는 정원우"
    n "나는 나비연"
    h "나는 홍성영"
    s "나는 성유진"

    scene bg arcade
    "오락실 데이트이다"
    #jump hockey

    return
