"""Full translations EN + AR for all 85 activities.
Structure: TRANSLATIONS[id] = {'en': {...fields}, 'ar': {...fields}}
Fields per language: objectif, materiel (list), etapes (list), tip, defis (list of {level, text}).
"""

TRANSLATIONS = {
    # ═══════════════════════════════════════════════════════════════
    # PHASE 1 · IDs 1-16 (Getting Started + 15 Official DFRobot)
    # ═══════════════════════════════════════════════════════════════
    1: {
        'en': {
            'objectif': "Install the MakeCode library for Maqueen Lite and calibrate the line-tracking sensors before first use.",
            'materiel': ['micro:bit v2', 'Maqueen Lite', 'USB cable', 'MakeCode', '3× AAA batteries'],
            'etapes': [
                "Open makecode.microbit.org and create a new project",
                "Extensions → search 'maqueen-lite' → add",
                "Place the Maqueen on a line mat (or black tape)",
                "Blocks → Maqueen Lite → sensor calibration",
                "Adjust the sensor screws under the robot until reading is stable",
            ],
            'tip': "Without calibration, the line follower zigzags. Take 2 minutes to tune.",
            'defis': [
                {'level': 'easy', 'text': "Change the confirmation message to your name"},
                {'level': 'med', 'text': "Add a beep with music.playTone(262, 500) after calibration"},
            ],
        },
        'ar': {
            'objectif': "تثبيت مكتبة MakeCode لـ Maqueen Lite ومعايرة مستشعرات تتبع الخط قبل الاستخدام الأول.",
            'materiel': ['micro:bit v2', 'Maqueen Lite', 'كابل USB', 'MakeCode', '3 بطاريات AAA'],
            'etapes': [
                "افتح makecode.microbit.org وأنشئ مشروعاً جديداً",
                "الإضافات ← ابحث عن 'maqueen-lite' ← أضف",
                "ضع الـ Maqueen على بساط الخط (أو شريط أسود)",
                "المكعبات ← Maqueen Lite ← معايرة المستشعرات",
                "اضبط براغي المستشعرات أسفل الروبوت حتى تستقر القراءة",
            ],
            'tip': "بدون المعايرة، يتعرج متتبع الخط. خصص دقيقتين للضبط.",
            'defis': [
                {'level': 'easy', 'text': "غيّر رسالة التأكيد إلى اسمك"},
                {'level': 'med', 'text': "أضف صوت تنبيه music.playTone(262, 500) بعد المعايرة"},
            ],
        },
    },
    2: {
        'en': {
            'objectif': "Display the product identifier (ROB0148-EN) on the micro:bit's LED matrix.",
            'materiel': ['micro:bit', 'Maqueen Lite', 'MakeCode'],
            'etapes': [
                "On start, scroll the text 'ROB0148-EN'",
                "Upload the program to the micro:bit",
            ],
            'tip': "Each regional variant has its code: ROB0148-CN (China), -TW (Taiwan), -KR (Korea), -JP (Japan).",
            'defis': [
                {'level': 'easy', 'text': "Replace with your own name"},
                {'level': 'med', 'text': "Add a heart icon after the text"},
            ],
        },
        'ar': {
            'objectif': "عرض معرّف المنتج (ROB0148-EN) على مصفوفة LED الخاصة بـ micro:bit.",
            'materiel': ['micro:bit', 'Maqueen Lite', 'MakeCode'],
            'etapes': [
                "عند البدء، قم بتمرير النص 'ROB0148-EN'",
                "ارفع البرنامج إلى micro:bit",
            ],
            'tip': "لكل نسخة إقليمية رمزها: ROB0148-CN (الصين)، -TW (تايوان)، -KR (كوريا)، -JP (اليابان).",
            'defis': [
                {'level': 'easy', 'text': "استبدل بالاسم الخاص بك"},
                {'level': 'med', 'text': "أضف أيقونة قلب بعد النص"},
            ],
        },
    },
    3: {
        'en': {
            'objectif': "Make the two front LEDs of the Maqueen (red, controlled by P8 and P12) blink to simulate a flashing beacon.",
            'materiel': ['Maqueen Lite', 'MakeCode'],
            'etapes': [
                "Turn on both front LEDs",
                "Wait 500 ms",
                "Turn off both LEDs",
                "Wait 500 ms",
                "Repeat forever",
            ],
            'tip': "P8 = left LED, P12 = right LED. Value 1 = on, 0 = off.",
            'defis': [
                {'level': 'easy', 'text': "Alternate left/right instead of both together"},
                {'level': 'med', 'text': "Change speed: 100 ms, then 1000 ms"},
                {'level': 'hard', 'text': "Simulate police lights: 3 fast blinks, then 1 s pause"},
            ],
        },
        'ar': {
            'objectif': "جعل مصباحَي LED الأماميين للـ Maqueen (أحمر، بواسطة P8 و P12) يومضان لمحاكاة ضوء تحذير.",
            'materiel': ['Maqueen Lite', 'MakeCode'],
            'etapes': [
                "أضئ كلا المصباحَين الأماميين",
                "انتظر 500 ميلي ثانية",
                "أطفئ كلا المصباحَين",
                "انتظر 500 ميلي ثانية",
                "كرر إلى الأبد",
            ],
            'tip': "P8 = المصباح الأيسر، P12 = المصباح الأيمن. القيمة 1 = مضاء، 0 = مطفأ.",
            'defis': [
                {'level': 'easy', 'text': "أضئ بالتناوب بدلاً من معاً"},
                {'level': 'med', 'text': "غيّر السرعة: 100 ميلي ثانية، ثم 1000"},
                {'level': 'hard', 'text': "حاكِ ضوء الشرطة: 3 ومضات سريعة، ثم توقف لثانية"},
            ],
        },
    },
    4: {
        'en': {
            'objectif': "Learn to command the two N20 motors of the Maqueen: forward, backward, turn, stop.",
            'materiel': ['Maqueen Lite', '3× AAA batteries', 'MakeCode'],
            'etapes': [
                "Move forward at speed 150 for 1 second",
                "Move backward at speed 150 for 1 second",
                "Turn right (left forward, right backward) for 1 second",
                "Stop both motors",
            ],
            'tip': "Speed range is 0 to 255. Below 50, motors may not move at all.",
            'defis': [
                {'level': 'easy', 'text': "Do a U-turn (180°) and return to start"},
                {'level': 'med', 'text': "Draw a square (4 sides + 4 right angles)"},
                {'level': 'hard', 'text': "Draw an equilateral triangle (3 sides + 3 120° turns)"},
            ],
        },
        'ar': {
            'objectif': "تعلّم التحكم بمحركَي N20 للـ Maqueen: أمامي، خلفي، استدارة، توقف.",
            'materiel': ['Maqueen Lite', '3 بطاريات AAA', 'MakeCode'],
            'etapes': [
                "تقدم بسرعة 150 لمدة ثانية",
                "تراجع بسرعة 150 لمدة ثانية",
                "استدر يميناً (يسار أمام، يمين خلف) لثانية",
                "أوقف كلا المحركَين",
            ],
            'tip': "نطاق السرعة من 0 إلى 255. تحت 50، قد لا تتحرك المحركات أبداً.",
            'defis': [
                {'level': 'easy', 'text': "استدر 180° وعد إلى نقطة البداية"},
                {'level': 'med', 'text': "ارسم مربعاً (4 أضلاع + 4 زوايا قائمة)"},
                {'level': 'hard', 'text': "ارسم مثلثاً متساوي الأضلاع (3 أضلاع + 3 دورات بـ 120°)"},
            ],
        },
    },
    5: {
        'en': {
            'objectif': "Create a 'breathing' effect on the 4 ambient RGB LEDs — color fades in and out gently, like a breath.",
            'materiel': ['Maqueen Lite', 'MakeCode'],
            'etapes': [
                "For each brightness from 0 to 255 (ramp up)",
                "Light the 4 RGB LEDs at that brightness",
                "Small pause (10 ms)",
                "For each brightness from 255 to 0 (ramp down)",
                "Repeat",
            ],
            'tip': "4 RGB LEDs means 16 million colors. Try pure blue, pure green, then combine.",
            'defis': [
                {'level': 'easy', 'text': "Change color (try pure blue, green, orange)"},
                {'level': 'med', 'text': "Full rainbow cycle (red → orange → yellow → green → blue → purple)"},
                {'level': 'hard', 'text': "Sync breathing with a sound on the buzzer"},
            ],
        },
        'ar': {
            'objectif': "إنشاء تأثير 'التنفس' على مصابيح RGB الأربعة — يتلاشى اللون ويظهر بلطف، كالنفس.",
            'materiel': ['Maqueen Lite', 'MakeCode'],
            'etapes': [
                "لكل شدة من 0 إلى 255 (تزايد)",
                "أضئ المصابيح الأربعة بتلك الشدة",
                "توقف قصير (10 ميلي ثانية)",
                "لكل شدة من 255 إلى 0 (تناقص)",
                "كرر",
            ],
            'tip': "4 مصابيح RGB تعني 16 مليون لون. جرّب الأزرق النقي، ثم الأخضر، ثم امزج.",
            'defis': [
                {'level': 'easy', 'text': "غيّر اللون (جرّب الأزرق، الأخضر، البرتقالي)"},
                {'level': 'med', 'text': "دورة قوس قزح كاملة (أحمر ← برتقالي ← أصفر ← أخضر ← أزرق ← بنفسجي)"},
                {'level': 'hard', 'text': "زامن التنفس مع صوت على صافرة الإنذار"},
            ],
        },
    },
    6: {
        'en': {
            'objectif': "Control a servo motor connected to the Maqueen's S1 port — sweep from 0 to 150 degrees repeatedly.",
            'materiel': ['Maqueen Lite', '9g servo', 'MakeCode'],
            'etapes': [
                "Turn servo to 0°",
                "Wait 500 ms",
                "Turn servo to 150°",
                "Wait 500 ms",
                "Repeat",
            ],
            'tip': "Standard servos go 0 to 180°. Maqueen recommends 0-150° to avoid forcing.",
            'defis': [
                {'level': 'easy', 'text': "Replace sweep with 3 positions (0°, 75°, 150°)"},
                {'level': 'med', 'text': "Control servo with buttons A (-10°) and B (+10°)"},
                {'level': 'hard', 'text': "Attach a small flag, program a 'wave' when A is pressed"},
            ],
        },
        'ar': {
            'objectif': "التحكم بمحرك سيرفو متصل بمنفذ S1 في الـ Maqueen — مسح من 0 إلى 150 درجة بشكل متكرر.",
            'materiel': ['Maqueen Lite', 'سيرفو 9 غرام', 'MakeCode'],
            'etapes': [
                "أدر السيرفو إلى 0°",
                "انتظر 500 ميلي ثانية",
                "أدر السيرفو إلى 150°",
                "انتظر 500 ميلي ثانية",
                "كرر",
            ],
            'tip': "السيرفو القياسي يتحرك من 0 إلى 180°. الـ Maqueen يوصي بـ 0-150° لتفادي الإجهاد.",
            'defis': [
                {'level': 'easy', 'text': "استبدل المسح بـ 3 مواضع (0°, 75°, 150°)"},
                {'level': 'med', 'text': "تحكم في السيرفو بالأزرار A (-10°) و B (+10°)"},
                {'level': 'hard', 'text': "ارفق علماً صغيراً، ابرمج 'تحية' عند ضغط A"},
            ],
        },
    },
    7: {
        'en': {
            'objectif': "Read distance in centimeters using the SR04 ultrasonic module and display it on the micro:bit's LED matrix.",
            'materiel': ['Maqueen Lite', 'SR04 or SR04P ultrasonic sensor', 'MakeCode'],
            'etapes': [
                "Connect the sensor to the Maqueen's ultrasonic port",
                "In a loop, read distance via maqueen.ultrasonic()",
                "Show the number on the LED matrix",
                "Wait 100 ms to avoid multiple echoes",
            ],
            'tip': "Useful range: 3 cm to 400 cm. If return is 0 or < 5, ignore (false signal).",
            'defis': [
                {'level': 'easy', 'text': "Light a red LED when distance < 10 cm"},
                {'level': 'med', 'text': "Play a sound whose frequency changes with distance (sonar)"},
                {'level': 'hard', 'text': "Record minimum distance seen in the last 10 seconds"},
            ],
        },
        'ar': {
            'objectif': "قراءة المسافة بالسنتيمتر باستخدام مستشعر SR04 بالموجات فوق الصوتية وعرضها على مصفوفة LED.",
            'materiel': ['Maqueen Lite', 'مستشعر SR04 أو SR04P', 'MakeCode'],
            'etapes': [
                "وصّل المستشعر بمنفذ الموجات فوق الصوتية",
                "في حلقة، اقرأ المسافة عبر maqueen.ultrasonic()",
                "اعرض الرقم على مصفوفة LED",
                "انتظر 100 ميلي ثانية لتفادي تداخل الأصداء",
            ],
            'tip': "المدى المفيد: 3 سم إلى 400 سم. إذا كانت القراءة 0 أو < 5، تجاهل (إشارة خاطئة).",
            'defis': [
                {'level': 'easy', 'text': "أضئ مصباحاً أحمر عندما تكون المسافة < 10 سم"},
                {'level': 'med', 'text': "شغّل صوتاً يتغير ترددّه مع المسافة (سونار)"},
                {'level': 'hard', 'text': "سجّل أقل مسافة شوهدت خلال آخر 10 ثوانٍ"},
            ],
        },
    },
    8: {
        'en': {
            'objectif': "Read the state of the two infrared line-tracking sensors. On black line → 0; on white zone → 1.",
            'materiel': ['Maqueen Lite', 'Sheet with black line', 'MakeCode'],
            'etapes': [
                "Read the left sensor (P13) and right sensor (P14)",
                "Display the left sensor's value on the LED matrix",
                "Add a short pause",
            ],
            'tip': "If both sensors always read 0 or always 1: recalibrate (see activity 1).",
            'defis': [
                {'level': 'easy', 'text': "Show L or R based on which sensor sees the line"},
                {'level': 'med', 'text': "Light the matching front LED when each sensor sees black"},
                {'level': 'hard', 'text': "Combine the 2 sensors: show an arrow based on line position"},
            ],
        },
        'ar': {
            'objectif': "قراءة حالة مستشعرَي تتبع الخط بالأشعة تحت الحمراء. على الخط الأسود ← 0 ؛ على المنطقة البيضاء ← 1.",
            'materiel': ['Maqueen Lite', 'ورقة بخط أسود', 'MakeCode'],
            'etapes': [
                "اقرأ المستشعر الأيسر (P13) والمستشعر الأيمن (P14)",
                "اعرض قيمة المستشعر الأيسر على مصفوفة LED",
                "أضف توقفاً قصيراً",
            ],
            'tip': "إذا قرأ المستشعران دائماً 0 أو دائماً 1: أعد المعايرة (راجع النشاط 1).",
            'defis': [
                {'level': 'easy', 'text': "اعرض L أو R حسب أي مستشعر يرى الخط"},
                {'level': 'med', 'text': "أضئ مصباح LED الأمامي المقابل عندما يرى كل مستشعر اللون الأسود"},
                {'level': 'hard', 'text': "اجمع المستشعرَين: اعرض سهماً حسب موضع الخط"},
            ],
        },
    },
    9: {
        'en': {
            'objectif': "Learn to read key codes from an NEC infrared remote, so you can use them later.",
            'materiel': ['Maqueen Lite', 'IR remote (ROB0148-EN-3 kit)', 'MakeCode'],
            'etapes': [
                "Install the IR-remote extension in MakeCode",
                "Connect the IR receiver (default on P16)",
                "On IR trigger, show the last 2 digits of the code",
            ],
            'tip': "NEC protocol is the most common. Codes vary between remotes: take note of yours!",
            'defis': [
                {'level': 'easy', 'text': "Write down codes for the 10 number keys"},
                {'level': 'med', 'text': "Show a different icon for each digit 0-9"},
                {'level': 'hard', 'text': "Reconstruct a 4-digit safe PIN"},
            ],
        },
        'ar': {
            'objectif': "تعلّم قراءة رموز مفاتيح جهاز تحكم عن بُعد بالأشعة تحت الحمراء NEC لاستخدامها لاحقاً.",
            'materiel': ['Maqueen Lite', 'جهاز تحكم IR (طقم ROB0148-EN-3)', 'MakeCode'],
            'etapes': [
                "ثبّت إضافة IR-remote في MakeCode",
                "وصّل مستقبل IR (الافتراضي على P16)",
                "عند تلقي إشارة IR، اعرض آخر رقمين من الرمز",
            ],
            'tip': "بروتوكول NEC هو الأكثر شيوعاً. الرموز تختلف بين أجهزة التحكم: دوّن الخاص بك!",
            'defis': [
                {'level': 'easy', 'text': "دوّن رموز مفاتيح الأرقام العشرة"},
                {'level': 'med', 'text': "اعرض أيقونة مختلفة لكل رقم 0-9"},
                {'level': 'hard', 'text': "أعد بناء رمز PIN بـ 4 أرقام لخزنة"},
            ],
        },
    },
    10: {
        'en': {
            'objectif': "Drive the Maqueen with an infrared remote. Keys 2 = forward, 8 = back, 4 = left, 6 = right, 5 = stop.",
            'materiel': ['Maqueen Lite', 'IR remote', 'MakeCode'],
            'etapes': [
                "Read the key pressed",
                "Based on the key, run the motors",
                "Key 5 → stop",
            ],
            'tip': "Key codes depend on the remote. Use activity 9 to note yours first.",
            'defis': [
                {'level': 'easy', 'text': "Add a horn on key 0"},
                {'level': 'med', 'text': "Keys 1-3 = three different speeds"},
                {'level': 'hard', 'text': "Turbo mode: hold a key = speed 255"},
            ],
        },
        'ar': {
            'objectif': "قِد الـ Maqueen بجهاز تحكم IR. المفتاح 2 = أمام، 8 = خلف، 4 = يسار، 6 = يمين، 5 = توقف.",
            'materiel': ['Maqueen Lite', 'جهاز تحكم IR', 'MakeCode'],
            'etapes': [
                "اقرأ المفتاح المضغوط",
                "حسب المفتاح، شغّل المحركات",
                "المفتاح 5 ← توقف",
            ],
            'tip': "رموز المفاتيح تعتمد على جهاز التحكم. استخدم النشاط 9 لتدوين الخاص بك أولاً.",
            'defis': [
                {'level': 'easy', 'text': "أضف بوقاً على المفتاح 0"},
                {'level': 'med', 'text': "المفاتيح 1-3 = ثلاث سرعات مختلفة"},
                {'level': 'hard', 'text': "وضع توربو: ضغط مطوّل = سرعة 255"},
            ],
        },
    },
    11: {
        'en': {
            'objectif': "The robot drives forward; when an obstacle is detected within 30 cm, it randomly turns left or right, then continues.",
            'materiel': ['Maqueen Lite', 'SR04 ultrasonic sensor', 'MakeCode'],
            'etapes': [
                "Drive forward continuously",
                "Read ultrasonic distance",
                "If distance < 30 cm: randomly pick left or right, turn 500 ms",
                "Otherwise, keep driving forward",
            ],
            'tip': "Use Math.randomRange(0, 1) for a binary random choice.",
            'defis': [
                {'level': 'easy', 'text': "Light a red LED when robot detects an obstacle"},
                {'level': 'med', 'text': "Progressive beep: closer obstacle = higher pitch"},
                {'level': 'hard', 'text': "Exploration mode: count obstacles met in 1 minute"},
            ],
        },
        'ar': {
            'objectif': "يتحرك الروبوت للأمام؛ عند اكتشاف عائق ضمن 30 سم، يستدير عشوائياً يساراً أو يميناً ثم يتابع.",
            'materiel': ['Maqueen Lite', 'مستشعر SR04', 'MakeCode'],
            'etapes': [
                "تحرك للأمام باستمرار",
                "اقرأ المسافة بالموجات فوق الصوتية",
                "إذا كانت المسافة < 30 سم: اختر عشوائياً يسار أو يمين، استدر 500 ميلي ثانية",
                "خلاف ذلك، تابع التقدم",
            ],
            'tip': "استخدم Math.randomRange(0, 1) لاختيار عشوائي ثنائي.",
            'defis': [
                {'level': 'easy', 'text': "أضئ مصباحاً أحمر عندما يكتشف الروبوت عائقاً"},
                {'level': 'med', 'text': "صفير تدريجي: عائق أقرب = نغمة أعلى"},
                {'level': 'hard', 'text': "وضع الاستكشاف: احسب العوائق خلال دقيقة"},
            ],
        },
    },
    12: {
        'en': {
            'objectif': "The robot follows a black line on white background. If both sensors see black, it drives forward; if only one sensor sees the line, it corrects by turning.",
            'materiel': ['Maqueen Lite', 'Sheet with black line (or tape)', 'MakeCode'],
            'etapes': [
                "Read both sensors (left P13, right P14)",
                "Both see line (0, 0) → forward",
                "Only left sees line (0, 1) → turn left",
                "Only right sees line (1, 0) → turn right",
                "Neither (1, 1) → spin to find line again",
            ],
            'tip': "Value 0 = black, 1 = white. If inverted, robot 'runs from' the line instead of following.",
            'defis': [
                {'level': 'easy', 'text': "Front LEDs red on straight, green in turns"},
                {'level': 'med', 'text': "Count laps with a marker (perpendicular line every X cm)"},
                {'level': 'hard', 'text': "Proportional line follower: more deviation = sharper turn"},
            ],
        },
        'ar': {
            'objectif': "يتبع الروبوت خطاً أسود على خلفية بيضاء. إذا رأى المستشعران الخط، يتقدم؛ إذا رآه أحدهما فقط، يصحح بالاستدارة.",
            'materiel': ['Maqueen Lite', 'ورقة بخط أسود (أو شريط)', 'MakeCode'],
            'etapes': [
                "اقرأ كلا المستشعرَين (يسار P13، يمين P14)",
                "كلاهما يرى الخط (0, 0) ← أمام",
                "الأيسر فقط يرى الخط (0, 1) ← استدر يساراً",
                "الأيمن فقط يرى الخط (1, 0) ← استدر يميناً",
                "لا أحد (1, 1) ← دور للبحث عن الخط",
            ],
            'tip': "القيمة 0 = أسود، 1 = أبيض. إن كانت معكوسة، يهرب الروبوت من الخط بدلاً من اتباعه.",
            'defis': [
                {'level': 'easy', 'text': "مصابيح أمامية حمراء على المستقيم، خضراء في المنعطفات"},
                {'level': 'med', 'text': "احسب اللفات بعلامة (خط عمودي كل X سم)"},
                {'level': 'hard', 'text': "متتبع نسبي: انحراف أكبر = استدارة أحدّ"},
            ],
        },
    },
    13: {
        'en': {
            'objectif': "The robot moves forward when you shine light on the ambient LEDs. Brighter light = faster. In darkness, it stops.",
            'materiel': ['Maqueen Lite', 'Flashlight or phone', 'MakeCode'],
            'etapes': [
                "Read the light sensor value (built into micro:bit)",
                "Convert brightness (0-255) into motor speed",
                "Drive the robot at that speed",
            ],
            'tip': "Brightness is read via input.lightLevel() — from 0 (dark) to 255 (bright sunlight).",
            'defis': [
                {'level': 'easy', 'text': "Display brightness as a bar on the LED matrix"},
                {'level': 'med', 'text': "Invert: robot runs FROM light (nocturnal animal)"},
                {'level': 'hard', 'text': "Phototropism: turn to find brightest direction"},
            ],
        },
        'ar': {
            'objectif': "يتحرك الروبوت للأمام عند تسليط الضوء على مصابيح المحيط. ضوء أشد = أسرع. في الظلام، يتوقف.",
            'materiel': ['Maqueen Lite', 'مصباح يدوي أو هاتف', 'MakeCode'],
            'etapes': [
                "اقرأ قيمة مستشعر الضوء (المدمج في micro:bit)",
                "حوّل السطوع (0-255) إلى سرعة المحرك",
                "اجعل الروبوت يسير بتلك السرعة",
            ],
            'tip': "السطوع يُقرأ عبر input.lightLevel() — من 0 (ظلام) إلى 255 (شمس ساطعة).",
            'defis': [
                {'level': 'easy', 'text': "اعرض السطوع كشريط على مصفوفة LED"},
                {'level': 'med', 'text': "اعكس: الروبوت يهرب من الضوء (حيوان ليلي)"},
                {'level': 'hard', 'text': "الانجذاب الضوئي: استدر للعثور على أشد الاتجاهات سطوعاً"},
            ],
        },
    },
    14: {
        'en': {
            'objectif': "Drive the Maqueen with a second micro:bit (or DFRobot's micro:Gamepad) via radio. Joystick or buttons.",
            'materiel': ['2× micro:bit', 'Maqueen Lite', 'micro:Gamepad (optional)'],
            'etapes': [
                "Remote: on start, join radio group 1",
                "Remote: send 'F' (forward), 'B' (back), 'L', 'R', 'S'",
                "Robot: same group 1, read received messages",
                "Robot: run motors based on message",
            ],
            'tip': "Both micro:bits must share the same radio group (radio.setGroup).",
            'defis': [
                {'level': 'easy', 'text': "Add a horn (button A+B = buzzer)"},
                {'level': 'med', 'text': "Speed proportional to micro:bit tilt"},
                {'level': 'hard', 'text': "Race mode: 2 robots, each on its own radio group, timer on remote"},
            ],
        },
        'ar': {
            'objectif': "قِد الـ Maqueen بـ micro:bit ثانٍ (أو micro:Gamepad من DFRobot) عبر الراديو. عصا التحكم أو الأزرار.",
            'materiel': ['2× micro:bit', 'Maqueen Lite', 'micro:Gamepad (اختياري)'],
            'etapes': [
                "الجهاز البعيد: عند البدء، انضم إلى مجموعة الراديو 1",
                "الجهاز البعيد: أرسل 'F' (أمام)، 'B' (خلف)، 'L'، 'R'، 'S'",
                "الروبوت: نفس المجموعة 1، اقرأ الرسائل المستلمة",
                "الروبوت: شغّل المحركات حسب الرسالة",
            ],
            'tip': "يجب أن يكون كلا الجهازَين على نفس مجموعة الراديو (radio.setGroup).",
            'defis': [
                {'level': 'easy', 'text': "أضف بوقاً (الزر A+B = صافرة)"},
                {'level': 'med', 'text': "السرعة متناسبة مع ميل micro:bit"},
                {'level': 'hard', 'text': "وضع السباق: روبوتان، مجموعة راديو مستقلة، مؤقت على الجهاز البعيد"},
            ],
        },
    },
    15: {
        'en': {
            'objectif': "Advanced IR control: progressive driving, horn, LED colors, speed modes. All from the remote.",
            'materiel': ['Maqueen Lite', 'IR remote (ROB0148-EN-3 kit)', 'MakeCode'],
            'etapes': [
                "Directional keys 2/4/6/8 = driving",
                "Key 5 = emergency stop",
                "Key 0 = horn",
                "Keys 1-3 = 3 preset speeds",
                "Keys 7-9 = 3 ambient colors",
            ],
            'tip': "Store speed in a global variable — change it with 1/2/3 and use it in all driving keys.",
            'defis': [
                {'level': 'easy', 'text': "Add a 'disco' mode with one key (random colors)"},
                {'level': 'med', 'text': "Temporary turbo: key # → speed 255 for 3 seconds"},
                {'level': 'hard', 'text': "Trip memory: key * saves last 30 commands and replays them"},
            ],
        },
        'ar': {
            'objectif': "تحكم IR متقدم: قيادة تدريجية، بوق، ألوان LED، أوضاع السرعة. كل ذلك من جهاز التحكم.",
            'materiel': ['Maqueen Lite', 'جهاز تحكم IR (طقم ROB0148-EN-3)', 'MakeCode'],
            'etapes': [
                "المفاتيح الاتجاهية 2/4/6/8 = القيادة",
                "المفتاح 5 = توقف طارئ",
                "المفتاح 0 = بوق",
                "المفاتيح 1-3 = 3 سرعات مسبقة الضبط",
                "المفاتيح 7-9 = 3 ألوان محيطة",
            ],
            'tip': "احفظ السرعة في متغير عام — غيّرها بـ 1/2/3 واستخدمها في كل مفاتيح القيادة.",
            'defis': [
                {'level': 'easy', 'text': "أضف وضع 'ديسكو' بمفتاح واحد (ألوان عشوائية)"},
                {'level': 'med', 'text': "توربو مؤقت: المفتاح # ← سرعة 255 لمدة 3 ثوانٍ"},
                {'level': 'hard', 'text': "ذاكرة الرحلة: * يحفظ آخر 30 أمراً ويعيد تشغيلها"},
            ],
        },
    },
    16: {
        'en': {
            'objectif': "Technical reference: ports, pins, sensors, component limits. Keep this handy when you build.",
            'materiel': ['This guide! 📚'],
            'etapes': [
                "Power: 3.5–5 V (3× AAA or Li-ion 3.7 V)",
                "Motors: 2× N20 metal, PWM-driven",
                "Front LEDs: P8 (left), P12 (right), 0/1 on/off",
                "Ambient RGB LEDs: 4 NeoPixel, 16M colors, via Maqueen lib",
                "Line sensors: P13 (left), P14 (right), 0 = black, 1 = white",
                "Ultrasonic: dedicated SR04/SR04P port (5V)",
                "Servo: S1 + S2 on AnalogPin",
                "IR: NEC receiver on P16",
                "I²C extension: 5V, for extra modules",
                "Available pins: P0, P1, P2 (Gravity)",
            ],
            'tip': "Print this page and tape it next to your workbench. You'll reference it hundreds of times.",
            'defis': [],
        },
        'ar': {
            'objectif': "المرجع التقني: المنافذ، الأطراف، المستشعرات، حدود كل مكون. اجعلها في متناول يدك أثناء البناء.",
            'materiel': ['هذا الدليل! 📚'],
            'etapes': [
                "الطاقة: 3.5–5 فولت (3 × AAA أو ليثيوم 3.7 فولت)",
                "المحركات: 2 × N20 معدني، PWM",
                "LED أمامية: P8 (يسار)، P12 (يمين)، 0/1 تشغيل/إيقاف",
                "LED محيطة RGB: 4 NeoPixel، 16 مليون لون، عبر مكتبة Maqueen",
                "مستشعرات الخط: P13 (يسار)، P14 (يمين)، 0 = أسود، 1 = أبيض",
                "موجات فوق صوتية: منفذ مخصص SR04/SR04P (5 فولت)",
                "سيرفو: S1 + S2 على AnalogPin",
                "IR: مستقبل NEC على P16",
                "تمديد I²C: 5 فولت، لوحدات إضافية",
                "أطراف متاحة: P0, P1, P2 (Gravity)",
            ],
            'tip': "اطبع هذه الصفحة وألصقها بجوار طاولة عملك. ستراجعها مئات المرات.",
            'defis': [],
        },
    },
}

print(f"Translations file part 1 loaded: {len(TRANSLATIONS)} activities (Phase 1)")
