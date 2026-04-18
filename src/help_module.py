"""Help panel content: pinout diagram, code cheatsheet, FAQ — trilingual."""

PINOUT_LABELS = {
    'fr': {
        'rgb_top': 'LEDs NeoPixel RGB ×4', 'rgb_sub': 'P15 · 16M couleurs',
        'microbit': 'micro:bit v1 ou v2',
        'rgb_right': 'LEDs ambiance', 'rgb_right_sub': '(4 NeoPixels)',
        'motor_l': 'Moteur M1 / N20', 'motor_l_sub': 'PWM · 0-255 vitesse',
        'motor_r': 'Moteur M2 / N20', 'motor_r_sub': 'PWM · 0-255 vitesse',
        'led_l': 'LED avant gauche', 'led_l_sub': 'P8 · ON/OFF',
        'led_r': 'LED avant droite', 'led_r_sub': 'P12 · ON/OFF',
        'line_sensors': 'Capteurs ligne IR', 'line_sub': 'P13 (G) · P14 (D) · 0/1',
        'ultra': 'Port ultrasons (SR04)', 'ultra_sub': '3-400 cm · 5V',
        'bat': 'Batterie : 3× AAA', 'bat_sub': 'ou Li-ion 3,7V',
        'ext': 'Extensions (S1, S2, I²C)', 'ext_sub': 'Servo · P0/P1/P2',
    },
    'en': {
        'rgb_top': 'RGB NeoPixel LEDs ×4', 'rgb_sub': 'P15 · 16M colors',
        'microbit': 'micro:bit v1 or v2',
        'rgb_right': 'Ambient LEDs', 'rgb_right_sub': '(4 NeoPixels)',
        'motor_l': 'Motor M1 / N20', 'motor_l_sub': 'PWM · 0-255 speed',
        'motor_r': 'Motor M2 / N20', 'motor_r_sub': 'PWM · 0-255 speed',
        'led_l': 'Front LED left', 'led_l_sub': 'P8 · ON/OFF',
        'led_r': 'Front LED right', 'led_r_sub': 'P12 · ON/OFF',
        'line_sensors': 'IR line sensors', 'line_sub': 'P13 (L) · P14 (R) · 0/1',
        'ultra': 'Ultrasonic port (SR04)', 'ultra_sub': '3-400 cm · 5V',
        'bat': 'Battery: 3× AAA', 'bat_sub': 'or Li-ion 3.7V',
        'ext': 'Extensions (S1, S2, I²C)', 'ext_sub': 'Servo · P0/P1/P2',
    },
    'ar': {
        'rgb_top': 'مصابيح RGB NeoPixel ×4', 'rgb_sub': 'P15 · 16M لون',
        'microbit': 'micro:bit v1 أو v2',
        'rgb_right': 'مصابيح محيطية', 'rgb_right_sub': '(4 NeoPixels)',
        'motor_l': 'محرك M1 / N20', 'motor_l_sub': 'PWM · سرعة 0-255',
        'motor_r': 'محرك M2 / N20', 'motor_r_sub': 'PWM · سرعة 0-255',
        'led_l': 'مصباح أمامي أيسر', 'led_l_sub': 'P8 · تشغيل/إيقاف',
        'led_r': 'مصباح أمامي أيمن', 'led_r_sub': 'P12 · تشغيل/إيقاف',
        'line_sensors': 'مستشعرات خط IR', 'line_sub': 'P13 (يسار) · P14 (يمين) · 0/1',
        'ultra': 'منفذ الموجات فوق الصوتية (SR04)', 'ultra_sub': '3-400 سم · 5V',
        'bat': 'البطارية: 3× AAA', 'bat_sub': 'أو Li-ion 3.7V',
        'ext': 'التمديدات (S1, S2, I²C)', 'ext_sub': 'سيرفو · P0/P1/P2',
    },
}

