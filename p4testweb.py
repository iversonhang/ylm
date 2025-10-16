import streamlit as st
import random
from fractions import Fraction

# --- All your question generation functions go here ---
# (No changes are needed to the logic of these functions)

def generate_english_questions(num_questions=20):
    question_bank = [
        {"question": "I love drawing beautiful pictures, so {} is my favourite subject.", "options": ["Visual Arts", "Music", "P.E.", "Maths"], "answer": "Visual Arts", "explanation": "The sentence mentions a love for drawing, which corresponds to the subject Visual Arts."},
        {"question": "During {}, I like staying in the playground and sketching.", "options": ["the lesson", "lunchtime", "recess", "the exam"], "answer": "recess", "explanation": "'Recess' is the short break between classes, a suitable time for sketching in the playground."},
        {"question": "She was the {} of the painting competition and won a prize.", "options": ["winner", "loser", "player", "teacher"], "answer": "winner", "explanation": "A person who wins a competition is called the 'winner'."},
        {"question": "She won a beautiful {} and put it on the shelf.", "options": ["medal", "trophy", "certificate", "sticker"], "answer": "trophy", "explanation": "A 'trophy' is a cup or other decorative object awarded as a prize."},
        {"question": "When I am free, I also enjoy playing {}.", "options": ["sports", "games", "musical instruments", "chess"], "answer": "musical instruments", "explanation": "The text mentions a guitar and piano, which are types of musical instruments."},
        {"question": "He _____ his leg when he fell down yesterday.", "options": ["hurts", "hurt", "is hurting", "was hurt"], "answer": "hurt", "explanation": "'Yesterday' indicates the past tense. The past tense of 'hurt' is 'hurt'."},
        {"question": "My friends and I are going to the cinema {} Saturday.", "options": ["in", "at", "on", "by"], "answer": "on", "explanation": "We use the preposition 'on' for specific days of the week."},
        {"question": "There are many _____ in the library.", "options": ["book", "books", "book's", "books'"], "answer": "books", "explanation": "'Many' indicates a plural noun, so we use 'books'."},
        {"question": "Mary is {} than her sister.", "options": ["tall", "taller", "tallest", "more tall"], "answer": "taller", "explanation": "When comparing two people, we use the comparative form of the adjective ('taller')."},
        {"question": "Listen! Someone {} the piano.", "options": ["plays", "played", "is playing", "will play"], "answer": "is playing", "explanation": "'Listen!' suggests an action happening now, which requires the Present Continuous tense."},
        {"question": "How {} water is in the bottle? Not much.", "options": ["many", "much", "long", "often"], "answer": "much", "explanation": "We use 'much' for uncountable nouns like 'water'."},
        {"question": "A baker is a person {} bakes bread.", "options": ["which", "who", "where", "what"], "answer": "who", "explanation": "'Who' is a relative pronoun used for people."},
        {"question": "I was tired, {} I went to bed early.", "options": ["but", "so", "because", "or"], "answer": "so", "explanation": "'So' is used to show the result or consequence of an action."},
        {"question": "You can find a dictionary in the reference {} of the library.", "options": ["room", "section", "floor", "desk"], "answer": "section", "explanation": "A 'section' is a specific part of a larger area, like a library."},
        {"question": "The opposite of 'polite' is {}.", "options": ["impolite", "unpolite", "dispolite", "nonpolite"], "answer": "impolite", "explanation": "The prefix 'im-' is often used to form the opposite of words starting with 'p'."},
        {"question": "My father usually {} the newspaper in the morning.", "options": ["read", "reads", "is reading", "has read"], "answer": "reads", "explanation": "'Usually' indicates a regular habit (Present Simple). For a third-person singular subject (father), we add '-s' to the verb."},
        {"question": "What is the past tense of the verb 'buy'?", "options": ["buyed", "bought", "bring", "brought"], "answer": "bought", "explanation": "'Buy' is an irregular verb; its past tense is 'bought'."},
        {"question": "The students are excited {} the school picnic.", "options": ["of", "for", "with", "about"], "answer": "about", "explanation": "The correct preposition to use with 'excited' is 'about'."},
        {"question": "We live in a tall building. Our flat is on the tenth {}.", "options": ["level", "ground", "floor", "stage"], "answer": "floor", "explanation": "The different levels of a building are called 'floors'."},
        {"question": "Please be quiet. The baby {}.", "options": ["sleeps", "slept", "is sleeping", "was sleeping"], "answer": "is sleeping", "explanation": "The instruction 'Please be quiet' implies an action happening at this moment, requiring the Present Continuous tense."},
    ]
    return random.sample(question_bank, num_questions)

