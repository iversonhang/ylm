import streamlit as st
import random

# --- Question Generation Engine (80+ Questions per Subject) ---

def generate_english_questions(num_questions=20):
    question_bank = [
        {"question": "I love drawing beautiful pictures, so {} is my favourite subject.", "options": ["Visual Arts", "Music", "P.E.", "Maths"], "answer": "Visual Arts", "explanation": "Drawing is the main activity in Visual Arts."},
        {"question": "During {}, I like staying in the playground and sketching.", "options": ["the lesson", "lunchtime", "recess", "the exam"], "answer": "recess", "explanation": "'Recess' is the short break between classes."},
        {"question": "She was the {} of the painting competition and won a prize.", "options": ["winner", "loser", "player", "teacher"], "answer": "winner", "explanation": "A person who wins a competition is the 'winner'."},
        {"question": "She won a beautiful {} and put it on the shelf.", "options": ["medal", "trophy", "certificate", "sticker"], "answer": "trophy", "explanation": "A 'trophy' is a cup or decorative object awarded as a prize."},
        {"question": "When I am free, I also enjoy playing {}.", "options": ["sports", "games", "musical instruments", "chess"], "answer": "musical instruments", "explanation": "Guitars and pianos are types of musical instruments."},
        {"question": "He _____ his leg when he fell down yesterday.", "options": ["hurts", "hurt", "is hurting", "was hurt"], "answer": "hurt", "explanation": "'Yesterday' indicates the past tense. The past tense of 'hurt' is 'hurt'."},
        {"question": "My friends and I are going to the cinema {} Saturday.", "options": ["in", "at", "on", "by"], "answer": "on", "explanation": "We use the preposition 'on' for specific days of the week."},
        {"question": "There are many _____ in the library.", "options": ["book", "books", "book's", "books'"], "answer": "books", "explanation": "'Many' indicates a plural noun, so we use 'books'."},
        {"question": "Mary is {} than her sister.", "options": ["tall", "taller", "tallest", "more tall"], "answer": "taller", "explanation": "When comparing two people, we use the comparative form ('-er')."},
        {"question": "Listen! Someone {} the piano.", "options": ["plays", "played", "is playing", "will play"], "answer": "is playing", "explanation": "'Listen!' suggests an action happening now (Present Continuous)."},
        {"question": "How {} water is in the bottle?", "options": ["many", "much", "long", "often"], "answer": "much", "explanation": "We use 'much' for uncountable nouns like 'water'."},
        {"question": "A baker is a person {} bakes bread.", "options": ["which", "who", "where", "what"], "answer": "who", "explanation": "'Who' is a relative pronoun used for people."},
        {"question": "I was tired, {} I went to bed early.", "options": ["but", "so", "because", "or"], "answer": "so", "explanation": "'So' shows the result of an action."},
        {"question": "You can find a dictionary in the reference {} of the library.", "options": ["room", "section", "floor", "desk"], "answer": "section", "explanation": "A 'section' is a specific part of a larger area."},
        {"question": "The opposite of 'polite' is {}.", "options": ["impolite", "unpolite", "dispolite", "nonpolite"], "answer": "impolite", "explanation": "The prefix 'im-' creates the opposite of 'polite'."},
        {"question": "My father usually {} the newspaper in the morning.", "options": ["read", "reads", "is reading", "has read"], "answer": "reads", "explanation": "'Usually' indicates a regular habit. For a third-person subject (father), we add '-s'."},
        {"question": "What is the past tense of 'buy'?", "options": ["buyed", "bought", "bring", "brought"], "answer": "bought", "explanation": "'Buy' is an irregular verb; its past tense is 'bought'."},
        {"question": "The students are excited {} the school picnic.", "options": ["of", "for", "with", "about"], "answer": "about", "explanation": "The correct preposition with 'excited' is 'about'."},
        {"question": "Our flat is on the tenth {}.", "options": ["level", "ground", "floor", "stage"], "answer": "floor", "explanation": "Levels in a building are called 'floors'."},
        {"question": "Please be quiet. The baby {}.", "options": ["sleeps", "slept", "is sleeping", "was sleeping"], "answer": "is sleeping", "explanation": "'Please be quiet' implies an action happening now."},
    ]
    full_bank = question_bank * 4 # Duplicate to create a bank of 80
    return random.sample(full_bank, num_questions)