def gen_pinout_svg(lang='fr'):
    L = PINOUT_LABELS[lang]
    return f'''<svg viewBox="0 0 600 440" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<defs>
  <filter id="pglow-{lang}"><feGaussianBlur stdDeviation="2" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <linearGradient id="bodygrd-{lang}" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#d4af37" stop-opacity="0.2"/>
    <stop offset="100%" stop-color="#8b7820" stop-opacity="0.3"/>
  </linearGradient>
</defs>
<rect x="140" y="140" width="320" height="160" rx="24" fill="url(#bodygrd-{lang})" stroke="#d4af37" stroke-width="2"/>
<rect x="230" y="170" width="140" height="100" rx="6" fill="#050510"/>
<text x="300" y="225" text-anchor="middle" fill="#888" font-family="system-ui" font-size="12">micro:bit</text>
<circle cx="155" cy="220" r="32" fill="#2a2a2a" stroke="#555" stroke-width="2"/>
<circle cx="155" cy="220" r="12" fill="#666"/>
<circle cx="445" cy="220" r="32" fill="#2a2a2a" stroke="#555" stroke-width="2"/>
<circle cx="445" cy="220" r="12" fill="#666"/>
<circle cx="215" cy="310" r="10" fill="#ff0055" filter="url(#pglow-{lang})"/>
<circle cx="385" cy="310" r="10" fill="#ff0055" filter="url(#pglow-{lang})"/>
<circle cx="180" cy="160" r="6" fill="#a855f7" filter="url(#pglow-{lang})"/>
<circle cx="235" cy="145" r="6" fill="#22d3ee" filter="url(#pglow-{lang})"/>
<circle cx="365" cy="145" r="6" fill="#10b981" filter="url(#pglow-{lang})"/>
<circle cx="420" cy="160" r="6" fill="#eab308" filter="url(#pglow-{lang})"/>
<rect x="245" y="295" width="14" height="8" rx="2" fill="#666" stroke="#333"/>
<rect x="341" y="295" width="14" height="8" rx="2" fill="#666" stroke="#333"/>
<rect x="280" y="320" width="40" height="14" rx="4" fill="#333" stroke="#777"/>
<circle cx="290" cy="327" r="4" fill="#444"/>
<circle cx="310" cy="327" r="4" fill="#444"/>
<g font-family="system-ui, sans-serif" font-size="11" fill="#d0ddf0">
  <line x1="180" y1="160" x2="90" y2="80" stroke="#a855f7" stroke-width="1.5"/>
  <text x="20" y="75" fill="#a855f7">{L["rgb_top"]}</text>
  <text x="20" y="88" fill="#888" font-size="10">{L["rgb_sub"]}</text>
  <line x1="300" y1="170" x2="300" y2="120" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="300" y="110" text-anchor="middle" fill="#3b82f6">{L["microbit"]}</text>
  <line x1="420" y1="160" x2="510" y2="80" stroke="#eab308" stroke-width="1.5"/>
  <text x="515" y="75" fill="#eab308">{L["rgb_right"]}</text>
  <text x="515" y="88" fill="#888" font-size="10">{L["rgb_right_sub"]}</text>
  <line x1="155" y1="220" x2="60" y2="200" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="20" y="195" fill="#60a5fa">{L["motor_l"]}</text>
  <text x="20" y="208" fill="#888" font-size="10">{L["motor_l_sub"]}</text>
  <line x1="445" y1="220" x2="540" y2="200" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="548" y="195" fill="#60a5fa">{L["motor_r"]}</text>
  <text x="548" y="208" fill="#888" font-size="10">{L["motor_r_sub"]}</text>
  <line x1="215" y1="310" x2="100" y2="370" stroke="#ff0055" stroke-width="1.5"/>
  <text x="20" y="368" fill="#ff0055">{L["led_l"]}</text>
  <text x="20" y="381" fill="#888" font-size="10">{L["led_l_sub"]}</text>
  <line x1="385" y1="310" x2="500" y2="370" stroke="#ff0055" stroke-width="1.5"/>
  <text x="505" y="368" fill="#ff0055">{L["led_r"]}</text>
  <text x="505" y="381" fill="#888" font-size="10">{L["led_r_sub"]}</text>
  <line x1="252" y1="303" x2="180" y2="405" stroke="#10b981" stroke-width="1.5"/>
  <text x="60" y="420" fill="#10b981">{L["line_sensors"]}</text>
  <text x="60" y="433" fill="#888" font-size="10">{L["line_sub"]}</text>
  <line x1="300" y1="335" x2="300" y2="395" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="300" y="418" text-anchor="middle" fill="#f59e0b">{L["ultra"]}</text>
  <text x="300" y="432" text-anchor="middle" fill="#888" font-size="10">{L["ultra_sub"]}</text>
  <text x="550" y="260" text-anchor="end" fill="#eab308" font-size="10">{L["bat"]}</text>
  <text x="550" y="273" text-anchor="end" fill="#888" font-size="9">{L["bat_sub"]}</text>
  <text x="50" y="260" fill="#22d3ee" font-size="10">{L["ext"]}</text>
  <text x="50" y="273" fill="#888" font-size="9">{L["ext_sub"]}</text>
</g>
</svg>'''

PINOUT_SVG = gen_pinout_svg('fr')  # backward compat


