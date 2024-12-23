import random

# 놀이 카테고리와 추천할 놀이 목록
activities = {
    '게임 & 온라인 활동': [
        '모바일 게임 추천: Among Us, PUBG',
        '보드게임 추천: 카탄, 몬폴리',
        '친구들과 함께 할 수 있는 온라인 게임 추천: Fortnite, League of Legends',
        '소셜 미디어 챌린지: TikTok 댄스 챌린지 참여'
    ],
    '창의적인 활동': [
        'DIY 프로젝트: 방 꾸미기, 핸드메이드 액세서리 만들기',
        '미술 활동: 디지털 아트 그리기, 페인팅',
        '음악 만들기: GarageBand, FL Studio 사용해보기'
    ],
    '스포츠 & 운동': [
        '자전거 타기, 스케이트보드 타기',
        '배드민턴, 풋살',
        '홈트레이닝: 유튜브에서 홈트 영상 따라하기'
    ],
    '학습 & 자기계발': [
        '새로운 언어 배우기: Duolingo, Memrise',
        '코딩 배우기: Python, JavaScript 시작하기',
        '책 읽기: 청소년 소설 추천, 자기계발서 읽기'
    ],
    '소셜 활동': [
        '친구와 온라인 파티: Zoom으로 게임, 영화 관람',
        '친구들과 캠핑: 자연 탐험',
        '영화/드라마 추천: 넷플릭스 최신 콘텐츠'
    ]
}

# 사용자에게 카테고리 선택 받기
def get_category_choice():
    print("어떤 종류의 활동을 원하나요?")
    for idx, category in enumerate(activities.keys(), 1):
        print(f"{idx}. {category}")
    
    while True:
        try:
            choice = int(input("선택지 번호를 입력하세요: "))
            if 1 <= choice <= len(activities):
                return list(activities.keys())[choice - 1]
            else:
                print("올바른 번호를 입력해주세요.")
        except ValueError:
            print("번호는 숫자여야 합니다.")

# 카테고리 내에서 랜덤으로 활동 추천하기
def recommend_activity(category):
    activity_list = activities[category]
    recommended_activity = random.choice(activity_list)
    return recommended_activity

def main():
    category_choice = get_category_choice()
    recommended_activity = recommend_activity(category_choice)
    print(f"\n추천하는 활동: {recommended_activity}")

if __name__ == "__main__":
    main()
