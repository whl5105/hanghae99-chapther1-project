# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.hanghae99_chapter1

docs = [
        {
            'id': 1,
            'title': '빌리 엘리어트',
            'desc': '가장 아름다운 도전! 탄광촌의 소년, 꿈으로 날아오르다!! 80년대 광부 대파업 시기의 영국 북부 탄광촌을 배경으로, 복싱 수업 중 우연히 접한 발레를 통해 자신의 재능을 발견하고 꿈을 이뤄가는 소년 ‘빌리’의 여정. 꿈을 위해 역경에 맞서 싸우는 어린 소년과 가족의 유쾌하고 가슴 따뜻한 이야기가 아름다운 음악, 환상적인 춤과 절묘하게 조화를 이루며 ‘이 시대 최고의 영국 뮤지컬’이라는 찬사를 받는 뮤지컬.'
        },
        {
            'id' : 2,
            'title' : '지킬 앤 하이드',
            'desc' : '지금 이 순간, 단 하나의 선택! 뮤지컬 <지킬앤하이드> 대한민국 뮤지컬 역사상 가장 압도적인 흥행작. 2004년 국내 초연 이후 누적 회차 1,410회, 평균 객석 점유율 95%, 누적 관객수 150만 명을 돌파한 그 누구도 넘볼 수 없는 명성! 대한민국 뮤지컬의 절대적 기준이자 살아있는 신화 <지킬앤하이드>가 오디컴퍼니 창립 20주년 세 번째 라인업으로 돌아온다. 당신의 심장을 뛰게 할 전율의 무대. 대중적으로 큰 사랑을 받고 있는 대표곡 "This is the Moment", 아름답고 서정적인 선율의 "Someone Like You", "Once Upon a Dream", 숨이 멎을 듯 강렬한 "Alive", "The Confrontation"까지! 한국인이 가장 사랑하는 작곡가 프랭크 와일드혼의 주옥같은 넘버와 함께 최고의 무대를 선보인다. 끝나지 않은 신화를 이어갈 레전드 캐스트. 지킬과 하이드를 넘나드는 고난도 연기력과 폭발적인 가창력으로 선과 악의 양면성을 보여줄 ‘지킬/하이드’역의 류정한, 홍광호, 신성록. 강렬한 매력으로 비극적 로맨스를 더할 ‘루시’역의 윤공주, 아이비, 선민. 변함없는 사랑으로 지킬의 곁을 지키는 ‘엠마’역의 조정은, 최수진, 민경아까지. 전설의 주역과 NEW 캐스트의 만남으로 다시 한번 흥행 열풍을 이어간다.'
        },
        {
            'id': 3,
            'title': '레베카',
            'desc': '더 이상 수식어가 필요 없는 작품, 대작 뮤지컬 ‘레베카’가 11월 16일 충무아트센터 대극장에서 막을 올린다. 스릴러의 거장 알프레드 히치콕의 동명의 영화로도 유명한 ‘레베카’는 성장하는 여성 캐릭터를 중심으로 한 감동적인 로맨스와 반전에 반전을 거듭하는 서스펜스, 깊은 감정 변화를 절묘하게 담아낸 강렬한 선율, 극의 긴장감을 높여주는 화려한 세트 등으로 관객과 평단의 찬사에 가까운 호평을 이끌며 작품이 가진 위력을 매 시즌 입증해 왔다. 뮤지컬 ‘레베카’는 한국 초연 당시 작품 전체를 한국 정서에 맞게 업그레이드해 원작자인 미하엘 쿤체(Michael Kunze)와 실베스터 르베이 (Sylvester Levay)로부터 “한국 무대가 세계 최고다”라는 극찬을 받았으며, 제7회 더 뮤지컬 어워즈’ 연출상을 비롯해 무대상, 조명상, 음향상 등 5개 핵심 부문에서 수상의 영예를 안은 바 있다.'
        },
        {
            'id': 4,
            'title': '노트르담 드 파리',
            'desc': '이야기는 파리의 음유시인 그랭구와르의 새로운 시대에 대한 서곡으로 시작한다. 파리 노트르담 대성당의 프롤로 주교는 꼽추 종지기 콰지모도를 충직한 종으로 삼고 있다. 한편 성당 앞 광장에 모여 사는 집시들. 그곳에 클로팽과 아름다운 여인 에스메랄다가 산다.'
        },
        {
            'id': 5,
            'title': '팬레터',
            'desc': '대한민국의 창작 뮤지컬. 2015 우수 크리에이터 발굴 지원 사업의 최우수 선정작. 1930년대를 배경으로 천재 작가 ‘이상’과 ‘김유정’, 그리고 경성 문인들의 모임인 ‘구인회’의 일화를 모티브로 하여 당시 문인들의 사랑과 예술을 그린 작품이다.'

        },
        {
            'id': 6,
            'title': '하데스타운',
            'desc': '토니어워즈 8관왕, 그래미어워즈 최고 뮤지컬 앨범상 수상 등 브로드웨이를 뜨겁게 달군 뮤지컬 <하데스타운>(프로듀서 신동원/제작 에스앤코)이 전 세계 최초 라이선스 한국어 공연으로 오는 8월 LG아트센터에서 막을 올린다. 공연 소식이 전해진 이후 “8월만 기다립니다 –인스타그램 e_xi****”, “놓칠 수 없는 초연, 무조건 봐야해! –인스타그램 sem****”등과 같이 뜨거운 관심이 쏟아졌으며 전 세계 뮤지컬 애호가들의 주목을 한 몸에 받고 있는 작품답게 국내 캐스팅에 대한 궁금증도 날로 높아져갔다. 그리고 마침내 <하데스타운> 최초 한국 공연 초연 멤버 12인이 공개됐다. 뮤즈와 인간의 혼혈로 절대적 위력을 지닌 음악적 재능의 소유자이자 봄을 불러올 노래를 만들고 있는 몽상가 오르페우스 역에는 조형균, 박강현, 시우민이 캐스팅됐으며 <하데스타운>의 시작과 끝을 알리고 관객들을 새로운 뮤지컬의 세계로 인도할 헤르메스 역에는 최재림과 강홍석이 나란히 이름을 올렸다. 익숙한 여신의 모습과는 거리가 먼, 장난기 많고 자비롭지만 때론 날카로운 면모를 보이는 페르세포네 역은 김선영과 박혜나가 맡았으며 스스로 새로운 길을 개척해나가는 강인하면서 독립적인 영혼을 지닌 오르페우스의 뮤즈 에우리디케는 김환희와 김수하가 그려낼 예정이다.'
        },
        {
            'id': 7,
            'title': '아가사',
            'desc': '추리소설 작가 아가사 크리스티 세상에 기록되지 않은 11일 간의 실종 “모두, 각자의 미궁 속으로, 사라져” 1926년 12월 3일 영국의 유명 추리소설 작가 ‘아가사 크리스티’가 스타일스 저택에서의 티타임 후 돌연 실종된다. 그로부터 27년 후 1953년 슬럼프에 빠진 천재 작가 ‘레이몬드 애쉬튼’이 반복되는 악몽의 실마리인 자신의 과거 기억을 찾으려 아가사 실종 사건을 다시 추적하기 시작하는데… 아가사가 사라지기 전 마지막으로 티타임을 가진 사람들과 그녀의 미완성 원고 『미궁 속의 티타임』을 본 유일한 증인 ‘레이몬드’ 아가사가 하이드로 호텔에서 만난 미스터리한 남자 ‘로이’ 그리고 모든 기억을 잃어버린 ‘아가사 크리스티’ 아가사 실종 열하루 그녀에게 무슨 일이 있었던 것일까?'
        },
        {
            'id': 8,
            'title': '엑스칼리버',
            'desc': '6세기 영국, 암흑의 시대. 분열된 영국은 각 영토의 왕들의 내전으로 피비린내로 가득하다. 색슨족의 침략까지 예언된 가운데, 드루이드(Druid)교의 마법사이자 예언가인 멀린은 엑스칼리버를 자신의 부와 권력, 복수를 얻는 수단으로만 사용해 온 무자비한 왕, 우더 펜드라곤을 죽이고, 혼돈의 시대를 벗어나게 할 새로운 왕 아더를 왕좌에 앉히기 위한 오래된 계획을 실행에 옮긴다.'
        },
        {
            'id': 9,
            'title': '시카고',
            'desc': '1920년대 시카고의 교도소를 배경으로 부정한 사법부의 재판과정을 풍자. 남편과 여동생의 불륜 현장을 목격하고 둘을 살해한 벨마 켈리와 애인이 자신을 속인 것에 분노하여 정부를 살해한 록시 하트가 주인공이다. 밥 파시가 오리지널 버전의 안무를 맡았고, 작품의 제작을 주도했다. 존 칸더(John Kander)와 프레드 옙 콤비가 작곡과 작사를 했다. 1924년에 시카고 트리뷴지에 났던 살인 사건 기사를 소재로 하며, 연극 <시카고>를 바탕으로 만들어졌다.'
        }
]

db.forTheCulture.insert_many(docs)
