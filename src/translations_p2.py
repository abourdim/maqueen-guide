"""Phase 2 translations (IDs 17-45): Movement, LEDs/Sound, Sensors, Interactivity."""

TRANSLATIONS_P2 = {
    17: {
        'en': {
            'objectif': "The robot draws a perfect square: forward, turn right, 4 times in a row. Returns to the starting point.",
            'materiel': ['Maqueen Lite', 'Clear space ~50cm²'],
            'etapes': ["Repeat 4 times:", "Move forward 1 second", "Turn right 500 ms", "Stop at the end"],
            'tip': "If your square doesn't close, adjust turn duration (400-600 ms depending on batteries).",
            'defis': [
                {'level': 'easy', 'text': "Make a triangle (3 sides, turn 120°)"},
                {'level': 'med', 'text': "Draw a hexagon (6 sides, 60°)"},
                {'level': 'hard', 'text': "Draw an octagon, then retrace the path backwards"},
            ],
        },
        'ar': {
            'objectif': "يرسم الروبوت مربعاً مثالياً: يتقدم، يستدير يميناً، 4 مرات متتالية. يعود إلى نقطة البداية.",
            'materiel': ['Maqueen Lite', 'مساحة فارغة ~50 سم²'],
            'etapes': ["كرر 4 مرات:", "تقدم لثانية", "استدر يميناً 500 ميلي ثانية", "توقف في النهاية"],
            'tip': "إن لم يُغلق مربعك، اضبط مدة الاستدارة (400-600 ميلي ثانية حسب البطاريات).",
            'defis': [
                {'level': 'easy', 'text': "اصنع مثلثاً (3 أضلاع، استدر 120°)"},
                {'level': 'med', 'text': "ارسم سداسياً (6 أضلاع، 60°)"},
                {'level': 'hard', 'text': "ارسم ثمانياً، ثم عد على نفس المسار عكسياً"},
            ],
        },
    },
    18: {
        'en': {
            'objectif': "Use buttons A and B to change the robot's speed: A slows down, B speeds up.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "Start at speed 100",
                "If button A pressed: speed -30 (minimum 0)",
                "If button B pressed: speed +30 (maximum 255)",
                "Drive continuously at current speed",
            ],
            'tip': "Use Math.max and Math.min to keep speed between 0 and 255.",
            'defis': [
                {'level': 'easy', 'text': "Display speed as a bar (0-9 LEDs lit)"},
                {'level': 'med', 'text': "Button A+B = reset to 100"},
            ],
        },
        'ar': {
            'objectif': "استخدم الزرَين A و B لتغيير سرعة الروبوت: A يبطئ، B يسرع.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "ابدأ بسرعة 100",
                "إذا ضُغط A: السرعة -30 (الحد الأدنى 0)",
                "إذا ضُغط B: السرعة +30 (الحد الأقصى 255)",
                "تابع القيادة بالسرعة الحالية",
            ],
            'tip': "استخدم Math.max و Math.min لإبقاء السرعة بين 0 و 255.",
            'defis': [
                {'level': 'easy', 'text': "اعرض السرعة كشريط (0-9 مصابيح مضاءة)"},
                {'level': 'med', 'text': "الزر A+B = إعادة إلى 100"},
            ],
        },
    },
    19: {
        'en': {
            'objectif': "Drive the Maqueen by tilting a second micro:bit like a remote. The accelerometer detects tilt and sends over radio.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "Remote: in loop, read X and Y acceleration",
                "Send the values via radio",
                "Robot: listen on radio, convert to motor speeds",
                "Tilt forward = go, tilt back = reverse, left/right = turn",
            ],
            'tip': "Acceleration ranges -1023 to +1023. Divide by 5 for a sensible speed.",
            'defis': [
                {'level': 'med', 'text': "Show a direction arrow on the LED matrix"},
                {'level': 'hard', 'text': "Nitro mode: shake remote = 3 s at max speed"},
            ],
        },
        'ar': {
            'objectif': "قِد الـ Maqueen بإمالة micro:bit ثانٍ كجهاز تحكم. المسارع يكشف الميل ويرسل عبر الراديو.",
            'materiel': ['2× micro:bit', 'Maqueen Lite'],
            'etapes': [
                "الجهاز البعيد: في حلقة، اقرأ التسارع X و Y",
                "أرسل القيم عبر الراديو",
                "الروبوت: استمع للراديو، حوّل لسرعات المحرك",
                "ميل للأمام = تقدم، ميل للخلف = رجوع، يسار/يمين = استدارة",
            ],
            'tip': "التسارع من -1023 إلى +1023. اقسم على 5 للحصول على سرعة معقولة.",
            'defis': [
                {'level': 'med', 'text': "اعرض سهم الاتجاه على مصفوفة LED"},
                {'level': 'hard', 'text': "وضع النيترو: هز الجهاز = 3 ثوانٍ بأقصى سرعة"},
            ],
        },
    },
    20: {
        'en': {
            'objectif': "Time how long the robot takes to cover a given distance. Beep at start, beep at finish.",
            'materiel': ['Maqueen Lite', '2-meter tape', 'Stopwatch (optional)'],
            'etapes': [
                "On button A: start, record the time",
                "Drive forward for 3 seconds at max speed",
                "Stop, compute elapsed time",
                "Display the time in milliseconds",
            ],
            'tip': "input.runningTime() returns milliseconds since startup.",
            'defis': [
                {'level': 'easy', 'text': "3-2-1 countdown before the start"},
                {'level': 'med', 'text': "Record the best time of the session"},
                {'level': 'hard', 'text': "4-robot tournament with auto ranking"},
            ],
        },
        'ar': {
            'objectif': "قِس الوقت الذي يستغرقه الروبوت لقطع مسافة معينة. صفير عند البدء، صفير عند الوصول.",
            'materiel': ['Maqueen Lite', 'شريط 2 متر', 'ساعة إيقاف (اختياري)'],
            'etapes': [
                "عند ضغط A: ابدأ، سجّل الوقت",
                "تقدم لمدة 3 ثوانٍ بأقصى سرعة",
                "توقف، احسب الوقت المنقضي",
                "اعرض الوقت بالميلي ثانية",
            ],
            'tip': "input.runningTime() تُرجع الميلي ثانية منذ بدء التشغيل.",
            'defis': [
                {'level': 'easy', 'text': "عد تنازلي 3-2-1 قبل الانطلاق"},
                {'level': 'med', 'text': "سجّل أفضل وقت في الجلسة"},
                {'level': 'hard', 'text': "بطولة 4 روبوتات مع ترتيب تلقائي"},
            ],
        },
    },
    21: {
        'en': {
            'objectif': "The robot moves unpredictably: forward for a random duration, turn by a random angle, repeat. Like a curious fly.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "In loop: drive forward for a random duration (500-2000 ms)",
                "Randomly pick left or right",
                "Turn for a random duration (200-600 ms)",
                "Repeat",
            ],
            'tip': "Math.randomRange(a, b) returns an integer between a and b inclusive.",
            'defis': [
                {'level': 'easy', 'text': "Light a random-color LED at each direction change"},
                {'level': 'med', 'text': "Robot plays a different note at each movement"},
            ],
        },
        'ar': {
            'objectif': "يتحرك الروبوت بشكل غير متوقع: يتقدم لمدة عشوائية، يستدير بزاوية عشوائية، يكرر. كذبابة فضولية.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "في حلقة: تقدم لمدة عشوائية (500-2000 ميلي ثانية)",
                "اختر عشوائياً يسار أو يمين",
                "استدر لمدة عشوائية (200-600 ميلي ثانية)",
                "كرر",
            ],
            'tip': "Math.randomRange(a, b) تُرجع عدداً صحيحاً بين a و b شاملاً.",
            'defis': [
                {'level': 'easy', 'text': "أضئ مصباحاً بلون عشوائي عند كل تغيير اتجاه"},
                {'level': 'med', 'text': "يعزف الروبوت نغمة مختلفة مع كل حركة"},
            ],
        },
    },
    22: {
        'en': {
            'objectif': "Attach a marker to the Maqueen and make it draw spirals and flowers on a large sheet of paper.",
            'materiel': ['Maqueen Lite', 'Fine-tip marker', 'Tape', 'Large paper sheet'],
            'etapes': [
                "Tape the marker centered under the Maqueen (screw hole available)",
                "Drive with a small speed difference between the two motors",
                "Repeat for 20 seconds",
                "Admire the spiral!",
            ],
            'tip': "Small difference = big spiral. Big difference = small circles.",
            'defis': [
                {'level': 'easy', 'text': "Change speeds every 5 seconds to vary the drawing"},
                {'level': 'med', 'text': "Flower mode: alternate 3s forward, 3s back, 10 times"},
                {'level': 'hard', 'text': "Program your initials by chaining segments and turns"},
            ],
        },
        'ar': {
            'objectif': "ألصق قلماً بالـ Maqueen واجعله يرسم حلزونات وزهوراً على ورقة كبيرة.",
            'materiel': ['Maqueen Lite', 'قلم رفيع', 'شريط لاصق', 'ورقة كبيرة'],
            'etapes': [
                "ألصق القلم في المنتصف أسفل الـ Maqueen (فتحة برغي متاحة)",
                "قِد بفارق سرعة بسيط بين المحركَين",
                "كرر لمدة 20 ثانية",
                "أعجب بالحلزون!",
            ],
            'tip': "فارق صغير = حلزون كبير. فارق كبير = دوائر صغيرة.",
            'defis': [
                {'level': 'easy', 'text': "غيّر السرعات كل 5 ثوانٍ لتنويع الرسم"},
                {'level': 'med', 'text': "وضع الزهرة: ناوب 3 ثوانٍ أمام، 3 ثوانٍ خلف، 10 مرات"},
                {'level': 'hard', 'text': "ابرمج أحرف اسمك الأولى بربط مقاطع ومنعطفات"},
            ],
        },
    },
    23: {
        'en': {
            'objectif': "Record a sequence of movements (via buttons), then replay it identically. Foundation for a robot choreography.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "Record mode (button A): each button (up=forward, A+B=stop…) logs its time and direction",
                "Playback mode (button B): read the list and replay each action",
                "Clear: shake to empty the array",
            ],
            'tip': "To simplify, record just 5 predefined actions (F/B/L/R/S) with their duration.",
            'defis': [
                {'level': 'hard', 'text': "Save the sequence to flash so it survives a reboot"},
            ],
        },
        'ar': {
            'objectif': "سجّل تسلسلاً من الحركات (عبر الأزرار)، ثم أعد تشغيله بنفس الطريقة. أساس لكوريغرافيا الروبوت.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "وضع التسجيل (A): كل زر (أعلى=تقدم، A+B=توقف…) يسجّل وقته واتجاهه",
                "وضع الإعادة (B): اقرأ القائمة وكرر كل إجراء",
                "مسح: هز الجهاز لإفراغ المصفوفة",
            ],
            'tip': "للتبسيط، سجّل 5 إجراءات محددة فقط (F/B/L/R/S) مع مدتها.",
            'defis': [
                {'level': 'hard', 'text': "احفظ التسلسل في الفلاش ليبقى بعد إعادة التشغيل"},
            ],
        },
    },
    24: {
        'en': {
            'objectif': "Scroll a full rainbow through the Maqueen's 4 ambient RGB LEDs.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "Cycle through hues from 0 to 255",
                "Display the color on all 4 LEDs",
                "Small pause for visibility",
                "Repeat",
            ],
            'tip': "The neopixel library handles HSV hues. More natural for rainbows than RGB.",
            'defis': [
                {'level': 'easy', 'text': "Change scroll speed (10ms fast, 200ms slow)"},
                {'level': 'med', 'text': "Each LED has a 90° hue offset = gradient effect"},
            ],
        },
        'ar': {
            'objectif': "مرّر قوس قزح كاملاً عبر مصابيح RGB الأربعة في الـ Maqueen.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "دور عبر الألوان (hue) من 0 إلى 255",
                "اعرض اللون على المصابيح الأربعة",
                "توقف قصير للرؤية",
                "كرر",
            ],
            'tip': "مكتبة neopixel تدير الألوان HSV. أكثر طبيعية من RGB لأقواس قزح.",
            'defis': [
                {'level': 'easy', 'text': "غيّر سرعة التمرير (10 ميلي ثانية سريع، 200 بطيء)"},
                {'level': 'med', 'text': "كل مصباح بإزاحة 90° = تأثير تدرج"},
            ],
        },
    },
    25: {
        'en': {
            'objectif': "Simulate car turn signals: button A = left turn, B = right, A+B = hazard (both).",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "On button A: blink left LED (P8) every 500ms",
                "On button B: blink right LED (P12)",
                "On A+B: both blink together",
            ],
            'tip': "Use a global variable to track the active mode, and a forever loop for the blinking.",
            'defis': [
                {'level': 'easy', 'text': "Add a subtle beep with each blink"},
                {'level': 'med', 'text': "Ambient RGBs blink orange simultaneously"},
            ],
        },
        'ar': {
            'objectif': "حاكِ إشارات انعطاف السيارة: A = يسار، B = يمين، A+B = تحذير (كلاهما).",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "عند ضغط A: أومض المصباح الأيسر (P8) كل 500 ميلي ثانية",
                "عند ضغط B: أومض المصباح الأيمن (P12)",
                "عند A+B: كلاهما يومضان معاً",
            ],
            'tip': "استخدم متغيراً عاماً لتتبع الوضع النشط، وحلقة forever للوميض.",
            'defis': [
                {'level': 'easy', 'text': "أضف صفيراً خفيفاً مع كل وميض"},
                {'level': 'med', 'text': "مصابيح RGB تومض باللون البرتقالي في نفس الوقت"},
            ],
        },
    },
    26: {
        'en': {
            'objectif': "The robot becomes a lamp that turns on automatically when it's dark and off when it's bright.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "Read brightness continuously",
                "If brightness < 80: front LEDs on + bright white RGB",
                "Otherwise: LEDs off",
                "Short pause to avoid flickering",
            ],
            'tip': "Add hysteresis (margin between on/off thresholds) to avoid flickering.",
            'defis': [
                {'level': 'med', 'text': "Display brightness as a bar graph on the LED matrix"},
                {'level': 'hard', 'text': "Nightlight mode: soft red in dim light"},
            ],
        },
        'ar': {
            'objectif': "يصبح الروبوت مصباحاً يشتعل تلقائياً عندما يظلم وينطفئ عندما يكون الجو مضيئاً.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "اقرأ السطوع باستمرار",
                "إذا كان السطوع < 80: أضئ المصابيح الأمامية + RGB أبيض ساطع",
                "خلاف ذلك: أطفئ المصابيح",
                "توقف قصير لتفادي الوميض",
            ],
            'tip': "أضف هامشاً بين عتبات التشغيل والإطفاء لتفادي الوميض.",
            'defis': [
                {'level': 'med', 'text': "اعرض السطوع كشريط على مصفوفة LED"},
                {'level': 'hard', 'text': "وضع الضوء الليلي: أحمر ناعم في الإضاءة الخافتة"},
            ],
        },
    },
    27: {
        'en': {
            'objectif': "Play 8 notes using buttons and tilt of the micro:bit. Do, re, mi, fa, sol, la, ti, high do.",
            'materiel': ['micro:bit', 'Maqueen Lite (optional for speaker)'],
            'etapes': [
                "Button A: play DO",
                "Button B: play MI",
                "Button A+B: play SOL",
                "Tilt left: RE, right: FA, forward: LA, back: TI",
                "Shake: high DO",
            ],
            'tip': "music.playTone(262, 400) = Do for 400ms. Frequencies: 262, 294, 330, 349, 392, 440, 494, 523.",
            'defis': [
                {'level': 'easy', 'text': "Display the note name on the LED matrix"},
                {'level': 'med', 'text': "Program a known melody on one button"},
                {'level': 'hard', 'text': "Record mode: memorize 20 notes and replay"},
            ],
        },
        'ar': {
            'objectif': "اعزف 8 نغمات بالأزرار والميل. دو، ري، مي، فا، صول، لا، سي، دو حاد.",
            'materiel': ['micro:bit', 'Maqueen Lite (اختياري للسماعة)'],
            'etapes': [
                "الزر A: اعزف دو",
                "الزر B: اعزف مي",
                "الزر A+B: اعزف صول",
                "ميل يسار: ري، يمين: فا، أمام: لا، خلف: سي",
                "هز: دو حاد",
            ],
            'tip': "music.playTone(262, 400) = دو لمدة 400 ميلي ثانية. الترددات: 262, 294, 330, 349, 392, 440, 494, 523.",
            'defis': [
                {'level': 'easy', 'text': "اعرض اسم النغمة على مصفوفة LED"},
                {'level': 'med', 'text': "ابرمج لحناً معروفاً على زر واحد"},
                {'level': 'hard', 'text': "وضع تسجيل: احفظ 20 نغمة وأعد العزف"},
            ],
        },
    },
    28: {
        'en': {
            'objectif': "The robot becomes a disco ball: colors flash to the rhythm, motors spin, buzzer plays a melody.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "Main loop: pick a random RGB color",
                "Display on all 4 LEDs + front LEDs at 50% random",
                "Play a random note",
                "Motors: pivot in a random direction 200ms",
                "Repeat",
            ],
            'tip': "neopixel.rgb(r,g,b) accepts 0-255 values for each channel.",
            'defis': [
                {'level': 'easy', 'text': "Button A = slow mode (500ms between changes)"},
                {'level': 'med', 'text': "Program a real melody (not random) in a loop"},
            ],
        },
        'ar': {
            'objectif': "يصبح الروبوت كرة ديسكو: ألوان تومض بالإيقاع، محركات تدور، صافرة تعزف لحناً.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "الحلقة الرئيسية: اختر لون RGB عشوائياً",
                "اعرض على المصابيح الأربعة + الأمامية بنسبة 50% عشوائي",
                "اعزف نغمة عشوائية",
                "المحركات: دور عشوائياً لمدة 200 ميلي ثانية",
                "كرر",
            ],
            'tip': "neopixel.rgb(r,g,b) يقبل قيماً 0-255 لكل قناة.",
            'defis': [
                {'level': 'easy', 'text': "الزر A = وضع بطيء (500 ميلي ثانية بين التغييرات)"},
                {'level': 'med', 'text': "ابرمج لحناً حقيقياً (غير عشوائي) في حلقة"},
            ],
        },
    },
    29: {
        'en': {
            'objectif': "Use the micro:bit v2's built-in microphone to measure ambient volume. The robot lights up brighter when you shout.",
            'materiel': ['micro:bit V2', 'Maqueen Lite'],
            'etapes': [
                "Read sound level (input.soundLevel, 0-255)",
                "Convert to color: silent=blue, medium=green, loud=red",
                "Display on the 4 RGB LEDs",
                "Repeat",
            ],
            'tip': "The sensor is fast! Add a moving average for smoother rendering.",
            'defis': [
                {'level': 'easy', 'text': "Show a bar graph on the LED matrix for volume"},
            ],
        },
        'ar': {
            'objectif': "استخدم الميكروفون المدمج في micro:bit v2 لقياس مستوى الصوت المحيط. يضيء الروبوت أقوى عندما تصرخ.",
            'materiel': ['micro:bit V2', 'Maqueen Lite'],
            'etapes': [
                "اقرأ مستوى الصوت (input.soundLevel, 0-255)",
                "حوّل إلى لون: صمت=أزرق، متوسط=أخضر، عالي=أحمر",
                "اعرض على مصابيح RGB الأربعة",
                "كرر",
            ],
            'tip': "المستشعر سريع! أضف متوسط متحرك للعرض الأنعم.",
            'defis': [
                {'level': 'easy', 'text': "اعرض رسماً بيانياً شريطياً على مصفوفة LED للصوت"},
            ],
        },
    },
    30: {
        'en': {
            'objectif': "Simulate a flickering fireplace flame on the 4 RGB LEDs: orange, red, yellow mixed randomly.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "For each LED, pick a random orange-red color",
                "Vary intensity to simulate flickering",
                "Short pause (100ms)",
                "Loop",
            ],
            'tip': "The color palette of fire: rgb(255, 100-180, 0-50).",
            'defis': [
                {'level': 'med', 'text': "Add a cozy crackling sound on the buzzer"},
                {'level': 'hard', 'text': "React to wind (shake) = flames flicker faster"},
            ],
        },
        'ar': {
            'objectif': "حاكِ لهباً متذبذباً لمدفأة على مصابيح RGB الأربعة: برتقالي، أحمر، أصفر بشكل عشوائي.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "لكل مصباح، اختر لوناً برتقالياً-أحمر عشوائياً",
                "نوّع الشدة لمحاكاة التذبذب",
                "توقف قصير (100 ميلي ثانية)",
                "حلقة",
            ],
            'tip': "لوحة ألوان النار: rgb(255, 100-180, 0-50).",
            'defis': [
                {'level': 'med', 'text': "أضف صوت فرقعة دافئ على الصافرة"},
                {'level': 'hard', 'text': "تفاعل مع الرياح (هز) = اللهب يتذبذب أسرع"},
            ],
        },
    },
    31: {
        'en': {
            'objectif': "Emit a police siren sound + alternating red/blue LEDs. Perfect for a 'police cruiser' role-play.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "RGB LEDs alternate red and blue every 200ms",
                "Buzzer plays alternating tones (low, high, low, high)",
                "Loop continuously",
            ],
            'tip': "For the siren: alternate two frequencies 300-400Hz apart, like 500 and 900Hz.",
            'defis': [
                {'level': 'easy', 'text': "Button A = turn off the siren"},
                {'level': 'med', 'text': "Also move the robot slowly forward during the siren"},
            ],
        },
        'ar': {
            'objectif': "أصدر صوت صفارة شرطة + مصابيح حمراء/زرقاء بالتناوب. مثالي للعب دور 'سيارة الشرطة'.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "مصابيح RGB تتناوب الأحمر والأزرق كل 200 ميلي ثانية",
                "الصافرة تعزف نغمات متناوبة (منخفضة، عالية، منخفضة، عالية)",
                "حلقة مستمرة",
            ],
            'tip': "للصفارة: ناوب بين ترددين يفصلهما 300-400 هرتز، مثل 500 و 900 هرتز.",
            'defis': [
                {'level': 'easy', 'text': "الزر A = أطفئ الصفارة"},
                {'level': 'med', 'text': "حرّك الروبوت ببطء للأمام أثناء الصفارة"},
            ],
        },
    },
    32: {
        'en': {
            'objectif': "Display the current temperature (using the micro:bit's built-in sensor) on the LED matrix.",
            'materiel': ['micro:bit'],
            'etapes': [
                "Read input.temperature() in °C",
                "Display the number on the LED matrix",
                "Pause 2 seconds",
                "Repeat every second",
            ],
            'tip': "The micro:bit's temperature is slightly higher than true ambient (hot chip). Subtract 3°C for realism.",
            'defis': [
                {'level': 'easy', 'text': "Show 'COLD' / 'OK' / 'HOT' instead of the number"},
                {'level': 'med', 'text': "Sound an alarm if temp exceeds 30°C"},
                {'level': 'hard', 'text': "Log min and max of the session, show on button A"},
            ],
        },
        'ar': {
            'objectif': "اعرض درجة الحرارة الحالية (باستخدام المستشعر المدمج في micro:bit) على مصفوفة LED.",
            'materiel': ['micro:bit'],
            'etapes': [
                "اقرأ input.temperature() بالمئوية",
                "اعرض الرقم على مصفوفة LED",
                "توقف ثانيتَين",
                "كرر كل ثانية",
            ],
            'tip': "درجة حرارة micro:bit أعلى قليلاً من المحيط (شريحة حارة). اطرح 3° للواقعية.",
            'defis': [
                {'level': 'easy', 'text': "اعرض 'COLD' / 'OK' / 'HOT' بدل الرقم"},
                {'level': 'med', 'text': "أطلق إنذاراً إذا تجاوزت الحرارة 30°"},
                {'level': 'hard', 'text': "سجّل الحد الأدنى والأعلى للجلسة، اعرضه على الزر A"},
            ],
        },
    },
    33: {
        'en': {
            'objectif': "Show an arrow on the LED matrix that always points to magnetic North.",
            'materiel': ['micro:bit'],
            'etapes': [
                "Calibrate compass on first run (move micro:bit in figure-8)",
                "Read magnetic heading (0-360°)",
                "Convert to one of 8 directions (N/NE/E/SE/S/SW/W/NW)",
                "Display matching arrow",
            ],
            'tip': "input.compassHeading() auto-calibrates the first time. 'TILT TO FILL SCREEN' is normal.",
            'defis': [
                {'level': 'med', 'text': "Robot turns until it points North automatically"},
                {'level': 'hard', 'text': "Navigation: 'go 50 steps N, then 30 steps E'"},
            ],
        },
        'ar': {
            'objectif': "اعرض سهماً على مصفوفة LED يشير دائماً إلى الشمال المغناطيسي.",
            'materiel': ['micro:bit'],
            'etapes': [
                "عايّر البوصلة عند أول تشغيل (حرّك micro:bit كالرقم 8)",
                "اقرأ الاتجاه المغناطيسي (0-360°)",
                "حوّل إلى أحد 8 اتجاهات (ش/شش/ش/جش/ج/جغ/غ/شغ)",
                "اعرض السهم المقابل",
            ],
            'tip': "input.compassHeading() يعايّر تلقائياً أول مرة. 'TILT TO FILL SCREEN' طبيعي.",
            'defis': [
                {'level': 'med', 'text': "الروبوت يستدير حتى يشير للشمال تلقائياً"},
                {'level': 'hard', 'text': "الملاحة: 'اذهب 50 خطوة شمالاً، ثم 30 شرقاً'"},
            ],
        },
    },
    34: {
        'en': {
            'objectif': "The robot emits a sound whose frequency varies with the distance to an obstacle. Close = high, far = low. Like sonar.",
            'materiel': ['Maqueen Lite', 'SR04 ultrasonic sensor'],
            'etapes': [
                "In loop: measure ultrasonic distance",
                "Convert distance to frequency: 200Hz (far) to 2000Hz (close)",
                "Play the note for 100ms",
                "Pause 100ms to breathe",
            ],
            'tip': "Use Math.map to convert one range to another. distance 0-100 → frequency 2000-200.",
            'defis': [
                {'level': 'easy', 'text': "Light red LED if distance < 10cm"},
                {'level': 'med', 'text': "Beep faster (shorter pause) when close"},
            ],
        },
        'ar': {
            'objectif': "يصدر الروبوت صوتاً يتغير ترددّه بمسافة العائق. قريب = عالٍ، بعيد = منخفض. كالسونار.",
            'materiel': ['Maqueen Lite', 'مستشعر SR04'],
            'etapes': [
                "في حلقة: قِس المسافة بالموجات فوق الصوتية",
                "حوّل المسافة لتردد: 200 هرتز (بعيد) إلى 2000 هرتز (قريب)",
                "اعزف النغمة لمدة 100 ميلي ثانية",
                "توقف 100 ميلي ثانية للتنفس",
            ],
            'tip': "استخدم Math.map لتحويل مدى لمدى آخر. المسافة 0-100 ← التردد 2000-200.",
            'defis': [
                {'level': 'easy', 'text': "أضئ مصباحاً أحمر إذا كانت المسافة < 10 سم"},
                {'level': 'med', 'text': "صفير أسرع (توقف أقصر) عند القرب"},
            ],
        },
    },
    35: {
        'en': {
            'objectif': "Use the accelerometer to turn the micro:bit into a bubble level: a center LED lights up when it's horizontal.",
            'materiel': ['micro:bit'],
            'etapes': [
                "Read X and Y acceleration",
                "If |X| < 50 and |Y| < 50: light center LED + success beep",
                "Otherwise: light a LED indicating tilt direction",
            ],
            'tip': "To show direction, map X and Y to 0-4 coordinates on the 5x5 matrix.",
            'defis': [
                {'level': 'easy', 'text': "Play a validation sound each time you find horizontal"},
                {'level': 'med', 'text': "Show a green cross when level, red otherwise"},
            ],
        },
        'ar': {
            'objectif': "استخدم المسارع لتحويل micro:bit إلى ميزان فقاعة: مصباح مركزي يضيء عندما يكون أفقياً.",
            'materiel': ['micro:bit'],
            'etapes': [
                "اقرأ تسارع X و Y",
                "إذا |X| < 50 و |Y| < 50: أضئ مصباح المركز + صفير نجاح",
                "خلاف ذلك: أضئ مصباحاً يشير لاتجاه الميل",
            ],
            'tip': "لإظهار الاتجاه، حوّل X و Y إلى إحداثيات 0-4 على المصفوفة 5×5.",
            'defis': [
                {'level': 'easy', 'text': "اعزف صوت تأكيد كلما وجدت الأفقية"},
                {'level': 'med', 'text': "اعرض صليباً أخضر عند الأفقية، أحمر خلاف ذلك"},
            ],
        },
    },
    36: {
        'en': {
            'objectif': "The robot sounds an alarm if shaken or dropped. Uses Gesture.Shake and FreeFall.",
            'materiel': ['micro:bit', 'Maqueen Lite'],
            'etapes': [
                "On free fall (Gesture.FreeFall): RED alarm + loud buzzer",
                "On shock (Gesture.Shake): show ⚠️ + beep",
                "Button A: reset, calm message",
            ],
            'tip': "FreeFall detects when acceleration tends to 0 (free fall).",
            'defis': [
                {'level': 'med', 'text': "Count the number of falls in the session"},
                {'level': 'hard', 'text': "Send a radio alert to another micro:bit if fallen"},
            ],
        },
        'ar': {
            'objectif': "يطلق الروبوت إنذاراً إذا هُز أو سقط. يستخدم Gesture.Shake و FreeFall.",
            'materiel': ['micro:bit', 'Maqueen Lite'],
            'etapes': [
                "عند السقوط الحر (Gesture.FreeFall): إنذار أحمر + صافرة عالية",
                "عند الصدمة (Gesture.Shake): اعرض ⚠️ + صفير",
                "الزر A: إعادة، رسالة هادئة",
            ],
            'tip': "FreeFall يكشف عندما يقترب التسارع من 0 (سقوط حر).",
            'defis': [
                {'level': 'med', 'text': "احسب عدد السقطات في الجلسة"},
                {'level': 'hard', 'text': "أرسل تنبيه راديو لـ micro:bit آخر عند السقوط"},
            ],
        },
    },
    37: {
        'en': {
            'objectif': "Attach the micro:bit to your shoe. It counts your steps by detecting acceleration peaks.",
            'materiel': ['micro:bit', 'Elastic band or tape'],
            'etapes': [
                "In loop: read acceleration magnitude",
                "If acceleration > threshold (1800): increment counter",
                "Wait 500ms to avoid counting one step twice",
                "Button A: display total",
            ],
            'tip': "input.acceleration(Dimension.Strength) gives magnitude (always ≥ 0).",
            'defis': [
                {'level': 'easy', 'text': "Play a sound every 10 steps"},
                {'level': 'med', 'text': "Reset with shake"},
            ],
        },
        'ar': {
            'objectif': "ألصق micro:bit بحذائك. يعدّ خطواتك باكتشاف ذرى التسارع.",
            'materiel': ['micro:bit', 'شريط مطاطي أو لاصق'],
            'etapes': [
                "في حلقة: اقرأ مقدار التسارع",
                "إذا التسارع > العتبة (1800): زِد العداد",
                "انتظر 500 ميلي ثانية لتفادي عدّ الخطوة مرتَين",
                "الزر A: اعرض الإجمالي",
            ],
            'tip': "input.acceleration(Dimension.Strength) تعطي المقدار (دائماً ≥ 0).",
            'defis': [
                {'level': 'easy', 'text': "اعزف صوتاً كل 10 خطوات"},
                {'level': 'med', 'text': "إعادة التعيين بالهز"},
            ],
        },
    },
    38: {
        'en': {
            'objectif': "Set up the Maqueen in sentinel mode: if it detects ultrasonic movement, siren + red LED flash.",
            'materiel': ['Maqueen Lite', 'SR04 ultrasonic sensor'],
            'etapes': [
                "Read baseline distance",
                "In loop: compare current distance to baseline",
                "If difference > 20 cm: alarm",
                "Key A: reset baseline (after moving)",
            ],
            'tip': "Wait 5 seconds after boot before reading baseline to allow time to place the robot.",
            'defis': [
                {'level': 'med', 'text': "Count intrusions and display"},
                {'level': 'hard', 'text': "Send a radio message to a surveillance micro:bit"},
            ],
        },
        'ar': {
            'objectif': "ضع الـ Maqueen في وضع الحارس: إذا كشف حركة بالموجات فوق الصوتية، صافرة + وميض LED أحمر.",
            'materiel': ['Maqueen Lite', 'مستشعر SR04'],
            'etapes': [
                "اقرأ المسافة الأساسية",
                "في حلقة: قارن المسافة الحالية بالأساسية",
                "إذا الفرق > 20 سم: إنذار",
                "الزر A: أعِد تعيين الأساسية (بعد التحريك)",
            ],
            'tip': "انتظر 5 ثوانٍ بعد التشغيل قبل قراءة الأساسية لإعطاء وقت لوضع الروبوت.",
            'defis': [
                {'level': 'med', 'text': "احسب التدخلات واعرضها"},
                {'level': 'hard', 'text': "أرسل رسالة راديو إلى micro:bit حارس"},
            ],
        },
    },
    39: {
        'en': {
            'objectif': "Walk the Maqueen around the house. It records the light level at each button press, then displays a graph.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "Button A: record current brightness in an array",
                "Button B: show all values as a bar graph on the LED matrix",
                "Shake: clear the list",
            ],
            'tip': "The 5x5 LED matrix can show 5 readings side-by-side, each from 0 to 5 LEDs tall.",
            'defis': [
                {'level': 'med', 'text': "Save values with their timestamps"},
                {'level': 'hard', 'text': "Send data over radio to another micro:bit that scrolls them"},
            ],
        },
        'ar': {
            'objectif': "تجوّل بالـ Maqueen في المنزل. يسجّل مستوى الضوء عند كل ضغطة زر، ثم يعرض رسماً بيانياً.",
            'materiel': ['Maqueen Lite'],
            'etapes': [
                "الزر A: سجّل السطوع الحالي في مصفوفة",
                "الزر B: اعرض كل القيم كرسم بياني شريطي على مصفوفة LED",
                "هز: امسح القائمة",
            ],
            'tip': "مصفوفة LED 5×5 يمكنها عرض 5 قراءات جنباً إلى جنب، كل منها بطول 0-5 مصابيح.",
            'defis': [
                {'level': 'med', 'text': "احفظ القيم مع أوقاتها"},
                {'level': 'hard', 'text': "أرسل البيانات عبر الراديو إلى micro:bit يمرّرها"},
            ],
        },
    },
    40: {
        'en': {
            'objectif': "Ask a yes/no question to the Maqueen, shake it, and it answers with a mysterious icon. Guaranteed oracle!",
            'materiel': ['micro:bit', 'Maqueen Lite'],
            'etapes': [
                "On Shake: randomly pick from 8 answers",
                "Show matching icon/text",
                "Add a theatrical ambient color",
            ],
            'tip': "The 8 classic answers: YES, NO, MAYBE, OF COURSE, NEVER, ASK LATER, STARS FAVOR, UNCERTAIN.",
            'defis': [
                {'level': 'easy', 'text': "Play a mystical melody before the answer"},
                {'level': 'med', 'text': "After 3 questions, offer a long prophecy (scrolling text)"},
            ],
        },
        'ar': {
            'objectif': "اطرح سؤال نعم/لا على الـ Maqueen، هزّه، فيجيب بأيقونة غامضة. عرّاف مضمون!",
            'materiel': ['micro:bit', 'Maqueen Lite'],
            'etapes': [
                "عند الهز: اختر عشوائياً من 8 إجابات",
                "اعرض الأيقونة/النص المقابل",
                "أضف لوناً محيطاً درامياً",
            ],
            'tip': "الإجابات الثمانية الكلاسيكية: نعم، لا، ربما، بالتأكيد، أبداً، اسأل لاحقاً، النجوم مؤاتية، غير مؤكد.",
            'defis': [
                {'level': 'easy', 'text': "اعزف لحناً غامضاً قبل الإجابة"},
                {'level': 'med', 'text': "بعد 3 أسئلة، قدم نبوءة طويلة (نص متمرر)"},
            ],
        },
    },
    41: {
        'en': {
            'objectif': "On shake, the micro:bit shows a random 1-6 number like a real die. With animation and sound.",
            'materiel': ['micro:bit'],
            'etapes': [
                "On Shake: 'rolling' animation (fast scrolling numbers)",
                "Random draw between 1 and 6",
                "Display the result",
                "Validation beep",
            ],
            'tip': "Show 5-6 random numbers very fast to simulate rolling before the final result.",
            'defis': [
                {'level': 'easy', 'text': "Show die pips (dots) instead of the number"},
                {'level': 'med', 'text': "2-dice mode: sum and display"},
                {'level': 'hard', 'text': "20-sided die for RPGs"},
            ],
        },
        'ar': {
            'objectif': "عند الهز، يعرض micro:bit رقماً عشوائياً من 1 إلى 6 كحجر نرد حقيقي. مع رسوم متحركة وصوت.",
            'materiel': ['micro:bit'],
            'etapes': [
                "عند الهز: رسم متحرك للتدوير (أرقام متمررة بسرعة)",
                "سحب عشوائي بين 1 و 6",
                "اعرض النتيجة",
                "صفير تأكيد",
            ],
            'tip': "اعرض 5-6 أرقام عشوائية بسرعة لمحاكاة التدوير قبل النتيجة النهائية.",
            'defis': [
                {'level': 'easy', 'text': "اعرض نقاط النرد بدل الرقم"},
                {'level': 'med', 'text': "وضع حجرَين: مجموع وعرض"},
                {'level': 'hard', 'text': "نرد بـ 20 وجهاً لألعاب الأدوار"},
            ],
        },
    },
    42: {
        'en': {
            'objectif': "Play rock-paper-scissors against your micro:bit. You shake to make your choice, the micro:bit reveals its own and the result.",
            'materiel': ['micro:bit'],
            'etapes': [
                "Button A = Rock, B = Paper, A+B = Scissors",
                "On human choice: micro:bit picks randomly",
                "Show its choice then compare",
                "Show result: W/L/=",
            ],
            'tip': "Rules: Rock > Scissors > Paper > Rock. Else: tie.",
            'defis': [
                {'level': 'easy', 'text': "Keep win score and show on logo button"},
                {'level': 'med', 'text': "Best of 5 matches"},
            ],
        },
        'ar': {
            'objectif': "العب حجرة-ورقة-مقص ضد micro:bit. تهز لتختار، يكشف هو اختياره والنتيجة.",
            'materiel': ['micro:bit'],
            'etapes': [
                "الزر A = حجرة، B = ورقة، A+B = مقص",
                "عند اختيار الإنسان: micro:bit يختار عشوائياً",
                "اعرض اختياره ثم قارن",
                "اعرض النتيجة: ف/خ/=",
            ],
            'tip': "القواعد: الحجر > المقص > الورقة > الحجر. خلاف ذلك: تعادل.",
            'defis': [
                {'level': 'easy', 'text': "احفظ نقاط الفوز واعرضها على زر الشعار"},
                {'level': 'med', 'text': "أفضل من 5 جولات"},
            ],
        },
    },
    43: {
        'en': {
            'objectif': "The micro:bit shows an arrow sequence (↑↓←→). You repeat it by pressing in the same order. One more arrow each round.",
            'materiel': ['micro:bit'],
            'etapes': [
                "Start with 1 random arrow in the sequence",
                "Show the sequence (arrow + sound)",
                "User presses: A = left, B = right, shake = up, tilt forward = down",
                "If correct: add 1 arrow. Else: game over + score",
            ],
            'tip': "The bigger the sequence, the harder. Level 10 = achievement!",
            'defis': [
                {'level': 'easy', 'text': "Add a different RGB color per direction"},
                {'level': 'hard', 'text': "Save high score and show on startup"},
            ],
        },
        'ar': {
            'objectif': "يعرض micro:bit تسلسل أسهم (↑↓←→). كررها بالضغط بنفس الترتيب. سهم إضافي كل جولة.",
            'materiel': ['micro:bit'],
            'etapes': [
                "ابدأ بسهم عشوائي واحد في التسلسل",
                "اعرض التسلسل (سهم + صوت)",
                "المستخدم يضغط: A = يسار، B = يمين، هز = أعلى، ميل أمام = أسفل",
                "إذا صحيح: أضف سهماً. خلاف ذلك: انتهت اللعبة + النتيجة",
            ],
            'tip': "كلما زاد التسلسل، صعب أكثر. المستوى 10 = إنجاز!",
            'defis': [
                {'level': 'easy', 'text': "أضف لون RGB مختلف لكل اتجاه"},
                {'level': 'hard', 'text': "احفظ أعلى نتيجة واعرضها عند البدء"},
            ],
        },
    },
    44: {
        'en': {
            'objectif': "The robot reacts to the number of claps: 1 clap = red LEDs, 2 claps = green, 3 claps = dance!",
            'materiel': ['micro:bit V2 (built-in mic)', 'Maqueen Lite'],
            'etapes': [
                "Listen for Loud event (loud sound)",
                "Count claps within a 2-second window",
                "Based on total, trigger different action",
            ],
            'tip': "The micro:bit v2 has a Loud event that triggers on sound peaks.",
            'defis': [
                {'level': 'easy', 'text': "4 claps = robot spins full circle"},
                {'level': 'med', 'text': "Clap to turn on, clap again to turn off (hands-free remote)"},
            ],
        },
        'ar': {
            'objectif': "يتفاعل الروبوت مع عدد التصفيقات: 1 = مصابيح حمراء، 2 = خضراء، 3 = رقص!",
            'materiel': ['micro:bit V2 (مايكروفون مدمج)', 'Maqueen Lite'],
            'etapes': [
                "استمع لحدث الصوت العالي",
                "احسب التصفيقات ضمن نافذة ثانيتَين",
                "حسب الإجمالي، شغّل إجراءً مختلفاً",
            ],
            'tip': "micro:bit v2 له حدث loud يُطلق عند ذرى الصوت.",
            'defis': [
                {'level': 'easy', 'text': "4 تصفيقات = يدور الروبوت دورة كاملة"},
                {'level': 'med', 'text': "صفق للتشغيل، صفق مجدداً للإطفاء (تحكم دون يدَين)"},
            ],
        },
    },
    45: {
        'en': {
            'objectif': "Pass the micro:bit from one player to another. If you shake and a red light lights up, you lose! Only chance decides.",
            'materiel': ['micro:bit', 'Maqueen Lite'],
            'etapes': [
                "On Shake: pick random 1-6",
                "If 1: show X + siren + red LEDs → you lose",
                "Otherwise: show ✓ + soft sound + green LEDs → pass to next",
            ],
            'tip': "Great pass-the-parcel game for groups: no one knows who'll lose.",
            'defis': [
                {'level': 'easy', 'text': "Increase difficulty: 2 out of 6 chance to lose"},
                {'level': 'med', 'text': "Tournament mode: count losses of each player with 3 micro:bits"},
            ],
        },
        'ar': {
            'objectif': "مرّر micro:bit من لاعب لآخر. إذا هززت وأضاء ضوء أحمر، خسرت! الصدفة وحدها تقرر.",
            'materiel': ['micro:bit', 'Maqueen Lite'],
            'etapes': [
                "عند الهز: اختر عشوائياً 1-6",
                "إذا 1: اعرض X + صافرة + مصابيح حمراء ← خسرت",
                "خلاف ذلك: اعرض ✓ + صوت ناعم + مصابيح خضراء ← مرر للتالي",
            ],
            'tip': "لعبة تمرير ممتازة للمجموعات: لا أحد يعرف من سيخسر.",
            'defis': [
                {'level': 'easy', 'text': "زِد الصعوبة: 2 من 6 احتمال الخسارة"},
                {'level': 'med', 'text': "وضع البطولة: احسب خسارات كل لاعب بـ 3 micro:bits"},
            ],
        },
    },
}

print(f"Phase 2 translations: {len(TRANSLATIONS_P2)} activities (IDs 17-45)")
