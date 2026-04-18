"""Phase 3 translations EN + AR for advanced activities (IDs 46-85).
Robotique (46-57), Communication (58-63), Défis hacker (64-73), IA (74-85)."""

TRANSLATIONS_P3 = {

    # ═══ ROBOTIQUE (46-57) ═══
    46: {
        'en': {
            'objectif': "Two robots battle in a circular ring. Stay inside the white circle while pushing your opponent out. Use line sensors (edge detection) + ultrasound (enemy detection).",
            'materiel': ['2× Maqueen Lite', '2× ultrasonic sensors', 'Ring (white disc ~1m, black edge)'],
            'etapes': [
                "Wait for start signal (button A)",
                "Read line sensors — if edge detected, back up fast",
                "Read ultrasound — if enemy < 25 cm, charge at max speed",
                "Otherwise turn slowly to search for the enemy",
            ],
            'tip': "The black/white ring is key: black = edge. Print a 1m circle on paper or use black tape.",
            'defis': [
                {'level': 'easy', 'text': "Show the score (number of wins) with button B"},
                {'level': 'med', 'text': "Aggressive mode: charge even without detecting enemy after 5 seconds"},
                {'level': 'hard', 'text': "3-robot tournament: radio to count wins globally"},
            ],
        },
        'ar': {
            'objectif': "روبوتان يتواجهان في حلبة دائرية. ابقَ داخل الدائرة البيضاء بينما تدفع خصمك خارجها. استخدم مستشعرات الخط (الحافة) + الموجات فوق الصوتية (العدو).",
            'materiel': ['2× Maqueen Lite', '2× مستشعرات موجات فوق صوتية', 'حلبة (قرص أبيض ~1م، حافة سوداء)'],
            'etapes': [
                "انتظر إشارة البداية (الزر A)",
                "اقرأ مستشعرات الخط — إذا اكتُشفت الحافة، تراجع بسرعة",
                "اقرأ الموجات فوق الصوتية — إذا كان العدو < 25 سم، اندفع بأقصى سرعة",
                "وإلا فاستدر ببطء للبحث عن العدو",
            ],
            'tip': "الحلبة السوداء/البيضاء ضرورية: الأسود = الحافة. اطبع دائرة قطرها متر على ورق أو استخدم شريطاً أسود.",
            'defis': [
                {'level': 'easy', 'text': "اعرض النتيجة (عدد الانتصارات) بالزر B"},
                {'level': 'med', 'text': "الوضع الهجومي: اندفع حتى دون اكتشاف العدو بعد 5 ثوانٍ"},
                {'level': 'hard', 'text': "بطولة من 3 روبوتات: استخدم الراديو لحساب الانتصارات عالمياً"},
            ],
        },
    },
    47: {
        'en': {
            'objectif': "The robot autonomously traverses a maze using the right-hand rule: always turn right if possible, otherwise go straight, otherwise turn left.",
            'materiel': ['Maqueen Lite', 'Ultrasound', 'Cardboard/foam maze'],
            'etapes': [
                "Read distance ahead",
                "If wall ahead (<15cm), turn left",
                "Otherwise advance a bit, then check for right opening",
                "If opening on right, turn right",
            ],
            'tip': "The right-hand rule guarantees escape from any simply-connected maze (no islands).",
            'defis': [
                {'level': 'easy', 'text': "Show 🏁 on LED matrix at finish (button A)"},
                {'level': 'med', 'text': "Timer: display time to escape"},
                {'level': 'hard', 'text': "Dijkstra algorithm: record path, optimize on 2nd run"},
            ],
        },
        'ar': {
            'objectif': "يعبر الروبوت المتاهة ذاتياً باستخدام قاعدة اليد اليمنى: استدر يميناً دائماً إن أمكن، وإلا فامشِ مستقيماً، وإلا فاستدر يساراً.",
            'materiel': ['Maqueen Lite', 'موجات فوق صوتية', 'متاهة من الكرتون أو الفوم'],
            'etapes': [
                "اقرأ المسافة الأمامية",
                "إذا كان هناك جدار أمامك (<15سم)، استدر يساراً",
                "وإلا تقدم قليلاً ثم تحقق من وجود فتحة يمنى",
                "إذا كانت هناك فتحة يمنى، استدر يميناً",
            ],
            'tip': "قاعدة اليد اليمنى تضمن الخروج من أي متاهة متصلة بسيطة (بدون جزر).",
            'defis': [
                {'level': 'easy', 'text': "اعرض 🏁 على مصفوفة LED عند النهاية (الزر A)"},
                {'level': 'med', 'text': "المؤقت: اعرض وقت الخروج"},
                {'level': 'hard', 'text': "خوارزمية ديكسترا: سجل المسار، وحسّنه في المحاولة الثانية"},
            ],
        },
    },
    48: {
        'en': {
            'objectif': "Attach a marker to the robot and program it to draw: spiral, flower, star, or your name.",
            'materiel': ['Maqueen Lite', 'Marker (+ tape)', 'Large white sheet'],
            'etapes': [
                "Tape the marker at the robot's center (under the chassis)",
                "For a spiral: advance while turning slightly, increase the turn each lap",
                "For a flower: 8 petals, each = advance, turn 135°, return, turn 45°",
                "Test on scratch paper first",
            ],
            'tip': "Use light weight (thin marker) to avoid skidding. Adjust marker pressure with tape.",
            'defis': [
                {'level': 'easy', 'text': "Draw a perfect circle (fixed unequal speeds)"},
                {'level': 'med', 'text': "Draw a square with exactly 20 cm sides"},
                {'level': 'hard', 'text': "Program that writes your name's letters as motion"},
            ],
        },
        'ar': {
            'objectif': "ثبّت قلماً على الروبوت وبرمجه للرسم: لولب، زهرة، نجمة، أو اسمك.",
            'materiel': ['Maqueen Lite', 'قلم (+ شريط لاصق)', 'ورقة بيضاء كبيرة'],
            'etapes': [
                "ألصق القلم في مركز الروبوت (تحت الهيكل)",
                "للولب: تقدم مع الدوران قليلاً، وزد الدوران في كل دورة",
                "للزهرة: 8 بتلات، كل واحدة = تقدم، استدر 135°، ارجع، استدر 45°",
                "اختبر على ورقة تجريبية أولاً",
            ],
            'tip': "استخدم وزناً خفيفاً (قلم رفيع) لتجنب انزلاق الروبوت. اضبط ضغط القلم بالشريط اللاصق.",
            'defis': [
                {'level': 'easy', 'text': "ارسم دائرة مثالية (سرعتان ثابتتان مختلفتان)"},
                {'level': 'med', 'text': "ارسم مربعاً أضلاعه 20 سم بالضبط"},
                {'level': 'hard', 'text': "برنامج يكتب حروف اسمك بالحركة"},
            ],
        },
    },
    49: {
        'en': {
            'objectif': "The robot follows a line to a destination (double black line = stop), waits 3 seconds, then continues. Simulates a delivery.",
            'materiel': ['Maqueen Lite', 'Line with 1-2 perpendicular markers'],
            'etapes': [
                "Follow the line normally",
                "If both sensors read black for > 200ms, that's a marker",
                "Stop for 3 seconds, play a beep",
                "Resume following",
            ],
            'tip': "Marker = black line perpendicular to path, ~3cm thick. Both sensors detect it simultaneously.",
            'defis': [
                {'level': 'easy', 'text': "Show the delivery number at each stop (1, 2, 3...)"},
                {'level': 'med', 'text': "Add a servo that 'drops' an object at each stop"},
                {'level': 'hard', 'text': "Multi-destinations: 3 different markers (line counts), each = different action"},
            ],
        },
        'ar': {
            'objectif': "يتبع الروبوت خطاً إلى وجهة (خط أسود مزدوج = توقف)، ينتظر 3 ثوانٍ، ثم يكمل. محاكاة لعملية توصيل.",
            'materiel': ['Maqueen Lite', 'خط مع 1-2 علامة عمودية'],
            'etapes': [
                "اتبع الخط بشكل طبيعي",
                "إذا قرأ المستشعران الأسود لأكثر من 200 مللي ثانية، فهذه علامة",
                "توقف لمدة 3 ثوانٍ، وشغل صفيراً",
                "استأنف المتابعة",
            ],
            'tip': "العلامة = خط أسود عمودي على المسار، بسماكة ~3 سم. يكتشفها المستشعران في نفس الوقت.",
            'defis': [
                {'level': 'easy', 'text': "اعرض رقم التسليم عند كل توقف (1، 2، 3...)"},
                {'level': 'med', 'text': "أضف محرك سيرفو 'يسقط' جسماً عند كل توقف"},
                {'level': 'hard', 'text': "وجهات متعددة: 3 علامات مختلفة (عدد الخطوط)، كل منها = إجراء مختلف"},
            ],
        },
    },
    50: {
        'en': {
            'objectif': "Enhanced line follower: correction is proportional to error. The more the robot deviates, the stronger it corrects. Smooth and fast.",
            'materiel': ['Maqueen Lite', 'Track with black line'],
            'etapes': [
                "Compute error = left - right (−1, 0 or +1)",
                "Left speed = base − error × correction",
                "Right speed = base + error × correction",
                "Tune the correction constant (10-30) to find the sweet spot",
            ],
            'tip': "This is a P (proportional) controller. With 2 sensors, error has only 3 values, but the principle already works better than if/else.",
            'defis': [
                {'level': 'easy', 'text': "Increase base to 150: faster but less stable"},
                {'level': 'med', 'text': "Add a D (derivative) controller: kD × (err - prev_err)"},
                {'level': 'hard', 'text': "Race: 3 laps, time with and without proportional correction"},
            ],
        },
        'ar': {
            'objectif': "نسخة محسّنة من متابع الخط: التصحيح يتناسب مع الخطأ. كلما زاد انحراف الروبوت، زادت قوة التصحيح. سلس وسريع.",
            'materiel': ['Maqueen Lite', 'مسار بخط أسود'],
            'etapes': [
                "احسب الخطأ = يسار - يمين (−1، 0 أو +1)",
                "السرعة اليسرى = الأساس − الخطأ × التصحيح",
                "السرعة اليمنى = الأساس + الخطأ × التصحيح",
                "اضبط ثابت التصحيح (10-30) لإيجاد النقطة المثلى",
            ],
            'tip': "هذا متحكم P (نسبي). مع مستشعرين، للخطأ 3 قيم فقط، لكن المبدأ يعمل بالفعل أفضل من if/else.",
            'defis': [
                {'level': 'easy', 'text': "ارفع الأساس إلى 150: أسرع لكن أقل استقراراً"},
                {'level': 'med', 'text': "أضف متحكم D (تفاضلي): kD × (الخطأ - الخطأ_السابق)"},
                {'level': 'hard', 'text': "سباق: 3 دورات، قس الوقت مع وبدون التصحيح النسبي"},
            ],
        },
    },
    51: {
        'en': {
            'objectif': "3+ robots on the same radio group avoid each other and synchronize. Each broadcasts its position/speed; each adjusts based on others. Emergent behavior.",
            'materiel': ['3× Maqueen Lite', 'Large space'],
            'etapes': [
                "Each robot has a unique ID (0, 1, 2)",
                "Each broadcasts its status (alive + ultrasound distance) 5× per second",
                "If a neighbor is close (d < 15), slow down and turn",
                "Otherwise advance normally",
            ],
            'tip': "Distributed systems: no leader, just local rules. The result (coordination) emerges naturally.",
            'defis': [
                {'level': 'med', 'text': "Robots form a line (follow-the-leader)"},
                {'level': 'hard', 'text': "Circle: all robots arrange in equidistant circle"},
                {'level': 'hard', 'text': "Intruder detection: if a robot loses a neighbor > 5s, global alarm"},
            ],
        },
        'ar': {
            'objectif': "3+ روبوتات على نفس مجموعة الراديو تتجنب بعضها وتتزامن. كل منها يبث موقعه/سرعته؛ كل منها يتكيف مع الآخرين. سلوك ناشئ.",
            'materiel': ['3× Maqueen Lite', 'مساحة كبيرة'],
            'etapes': [
                "لكل روبوت معرف فريد (0، 1، 2)",
                "كل روبوت يبث حالته (حي + مسافة الموجات فوق الصوتية) 5× في الثانية",
                "إذا كان جار قريباً (d < 15)، أبطئ واستدر",
                "وإلا فتقدم بشكل طبيعي",
            ],
            'tip': "الأنظمة الموزعة: لا قائد، فقط قواعد محلية. النتيجة (التنسيق) تنشأ طبيعياً.",
            'defis': [
                {'level': 'med', 'text': "تشكل الروبوتات خطاً (اتبع القائد)"},
                {'level': 'hard', 'text': "دائرة: تترتب كل الروبوتات في دائرة متساوية الأبعاد"},
                {'level': 'hard', 'text': "كشف المتسلل: إذا فقد روبوت جاراً > 5 ثوانٍ، إنذار عام"},
            ],
        },
    },
    52: {
        'en': {
            'objectif': "Add a 1-servo arm that picks up small objects (light cubes, pom-poms). Coordinate motor + arm to pick up and drop.",
            'materiel': ['Maqueen Lite', 'Servo', 'Cardboard for the arm', 'Small cubes/pom-poms'],
            'etapes': [
                "Attach a cardboard arm to the servo",
                "Arm raised by default (90°)",
                "Advance to the object",
                "Lower the arm (10°) to pick up",
                "Reverse with the object to the destination",
                "Raise the arm to drop",
            ],
            'tip': "A simple cardboard hook works — no need for a gripper. Timing is everything.",
            'defis': [
                {'level': 'med', 'text': "Combine with ultrasound: auto-stop 5cm from object"},
                {'level': 'hard', 'text': "Smart excavator: follows line to object, picks it up, returns it"},
            ],
        },
        'ar': {
            'objectif': "أضف ذراعاً بمحرك سيرفو واحد لالتقاط أجسام صغيرة (مكعبات خفيفة، بومبومات). نسّق المحرك + الذراع لالتقاط وإنزال.",
            'materiel': ['Maqueen Lite', 'محرك سيرفو', 'كرتون للذراع', 'مكعبات/بومبومات صغيرة'],
            'etapes': [
                "ثبّت ذراعاً من الكرتون على محرك السيرفو",
                "الذراع مرفوعة افتراضياً (90°)",
                "تقدم إلى الجسم",
                "أنزل الذراع (10°) للالتقاط",
                "تراجع بالجسم إلى الوجهة",
                "ارفع الذراع لإسقاطه",
            ],
            'tip': "خطاف كرتوني بسيط يكفي — لا حاجة لماسك. التوقيت هو كل شيء.",
            'defis': [
                {'level': 'med', 'text': "ادمج مع الموجات فوق الصوتية: توقف تلقائي على بُعد 5 سم من الجسم"},
                {'level': 'hard', 'text': "حفار ذكي: يتبع خطاً إلى الجسم، يلتقطه، ويعيده"},
            ],
        },
    },
    53: {
        'en': {
            'objectif': "Simulate an autonomous vacuum: cover the whole area in pseudo-random path, avoid obstacles and falls (stairs).",
            'materiel': ['Maqueen Lite', 'Ultrasound', 'Bounded square space'],
            'etapes': [
                "Advance for 2 random seconds",
                "If obstacle → turn randomly left or right",
                "Repeat for 5 minutes",
                "Blue LEDs blink (active indicator)",
            ],
            'tip': "Roomba uses exactly this algorithm ('random walk'). No mapping needed — probability covers everything.",
            'defis': [
                {'level': 'med', 'text': "Detect table edge with line sensors (avoid falls)"},
                {'level': 'hard', 'text': "Targeted mode: if button B pressed, return to start (compass)"},
            ],
        },
        'ar': {
            'objectif': "محاكاة مكنسة كهربائية ذاتية: تغطي المنطقة كلها بمسار شبه عشوائي، تتجنب العقبات والسقوط (الدرج).",
            'materiel': ['Maqueen Lite', 'موجات فوق صوتية', 'مساحة مربعة محدودة'],
            'etapes': [
                "تقدم لـ 2 ثانية عشوائية",
                "إذا كان هناك عقبة → استدر عشوائياً يساراً أو يميناً",
                "كرر لمدة 5 دقائق",
                "المصابيح الزرقاء تومض (مؤشر النشاط)",
            ],
            'tip': "يستخدم Roomba هذه الخوارزمية بالضبط ('المشي العشوائي'). لا حاجة لرسم الخريطة — الاحتمالية تغطي كل شيء.",
            'defis': [
                {'level': 'med', 'text': "اكتشف حافة الطاولة بمستشعرات الخط (تجنب السقوط)"},
                {'level': 'hard', 'text': "الوضع المستهدف: عند الضغط على الزر B، عد إلى البداية (البوصلة)"},
            ],
        },
    },
    54: {
        'en': {
            'objectif': "The robot follows a line, stops at 4 'exhibits' (markers), plays a different melody, shows an emoji, then continues.",
            'materiel': ['Maqueen Lite', 'Track with 4 distinct markers (line count)'],
            'etapes': [
                "Follow the line",
                "Count encountered markers (count variable)",
                "At each marker: stop, play melody #count, show icon",
                "Pause 5 seconds then resume",
            ],
            'tip': "Use a melody array ['C-E-G', 'D-F-A', ...] indexed by count. Simple and readable.",
            'defis': [
                {'level': 'easy', 'text': "Different icon at each stop (Heart, Happy, Duck, House)"},
                {'level': 'med', 'text': "Voice announcement via buzzer: characteristic melody per exhibit"},
                {'level': 'hard', 'text': "Visit loop: auto-return to exhibit 1 after the 4th"},
            ],
        },
        'ar': {
            'objectif': "يتبع الروبوت خطاً، يتوقف عند 4 'معروضات' (علامات)، يعزف لحناً مختلفاً، يعرض إيموجي، ثم يكمل.",
            'materiel': ['Maqueen Lite', 'مسار مع 4 علامات مميزة (عدد الخطوط)'],
            'etapes': [
                "اتبع الخط",
                "احسب العلامات المواجهة (متغير count)",
                "عند كل علامة: توقف، اعزف اللحن رقم count، اعرض أيقونة",
                "انتظر 5 ثوانٍ ثم استأنف",
            ],
            'tip': "استخدم مصفوفة ألحان ['C-E-G'، 'D-F-A'، ...] مرقمة بـ count. بسيط وقابل للقراءة.",
            'defis': [
                {'level': 'easy', 'text': "أيقونة مختلفة عند كل توقف (قلب، سعيد، بطة، بيت)"},
                {'level': 'med', 'text': "إعلان صوتي عبر الصفارة: لحن مميز لكل معروضة"},
                {'level': 'hard', 'text': "حلقة الزيارة: عودة تلقائية إلى المعروضة 1 بعد الرابعة"},
            ],
        },
    },
    55: {
        'en': {
            'objectif': "A robot with personality: gets hungry every 30 seconds (sad face, slows down). Shine a light to 'feed' it. Happy, it zooms everywhere.",
            'materiel': ['Maqueen Lite', 'Flashlight or phone light'],
            'etapes': [
                "Global state: mood (0 = hungry, 100 = full)",
                "Every second: mood decreases by 1 (min 0)",
                "If mood < 30: sad icon, slow movements",
                "If mood > 70: happy icon, zoom",
                "If light > 100 for 3s: mood += 50",
            ],
            'tip': "Simple state machine. Kids love it — they really 'feed' their robot.",
            'defis': [
                {'level': 'easy', 'text': "Add a 'sleep' state if mood stays > 80 for 30s"},
                {'level': 'med', 'text': "Different sounds per mood: purr when happy, whine when hungry"},
                {'level': 'hard', 'text': "Grooming pet: washes (10s zigzag) when mood > 80"},
            ],
        },
        'ar': {
            'objectif': "روبوت بشخصية: يجوع كل 30 ثانية (وجه حزين، يبطئ). سلط ضوءاً لـ 'تطعمه'. سعيداً، يندفع في كل مكان.",
            'materiel': ['Maqueen Lite', 'مصباح يدوي أو ضوء الهاتف'],
            'etapes': [
                "الحالة العامة: mood (0 = جائع، 100 = شبعان)",
                "كل ثانية: ينقص mood بـ 1 (أدنى 0)",
                "إذا mood < 30: أيقونة حزينة، حركات بطيئة",
                "إذا mood > 70: أيقونة سعيدة، اندفاع",
                "إذا ضوء > 100 لـ 3 ثوانٍ: mood += 50",
            ],
            'tip': "آلة حالة بسيطة. الأطفال يعشقونها — يطعمون روبوتهم حقاً.",
            'defis': [
                {'level': 'easy', 'text': "أضف حالة 'نوم' إذا بقي mood > 80 لمدة 30 ثانية"},
                {'level': 'med', 'text': "أصوات مختلفة حسب الحالة: خرخرة سعيداً، أنين جائعاً"},
                {'level': 'hard', 'text': "حيوان أنيق: يغتسل (تعرج 10 ثوان) عندما mood > 80"},
            ],
        },
    },
    56: {
        'en': {
            'objectif': "Robot stays still at a passage point. If something passes (ultrasound < 50 cm), alarm: red LEDs + buzzer + scrolled message.",
            'materiel': ['Maqueen Lite', 'Ultrasound', 'A corridor / doorway'],
            'etapes': [
                "Wait 5s to allow exit",
                "Activate surveillance",
                "Read ultrasound continuously",
                "If < 50 cm: ALARM for 10s",
                "Return to surveillance",
            ],
            'tip': "Place at a door's foot facing the entrance. When someone passes, prank guaranteed.",
            'defis': [
                {'level': 'easy', 'text': "Change message: your name + '!!'"},
                {'level': 'med', 'text': "Silent mode: only LEDs + radio alerts another micro:bit"},
                {'level': 'hard', 'text': "Intrusion counter + on-demand display (button A)"},
            ],
        },
        'ar': {
            'objectif': "يبقى الروبوت ثابتاً في نقطة عبور. إذا مر شيء (موجات فوق صوتية < 50 سم)، إنذار: مصابيح حمراء + صفارة + رسالة متحركة.",
            'materiel': ['Maqueen Lite', 'موجات فوق صوتية', 'ممر / باب'],
            'etapes': [
                "انتظر 5 ثوانٍ للسماح بالخروج",
                "فعّل المراقبة",
                "اقرأ الموجات فوق الصوتية باستمرار",
                "إذا < 50 سم: إنذار لمدة 10 ثوانٍ",
                "عد إلى المراقبة",
            ],
            'tip': "ضعه عند قدم باب يواجه المدخل. عندما يمر أحد، مقلب مضمون.",
            'defis': [
                {'level': 'easy', 'text': "غير الرسالة: اسمك + '!!'"},
                {'level': 'med', 'text': "وضع صامت: مصابيح فقط + راديو ينبه micro:bit آخر"},
                {'level': 'hard', 'text': "عداد الاقتحام + عرض عند الطلب (الزر A)"},
            ],
        },
    },
    57: {
        'en': {
            'objectif': "2 robots race on a track. Each follows its line. First to 3 laps wins. Display of timer and winner.",
            'materiel': ['2× Maqueen Lite', 'Track (2 parallel paths or one with markers)'],
            'etapes': [
                "Each robot follows its line",
                "Count perpendicular markers (= laps)",
                "At 3 laps, broadcast 'win' via radio",
                "Other robot shows 'lost'; winner shows 'won'",
            ],
            'tip': "Use same radio group so each knows when the other finishes.",
            'defis': [
                {'level': 'med', 'text': "Time each lap (control.millis()) and show the best"},
                {'level': 'hard', 'text': "3-robot race: full ranking via radio"},
            ],
        },
        'ar': {
            'objectif': "روبوتان يتسابقان على مضمار. كل واحد يتبع خطه. أول من يصل إلى 3 دورات يفوز. عرض المؤقت والفائز.",
            'materiel': ['2× Maqueen Lite', 'مضمار (مساران متوازيان أو واحد بعلامات)'],
            'etapes': [
                "كل روبوت يتبع خطه",
                "احسب العلامات العمودية (= دورات)",
                "عند 3 دورات، بث 'فاز' عبر الراديو",
                "الروبوت الآخر يعرض 'خسر'؛ الفائز يعرض 'فاز'",
            ],
            'tip': "استخدم نفس مجموعة الراديو ليعرف كل منهما متى ينتهي الآخر.",
            'defis': [
                {'level': 'med', 'text': "وقّت كل دورة (control.millis()) واعرض الأفضل"},
                {'level': 'hard', 'text': "سباق 3 روبوتات: ترتيب كامل عبر الراديو"},
            ],
        },
    },

    # ═══ COMMUNICATION (58-63) ═══
    58: {
        'en': {
            'objectif': "Robot A sends a radio message every second. Robot B reacts: flashing LEDs, short beep. Simple, but it's the foundation of everything.",
            'materiel': ['2× Maqueen Lite'],
            'etapes': [
                "Both robots: radio.setGroup(7)",
                "Robot A: send 'ping' every second",
                "Robot B: on receive, flash + beep",
            ],
            'tip': "The radio group is like WiFi: 0-255 groups, each isolated. Choose a unique number.",
            'defis': [
                {'level': 'easy', 'text': "Change group to 99 and 100: verify no interference"},
                {'level': 'med', 'text': "Ping-pong: B replies 'pong' when receiving 'ping'"},
                {'level': 'hard', 'text': "Measure response delay (control.millis())"},
            ],
        },
        'ar': {
            'objectif': "الروبوت A يرسل رسالة راديو كل ثانية. الروبوت B يتفاعل: مصابيح وامضة، صفير قصير. بسيط، لكنه أساس كل شيء.",
            'materiel': ['2× Maqueen Lite'],
            'etapes': [
                "كلا الروبوتين: radio.setGroup(7)",
                "الروبوت A: أرسل 'ping' كل ثانية",
                "الروبوت B: عند الاستقبال، وميض + صفير",
            ],
            'tip': "مجموعة الراديو مثل WiFi: 256 مجموعة، كل واحدة معزولة. اختر رقماً فريداً.",
            'defis': [
                {'level': 'easy', 'text': "غير المجموعة إلى 99 و100: تحقق من عدم التداخل"},
                {'level': 'med', 'text': "بينغ-بونغ: B يرد 'pong' عند استقبال 'ping'"},
                {'level': 'hard', 'text': "قس تأخير الاستجابة (control.millis())"},
            ],
        },
    },
    59: {
        'en': {
            'objectif': "Tilt a micro:bit in your hand to drive the robot: tilt forward = advance, back = reverse, left/right = turn. Natural feel.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "Remote reads input.acceleration(X) and (Y)",
                "Send values via radio",
                "Robot receives → converts to motor speeds",
                "Tilt > 300 = significant inclination",
            ],
            'tip': "Accelerometer gives −1024 to +1024. ~30° tilt ≈ 500.",
            'defis': [
                {'level': 'med', 'text': "Turbo mode: shake remote = 2 seconds boost"},
                {'level': 'hard', 'text': "Deadzone: ignore small tilts (<100) to stay straight"},
            ],
        },
        'ar': {
            'objectif': "أمِل micro:bit في يدك لقيادة الروبوت: أمل إلى الأمام = تقدم، إلى الخلف = تراجع، يسار/يمين = استدارة. إحساس طبيعي.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "جهاز التحكم يقرأ input.acceleration(X) و(Y)",
                "أرسل القيم عبر الراديو",
                "الروبوت يستقبل → يحول إلى سرعات محركات",
                "إمالة > 300 = ميل كبير",
            ],
            'tip': "مقياس التسارع يعطي −1024 إلى +1024. إمالة ~30° ≈ 500.",
            'defis': [
                {'level': 'med', 'text': "وضع التوربو: هز جهاز التحكم = تعزيز لـ 2 ثانية"},
                {'level': 'hard', 'text': "منطقة ميتة: تجاهل الإمالات الصغيرة (<100) للبقاء مستقيماً"},
            ],
        },
    },
    60: {
        'en': {
            'objectif': "Type messages on a remote in Morse (button A = dot, B = dash). Robot receives and translates on the LED matrix.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "Remote: A = short, B = long, A+B = send letter",
                "Build a string '.-.--' progressively",
                "On send, transmit the string via radio",
                "Robot: decode morse → letter → display",
            ],
            'tip': "Morse dictionary: {'.-': 'A', '-...': 'B', '-.-.': 'C', ...}. Simple lookup.",
            'defis': [
                {'level': 'med', 'text': "Complete the morse alphabet (26 letters)"},
                {'level': 'hard', 'text': "Word mode: special separator (long AB) to compose words"},
            ],
        },
        'ar': {
            'objectif': "اكتب رسائل على جهاز التحكم بشيفرة مورس (الزر A = نقطة، B = شرطة). الروبوت يستقبل ويترجم على مصفوفة LED.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "جهاز التحكم: A = قصير، B = طويل، A+B = إرسال حرف",
                "ابنِ سلسلة '.-.--' تدريجياً",
                "عند الإرسال، انقل السلسلة عبر الراديو",
                "الروبوت: فك شيفرة مورس → حرف → اعرض",
            ],
            'tip': "قاموس مورس: {'.-': 'A', '-...': 'B', '-.-.': 'C', ...}. بحث بسيط.",
            'defis': [
                {'level': 'med', 'text': "أكمل الأبجدية المورسية (26 حرفاً)"},
                {'level': 'hard', 'text': "وضع الكلمات: فاصل خاص (AB طويل) لتأليف كلمات"},
            ],
        },
    },
    61: {
        'en': {
            'objectif': "The robot asks questions (different melodies). You answer via remote (A = yes, B = no). It counts correct answers.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "Robot sends 'Q1', 'Q2', etc. with associated sound",
                "You press A or B on remote",
                "Remote sends the answer",
                "Robot compares and increments score",
            ],
            'tip': "Prepare a table of correct answers in order. Kids play in teams with the quiz.",
            'defis': [
                {'level': 'med', 'text': "Time bonus: fast answers earn +2 points"},
                {'level': 'hard', 'text': "Multi-player: each with their remote, per-player score"},
            ],
        },
        'ar': {
            'objectif': "يطرح الروبوت أسئلة (ألحان مختلفة). تجيب عبر جهاز التحكم (A = نعم، B = لا). يحسب الإجابات الصحيحة.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "الروبوت يرسل 'Q1'، 'Q2'، إلخ مع صوت مرتبط",
                "اضغط A أو B على جهاز التحكم",
                "جهاز التحكم يرسل الإجابة",
                "الروبوت يقارن ويزيد النتيجة",
            ],
            'tip': "أعد جدول إجابات صحيحة بالترتيب. الأطفال يلعبون كفرق مع الاختبار.",
            'defis': [
                {'level': 'med', 'text': "مكافأة الوقت: الإجابات السريعة تكسب +2 نقطتين"},
                {'level': 'hard', 'text': "متعدد اللاعبين: كل لاعب بجهاز تحكمه، نتيجة لكل لاعب"},
            ],
        },
    },
    62: {
        'en': {
            'objectif': "Send radio messages encrypted with a simple Caesar cipher. Only the robot with the right key can read.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "Shared key (e.g. 3) known to both",
                "Sender: each letter → code+3 (A → D, B → E...)",
                "Receiver: code−3 to decrypt",
                "Wrong key: gibberish",
            ],
            'tip': "Caesar cipher = ancestral. Easy to crack (26 possibilities) but pedagogically perfect.",
            'defis': [
                {'level': 'med', 'text': "Change key every minute (control.millis() / 60000)"},
                {'level': 'hard', 'text': "Brute-force decryptor: try all 26 keys on a received message"},
            ],
        },
        'ar': {
            'objectif': "أرسل رسائل راديو مشفرة بشيفرة قيصر البسيطة. فقط الروبوت الذي لديه المفتاح الصحيح يمكنه القراءة.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "مفتاح مشترك (مثلاً 3) يعرفه كلاهما",
                "المرسل: كل حرف → رمز+3 (A → D، B → E...)",
                "المستقبل: رمز−3 لفك التشفير",
                "مفتاح خاطئ: هراء",
            ],
            'tip': "شيفرة قيصر = قديمة. سهلة الكسر (26 احتمالاً) لكنها مثالية تعليمياً.",
            'defis': [
                {'level': 'med', 'text': "غير المفتاح كل دقيقة (control.millis() / 60000)"},
                {'level': 'hard', 'text': "فك تشفير بالقوة الغاشمة: جرب كل المفاتيح الـ26 على رسالة مستقبلة"},
            ],
        },
    },
    63: {
        'en': {
            'objectif': "Robot plays Simon: shows a sequence of RGB colors. Players reproduce via their remotes. Sequence grows each successful round.",
            'materiel': ['2+ micro:bit', 'Maqueen Lite'],
            'etapes': [
                "Robot generates sequence [0, 1, 2, 3] (R/G/B/Y)",
                "Shows each color 500ms, pause 200ms",
                "Players must reproduce with their buttons",
                "Remotes send their clicks",
                "At end, score if correct, game over otherwise",
            ],
            'tip': "The game's intelligence is on the robot. Remotes are 'dumb': they just send clicks.",
            'defis': [
                {'level': 'med', 'text': "Different sound per color (C, D, E, F)"},
                {'level': 'hard', 'text': "Player mode: each takes turns, one who messes up loses"},
            ],
        },
        'ar': {
            'objectif': "الروبوت يلعب Simon: يعرض سلسلة ألوان RGB. اللاعبون يكررون عبر أجهزة تحكمهم. السلسلة تنمو مع كل جولة ناجحة.",
            'materiel': ['2+ micro:bit', 'Maqueen Lite'],
            'etapes': [
                "الروبوت يولد سلسلة [0، 1، 2، 3] (R/G/B/Y)",
                "يعرض كل لون 500 مللي ثانية، يتوقف 200 مللي ثانية",
                "يجب على اللاعبين التكرار بأزرارهم",
                "أجهزة التحكم ترسل ضغطاتهم",
                "في النهاية، نقاط إذا صحيح، انتهت اللعبة وإلا",
            ],
            'tip': "ذكاء اللعبة على الروبوت. أجهزة التحكم 'غبية': ترسل الضغطات فقط.",
            'defis': [
                {'level': 'med', 'text': "صوت مختلف لكل لون (C، D، E، F)"},
                {'level': 'hard', 'text': "وضع اللاعبين: كل واحد بدوره، من يخطئ يخسر"},
            ],
        },
    },

    # ═══ DÉFIS HACKER (64-73) ═══
    64: {
        'en': {
            'objectif': "Scan all 256 radio channels, 2 seconds each, display received messages. Like a hacker listening to the airwaves.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "Loop over groups 0 → 255",
                "For each group: radio.setGroup(g), listen 2s",
                "If message received, display g and the message",
                "Continue scanning",
            ],
            'tip': "At home you'll hear nothing. In class, you'll discover other students' micro:bits.",
            'defis': [
                {'level': 'med', 'text': "Log active groups (array shown on button B)"},
                {'level': 'hard', 'text': "Activity graph on LED matrix (histogram by group)"},
            ],
        },
        'ar': {
            'objectif': "امسح جميع قنوات الراديو الـ256، 2 ثانية لكل واحدة، اعرض الرسائل المستقبلة. مثل هاكر يستمع إلى موجات الأثير.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "كرر على المجموعات من 0 إلى 255",
                "لكل مجموعة: radio.setGroup(g)، استمع 2 ثانية",
                "إذا استُقبلت رسالة، اعرض g والرسالة",
                "تابع المسح",
            ],
            'tip': "في البيت لن تسمع شيئاً. في الفصل، ستكتشف أجهزة micro:bit لطلاب آخرين.",
            'defis': [
                {'level': 'med', 'text': "سجل المجموعات النشطة (مصفوفة تُعرض عند الزر B)"},
                {'level': 'hard', 'text': "رسم بياني للنشاط على مصفوفة LED (مدرج تكراري حسب المجموعة)"},
            ],
        },
    },
    65: {
        'en': {
            'objectif': "Robot sends a secret morse message via front LEDs. A second robot with photodiodes decodes it. Optical communication.",
            'materiel': ['2× Maqueen Lite'],
            'etapes': [
                "Sender: dot = 200ms ON, dash = 600ms ON, pause = 200ms OFF",
                "Encode the string 'SOS' = '... --- ...'",
                "Receiver: read input.lightLevel() 20x/sec",
                "Measure pulse durations, reconstruct dots/dashes",
            ],
            'tip': "Work in dim light so the receiver sees flashes clearly.",
            'defis': [
                {'level': 'med', 'text': "Receiver: actually decode and display message"},
                {'level': 'hard', 'text': "Steganography: hide a message in 'normal' blinking"},
            ],
        },
        'ar': {
            'objectif': "الروبوت يرسل رسالة مورس سرية عبر المصابيح الأمامية. روبوت ثانٍ مزود بفوتوديود يفك تشفيرها. اتصال بصري.",
            'materiel': ['2× Maqueen Lite'],
            'etapes': [
                "المرسل: نقطة = 200 مللي ثانية ON، شرطة = 600 مللي ثانية ON، توقف = 200 مللي ثانية OFF",
                "شفّر السلسلة 'SOS' = '... --- ...'",
                "المستقبل: اقرأ input.lightLevel() 20 مرة/ثانية",
                "قس مدة النبضات، أعد بناء النقاط/الشرطات",
            ],
            'tip': "اعمل في إضاءة خافتة ليرى المستقبل الومضات بوضوح.",
            'defis': [
                {'level': 'med', 'text': "المستقبل: فك التشفير فعلياً واعرض الرسالة"},
                {'level': 'hard', 'text': "إخفاء المعلومات: أخفِ رسالة في وميض 'عادي'"},
            ],
        },
    },
    66: {
        'en': {
            'objectif': "Still, the robot measures vibrations (accelerometer). If shake exceeds threshold, log, date, and alarm. Real instrumentation.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "Read total acceleration = sqrt(x² + y² + z²)",
                "Normal value ≈ 1024 (1g gravity)",
                "If deviation > 200, event detected",
                "Show a 5x5 graph of the largest shake",
            ],
            'tip': "Place the robot on a table. Tap gently nearby, observe detection. Hard knock = magnitude 7 quake.",
            'defis': [
                {'level': 'med', 'text': "Log events with timestamp (in memory, 100 max)"},
                {'level': 'hard', 'text': "Network: 3 coordinated seismograph robots, triangulation"},
            ],
        },
        'ar': {
            'objectif': "ثابتاً، يقيس الروبوت الاهتزازات (مقياس التسارع). إذا تجاوز الاهتزاز العتبة، سجل، أرّخ، وأنذر. أدوات حقيقية.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "اقرأ التسارع الكلي = sqrt(x² + y² + z²)",
                "القيمة العادية ≈ 1024 (جاذبية 1g)",
                "إذا كان الانحراف > 200، اكتشف الحدث",
                "اعرض رسماً 5×5 لأكبر اهتزاز",
            ],
            'tip': "ضع الروبوت على طاولة. انقر بلطف قرباً، راقب الكشف. ضربة قوية = زلزال مقدار 7.",
            'defis': [
                {'level': 'med', 'text': "سجل الأحداث بطابع زمني (في الذاكرة، 100 كحد أقصى)"},
                {'level': 'hard', 'text': "شبكة: 3 روبوتات رصد زلازل منسقة، تثليث"},
            ],
        },
    },
    67: {
        'en': {
            'objectif': "Robot 'listens' to music via its microphone (v2). Each volume peak = one beat. It dances to the rhythm (spin + LED flash).",
            'materiel': ['Maqueen Lite', 'micro:bit v2 (for microphone)', 'Rhythmic music'],
            'etapes': [
                "Read input.soundLevel() continuously",
                "If level exceeds a dynamic threshold, it's a beat",
                "On each beat: LED flash + short rotation",
                "Debounce: ignore beats too close (<200ms)",
            ],
            'tip': "Strong bass detects well. Subtle classical, less so.",
            'defis': [
                {'level': 'med', 'text': "Count beats over 10s → display BPM"},
                {'level': 'hard', 'text': "Sync multiple robots via radio: group choreography on beats"},
            ],
        },
        'ar': {
            'objectif': "الروبوت 'يستمع' للموسيقى عبر ميكروفونه (v2). كل قمة صوت = ضربة واحدة. يرقص على الإيقاع (دوران + وميض LED).",
            'materiel': ['Maqueen Lite', 'micro:bit v2 (للميكروفون)', 'موسيقى إيقاعية'],
            'etapes': [
                "اقرأ input.soundLevel() باستمرار",
                "إذا تجاوز المستوى عتبة ديناميكية، فهي ضربة",
                "عند كل ضربة: وميض LED + دوران قصير",
                "إزالة الارتداد: تجاهل الضربات القريبة جداً (<200 مللي ثانية)",
            ],
            'tip': "الباس القوي يُكتشف جيداً. الكلاسيكي الدقيق أقل.",
            'defis': [
                {'level': 'med', 'text': "احسب الضربات على مدى 10 ثوانٍ → اعرض BPM"},
                {'level': 'hard', 'text': "زامن روبوتات متعددة عبر الراديو: تصميم رقصات جماعية على الإيقاع"},
            ],
        },
    },
    68: {
        'en': {
            'objectif': "A robot 'tries' all combinations 000-999 on a servo (simulating a rotary lock). When it finds the right code (hardcoded), it shows 🏆.",
            'materiel': ['Maqueen Lite', 'Servo', 'Cardboard dial'],
            'etapes': [
                "Secret code defined in code (e.g. 314)",
                "Iterate from 0 to 999",
                "For each code: position servo at corresponding angle (0-360 → 0-180°)",
                "If code == secret: trophy",
                "Otherwise: next after 50ms",
            ],
            'tip': "Pedagogical and visual. 1000 tries at 50ms = 50s max. Perfect for teaching brute-force to teens.",
            'defis': [
                {'level': 'med', 'text': "Display current code during search"},
                {'level': 'hard', 'text': "Random secret code: really searches blind"},
            ],
        },
        'ar': {
            'objectif': "روبوت 'يحاول' كل التركيبات 000-999 على محرك سيرفو (محاكاة قفل دوار). عندما يجد الرمز الصحيح (مُبرمج مسبقاً)، يعرض 🏆.",
            'materiel': ['Maqueen Lite', 'محرك سيرفو', 'قرص من الكرتون'],
            'etapes': [
                "رمز سري معرّف في الكود (مثلاً 314)",
                "كرر من 0 إلى 999",
                "لكل رمز: ضع السيرفو في الزاوية المقابلة (0-360 → 0-180°)",
                "إذا رمز == سري: جائزة",
                "وإلا: التالي بعد 50 مللي ثانية",
            ],
            'tip': "تعليمي ومرئي. 1000 محاولة بـ 50 مللي ثانية = 50 ثانية كحد أقصى. مثالي لشرح القوة الغاشمة للمراهقين.",
            'defis': [
                {'level': 'med', 'text': "اعرض الرمز الحالي خلال البحث"},
                {'level': 'hard', 'text': "رمز سري عشوائي: يبحث فعلاً بشكل أعمى"},
            ],
        },
    },
    69: {
        'en': {
            'objectif': "10 'genomes' (move sequences) evolve. Each genome tested 3s, scored by distance. Best reproduce (crossover + mutation). 10 generations → optimized walk emerges.",
            'materiel': ['Maqueen Lite', 'Large space'],
            'etapes': [
                "Population: 10 arrays of 6 commands each",
                "Test each: run 6 commands, measure final distance",
                "Top 3: reproduce (mix) + random mutation",
                "New generation, repeat",
                "Show generation number on LED",
            ],
            'tip': "Heavy concept but magical to see: after 10 generations robot has found its best walk by evolution.",
            'defis': [
                {'level': 'hard', 'text': "Sophisticated fitness: longest straight line"},
                {'level': 'hard', 'text': "Show average score evolution per generation"},
            ],
        },
        'ar': {
            'objectif': "10 'جينومات' (تسلسلات حركة) تتطور. كل جينوم يُختبر 3 ثوانٍ، يُقيّم حسب المسافة. الأفضل يتكاثر (تصالب + طفرة). 10 أجيال → مشية مثلى ناشئة.",
            'materiel': ['Maqueen Lite', 'مساحة كبيرة'],
            'etapes': [
                "السكان: 10 مصفوفات بـ 6 أوامر لكل منها",
                "اختبر كل واحدة: نفّذ الأوامر الستة، قس المسافة النهائية",
                "الأفضل 3: تكاثر (مزج) + طفرة عشوائية",
                "جيل جديد، كرر",
                "اعرض رقم الجيل على LED",
            ],
            'tip': "مفهوم ثقيل لكنه سحري: بعد 10 أجيال وجد الروبوت أفضل مشية له بالتطور.",
            'defis': [
                {'level': 'hard', 'text': "لياقة متطورة: أطول خط مستقيم"},
                {'level': 'hard', 'text': "اعرض تطور متوسط النقاط في كل جيل"},
            ],
        },
    },
    70: {
        'en': {
            'objectif': "Robot rotates 360° slowly, measures ultrasound distance every 15°. Result: polar 'map' shown on 24 LEDs (approximation).",
            'materiel': ['Maqueen Lite', 'Ultrasound', 'Room with walls'],
            'etapes': [
                "Store an array of 24 distances",
                "Turn a bit, measure, back off; repeat 24 times",
                "Normalize: max distance → full brightness",
                "Display on 5x5 matrix (projection)",
            ],
            'tip': "Serious robotics (real SLAM) needs odometry + 2D map. Here we simplify: just a primitive 'laser scanner'.",
            'defis': [
                {'level': 'med', 'text': "Circular radar: LED toward farthest direction"},
                {'level': 'hard', 'text': "Export 24 values via radio to a 2nd micro:bit that logs them"},
            ],
        },
        'ar': {
            'objectif': "الروبوت يدور 360° ببطء، يقيس مسافة الموجات فوق الصوتية كل 15°. النتيجة: 'خريطة' قطبية تُعرض على 24 LED (تقريبية).",
            'materiel': ['Maqueen Lite', 'موجات فوق صوتية', 'غرفة بجدران'],
            'etapes': [
                "احفظ مصفوفة من 24 مسافة",
                "در قليلاً، قس، تراجع؛ كرر 24 مرة",
                "طبّع: أقصى مسافة → إضاءة كاملة",
                "اعرض على مصفوفة 5×5 (إسقاط)",
            ],
            'tip': "الروبوتات الجادة (SLAM حقيقي) تحتاج قياس المسافات + خريطة ثنائية الأبعاد. هنا نبسط: فقط 'ماسح ليزر' بدائي.",
            'defis': [
                {'level': 'med', 'text': "رادار دائري: LED باتجاه أبعد اتجاه"},
                {'level': 'hard', 'text': "صدّر 24 قيمة عبر الراديو إلى micro:bit ثانٍ يسجلها"},
            ],
        },
    },
    71: {
        'en': {
            'objectif': "Robot self-destructs (symbolically) if you don't check in regularly. Press A every 15s, otherwise: red LEDs, shrill buzzer, 'TERMINATED' message.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "On boot: timer at 15 seconds",
                "Button A resets the timer",
                "When timer hits 0: activation",
                "Activation mode: 10s cyclical alarm then total stop",
            ],
            'tip': "Classic embedded pattern (watchdog). Used in pacemakers, nuclear plants, etc.",
            'defis': [
                {'level': 'med', 'text': "Longer check-in (30s), but countdown from 5 gets urgent"},
                {'level': 'hard', 'text': "Check-in via shake (instead of button)"},
            ],
        },
        'ar': {
            'objectif': "الروبوت يدمر نفسه (رمزياً) إذا لم تسجل دخولك بانتظام. اضغط A كل 15 ثانية، وإلا: مصابيح حمراء، صفارة حادة، رسالة 'انتهى'.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "عند التشغيل: مؤقت 15 ثانية",
                "الزر A يعيد ضبط المؤقت",
                "عندما يصل المؤقت إلى 0: تفعيل",
                "وضع التفعيل: إنذار دوري 10 ثوانٍ ثم توقف كامل",
            ],
            'tip': "نمط embedded كلاسيكي (مراقب). يُستخدم في منظمات ضربات القلب، المحطات النووية، إلخ.",
            'defis': [
                {'level': 'med', 'text': "تسجيل أطول (30 ثانية)، لكن العد التنازلي من 5 يصبح عاجلاً"},
                {'level': 'hard', 'text': "تسجيل الدخول عبر الاهتزاز (بدلاً من الزر)"},
            ],
        },
    },
    72: {
        'en': {
            'objectif': "Run 2 versions of code (e.g. naive vs proportional line follower), time per lap, record. Rigorous statistics.",
            'materiel': ['Maqueen Lite', 'Circular track'],
            'etapes': [
                "Version A (button A): naive if/else, timed",
                "Version B (button B): proportional control",
                "Each run: timestamp and result in memory",
                "A+B: show average of each version",
            ],
            'tip': "Real scientific debate: 'my code is faster' → prove it with numbers!",
            'defis': [
                {'level': 'med', 'text': "Display standard deviation (time dispersion)"},
                {'level': 'hard', 'text': "Send data via radio to PC/tablet that graphs it"},
            ],
        },
        'ar': {
            'objectif': "شغّل نسختين من الكود (مثلاً متابع خط ساذج ضد نسبي)، وقّت لكل دورة، سجل. إحصائيات صارمة.",
            'materiel': ['Maqueen Lite', 'مضمار دائري'],
            'etapes': [
                "النسخة A (الزر A): if/else ساذج، موقَّت",
                "النسخة B (الزر B): تحكم نسبي",
                "كل تشغيل: طابع زمني ونتيجة في الذاكرة",
                "A+B: اعرض متوسط كل نسخة",
            ],
            'tip': "نقاش علمي حقيقي: 'كودي أسرع' → أثبته بالأرقام!",
            'defis': [
                {'level': 'med', 'text': "اعرض الانحراف المعياري (تشتت الوقت)"},
                {'level': 'hard', 'text': "أرسل البيانات عبر الراديو إلى PC/جهاز لوحي يرسمها"},
            ],
        },
    },
    73: {
        'en': {
            'objectif': "Use the magnetometer to create a compass. Shows N/S/E/W based on orientation. Robot obeys 'go north for 3 seconds'.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "On boot: calibrate magnetometer (rotate micro:bit in all directions)",
                "Read input.compassHeading() (0-359)",
                "0-45 or 315-359 = N, 45-135 = E, 135-225 = S, 225-315 = W",
                "When button A, go north: turn until heading<10, then advance 3s",
            ],
            'tip': "Avoid heavy metal elements (iron table) that disturb the magnetometer.",
            'defis': [
                {'level': 'med', 'text': "Arrow on LED matrix pointing north"},
                {'level': 'hard', 'text': "Go-to: program a trip (N 3s, E 2s, S 1s) that returns to start"},
            ],
        },
        'ar': {
            'objectif': "استخدم مقياس المغناطيسية لإنشاء بوصلة. يعرض N/S/E/W حسب الاتجاه. الروبوت يطيع 'اذهب شمالاً لمدة 3 ثوانٍ'.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "عند التشغيل: معايرة مقياس المغناطيسية (أدر micro:bit في كل الاتجاهات)",
                "اقرأ input.compassHeading() (0-359)",
                "0-45 أو 315-359 = N، 45-135 = E، 135-225 = S، 225-315 = W",
                "عند الزر A، اذهب شمالاً: استدر حتى heading<10، ثم تقدم 3 ثوانٍ",
            ],
            'tip': "تجنب العناصر المعدنية الثقيلة (طاولة حديد) التي تُشوش على مقياس المغناطيسية.",
            'defis': [
                {'level': 'med', 'text': "سهم على مصفوفة LED يشير إلى الشمال"},
                {'level': 'hard', 'text': "اذهب-إلى: برمج رحلة (N 3 ثوانٍ، E 2 ثانية، S 1 ثانية) تعود إلى البداية"},
            ],
        },
    },

    # ═══ IA (74-85) ═══
    74: {
        'en': {
            'objectif': "Introduction to CreateAI (createai.microbit.org) and Google Teachable Machine. Understand when to use each. No code for this activity — conceptual tutorial.",
            'materiel': ['Computer with browser', 'micro:bit connected (USB)'],
            'etapes': [
                "Open createai.microbit.org",
                "Empty project, welcome",
                "Understand: CreateAI trains models that run on the micro:bit itself",
                "For images / audio: teachablemachine.withgoogle.com (runs on laptop)",
            ],
            'tip': "Simple rule: if you want gesture recognition (tilt), CreateAI. If image or sound, Teachable Machine.",
            'defis': [
                {'level': 'easy', 'text': "Create accounts on both platforms (free)"},
                {'level': 'easy', 'text': "Explore public examples: gesture, image, audio"},
            ],
        },
        'ar': {
            'objectif': "مقدمة إلى CreateAI (createai.microbit.org) و Google Teachable Machine. افهم متى تستخدم كل منهما. لا كود في هذا النشاط — دليل مفاهيمي.",
            'materiel': ['حاسوب بمتصفح', 'micro:bit متصل (USB)'],
            'etapes': [
                "افتح createai.microbit.org",
                "مشروع فارغ، أهلاً",
                "افهم: CreateAI يدرّب نماذج تعمل على micro:bit نفسه",
                "للصور / الصوت: teachablemachine.withgoogle.com (يعمل على الحاسوب)",
            ],
            'tip': "قاعدة بسيطة: إذا أردت التعرف على الإيماءات (ميل)، CreateAI. إذا صورة أو صوت، Teachable Machine.",
            'defis': [
                {'level': 'easy', 'text': "أنشئ حسابات على المنصتين (مجاناً)"},
                {'level': 'easy', 'text': "استكشف الأمثلة العامة: إيماءة، صورة، صوت"},
            ],
        },
    },
    75: {
        'en': {
            'objectif': "Train CreateAI on 3 gestures (shake, circle, calm). Upload model to micro:bit. Robot performs an action per gesture. No buttons needed.",
            'materiel': ['Maqueen Lite', 'Computer', 'createai.microbit.org'],
            'etapes': [
                "On CreateAI: record 3 actions (30 samples each)",
                "Class 1: shake hard — action = turn",
                "Class 2: make circle in air — action = advance 2s",
                "Class 3: do nothing — action = stop",
                "Export to micro:bit, code the reactions",
            ],
            'tip': "30 samples per class minimum. Vary execution speed for a robust model.",
            'defis': [
                {'level': 'med', 'text': "Add a 4th class: 'tap the floor'"},
                {'level': 'hard', 'text': "Use subtle gestures instead of large motions (micro-gestures)"},
            ],
        },
        'ar': {
            'objectif': "درّب CreateAI على 3 إيماءات (هز، دائرة، هادئ). ارفع النموذج على micro:bit. الروبوت ينفذ إجراءً لكل إيماءة. بدون أزرار.",
            'materiel': ['Maqueen Lite', 'حاسوب', 'createai.microbit.org'],
            'etapes': [
                "في CreateAI: سجّل 3 إجراءات (30 عينة لكل واحد)",
                "الصنف 1: هز بقوة — الإجراء = استدر",
                "الصنف 2: اصنع دائرة في الهواء — الإجراء = تقدم 2 ثانية",
                "الصنف 3: لا شيء — الإجراء = توقف",
                "صدّر إلى micro:bit، برمج ردود الفعل",
            ],
            'tip': "30 عينة لكل صنف كحد أدنى. نوّع سرعة التنفيذ لنموذج متين.",
            'defis': [
                {'level': 'med', 'text': "أضف صنفاً رابعاً: 'اضرب الأرض'"},
                {'level': 'hard', 'text': "استخدم إيماءات دقيقة بدلاً من حركات كبيرة (إيماءات صغرى)"},
            ],
        },
    },
    76: {
        'en': {
            'objectif': "CreateAI model that detects a fall (sudden acceleration then stillness). Useful for elderly, but here for a robot that 'calls for help'.",
            'materiel': ['Maqueen Lite', 'createai.microbit.org'],
            'etapes': [
                "Class 1: normal operation (walk, turn)",
                "Class 2: fall (simulation: shake then place down)",
                "Train + test + export",
                "On fall detection: alarm + SOS radio",
            ],
            'tip': "Simulate fall by dropping robot 20cm above soft surface. Do it 30 times.",
            'defis': [
                {'level': 'med', 'text': "Timer: after 10s without movement, relaunch alert"},
                {'level': 'hard', 'text': "Network: 2 robots monitor their respective masters"},
            ],
        },
        'ar': {
            'objectif': "نموذج CreateAI يكشف السقوط (تسارع مفاجئ ثم سكون). مفيد للمسنين، هنا لروبوت 'يستدعي المساعدة'.",
            'materiel': ['Maqueen Lite', 'createai.microbit.org'],
            'etapes': [
                "الصنف 1: تشغيل عادي (مشي، استدارة)",
                "الصنف 2: سقوط (محاكاة: هز ثم وضع)",
                "درّب + اختبر + صدّر",
                "عند كشف السقوط: إنذار + SOS راديو",
            ],
            'tip': "حاكِ السقوط بإسقاط الروبوت 20 سم فوق سطح ناعم. افعل ذلك 30 مرة.",
            'defis': [
                {'level': 'med', 'text': "مؤقت: بعد 10 ثوانٍ بدون حركة، أعد إطلاق التنبيه"},
                {'level': 'hard', 'text': "شبكة: روبوتان يراقبان أسيادهما المعنيين"},
            ],
        },
    },
    77: {
        'en': {
            'objectif': "CreateAI model that counts jumping jacks, squats, and rest. During workout, the robot encourages (LEDs, sounds) every 10 reps.",
            'materiel': ['Maqueen Lite worn or held', 'createai.microbit.org'],
            'etapes': [
                "3 classes: jumping jack, squat, rest",
                "30 samples per exercise (vary pace)",
                "Count consecutive detections",
                "Every 10: bravo!",
            ],
            'tip': "Hold robot in hand or pocket. Models capture whole-body movements well.",
            'defis': [
                {'level': 'med', 'text': "Personal goal: button A to start, auto-stop at 50"},
                {'level': 'hard', 'text': "Voice coach: different encouragement every 5 reps"},
            ],
        },
        'ar': {
            'objectif': "نموذج CreateAI يحسب قفز النط، القرفصاء، والراحة. خلال التمرين، الروبوت يشجع (LED، أصوات) كل 10 تكرارات.",
            'materiel': ['Maqueen Lite محمولاً أو ممسوكاً', 'createai.microbit.org'],
            'etapes': [
                "3 أصناف: قفز النط، قرفصاء، راحة",
                "30 عينة لكل تمرين (نوّع الإيقاع)",
                "احسب الاكتشافات المتتالية",
                "كل 10: برافو!",
            ],
            'tip': "امسك الروبوت في يدك أو جيبك. النماذج تلتقط حركات الجسم الكامل جيداً.",
            'defis': [
                {'level': 'med', 'text': "هدف شخصي: الزر A للبدء، توقف تلقائي عند 50"},
                {'level': 'hard', 'text': "مدرب صوتي: تشجيع مختلف كل 5 تكرارات"},
            ],
        },
    },
    78: {
        'en': {
            'objectif': "Robot climbs on your shoulder (micro:bit on shoulder, in strap). Train 'good posture' vs 'slouched'. Detects bad posture and alerts.",
            'materiel': ['Maqueen Lite', 'Strap to hold micro:bit on shoulder', 'createai.microbit.org'],
            'etapes': [
                "Class 1: sitting upright, shoulders back",
                "Class 2: slouched, shoulders forward",
                "Variation: stand up, walk",
                "On bad posture > 10s: red LEDs",
            ],
            'tip': "Walk in class: capture 'standing', 'sitting', 'walking'. Model learns your life, not just captures.",
            'defis': [
                {'level': 'med', 'text': "Stats: % of time in good posture over 1 hour"},
                {'level': 'hard', 'text': "Progressive reminder: soft light → light sound → alarm"},
            ],
        },
        'ar': {
            'objectif': "الروبوت يصعد على كتفك (micro:bit على الكتف، في حمالة). درّب 'وضعية جيدة' ضد 'مترهل'. يكشف الوضعية السيئة وينبه.",
            'materiel': ['Maqueen Lite', 'حمالة لحمل micro:bit على الكتف', 'createai.microbit.org'],
            'etapes': [
                "الصنف 1: جالس منتصباً، الكتفان للخلف",
                "الصنف 2: مترهل، الكتفان للأمام",
                "تنويع: قف، امشِ",
                "عند وضعية سيئة > 10 ثوانٍ: مصابيح حمراء",
            ],
            'tip': "امشِ في الفصل: التقط 'وقوف'، 'جلوس'، 'مشي'. النموذج يتعلم حياتك، ليس فقط لقطات.",
            'defis': [
                {'level': 'med', 'text': "إحصائيات: % من الوقت في وضعية جيدة على مدى ساعة"},
                {'level': 'hard', 'text': "تذكير تدريجي: ضوء ناعم → صوت خفيف → إنذار"},
            ],
        },
    },
    79: {
        'en': {
            'objectif': "Teachable Machine 'Pose model' detects where your face is (left/center/right) via webcam. Computer sends command to robot which turns to follow you.",
            'materiel': ['Maqueen Lite', 'Computer + webcam', 'teachablemachine.withgoogle.com'],
            'etapes': [
                "On Teachable: create 'Pose' project",
                "3 classes: face_left, face_center, face_right (30 photos each)",
                "Train, download tfjs model",
                "Create an HTML page that runs the model",
                "Page sends detected class to micro:bit via serial/radio → robot",
            ],
            'tip': "Architecture: webcam → laptop → radio → robot. Latency < 500ms possible.",
            'defis': [
                {'level': 'hard', 'text': "Zoom: the bigger your face (closer), the more robot backs up"},
                {'level': 'hard', 'text': "Emotion detection (Teachable Image) → robot reaction"},
            ],
        },
        'ar': {
            'objectif': "نموذج Teachable Machine 'Pose' يكشف مكان وجهك (يسار/وسط/يمين) عبر كاميرا الويب. الحاسوب يرسل الأمر إلى الروبوت الذي يستدير ليتبعك.",
            'materiel': ['Maqueen Lite', 'حاسوب + كاميرا ويب', 'teachablemachine.withgoogle.com'],
            'etapes': [
                "في Teachable: أنشئ مشروع 'Pose'",
                "3 أصناف: face_left، face_center، face_right (30 صورة لكل واحد)",
                "درّب، حمّل نموذج tfjs",
                "أنشئ صفحة HTML تشغل النموذج",
                "الصفحة ترسل الصنف المكتشف إلى micro:bit عبر serial/راديو → روبوت",
            ],
            'tip': "المعمارية: كاميرا ويب → حاسوب → راديو → روبوت. تأخير < 500 مللي ثانية ممكن.",
            'defis': [
                {'level': 'hard', 'text': "تكبير: كلما كبر وجهك (اقترب)، تراجع الروبوت أكثر"},
                {'level': 'hard', 'text': "كشف العاطفة (Teachable Image) → رد فعل الروبوت"},
            ],
        },
    },
    80: {
        'en': {
            'objectif': "Teachable Machine Image: recognizes 4 colored objects (red, blue, yellow, green). Robot moves to the corresponding zone.",
            'materiel': ['Maqueen Lite', 'Computer + webcam', '4 colored cards for zones'],
            'etapes': [
                "Teachable model: 4 photo classes (each object at 30 angles)",
                "Run model live in browser",
                "Show object to camera → class detected → radio to robot",
                "Robot: go to corresponding colored zone",
            ],
            'tip': "Perfect for miniature industrial sorting project. Kids love it — real factory robots.",
            'defis': [
                {'level': 'hard', 'text': "Add shapes (circle, square) besides colors"},
                {'level': 'hard', 'text': "After collection, robot gives a short report: how many of each"},
            ],
        },
        'ar': {
            'objectif': "Teachable Machine Image: يتعرف على 4 أجسام ملونة (أحمر، أزرق، أصفر، أخضر). الروبوت ينتقل إلى المنطقة المقابلة.",
            'materiel': ['Maqueen Lite', 'حاسوب + كاميرا ويب', '4 بطاقات ملونة للمناطق'],
            'etapes': [
                "نموذج Teachable: 4 أصناف صور (كل جسم بـ 30 زاوية)",
                "شغّل النموذج مباشرة في المتصفح",
                "أظهر الجسم للكاميرا → اكتُشف الصنف → راديو إلى الروبوت",
                "الروبوت: اذهب إلى المنطقة الملونة المقابلة",
            ],
            'tip': "مثالي لمشروع فرز صناعي مصغر. الأطفال يعشقونها — روبوتات مصنع حقيقية.",
            'defis': [
                {'level': 'hard', 'text': "أضف أشكالاً (دائرة، مربع) بالإضافة إلى الألوان"},
                {'level': 'hard', 'text': "بعد الجمع، يعطي الروبوت تقريراً قصيراً: كم من كل لون"},
            ],
        },
    },
    81: {
        'en': {
            'objectif': "Teachable Machine Audio: train 'go', 'stop', 'dance', 'ambient noise'. Speak — robot obeys. Works in French, Arabic, any language.",
            'materiel': ['Maqueen Lite', 'Computer + mic', 'teachablemachine.withgoogle.com'],
            'etapes': [
                "Teachable Audio: 4 classes",
                "30 audio samples per class (say each multiple times)",
                "Train, export",
                "Browser listens through mic and sends class to robot",
            ],
            'tip': "Short distinct words. 'go' and 'stop' will confuse less than 'come' and 'stop'.",
            'defis': [
                {'level': 'med', 'text': "Add 'horn' command that plays a melody"},
                {'level': 'hard', 'text': "Bilingual model: commands in French and Arabic"},
            ],
        },
        'ar': {
            'objectif': "Teachable Machine Audio: درّب على 'اذهب'، 'قف'، 'ارقص'، 'ضجيج محيط'. تكلم — الروبوت يطيع. يعمل بالفرنسية، العربية، أي لغة.",
            'materiel': ['Maqueen Lite', 'حاسوب + ميكروفون', 'teachablemachine.withgoogle.com'],
            'etapes': [
                "Teachable Audio: 4 أصناف",
                "30 عينة صوتية لكل صنف (قل كل واحدة عدة مرات)",
                "درّب، صدّر",
                "المتصفح يستمع عبر الميكروفون ويرسل الصنف إلى الروبوت",
            ],
            'tip': "كلمات قصيرة مميزة. 'اذهب' و'قف' ستتشوش أقل من 'تعال' و'قف'.",
            'defis': [
                {'level': 'med', 'text': "أضف أمر 'بوق' يعزف لحناً"},
                {'level': 'hard', 'text': "نموذج ثنائي اللغة: أوامر بالفرنسية والعربية"},
            ],
        },
    },
    82: {
        'en': {
            'objectif': "Teachable Audio: learn 3 patterns (1 clap, 2 claps, 3 claps). Each pattern = different action. Open/close lights, turn motor on/off, 'party mode'.",
            'materiel': ['Maqueen Lite', 'Computer + mic'],
            'etapes': [
                "Teachable: 'clap1', 'clap2', 'clap3', 'ambient'",
                "Record ~20 samples per clap pattern (vary speed)",
                "Different actions: toggle lamp, toggle music, party mode",
            ],
            'tip': "Train ambient noise as 4th class to reduce false positives.",
            'defis': [
                {'level': 'med', 'text': "'Secret sequence' mode: 3 claps then 2 claps to unlock something"},
                {'level': 'hard', 'text': "Discriminate this house vs neighbors: unique rhythmic signature"},
            ],
        },
        'ar': {
            'objectif': "Teachable Audio: تعلم 3 أنماط (تصفيقة واحدة، تصفيقتان، ثلاث). كل نمط = إجراء مختلف. فتح/إغلاق الأضواء، تشغيل/إيقاف المحرك، 'وضع الحفلة'.",
            'materiel': ['Maqueen Lite', 'حاسوب + ميكروفون'],
            'etapes': [
                "Teachable: 'clap1'، 'clap2'، 'clap3'، 'ambient'",
                "سجّل ~20 عينة لكل نمط تصفيق (نوّع السرعة)",
                "إجراءات مختلفة: تبديل المصباح، تبديل الموسيقى، وضع الحفلة",
            ],
            'tip': "درّب الضجيج المحيط كصنف رابع لتقليل الإيجابيات الكاذبة.",
            'defis': [
                {'level': 'med', 'text': "وضع 'تسلسل سري': 3 تصفيقات ثم 2 لفتح شيء"},
                {'level': 'hard', 'text': "تميز هذا المنزل عن الجيران: توقيع إيقاعي فريد"},
            ],
        },
    },
    83: {
        'en': {
            'objectif': "Mini on-device Q-learning: robot learns not to hit walls. Each collision = penalty. Every 5s without collision = reward. Over time it improves movement.",
            'materiel': ['Maqueen Lite', 'Ultrasound', 'Enclosed space'],
            'etapes': [
                "State: discretized ultrasound distance (close, medium, far)",
                "Actions: advance, turn-left, turn-right",
                "Q-table initialized to 0 (3 states × 3 actions = 9 values)",
                "After each action, reward (no collision) or penalty (collision)",
                "Q update: Q[s,a] += 0.1 * (reward + 0.9 * max(Q[s']) - Q[s,a])",
            ],
            'tip': "Real Q-learning: reinforcement learning. Chaotic at first, after 5 minutes robot 'understands'.",
            'defis': [
                {'level': 'hard', 'text': "Visualize Q-table on LED matrix (9 cells)"},
                {'level': 'hard', 'text': "Two phases: 2-min learning, then pure exploitation"},
            ],
        },
        'ar': {
            'objectif': "تعلم Q مصغر على الجهاز: الروبوت يتعلم عدم الاصطدام بالجدران. كل اصطدام = عقوبة. كل 5 ثوانٍ بدون اصطدام = مكافأة. بمرور الوقت يحسّن حركته.",
            'materiel': ['Maqueen Lite', 'موجات فوق صوتية', 'مساحة مغلقة'],
            'etapes': [
                "الحالة: مسافة الموجات فوق الصوتية مفصّلة (قريب، متوسط، بعيد)",
                "الإجراءات: تقدم، استدر يساراً، استدر يميناً",
                "جدول Q مهيأ إلى 0 (3 حالات × 3 إجراءات = 9 قيم)",
                "بعد كل إجراء، مكافأة (بدون اصطدام) أو عقوبة (اصطدام)",
                "تحديث Q: Q[s,a] += 0.1 * (reward + 0.9 * max(Q[s']) - Q[s,a])",
            ],
            'tip': "تعلم Q حقيقي: تعلم بالتعزيز. فوضوي في البداية، بعد 5 دقائق 'يفهم' الروبوت.",
            'defis': [
                {'level': 'hard', 'text': "تصور جدول Q على مصفوفة LED (9 خلايا)"},
                {'level': 'hard', 'text': "مرحلتان: تعلم لمدة دقيقتين، ثم استغلال صرف"},
            ],
        },
    },
    84: {
        'en': {
            'objectif': "Implement a mini neural network (2 inputs, 2 hidden, 2 outputs) to learn XOR. Pure MicroPython/TS, no library. 'Proof' that deep learning isn't magic.",
            'materiel': ['Maqueen Lite', 'Computer (for testing)'],
            'etapes': [
                "Define a 2-2-2 network with sigmoid",
                "Initialize weights randomly",
                "For each XOR pair (00, 01, 10, 11), forward + backward",
                "Repeat 1000 iterations",
                "Test: send [1, 0] to robot → output[0] > 0.5 = advance",
            ],
            'tip': "Long and dense. Only attempt if student has good math level. Otherwise use CreateAI and understand result without hand-implementation.",
            'defis': [
                {'level': 'hard', 'text': "Add full backprop and converge XOR"},
                {'level': 'hard', 'text': "Train on line following (2 sensors → 2 motors)"},
            ],
        },
        'ar': {
            'objectif': "نفّذ شبكة عصبية مصغرة (2 مدخل، 2 خفي، 2 مخرج) لتعلم XOR. MicroPython/TS صرف، بلا مكتبة. 'دليل' على أن التعلم العميق ليس سحراً.",
            'materiel': ['Maqueen Lite', 'حاسوب (للاختبار)'],
            'etapes': [
                "عرّف شبكة 2-2-2 مع sigmoid",
                "هيّئ الأوزان عشوائياً",
                "لكل زوج XOR (00، 01، 10، 11)، forward + backward",
                "كرر 1000 مرة",
                "اختبر: أرسل [1، 0] إلى الروبوت → output[0] > 0.5 = تقدم",
            ],
            'tip': "طويل وكثيف. جرّب فقط إذا كان الطالب جيداً في الرياضيات. وإلا استخدم CreateAI وافهم النتيجة بدون تنفيذ يدوي.",
            'defis': [
                {'level': 'hard', 'text': "أضف backprop كاملاً وحوّل XOR"},
                {'level': 'hard', 'text': "درّب على متابعة الخط (2 مستشعر → 2 محرك)"},
            ],
        },
    },
    85: {
        'en': {
            'objectif': "CreateAI on motion vibrations: robot learns to distinguish wood, carpet, tile, fabric, sand. Useful to optimize speed based on surface.",
            'materiel': ['Maqueen Lite', 'Various surfaces'],
            'etapes': [
                "CreateAI: 4-5 classes (one per surface)",
                "Each capture: advance 2s on the surface",
                "Train, export",
                "Robot adapts speed: fast on wood, slow on carpet",
            ],
            'tip': "Distinct vibratory signatures. Great demo of 'AI perceiving its environment differently'.",
            'defis': [
                {'level': 'med', 'text': "Counter: time spent on each surface"},
                {'level': 'hard', 'text': "If unknown surface, stops and asks (button A + manual class)"},
            ],
        },
        'ar': {
            'objectif': "CreateAI على اهتزازات الحركة: الروبوت يتعلم التمييز بين الخشب، السجاد، البلاط، القماش، الرمل. مفيد لتحسين السرعة حسب السطح.",
            'materiel': ['Maqueen Lite', 'أسطح متنوعة'],
            'etapes': [
                "CreateAI: 4-5 أصناف (واحد لكل سطح)",
                "كل التقاط: تقدم 2 ثانية على السطح",
                "درّب، صدّر",
                "الروبوت يكيّف السرعة: سريع على الخشب، بطيء على السجاد",
            ],
            'tip': "توقيعات اهتزازية مميزة. عرض رائع لـ 'ذكاء اصطناعي يدرك بيئته بشكل مختلف'.",
            'defis': [
                {'level': 'med', 'text': "عداد: الوقت المقضي على كل سطح"},
                {'level': 'hard', 'text': "إذا سطح مجهول، يتوقف ويسأل (الزر A + صنف يدوي)"},
            ],
        },
    },
}

print(f"Phase 3 translations: {len(TRANSLATIONS_P3)} activities (IDs 46-85)")
