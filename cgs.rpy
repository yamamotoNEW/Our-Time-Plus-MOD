image m_cg1_eye:
    "mod_assets/m_cg1_eye_1.png"
    choice:
        8.0
    choice:
        6.0
    choice:
        2.5
    "mod_assets/m_cg1_eye_0.png"
    0.1
    repeat

image m_cg1_base_mouth:
    "mod_assets/m_cg1_base_mouth_1.png"
    0.18
    "mod_assets/m_cg1_base_mouth_0.png"
    0.18
    repeat

image m_cg1_exp1_mouth:
    "mod_assets/m_cg1_exp1_mouth_1.png"
    0.18
    "mod_assets/m_cg1_exp1_mouth_0.png"
    0.18
    repeat
    
image m_cg1_base = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg1_base.png", (0, 0), "m_cg1_eye", (0, 0), WhileSpeaking("monika", "m_cg1_base_mouth", "mod_assets/m_cg1_base_mouth_1.png")) 
image m_cg1_base_exp1 = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg1_exp1.png", (0, 0), "m_cg1_eye", (0, 0), WhileSpeaking("monika", "m_cg1_exp1_mouth", "mod_assets/m_cg1_exp1_mouth_0.png"))

image m_cg_tvEvent_eye:
    "mod_assets/m_cg_tvEvent_eye_1.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    "mod_assets/m_cg_tvEvent_eye_0.png"
    0.1
    repeat

image m_cg_tvEvent_mouth:
    "mod_assets/m_cg_tvEvent_mouth_1.png"
    0.2
    "mod_assets/m_cg_tvEvent_mouth_0.png"
    0.2
    repeat
    
image m_cg_tvEvent = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg_tvEvent.png", (0, 0), "m_cg_tvEvent_eye", (0, 0), WhileSpeaking("monika","m_cg_tvEvent_mouth","mod_assets/m_cg_tvEvent_mouth_0.png"))

image m_cg_cafeEvent_eye:
    "mod_assets/m_cg_cafeEvent_eye_1.png"
    choice:
        7.0
    choice:
        4.0
    choice:
        2.5
    "mod_assets/m_cg_cafeEvent_eye_0.png"
    0.1
    repeat

image m_cg_cafeEvent_mouth:
    "mod_assets/m_cg_cafeEvent_mouth_1.png"
    0.2
    "mod_assets/m_cg_cafeEvent_mouth_0.png"
    0.2
    repeat

image m_cg_cafeEvent_1a = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg_cafeEvent_1a.png", (0, 0), "m_cg_cafeEvent_eye", (0, 0), WhileSpeaking("monika","m_cg_cafeEvent_mouth","mod_assets/m_cg_cafeEvent_mouth_0.png"))
image m_cg_cafeEvent_2a = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg_cafeEvent_2a.png", (0, 0), WhileSpeaking("monika","m_cg_cafeEvent_mouth","mod_assets/m_cg_cafeEvent_mouth_0.png"))
image m_cg_cafeEvent_3a = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg_cafeEvent_3a.png", (0, 0), WhileSpeaking("monika","m_cg_cafeEvent_mouth","mod_assets/m_cg_cafeEvent_mouth_1.png"))
image m_cg_cafeEvent_1b = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg_cafeEvent_1b.png", (0, 0), "m_cg_cafeEvent_eye", (0, 0), WhileSpeaking("monika","m_cg_cafeEvent_mouth","mod_assets/m_cg_cafeEvent_mouth_0.png"))
image m_cg_cafeEvent_2b = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg_cafeEvent_2b.png", (0, 0), WhileSpeaking("monika","m_cg_cafeEvent_mouth","mod_assets/m_cg_cafeEvent_mouth_0.png"))
image m_cg_cafeEvent_3b = LiveComposite((1280, 720), (0, 0), "ourtime_assets/cg/m_cg_cafeEvent_3b.png", (0, 0), WhileSpeaking("monika","m_cg_cafeEvent_mouth","mod_assets/m_cg_cafeEvent_mouth_1.png"))
image m_cg_cafeEvent_p2:
    "ourtime_assets/cg/m_cg_cafeEvent_p2.png"

image m_cg_cafeEvent_shaft1:
    "ourtime_assets/cg/m_cg_cafeEvent_sunshaft1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        9.0
        linear 4.0 alpha 0
        repeat
image m_cg_cafeEvent_shaft2:
    "ourtime_assets/cg/m_cg_cafeEvent_sunshaft2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        12.0
        linear 4.0 alpha 0
        repeat
image m_cg_cafeEvent_shaft3:
    "ourtime_assets/cg/m_cg_cafeEvent_sunshaft3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        24.0
        linear 2.0 alpha 0
        repeat