CHEATSHEET_SECTIONS = [
    {
        'title_fr': 'Moteurs', 'title_en': 'Motors', 'title_ar': 'المحركات', 'icon': '🚗',
        'items': [
            {
                'pattern_fr': 'Avancer', 'pattern_en': 'Move forward', 'pattern_ar': 'التقدم للأمام',
                'js': 'maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 150)',
                'py': 'maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 150)',
                'note_fr': 'Vitesse 0-255 · CW = horaire · Motors.M1 (gauche), M2 (droite), All',
                'note_en': 'Speed 0-255 · CW = clockwise · Motors.M1 (left), M2 (right), All',
                'note_ar': 'السرعة 0-255 · CW = باتجاه عقارب الساعة · Motors.M1 (يسار)، M2 (يمين)، All',
            },
            {
                'pattern_fr': 'Reculer', 'pattern_en': 'Move backward', 'pattern_ar': 'التراجع للخلف',
                'js': 'maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 150)',
                'py': 'maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 150)',
                'note_fr': 'CCW = anti-horaire',
                'note_en': 'CCW = counter-clockwise',
                'note_ar': 'CCW = عكس عقارب الساعة',
            },
            {
                'pattern_fr': 'Tourner à droite (pivot)', 'pattern_en': 'Turn right (pivot)', 'pattern_ar': 'الاستدارة لليمين (محور)',
                'js': 'maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 150)\nmaqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 150)',
                'py': 'maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 150)\nmaqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 150)',
                'note_fr': 'Chaque moteur dans une direction = rotation sur place',
                'note_en': 'Each motor in opposite direction = in-place rotation',
                'note_ar': 'كل محرك في اتجاه مختلف = دوران في المكان',
            },
            {
                'pattern_fr': 'Arrêter', 'pattern_en': 'Stop', 'pattern_ar': 'الإيقاف',
                'js': 'maqueen.motorStop(maqueen.Motors.All)',
                'py': 'maqueen.motor_stop(maqueen.Motors.ALL)',
                'note_fr': 'Stop immédiat des 2 moteurs',
                'note_en': 'Immediate stop of both motors',
                'note_ar': 'توقف فوري للمحركين',
            },
        ],
    },
    {
        'title_fr': 'LEDs avant', 'title_en': 'Front LEDs', 'title_ar': 'المصابيح الأمامية', 'icon': '💡',
        'items': [
            {
                'pattern_fr': 'Allumer LED gauche', 'pattern_en': 'Turn on left LED', 'pattern_ar': 'تشغيل المصباح الأيسر',
                'js': 'maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)',
                'py': 'maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)',
                'note_fr': 'LEDLeft/LEDRight · turnOn/turnOff (ou bien pins.digitalWritePin P8/P12)',
                'note_en': 'LEDLeft/LEDRight · turnOn/turnOff (or pins.digitalWritePin P8/P12)',
                'note_ar': 'LEDLeft/LEDRight · turnOn/turnOff (أو pins.digitalWritePin P8/P12)',
            },
            {
                'pattern_fr': 'Allumer LED droite', 'pattern_en': 'Turn on right LED', 'pattern_ar': 'تشغيل المصباح الأيمن',
                'js': 'maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)',
                'py': 'maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)',
                'note_fr': '', 'note_en': '', 'note_ar': '',
            },
        ],
    },
    {
        'title_fr': 'LEDs RGB ambiance', 'title_en': 'RGB ambient LEDs', 'title_ar': 'مصابيح RGB المحيطية', 'icon': '🌈',
        'items': [
            {
                'pattern_fr': '⚙️ Initialisation (une seule fois, en haut du code)',
                'pattern_en': '⚙️ Setup (once, at the top of your code)',
                'pattern_ar': '⚙️ التهيئة (مرة واحدة، في أعلى الكود)',
                'js': 'let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)',
                'py': 'strip = neopixel.create(DigitalPin.P15, 4, neopixel.NeoPixelMode.RGB)',
                'note_fr': 'Nécessite l\'extension « neopixel » · 4 LEDs sur P15',
                'note_en': 'Requires the "neopixel" extension · 4 LEDs on P15',
                'note_ar': 'يتطلب امتداد «neopixel» · 4 مصابيح على P15',
            },
            {
                'pattern_fr': 'Toutes les LEDs rouges', 'pattern_en': 'All LEDs red', 'pattern_ar': 'كل المصابيح حمراء',
                'js': 'strip.showColor(neopixel.colors(NeoPixelColors.Red))',
                'py': 'strip.show_color(neopixel.colors(NeoPixelColors.RED))',
                'note_fr': 'Couleurs : Red, Green, Blue, Yellow, Purple, White, Black (off)',
                'note_en': 'Colors: Red, Green, Blue, Yellow, Purple, White, Black (off)',
                'note_ar': 'الألوان: Red, Green, Blue, Yellow, Purple, White, Black (إيقاف)',
            },
            {
                'pattern_fr': 'Couleur RGB custom', 'pattern_en': 'Custom RGB color', 'pattern_ar': 'لون RGB مخصص',
                'js': 'strip.showColor(neopixel.rgb(255, 100, 0))',
                'py': 'strip.show_color(neopixel.rgb(255, 100, 0))',
                'note_fr': 'rgb(rouge, vert, bleu), 0-255 par canal',
                'note_en': 'rgb(red, green, blue), 0-255 per channel',
                'note_ar': 'rgb(أحمر، أخضر، أزرق)، 0-255 لكل قناة',
            },
            {
                'pattern_fr': 'Éteindre toutes les LEDs', 'pattern_en': 'Turn off all LEDs', 'pattern_ar': 'إطفاء كل المصابيح',
                'js': 'strip.clear()\nstrip.show()',
                'py': 'strip.clear()\nstrip.show()',
                'note_fr': '`.clear()` prépare, `.show()` applique',
                'note_en': '`.clear()` prepares, `.show()` applies',
                'note_ar': '`.clear()` يحضّر، `.show()` يطبّق',
            },
            {
                'pattern_fr': 'Une seule LED (index 0-3)', 'pattern_en': 'Single LED (index 0-3)', 'pattern_ar': 'مصباح واحد (الفهرس 0-3)',
                'js': 'strip.setPixelColor(0, neopixel.rgb(255, 0, 0))\nstrip.show()',
                'py': 'strip.set_pixel_color(0, neopixel.rgb(255, 0, 0))\nstrip.show()',
                'note_fr': 'Index 0-3 pour les 4 LEDs · appeler `.show()` pour appliquer',
                'note_en': 'Index 0-3 for the 4 LEDs · call `.show()` to apply',
                'note_ar': 'الفهرس 0-3 للمصابيح الأربعة · استدعِ `.show()` للتطبيق',
            },
        ],
    },
    {
        'title_fr': 'Capteurs', 'title_en': 'Sensors', 'title_ar': 'المستشعرات', 'icon': '📡',
        'items': [
            {
                'pattern_fr': 'Lire capteur de ligne gauche', 'pattern_en': 'Read left line sensor', 'pattern_ar': 'قراءة مستشعر الخط الأيسر',
                'js': 'let left = maqueen.readPatrol(maqueen.Patrol.PatrolLeft)',
                'py': 'left = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)',
                'note_fr': '0 = blanc, 1 = noir (ligne détectée) · PatrolRight pour le droit',
                'note_en': '0 = white, 1 = black (line detected) · PatrolRight for the right',
                'note_ar': '0 = أبيض، 1 = أسود (تم كشف الخط) · PatrolRight لليمين',
            },
            {
                'pattern_fr': 'Lire distance ultrasons', 'pattern_en': 'Read ultrasonic distance', 'pattern_ar': 'قراءة المسافة بالموجات فوق الصوتية',
                'js': 'let d = maqueen.Ultrasonic()',
                'py': 'd = maqueen.ultrasonic()',
                'note_fr': 'Portée : 3 à 400 cm · < 3 = erreur',
                'note_en': 'Range: 3 to 400 cm · < 3 = error',
                'note_ar': 'المدى: 3 إلى 400 سم · < 3 = خطأ',
            },
            {
                'pattern_fr': 'Lire luminosité (micro:bit)', 'pattern_en': 'Read brightness (micro:bit)', 'pattern_ar': 'قراءة السطوع (micro:bit)',
                'js': 'let light = input.lightLevel()',
                'py': 'light = input.light_level()',
                'note_fr': '0 (noir) à 255 (plein soleil)',
                'note_en': '0 (dark) to 255 (full sun)',
                'note_ar': '0 (معتم) إلى 255 (شمس ساطعة)',
            },
        ],
    },
    {
        'title_fr': 'Servo & extensions', 'title_en': 'Servo & extensions', 'title_ar': 'السيرفو والتمديدات', 'icon': '🔧',
        'items': [
            {
                'pattern_fr': 'Positionner servo (S1)', 'pattern_en': 'Position servo (S1)', 'pattern_ar': 'تحديد موضع السيرفو (S1)',
                'js': 'maqueen.servoRun(maqueen.Servos.S1, 90)',
                'py': 'maqueen.servo_run(maqueen.Servos.S1, 90)',
                'note_fr': 'Angle 0-180° · Servos.S1 / Servos.S2',
                'note_en': 'Angle 0-180° · Servos.S1 / Servos.S2',
                'note_ar': 'زاوية 0-180° · Servos.S1 / Servos.S2',
            },
        ],
    },
    {
        'title_fr': 'Son (buzzer)', 'title_en': 'Sound (buzzer)', 'title_ar': 'الصوت (الصفارة)', 'icon': '🎵',
        'items': [
            {
                'pattern_fr': 'Jouer une note', 'pattern_en': 'Play a note', 'pattern_ar': 'عزف نغمة',
                'js': 'music.playTone(262, 500)',
                'py': 'music.play_tone(262, 500)',
                'note_fr': '262 Hz = Do médian · 500 ms durée',
                'note_en': '262 Hz = middle C · 500 ms duration',
                'note_ar': '262 Hz = دو الأوسط · مدة 500 مللي ثانية',
            },
            {
                'pattern_fr': 'Mélodie intégrée', 'pattern_en': 'Built-in melody', 'pattern_ar': 'لحن مدمج',
                'js': 'music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)',
                'py': 'music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)',
                'note_fr': 'Melodies.Dadadadum, Birthday, Entertainer, Prelude, ODE, etc.',
                'note_en': 'Melodies.Dadadadum, Birthday, Entertainer, Prelude, ODE, etc.',
                'note_ar': 'Melodies.Dadadadum، Birthday، Entertainer، Prelude، ODE، إلخ.',
            },
        ],
    },
    {
        'title_fr': 'Radio (communication)', 'title_en': 'Radio (communication)', 'title_ar': 'الراديو (الاتصال)', 'icon': '📻',
        'items': [
            {
                'pattern_fr': 'Configurer groupe', 'pattern_en': 'Set group', 'pattern_ar': 'تعيين المجموعة',
                'js': 'radio.setGroup(7)',
                'py': 'radio.set_group(7)',
                'note_fr': 'Groupe 0-255 · Même groupe = même canal',
                'note_en': 'Group 0-255 · Same group = same channel',
                'note_ar': 'المجموعة 0-255 · نفس المجموعة = نفس القناة',
            },
            {
                'pattern_fr': 'Envoyer', 'pattern_en': 'Send', 'pattern_ar': 'إرسال',
                'js': 'radio.sendString("hello")\nradio.sendValue("temp", 22)',
                'py': 'radio.send_string("hello")\nradio.send_value("temp", 22)',
                'note_fr': 'Portée ~70m en champ libre',
                'note_en': 'Range ~70m in open field',
                'note_ar': 'المدى ~70م في الفضاء المفتوح',
            },
            {
                'pattern_fr': 'Recevoir', 'pattern_en': 'Receive', 'pattern_ar': 'استقبال',
                'js': 'radio.onReceivedString(function (s) { basic.showString(s) })',
                'py': 'def on_recv(s):\n    basic.show_string(s)\nradio.on_received_string(on_recv)',
                'note_fr': '', 'note_en': '', 'note_ar': '',
            },
        ],
    },
    {
        'title_fr': 'Interaction', 'title_en': 'Interaction', 'title_ar': 'التفاعل', 'icon': '🎮',
        'items': [
            {
                'pattern_fr': 'Bouton A pressé', 'pattern_en': 'Button A pressed', 'pattern_ar': 'الضغط على الزر A',
                'js': 'input.onButtonPressed(Button.A, function () { /* ... */ })',
                'py': 'def on_a():\n    pass\ninput.on_button_pressed(Button.A, on_a)',
                'note_fr': 'Button.A, Button.B, Button.AB (les deux)',
                'note_en': 'Button.A, Button.B, Button.AB (both)',
                'note_ar': 'Button.A، Button.B، Button.AB (كلاهما)',
            },
            {
                'pattern_fr': 'Secoue détectée', 'pattern_en': 'Shake detected', 'pattern_ar': 'كشف الاهتزاز',
                'js': 'input.onGesture(Gesture.Shake, function () { /* ... */ })',
                'py': 'def on_shake():\n    pass\ninput.on_gesture(Gesture.SHAKE, on_shake)',
                'note_fr': 'Autres : TiltLeft, TiltRight, LogoUp, ScreenUp',
                'note_en': 'Others: TiltLeft, TiltRight, LogoUp, ScreenUp',
                'note_ar': 'أخرى: TiltLeft، TiltRight، LogoUp، ScreenUp',
            },
        ],
    },
    {
        'title_fr': 'Affichage', 'title_en': 'Display', 'title_ar': 'العرض', 'icon': '📺',
        'items': [
            {
                'pattern_fr': 'Afficher un texte', 'pattern_en': 'Show text', 'pattern_ar': 'عرض نص',
                'js': 'basic.showString("Hello")',
                'py': 'basic.show_string("Hello")',
                'note_fr': 'Défile sur les 25 LEDs',
                'note_en': 'Scrolls across the 25 LEDs',
                'note_ar': 'يتحرك على المصابيح الـ25',
            },
            {
                'pattern_fr': 'Afficher un nombre', 'pattern_en': 'Show number', 'pattern_ar': 'عرض رقم',
                'js': 'basic.showNumber(42)',
                'py': 'basic.show_number(42)',
                'note_fr': '', 'note_en': '', 'note_ar': '',
            },
            {
                'pattern_fr': 'Icône prédéfinie', 'pattern_en': 'Predefined icon', 'pattern_ar': 'أيقونة معرّفة مسبقاً',
                'js': 'basic.showIcon(IconNames.Heart)',
                'py': 'basic.show_icon(IconNames.HEART)',
                'note_fr': 'Heart, Happy, Sad, Duck, House, Skull, Yes, No…',
                'note_en': 'Heart, Happy, Sad, Duck, House, Skull, Yes, No…',
                'note_ar': 'Heart, Happy, Sad, Duck, House, Skull, Yes, No…',
            },
            {
                'pattern_fr': 'Effacer écran', 'pattern_en': 'Clear screen', 'pattern_ar': 'مسح الشاشة',
                'js': 'basic.clearScreen()',
                'py': 'basic.clear_screen()',
                'note_fr': '', 'note_en': '', 'note_ar': '',
            },
        ],
    },
]