def generate_maths_questions(num_questions=20):
    questions = []
    for i in range(num_questions):
        q_type_index = i % 5
        if q_type_index == 0: # Divisibility
            num = random.randint(100, 500)
            divisor = random.choice([3, 5, 10])
            remainder = num % divisor
            add_needed = (divisor - remainder) % divisor
            answer = add_needed if add_needed != 0 else 0
            explanation = f"{num} ÷ {divisor} = {num//divisor} ... {remainder}\n需要加上 {add_needed} 才能被 {divisor} 整除。"
            questions.append({"question": f"{num} 最少要加上多少才能被 {divisor} 整除？", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 1: # Number Formation
            digits = random.sample(range(10), 5)
            while 0 not in digits: digits = random.sample(range(10), 5)
            non_zero_digits = sorted([d for d in digits if d != 0])
            first_digit = non_zero_digits[0]
            remaining_sorted = sorted([d for d in digits if d != first_digit])
            answer = int(str(first_digit) + "".join(map(str, remaining_sorted)))
            explanation = f"要組成最小的五位數，應把最小的非零數字放在最高位，其餘數字由小至大排列。"
            questions.append({"question": f"用 {', '.join(map(str, digits))} 組成一個最小的五位數。", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 2: # Factors
            num = random.randint(20, 80)
            factors = [i for i in range(1, num + 1) if num % i == 0]
            answer = len(factors)
            explanation = f"{num} 的因數是: {', '.join(map(str, factors))}\n所以共有 {answer} 個因數。"
            questions.append({"question": f"{num} 共有多少個因數？", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 3: # Word Problem (Multiplication)
            price = random.randint(15, 80)
            qty = random.randint(12, 30)
            answer = price * qty
            explanation = f"算式: {price} × {qty} = {answer} 元"
            questions.append({"question": f"每盒顏色筆售 {price} 元，老師買了 {qty} 盒，共需付多少元？", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 4: # Fraction Comparison
            d1 = random.randint(10, 20); n1 = random.randint(1, d1 - 1); n2 = random.randint(1, d1 - 1)
            d2 = random.randint(5, 15)
            while d1 == d2: d2 = random.randint(5, 15)
            n3 = random.randint(1, d2 - 1)
            fractions_str = [f"{n1}/{d1}", f"{n2}/{d1}", f"{n3}/{d2}"]
            random.shuffle(fractions_str)
            sorted_fractions = sorted(fractions_str, key=lambda f: eval(f))
            answer = ", ".join(sorted_fractions)
            explanation = f"先把同分母分數比較大小，然後再與異分母分數進行通分比較。"
            questions.append({"question": f"把下列分數由小至大排列: {', '.join(fractions_str)}", "answer": answer, "explanation": explanation})
    random.shuffle(questions)
    return questions

def generate_chinese_questions(num_questions=20):
    question_bank = [
        {"question": "仲恆（　）地練習跳遠，完全沒有發現自己已練習兩個多小時了。", "options": ["全神貫注", "得意忘形", "心直口快", "驚惶失措"], "answer": "全神貫注", "explanation": "「全神貫注」形容精神高度集中。"},
        {"question": "無論前路有多艱苦，我們也要懷着（　）的精神，克服重重難關。", "options": ["不屈不撓", "垂涎三尺", "一絲不苟", "得意忘形"], "answer": "不屈不撓", "explanation": "「不屈不撓」指在壓力和困難面前不屈服，表現堅強。"},
        {"question": "詠芝做任何事情都（　），每項細節也處理得極有條理。", "options": ["一絲不苟", "不厭其煩", "心直口快", "驚惶失措"], "answer": "一絲不苟", "explanation": "「一絲不苟」形容辦事認真，連最細微的地方也不放過。"},
        {"question": "小文跟朋友玩得（　），一時沒有留意交通燈號便過馬路。", "options": ["得意忘形", "全神貫注", "不屈不撓", "垂涎三尺"], "answer": "得意忘形", "explanation": "「得意忘形」形容因高興而失去常態。"},
        {"question": "這是我第一次品（　）婆婆自製的草莓果醬呢！", "options": ["嘗", "常", "賞"], "answer": "嘗", "explanation": "「品嘗」指嘗試、辨別味道。"},
        {"question": "小安把肉餡材料攪（　）均勻後，姐姐就開始包餃子了。", "options": ["拌", "伴", "絆"], "answer": "拌", "explanation": "「攪拌」指混合、拌和。"},
        {"question": "我們（　）盡力應付這次的考試。", "options": ["務須", "必須", "須臾"], "answer": "務須", "explanation": "「務須」是書面語，表示必須、一定要。"},
        {"question": "這本詞典十分（　），解釋詳盡，例子也十分生活化。", "options": ["使用", "實用", "食用"], "answer": "實用", "explanation": "「實用」指有實際用處。"},
        {"question": "以下哪個是「勤」字的部首？", "options": ["力", "堇", "廿"], "answer": "力", "explanation": "「勤」字的部首是「力」部。"},
        {"question": "「溫文爾雅」是形容一個人怎樣？", "options": ["態度溫和，舉止文雅", "性格暴躁", "身體溫暖", "非常有名"], "answer": "態度溫和，舉止文雅", "explanation": "這是一個褒義詞，用來稱讚人有禮貌和教養。"},
        {"question": "選出正確的句子。", "options": ["他不但品性純良，而且待人有禮。", "他不但品性純良，但待人有禮。", "他不但品性純良，所以待人有禮。"], "answer": "他不但品性純良，而且待人有禮。", "explanation": "「不但……而且……」用於表示遞進關係。"},
        {"question": "「疲倦」的近義詞是什麼？", "options": ["疲勞", "精神", "興奮", "勤奮"], "answer": "疲勞", "explanation": "「疲勞」和「疲倦」都指身體勞累的感覺。"},
        {"question": "「光明」的反義詞是什麼？", "options": ["黑暗", "光亮", "明亮", "晴朗"], "answer": "黑暗", "explanation": "「黑暗」與「光明」是相對的狀態。"},
        {"question": "「同學們一邊唱歌，一邊跳舞。」這是一個什麼複句？", "options": ["並列複句", "因果複句", "條件複句", "轉折複句"], "answer": "並列複句", "explanation": "「一邊……一邊……」表示兩個動作同時進行，屬於並列關係。"},
        {"question": "「即使天氣惡劣，我們（　）要準時上學。」", "options": ["也", "才", "就", "都"], "answer": "也", "explanation": "「即使……也……」是常用的關聯詞，表示假設關係。"},
        {"question": "「與其在這裏空等，（　）主動出擊尋找機會。」", "options": ["不如", "不如", "不但", "而且"], "answer": "不如", "explanation": "「與其……不如……」表示選擇關係，寧願選擇後者。"},
        {"question": "「驚弓之鳥」比喻受過驚嚇的人，遇到一點動靜就非常害怕。", "options": ["正確", "錯誤"], "answer": "正確", "explanation": "這是一個比喻用法，形容人過度驚慌。"},
        {"question": "「這件衣服的價錢不貴。」是哪種句子？", "options": ["敘述句", "疑問句", "感歎句", "祈使句"], "answer": "敘述句", "explanation": "敘述句用來陳述一件事情。"},
        {"question": "「小鳥在天上自由自在地飛翔。」句子中的「自由自在地」是什麼？", "options": ["名詞", "動詞", "形容詞", "副詞"], "answer": "副詞", "explanation": "副詞用來修飾動詞「飛翔」，形容飛翔的狀態。"},
        {"question": "請選出沒有錯別字的詞語。", "options": ["再接再厲", "再接再勵", "再接再厲", "再接再勵"], "answer": "再接再厲", "explanation": "正確的寫法是「再接再厲」，比喻繼續努力，毫不鬆懈。"},
    ]
    return random.sample(question_bank, num_questions)

def generate_gs_questions(num_questions=20):
    question_bank = [
        {"question": "佛朗明哥舞是哪個國家的特色舞蹈？", "options": ["西班牙", "泰國", "中國", "印度"], "answer": "西班牙", "explanation": "佛朗明哥舞是源於西班牙南部地區的一種藝術形式。"},
        {"question": "以下哪一個是中國具代表性的建築物？", "options": ["故宮", "法隆寺", "玉佛寺", "凡爾賽宮"], "answer": "故宮", "explanation": "北京故宮是中國明清兩代的皇家宮殿，是中國古代宮廷建築之精華。"},
        {"question": "七大洲中，面積最大和最小的大洲分別是？", "options": ["亞洲和大洋洲", "非洲和北美洲", "亞洲和南極洲", "北美洲和南美洲"], "answer": "亞洲和大洋洲", "explanation": "亞洲是世界上面積最大的洲，大洋洲是面積最小的洲。"},
        {"question": "地殼下，什麼東西流動會移動板塊，或會引致災害？", "options": ["岩漿", "地心", "化石", "沙礫"], "answer": "岩漿", "explanation": "地幔中的岩漿對流是推動板塊運動的主要動力。"},
        {"question": "沿江河生活的人，會居住在哪一種特色房屋？", "options": ["吊腳樓", "四合院", "土樓", "窑洞"], "answer": "吊腳樓", "explanation": "吊腳樓是一種適應南方多雨、潮濕氣候的建築，常見於沿江河地區。"},
        {"question": "清真寺的拱頂設計，是什麼宗教的建築特色？", "options": ["伊斯蘭教", "佛教", "基督教", "道教"], "answer": "伊斯蘭教", "explanation": "圓拱頂和宣禮塔是清真寺的標誌性建築特色。"},
        {"question": "為了免被太陽灼傷，沙漠地區的人會穿着什麼特色的衣服？", "options": ["寬鬆的長袍", "緊身的短褲", "厚重的毛衣", "防水的雨衣"], "answer": "寬鬆的長袍", "explanation": "寬鬆的長袍有助於通風散熱，並能遮擋陽光，防止皮膚灼傷。"},
        {"question": "圖中的民族居住在哪一種特色房屋？(蒙古包)", "options": ["蒙古包", "窑洞", "土樓", "冰屋"], "answer": "蒙古包", "explanation": "蒙古包是蒙古族等遊牧民族的傳統住房，易於拆搭和搬遷。"},
        {"question": "居住在極地的人，會利用什麼來建造特色房屋？", "options": ["冰塊", "木材", "泥土", "石頭"], "answer": "冰塊", "explanation": "因紐特人會利用冰塊建造冰屋（雪屋）作為臨時住所。"},
        {"question": "中國水墨畫的常見題材是什麼？", "options": ["山水、花鳥", "人物肖像", "抽象圖案", "城市建築"], "answer": "山水、花鳥", "explanation": "山水、花鳥、人物是中國水墨畫最主要的三大畫科。"},
        {"question": "火山爆發會對人類造成什麼損害？", "options": ["火山灰影響呼吸", "熔岩摧毀房屋", "引發地震", "以上皆是"], "answer": "以上皆是", "explanation": "火山爆發會噴出火山灰、熔岩，並可能引發地震和海嘯，造成多方面的嚴重損害。"},
        {"question": "中國傳統的彈撥樂器是什麼？", "options": ["琵琶", "笛", "鋼琴", "二胡"], "answer": "琵琶", "explanation": "琵琶是一種歷史悠久的彈撥樂器。笛是吹奏樂器，二胡是拉弦樂器。"},
        {"question": "哪一個大洋位於亞洲和美洲之間？", "options": ["太平洋", "大西洋", "印度洋", "北冰洋"], "answer": "太平洋", "explanation": "太平洋是世界上面積最大的海洋，位於亞洲、澳洲、北美洲和南美洲之間。"},
        {"question": "龍捲風是一種怎樣的自然災害？", "options": ["強烈旋轉的氣柱", "大量的降雪", "長時間的乾旱", "河水泛濫"], "answer": "強烈旋轉的氣柱", "explanation": "龍捲風是從雷暴雲底部伸展至地面的、猛烈旋轉的空氣柱。"},
        {"question": "四合院是中國哪個地區的傳統民居？", "options": ["華北地區 (如北京)", "華南地區", "西北地區", "西藏地區"], "answer": "華北地區 (如北京)", "explanation": "四合院是北京以及華北地區的傳統合院式建築。"},
        {"question": "哪種災害發生後，我們應該躲在堅固的桌子下？", "options": ["地震", "颱風", "水災", "火災"], "answer": "地震", "explanation": "在室內遇到地震時，應採取「伏地、掩護、穩住」的原則，躲在堅固的家具下。"},
        {"question": "以下哪項不是可再生能源？", "options": ["煤炭", "太陽能", "風能", "水力"], "answer": "煤炭", "explanation": "煤炭是化石燃料，屬於不可再生能源。太陽能、風能和水力是可再生能源。"},
        {"question": "中國的京劇臉譜中，紅色通常代表什麼性格？", "options": ["忠誠、英勇", "奸詐、多疑", "兇猛、粗魯", "神秘、莊嚴"], "answer": "忠誠、英勇", "explanation": "在京劇臉譜中，紅色一般代表忠勇、正直的人物，如關羽。"},
        {"question": "哪個節日有吃月餅和賞月的習俗？", "options": ["中秋節", "春節", "端午節", "清明節"], "answer": "中秋節", "explanation": "中秋節是華人社會的重要傳統節日，以月圓象徵人團圓。"},
        {"question": "在進行戶外活動時，遇到雷暴應該怎樣做？", "options": ["立即到室內躲避", "站在大樹下", "繼續在水中游泳", "跑到空曠的高地"], "answer": "立即到室內躲避", "explanation": "雷暴天氣時，應盡快進入堅固的建築物內，遠離樹木、金屬物體和水源，以防雷擊。"},
    ]
    return random.sample(question_bank, num_questions)


# --- Streamlit Web App Logic ---

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'quiz_questions' not in st.session_state:
    st.session_state.quiz_questions = []
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'subject' not in st.session_state:
    st.session_state.subject = ''

subjects = {
    "中文": generate_chinese_questions, 
    "英文": generate_english_questions,
    "數學": generate_maths_questions, 
    "常識": generate_gs_questions
}

def start_quiz(subject_name):
    """Sets up the state for a new quiz."""
    st.session_state.subject = subject_name
    st.session_state.quiz_questions = subjects[subject_name](20)
    st.session_state.user_answers = []
    st.session_state.current_question = 0
    st.session_state.page = 'quiz'

def display_start_page():
    st.title("四年級溫習程式")
    st.header("請選擇要練習的科目")

    for subject in subjects:
        if st.button(subject, key=subject):
            start_quiz(subject)
            st.rerun() # Rerun the script to show the quiz page

def display_quiz_page():
    st.title(f"科目：{st.session_state.subject}")
    
    idx = st.session_state.current_question
    q_data = st.session_state.quiz_questions[idx]
    
    st.subheader(f"第 {idx + 1} / 20 題")
    st.write(q_data['question'])

    with st.form(key=f"q_{idx}"):
        if 'options' in q_data:
            user_answer = st.radio("請選擇答案：", q_data['options'], index=None, key=f"radio_{idx}")
        else: # Math calculation
            user_answer = st.text_input("請輸入答案：", key=f"text_{idx}")
        
        submitted = st.form_submit_button("提交答案")
        if submitted:
            st.session_state.user_answers.append(user_answer)
            if st.session_state.current_question < 19:
                st.session_state.current_question += 1
            else:
                st.session_state.page = 'results'
            st.rerun()

def display_results_page():
    st.title("測驗結果")
    
    score = 0
    for i, q_data in enumerate(st.session_state.quiz_questions):
        user_ans = st.session_state.user_answers[i]
        correct_ans = q_data['answer']
        is_correct = (user_ans == correct_ans)
        if is_correct:
            score += 1

        with st.container(border=True):
            st.subheader(f"第 {i+1} 題：{q_data['question']}")
            if is_correct:
                st.success(f"你的答案：{user_ans} (正確 ✓)")
            else:
                st.error(f"你的答案：{user_ans} (錯誤 ✗)")
                st.info(f"正確答案：{correct_ans}")
            
            if 'explanation' in q_data:
                st.markdown(f"**詳解：** {q_data['explanation']}")

    st.header(f"總分：{score} / 20")

    if st.button("返回主選單"):
        st.session_state.page = 'start'
        st.rerun()

# --- Main App Router ---
if st.session_state.page == 'start':
    display_start_page()
elif st.session_state.page == 'quiz':
    display_quiz_page()
elif st.session_state.page == 'results':
    display_results_page()