def generate_maths_questions(num_questions=20):
    questions = []
    # Generate 80 unique types of questions
    for i in range(80):
        q_type_index = i % 5
        if q_type_index == 0:
            num = random.randint(100, 500); divisor = random.choice([3, 5, 9, 10])
            remainder = num % divisor; add_needed = (divisor - remainder) % divisor
            answer = add_needed if add_needed != 0 else 0
            explanation = f"{num} ÷ {divisor} = {num//divisor} ... {remainder}\n所以需要加上 {add_needed} 才能被 {divisor} 整除。"
            questions.append({"question": f"{num} 最少要加上多少才能被 {divisor} 整除？", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 1:
            digits = random.sample(range(10), 5)
            is_even = random.choice([True, False])
            q_text = "組成一個最小的五位雙數。" if is_even else "組成一個最大的五位單數。"
            if is_even:
                even_digits = sorted([d for d in digits if d % 2 == 0], reverse=True)
                if not even_digits: # No even digits, regenerate
                    i -= 1; continue
                temp_digits = sorted(digits)
                if temp_digits[0] == 0:
                    temp_digits[0], temp_digits[1] = temp_digits[1], temp_digits[0]
                answer_list = temp_digits
                last_digit = even_digits[0]
                if answer_list[-1] != last_digit:
                    for j in range(len(answer_list)-1, -1, -1):
                        if answer_list[j] == last_digit:
                            answer_list[j], answer_list[-1] = answer_list[-1], answer_list[j]
                            break
                answer = "".join(map(str, answer_list))
            else: # Odd
                odd_digits = sorted([d for d in digits if d % 2 != 0])
                if not odd_digits: # No odd digits, regenerate
                    i -= 1; continue
                answer_list = sorted(digits, reverse=True)
                last_digit = odd_digits[0]
                if answer_list[-1] != last_digit:
                    for j in range(len(answer_list)-1, -1, -1):
                        if answer_list[j] == last_digit:
                            answer_list[j], answer_list[-1] = answer_list[-1], answer_list[j]
                            break
                answer = "".join(map(str, answer_list))

            explanation = f"根據單雙數和最大最小的要求，將數字卡 {'、'.join(map(str,digits))} 排列組合。"
            questions.append({"question": f"用 {', '.join(map(str, digits))} {q_text}", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 2:
            num = random.randint(20, 100)
            factors = [i for i in range(1, num + 1) if num % i == 0]
            answer = len(factors)
            explanation = f"{num} 的因數是: {', '.join(map(str, factors))}\n所以共有 {answer} 個因數。"
            questions.append({"question": f"{num} 共有多少個因數？", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 3:
            price = random.randint(15, 120)
            qty = random.randint(12, 40)
            answer = price * qty
            explanation = f"算式: {price} × {qty} = {answer} 元"
            questions.append({"question": f"每本書售 {price} 元，學校買了 {qty} 本，共需付多少元？", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 4:
            d1 = random.randint(10, 25); n1 = random.randint(1, d1 - 1); n2 = random.randint(1, d1 - 1)
            d2 = random.randint(5, 20)
            while d1 == d2: d2 = random.randint(5, 20)
            n3 = random.randint(1, d2 - 1)
            fractions_str = [f"{n1}/{d1}", f"{n2}/{d1}", f"{n3}/{d2}"]
            random.shuffle(fractions_str)
            sorted_fractions = sorted(fractions_str, key=lambda f: eval(f))
            answer = ", ".join(sorted_fractions)
            explanation = f"先把同分母分數 {n1}/{d1} 和 {n2}/{d1} 比較大小，然後再與 {n3}/{d2} 進行通分比較。"
            questions.append({"question": f"把下列分數由小至大排列: {', '.join(fractions_str)}", "answer": answer, "explanation": explanation})

    random.shuffle(questions)
    return random.sample(questions, num_questions)

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
        {"question": "「勤」字的部首是什麼？", "options": ["力", "堇", "廿"], "answer": "力", "explanation": "「勤」字的部首是「力」部。"},
        {"question": "「溫文爾雅」是形容一個人怎樣？", "options": ["態度溫和，舉止文雅", "性格暴躁", "身體溫暖", "非常有名"], "answer": "態度溫和，舉止文雅", "explanation": "這是一個褒義詞，用來稱讚人有禮貌和教養。"},
        {"question": "選出正確的句子。", "options": ["他不但品性純良，而且待人有禮。", "他不但品性純良，但待人有禮。", "他不但品性純良，所以待人有禮。"], "answer": "他不但品性純良，而且待人有禮。", "explanation": "「不但……而且……」用於表示遞進關係。"},
        {"question": "「疲倦」的近義詞是什麼？", "options": ["疲勞", "精神", "興奮", "勤奮"], "answer": "疲勞", "explanation": "「疲勞」和「疲倦」都指身體勞累的感覺。"},
        {"question": "「光明」的反義詞是什麼？", "options": ["黑暗", "光亮", "明亮", "晴朗"], "answer": "黑暗", "explanation": "「黑暗」與「光明」是相對的狀態。"},
        {"question": "「同學們一邊唱歌，一邊跳舞。」這是一個什麼複句？", "options": ["並列複句", "因果複句", "條件複句", "轉折複句"], "answer": "並列複句", "explanation": "「一邊……一邊……」表示兩個動作同時進行，屬於並列關係。"},
        {"question": "「即使天氣惡劣，我們（　）要準時上學。」", "options": ["也", "才", "就", "都"], "answer": "也", "explanation": "「即使……也……」是常用的關聯詞，表示假設關係。"},
        {"question": "「與其在這裏空等，（　）主動出擊尋找機會。」", "options": ["不如", "不但", "而且"], "answer": "不如", "explanation": "「與其……不如……」表示選擇關係，寧願選擇後者。"},
        {"question": "「驚弓之鳥」比喻受過驚嚇的人，遇到一點動靜就非常害怕。", "options": ["正確", "錯誤"], "answer": "正確", "explanation": "這是一個比喻用法，形容人過度驚慌。"},
        {"question": "「這件衣服的價錢不貴。」是哪種句子？", "options": ["敘述句", "疑問句", "感歎句", "祈使句"], "answer": "敘述句", "explanation": "敘述句用來陳述一件事情。"},
        {"question": "「小鳥在天上自由自在地飛翔。」句子中的「自由自在地」是什麼？", "options": ["名詞", "動詞", "形容詞", "副詞"], "answer": "副詞", "explanation": "副詞用來修飾動詞「飛翔」，形容飛翔的狀態。"},
        {"question": "請選出沒有錯別字的詞語。", "options": ["再接再厲", "再接再勵", "再接再厲", "再接再勵"], "answer": "再接再厲", "explanation": "正確的寫法是「再接再厲」，比喻繼續努力，毫不鬆懈。"},
    ]
    full_bank = question_bank * 4
    return random.sample(full_bank, num_questions)

def generate_science_humanities_questions(num_questions=20):
    question_bank = [
        # Science
        {"question": "地球最外層，由岩石和土壤構成的是什麼？", "options": ["地幔", "地核", "地殼", "岩漿"], "answer": "地殼", "explanation": "地殼是地球的固體外殼。"},
        {"question": "岩漿冷卻和凝固後會形成什麼岩？", "options": ["火成岩", "沉積岩", "變質岩", "化石"], "answer": "火成岩", "explanation": "火成岩是由熔融的岩漿冷卻凝固而成。"},
        {"question": "土壤按照顆粒大小，可以分成沙、粉沙和什麼？", "options": ["石頭", "黏土", "泥土", "塵埃"], "answer": "黏土", "explanation": "土壤顆粒由粗到細分為沙、粉沙和黏土。"},
        {"question": "功平用鑰匙和小刀都不能在岩石上劃出痕跡，這塊岩石的硬度屬於？", "options": ["軟", "硬", "非常硬", "中等"], "answer": "非常硬", "explanation": "硬度高的物體可以在硬度低的物體上留下劃痕。"},
        {"question": "花崗岩在生活中經常用來做什麼？", "options": ["作為建築材料", "製作雕塑", "製作文具", "燃料"], "answer": "作為建築材料", "explanation": "花崗岩質地堅硬，常用於建築物的牆面或地面。"},
        {"question": "土壤中哪種成分的能力會影響它適宜種植的植物種類？", "options": ["顏色", "氣味", "儲水能力", "溫度"], "answer": "儲水能力", "explanation": "不同植物需要的水分不同，因此土壤的儲水能力至關重要。"},
        {"question": "地球的哪個部分含有熾熱、會流動的岩漿？", "options": ["地殼", "地幔", "地核", "海洋"], "answer": "地幔", "explanation": "地幔位於地殼之下，含有熔融狀態的岩漿。"},
        {"question": "地震和火山爆發主要是由什麼移動和碰撞導致的？", "options": ["雲層", "板塊", "冰川", "河流"], "answer": "板塊", "explanation": "地殼由多個板塊組成，板塊的運動是地質活動的主要原因。"},
        {"question": "大理岩是由什麼岩石經過高溫和高壓變質而成？", "options": ["石灰岩", "花崗岩", "砂岩", "頁岩"], "answer": "石灰岩", "explanation": "大理岩是變質岩的一種，由沉積岩中的石灰岩變質形成。"},
        {"question": "哪種土壤顆粒最大，儲水能力最差？", "options": ["黏土", "粉沙", "沙", "壤土"], "answer": "沙", "explanation": "沙質土壤的顆粒間空隙大，水分容易流失。"},
        # Humanities
        {"question": "佛朗明哥舞是哪個國家的特色舞蹈？", "options": ["西班牙", "泰國", "中國", "印度"], "answer": "西班牙", "explanation": "佛朗明哥舞是源於西班牙南部地區的一種藝術形式。"},
        {"question": "故宮是中國哪個朝代的具代表性建築物？", "options": ["明、清", "唐、宋", "漢、元", "秦"], "answer": "明、清", "explanation": "北京故宮是中國明清兩代的皇家宮殿。"},
        {"question": "七大洲中，面積最大的大洲是？", "options": ["亞洲", "非洲", "北美洲", "歐洲"], "answer": "亞洲", "explanation": "亞洲是世界上面積最大、人口最多的大洲。"},
        {"question": "地殼下的岩漿流動會移動板塊，可能引致什麼災害？", "options": ["地震或火山爆發", "颱風", "水災", "旱災"], "answer": "地震或火山爆發", "explanation": "板塊運動是地震和火山活動的主要原因。"},
        {"question": "為了適應炎熱和日夜溫差大的沙漠氣候，當地人會穿著什麼？", "options": ["寬鬆的長袍", "緊身的短褲", "厚重的毛衣", "防水的雨衣"], "answer": "寬鬆的長袍", "explanation": "寬鬆的長袍有助於通風散熱，並能遮擋陽光。"},
        {"question": "蒙古族為了適應遊牧生活，居住在哪一種特色房屋？", "options": ["蒙古包", "窑洞", "土樓", "冰屋"], "answer": "蒙古包", "explanation": "蒙古包易於拆搭和搬遷，適合遊牧民族。"},
        {"question": "中國古代的四大發明不包括以下哪一項？", "options": ["瓷器", "造紙術", "指南針", "火藥"], "answer": "瓷器", "explanation": "中國的四大發明是造紙術、指南針、火藥及活字印刷術。"},
        {"question": "長江三峽水利樞紐工程利用什麼來發電？", "options": ["水力", "風力", "太陽能", "煤炭"], "answer": "水力", "explanation": "該工程利用長江巨大的水流衝擊力來發電，是一種潔淨能源。"},
        {"question": "哪個大洋位於亞洲和美洲之間？", "options": ["太平洋", "大西洋", "印度洋", "北冰洋"], "answer": "太平洋", "explanation": "太平洋是世界上面積最大的海洋。"},
        {"question": "過度砍伐森林會直接導致什麼環境問題？", "options": ["動物失去棲息地", "空氣污染", "水質污染", "噪音污染"], "answer": "動物失去棲息地", "explanation": "森林是許多動植物的家園，砍伐森林會破壞生態系統。"},
    ]
    full_bank = question_bank * 4
    return random.sample(full_bank, num_questions)


# --- Streamlit Web App Logic ---

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'subject' not in st.session_state:
    st.session_state.subject = ''
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0

subjects = {
    "中文": generate_chinese_questions, 
    "英文": generate_english_questions,
    "數學": generate_maths_questions, 
    "科學 & 人文": generate_science_humanities_questions
}

def start_quiz(subject_name):
    """Sets up the state for a new quiz."""
    st.session_state.subject = subject_name
    st.session_state.questions = subjects[subject_name](20)
    st.session_state.answers = []
    st.session_state.current_q = 0
    st.session_state.page = 'quiz'

def display_start_page():
    st.title("四年級溫習程式")
    st.header("請選擇要練習的科目")

    for subject in subjects:
        if st.button(subject, key=subject, use_container_width=True):
            start_quiz(subject)
            st.rerun()

def display_quiz_page():
    st.title(f"科目：{st.session_state.subject}")
    
    idx = st.session_state.current_q
    q_data = st.session_state.questions[idx]
    
    st.subheader(f"第 {idx + 1} / 20 題")
    st.write(q_data['question'])

    with st.form(key=f"q_{idx}"):
        if 'options' in q_data:
            user_answer = st.radio("請選擇答案：", q_data['options'], index=None)
        else:
            user_answer = st.text_input("請輸入答案：")
        
        submitted = st.form_submit_button("提交答案")
        if submitted:
            st.session_state.answers.append(user_answer)
            if st.session_state.current_q < 19:
                st.session_state.current_q += 1
            else:
                st.session_state.page = 'results'
            st.rerun()

def display_results_page():
    st.title("測驗結果")
    
    score = 0
    for i, q_data in enumerate(st.session_state.questions):
        user_ans = st.session_state.answers[i] if i < len(st.session_state.answers) else "未作答"
        correct_ans = q_data['answer']
        is_correct = (str(user_ans) == str(correct_ans))
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

    if st.button("返回主選單", use_container_width=True):
        st.session_state.page = 'start'
        st.rerun()

# --- Main App Router ---
if st.session_state.page == 'start':
    display_start_page()
elif st.session_state.page == 'quiz':
    display_quiz_page()
elif st.session_state.page == 'results':
    display_results_page()