FAQ = [
    {
        'q_fr': 'Mon robot ne bouge pas quand je lance le code',
        'q_en': "My robot doesn't move when I run the code",
        'q_ar': 'روبوتي لا يتحرك عند تشغيل الكود',
        'a_fr': [
            '✓ Interrupteur ON (souvent oublié — sur le côté du Maqueen)',
            '✓ Les 3 piles AAA sont-elles neuves ? Sous 2V, les LEDs allument mais le moteur ne tourne plus',
            '✓ Le micro:bit est-il bien enfoncé dans le connecteur ?',
            '✓ As-tu installé l\'extension « maqueen » dans MakeCode (Extensions → chercher « maqueen ») ?',
            '✓ As-tu bien téléversé le .hex sur le micro:bit (la LED jaune a-t-elle clignoté lors du transfert) ?',
        ],
        'a_en': [
            '✓ Switch ON (often forgotten — on the side of the Maqueen)',
            '✓ Are the 3 AAA batteries fresh? Below 2V, LEDs light but motor won\'t turn',
            '✓ Is the micro:bit fully seated in the connector?',
            '✓ Did you install the "maqueen" extension in MakeCode (Extensions → search "maqueen")?',
            '✓ Did you upload the .hex to the micro:bit (did the yellow LED blink during transfer)?',
        ],
        'a_ar': [
            '✓ زر التشغيل ON (غالباً ما يُنسى — على جانب Maqueen)',
            '✓ هل البطاريات AAA الثلاث جديدة؟ تحت 2V، تضيء المصابيح لكن المحرك لا يدور',
            '✓ هل micro:bit مُثبت بإحكام في الموصل؟',
            '✓ هل ثبّتت امتداد «maqueen» في MakeCode (Extensions → ابحث عن «maqueen»)؟',
            '✓ هل رفعت ملف .hex إلى micro:bit (هل ومض المصباح الأصفر أثناء النقل)؟',
        ],
    },
    {
        'q_fr': 'Le robot tourne en rond / ne suit pas la ligne correctement',
        'q_en': "Robot spins in circles / doesn't follow the line correctly",
        'q_ar': 'الروبوت يدور في دوائر / لا يتبع الخط بشكل صحيح',
        'a_fr': [
            '✓ Calibration des capteurs : ajuste les petites vis sous le robot',
            '✓ La ligne doit être noire mate sur fond blanc (pas brillant — évite le scotch brillant)',
            '✓ Largeur ligne idéale : 1,5 à 2 cm',
            '✓ Vitesse trop élevée = le robot « perd » la ligne dans les virages',
            '✓ Luminosité ambiante : évite le plein soleil ou les néons clignotants',
        ],
        'a_en': [
            '✓ Sensor calibration: adjust the small screws under the robot',
            '✓ Line must be matte black on white background (not shiny — avoid shiny tape)',
            '✓ Ideal line width: 1.5 to 2 cm',
            '✓ Too high speed = robot "loses" the line in curves',
            '✓ Ambient light: avoid direct sunlight or flickering fluorescent bulbs',
        ],
        'a_ar': [
            '✓ معايرة المستشعرات: اضبط البراغي الصغيرة تحت الروبوت',
            '✓ يجب أن يكون الخط أسود مطفي على خلفية بيضاء (غير لامع — تجنب الشريط اللامع)',
            '✓ العرض المثالي للخط: 1.5 إلى 2 سم',
            '✓ سرعة عالية جداً = الروبوت «يفقد» الخط في المنعطفات',
            '✓ الإضاءة المحيطة: تجنب ضوء الشمس المباشر أو النيون الوامض',
        ],
    },
    {
        'q_fr': 'L\'ultrason renvoie 0 ou des valeurs absurdes',
        'q_en': 'Ultrasonic returns 0 or nonsense values',
        'q_ar': 'الموجات فوق الصوتية ترجع 0 أو قيماً غير منطقية',
        'a_fr': [
            '✓ Vérifie la connexion du capteur (4 broches : VCC, Trig, Echo, GND)',
            '✓ Le capteur doit pointer droit devant, pas d\'angle',
            '✓ Portée utile : 3 cm à 400 cm · sous 3 cm retour aléatoire',
            '✓ Les tissus et mousses absorbent — difficile à détecter',
            '✓ Pause de 50-100 ms entre deux lectures pour éviter les échos',
        ],
        'a_en': [
            '✓ Check sensor connection (4 pins: VCC, Trig, Echo, GND)',
            '✓ Sensor must point straight ahead, no angle',
            '✓ Useful range: 3 cm to 400 cm · under 3 cm returns random values',
            '✓ Fabrics and foam absorb — hard to detect',
            '✓ 50-100 ms pause between readings to avoid echoes',
        ],
        'a_ar': [
            '✓ افحص توصيل المستشعر (4 دبابيس: VCC، Trig، Echo، GND)',
            '✓ يجب أن يشير المستشعر للأمام مباشرة، بدون زاوية',
            '✓ المدى المفيد: 3 سم إلى 400 سم · تحت 3 سم ترجع قيم عشوائية',
            '✓ الأقمشة والإسفنج تمتص الصوت — يصعب اكتشافها',
            '✓ توقف 50-100 مللي ثانية بين القراءات لتجنب الأصداء',
        ],
    },
    {
        'q_fr': 'Les LEDs RGB ne s\'allument pas',
        'q_en': "RGB LEDs don't light up",
        'q_ar': 'مصابيح RGB لا تضيء',
        'a_fr': [
            '✓ Installe l\'extension « neopixel » en plus de « maqueen »',
            '✓ Crée un strip : `let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)` puis utilise `strip.showColor(...)`',
            '✓ Les LEDs RGB sont sur P15 (4 NeoPixels)',
            '✓ Pour une couleur très vive, utilise 255 par canal (ex: rgb(255,0,0))',
        ],
        'a_en': [
            '✓ Install the "neopixel" extension in addition to "maqueen"',
            '✓ Create a strip: `let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)`, then use `strip.showColor(...)`',
            '✓ RGB LEDs are on P15 (4 NeoPixels)',
            '✓ For very bright color, use 255 per channel (e.g. rgb(255,0,0))',
        ],
        'a_ar': [
            '✓ ثبّت امتداد «neopixel» بالإضافة إلى «maqueen»',
            '✓ أنشئ strip: `let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)` ثم استخدم `strip.showColor(...)`',
            '✓ مصابيح RGB على P15 (4 NeoPixels)',
            '✓ للحصول على لون مشع جداً، استخدم 255 لكل قناة (مثلاً rgb(255,0,0))',
        ],
    },
    {
        'q_fr': 'Les deux robots ne se parlent pas en radio',
        'q_en': "The two robots don't talk to each other over radio",
        'q_ar': 'الروبوتان لا يتواصلان عبر الراديو',
        'a_fr': [
            '✓ Les deux doivent avoir radio.setGroup(X) avec le MÊME nombre X',
            '✓ Utilise un groupe unique (ex: 42) pas 0 qui est le défaut partagé par tout le monde',
            '✓ Portée : ~70m en extérieur, ~10m à travers murs',
            '✓ radio.setTransmitPower(7) pour puissance max',
        ],
        'a_en': [
            '✓ Both must have radio.setGroup(X) with the SAME number X',
            '✓ Use a unique group (e.g. 42) not 0 which is everyone\'s default',
            '✓ Range: ~70m outdoors, ~10m through walls',
            '✓ radio.setTransmitPower(7) for max power',
        ],
        'a_ar': [
            '✓ يجب أن يكون لكليهما radio.setGroup(X) بنفس الرقم X',
            '✓ استخدم مجموعة فريدة (مثلاً 42) وليس 0 وهي المجموعة الافتراضية للجميع',
            '✓ المدى: ~70م في الخارج، ~10م عبر الجدران',
            '✓ radio.setTransmitPower(7) للحصول على أقصى قوة',
        ],
    },
    {
        'q_fr': 'Ma télécommande IR ne fait rien',
        'q_en': "My IR remote does nothing",
        'q_ar': 'جهاز التحكم IR الخاص بي لا يفعل شيئاً',
        'a_fr': [
            '✓ La télécommande est dans le kit ROB0148-EN-3 (pas le kit standard)',
            '✓ Le capteur IR est sur P16 — pas besoin de brancher',
            '✓ Enlève le film plastique de la pile bouton de la télécommande (souvent oublié)',
            '✓ Pointe la télécommande directement vers l\'avant du Maqueen',
            '✓ Les codes touches varient par télécommande — utilise l\'activité #9 pour noter les tiens',
        ],
        'a_en': [
            '✓ The remote comes with the ROB0148-EN-3 kit (not the standard kit)',
            '✓ IR sensor is on P16 — no need to connect',
            '✓ Remove the plastic film from the remote\'s button battery (often forgotten)',
            '✓ Point the remote directly at the Maqueen\'s front',
            '✓ Button codes vary by remote — use activity #9 to note yours',
        ],
        'a_ar': [
            '✓ جهاز التحكم يأتي مع طقم ROB0148-EN-3 (وليس الطقم القياسي)',
            '✓ مستشعر IR على P16 — لا حاجة للتوصيل',
            '✓ أزل الشريط البلاستيكي من بطارية زر جهاز التحكم (غالباً ما يُنسى)',
            '✓ وجّه جهاز التحكم مباشرة نحو مقدمة Maqueen',
            '✓ رموز الأزرار تختلف حسب جهاز التحكم — استخدم النشاط #9 لتسجيل رموزك',
        ],
    },
    {
        'q_fr': 'CreateAI / Teachable Machine : le modèle ne marche pas',
        'q_en': "CreateAI / Teachable Machine: the model isn't working",
        'q_ar': 'CreateAI / Teachable Machine: النموذج لا يعمل',
        'a_fr': [
            '✓ CreateAI nécessite un micro:bit v2 (avec accéléromètre haute résolution)',
            '✓ Minimum 30 échantillons par classe pour un modèle utilisable',
            '✓ Varie les conditions (vitesse, position, environnement) à l\'entraînement',
            '✓ Teachable Machine s\'exécute dans le navigateur — le robot reçoit via radio',
            '✓ Latence typique : 200-500ms entre l\'action et la réaction du robot',
        ],
        'a_en': [
            '✓ CreateAI requires a micro:bit v2 (with high-resolution accelerometer)',
            '✓ Minimum 30 samples per class for a usable model',
            '✓ Vary conditions (speed, position, environment) during training',
            '✓ Teachable Machine runs in the browser — robot receives via radio',
            '✓ Typical latency: 200-500ms between action and robot reaction',
        ],
        'a_ar': [
            '✓ CreateAI يتطلب micro:bit v2 (بمقياس تسارع عالي الدقة)',
            '✓ 30 عينة كحد أدنى لكل صنف للحصول على نموذج قابل للاستخدام',
            '✓ نوّع الظروف (السرعة، الموضع، البيئة) أثناء التدريب',
            '✓ Teachable Machine يعمل في المتصفح — الروبوت يستقبل عبر الراديو',
            '✓ التأخير النموذجي: 200-500 مللي ثانية بين الإجراء ورد فعل الروبوت',
        ],
    },
    {
        'q_fr': 'Le robot est lent / saccadé',
        'q_en': "Robot is slow / jerky",
        'q_ar': 'الروبوت بطيء / متقطع',
        'a_fr': [
            '✓ Piles faibles — change-les (ne mélange pas anciennes et nouvelles)',
            '✓ Vitesse < 50 = moteurs en limite — utilise ≥ 80 pour fluidité',
            '✓ Trop de basic.pause() dans ta boucle = saccades',
            '✓ Les surfaces moquette / tapis freinent considérablement',
            '✓ Le poids (ajouts sur le robot) réduit la vitesse — reste léger',
        ],
        'a_en': [
            '✓ Weak batteries — replace them (don\'t mix old and new)',
            '✓ Speed < 50 = motors at limit — use ≥ 80 for smoothness',
            '✓ Too many basic.pause() in your loop = jerky behavior',
            '✓ Carpet / rug surfaces slow it down considerably',
            '✓ Weight (additions on the robot) reduces speed — stay light',
        ],
        'a_ar': [
            '✓ بطاريات ضعيفة — استبدلها (لا تخلط القديمة مع الجديدة)',
            '✓ السرعة < 50 = المحركات عند الحد — استخدم ≥ 80 للسلاسة',
            '✓ الكثير من basic.pause() في حلقتك = تقطع',
            '✓ سطوح السجاد / البساط تبطئه كثيراً',
            '✓ الوزن (إضافات على الروبوت) يقلل السرعة — ابقِه خفيفاً',
        ],
    },
    {
        'q_fr': 'Erreur 020 / 050 / autre code face triste sur le micro:bit',
        'q_en': "Error 020 / 050 / other sad-face code on the micro:bit",
        'q_ar': 'خطأ 020 / 050 / رمز وجه حزين آخر على micro:bit',
        'a_fr': [
            '✓ 020 = division par 0 — vérifie tes calculs',
            '✓ 050 = problème radio — appelle radio.setGroup() avant d\'utiliser la radio',
            '✓ 980 = accélération hors limites — vérifie que les valeurs ont du sens',
            '✓ Face triste persistante = téléverser à nouveau (bouton reset)',
        ],
        'a_en': [
            '✓ 020 = division by 0 — check your calculations',
            '✓ 050 = radio issue — call radio.setGroup() before using radio',
            '✓ 980 = acceleration out of range — check values make sense',
            '✓ Persistent sad face = upload again (reset button)',
        ],
        'a_ar': [
            '✓ 020 = قسمة على 0 — تحقق من حساباتك',
            '✓ 050 = مشكلة راديو — استدعِ radio.setGroup() قبل استخدام الراديو',
            '✓ 980 = تسارع خارج النطاق — تحقق من منطقية القيم',
            '✓ وجه حزين مستمر = أعد الرفع (زر إعادة التعيين)',
        ],
    },
    {
        'q_fr': 'Comment imprimer ce guide pour la classe ?',
        'q_en': 'How to print this guide for class?',
        'q_ar': 'كيف أطبع هذا الدليل للصف؟',
        'a_fr': [
            '✓ Ctrl+P (ou Cmd+P sur Mac) dans le navigateur',
            '✓ Le CSS d\'impression retire automatiquement sidebar, panneaux et boutons',
            '✓ Format recommandé : A4, orientation portrait',
            '✓ Les couleurs sont adaptées pour bien rendre en imprimante',
            '✓ Chaque activité tient idéalement sur 1-2 pages',
        ],
        'a_en': [
            '✓ Ctrl+P (or Cmd+P on Mac) in the browser',
            '✓ Print CSS automatically removes sidebar, panels, and buttons',
            '✓ Recommended format: A4, portrait orientation',
            '✓ Colors are adapted for good printing',
            '✓ Each activity ideally fits on 1-2 pages',
        ],
        'a_ar': [
            '✓ Ctrl+P (أو Cmd+P على Mac) في المتصفح',
            '✓ CSS الطباعة يزيل تلقائياً الشريط الجانبي والألواح والأزرار',
            '✓ التنسيق الموصى به: A4، اتجاه عمودي',
            '✓ الألوان مُكيّفة للطباعة الجيدة',
            '✓ كل نشاط يتسع مثالياً على صفحة أو صفحتين',
        ],
    },
]

print(f"Help content: {len(CHEATSHEET_SECTIONS)} cheatsheet sections, {len(FAQ)} FAQ entries (trilingual)")
