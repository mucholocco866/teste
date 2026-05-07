## 1. Definição Dinâmica das Fontes (Ajustado para Font Transform)
define 999 gui.text_font = 'wells/Roboto-Regular.ttf'
define 999 gui.name_text_font = 'wells/Roboto-Regular.ttf'
define 999 gui.interface_text_font = 'wells/Roboto-Regular.ttf'

#### STYLES DEFINE
define wells_namebox_borders = Borders(5, 5, 5, 5)
define wells_text_size = 30

default persistent.pref_text_size_label = 24
default persistent.pref_text_size_dialogue = 24
default wells_menu_tab = "main" 
default persistent.font_escolhida = None
default persistent.wells_line_spacing = 5
default persistent.wells_text_size_mult = 1.0 # Multiplicador de tamanho
default persistent.wells_dialogue_y_offset = 0
default persistent.wells_dual_dialogue_offset = 200 # Valor inicial para separar os textos
default persistent.wells_dual_dialog_offset = 300
default persistent.wells_dual_dialogue_fix = False

init 999 python:
    config.developer = True
    config.console = True
    config.rollback_enabled = True
    config.language = "brazil"
    config.hard_rollback_limit = 128
    config.rollback_length = 128

init python:
    import os

    # --- FUNÇÕES ORIGINAIS MANTIDAS ---
    def toggle_power_save():
        if preferences.gl_framerate == 30:
            preferences.gl_framerate = None 
        else:
            preferences.gl_framerate = 30
        renpy.restart_interaction()

    def get_all_languages():
        languages = ["Default"]
        path = os.path.join(config.gamedir, 'tl')
        if os.path.exists(path):
            for entry in os.listdir(path):
                if os.path.isdir(os.path.join(path, entry)):
                    languages.append(entry)
        return languages

    def toggle_multiple_dialogue():
        persistent.multiple_dialogue = not persistent.multiple_dialogue
        renpy.restart_interaction()

    # --- NOVA FUNÇÃO DE FONTES (LÓGICA DE ACESSIBILIDADE) ---
    def listar_fontes():
        fontes = []
        path = os.path.join(config.gamedir, 'wells')
        if os.path.exists(path):
            for f in os.listdir(path):
                if f.endswith((".ttf", ".otf")):
                    fontes.append(f)
        return fontes

    # O "Segredo" que estava no 00accessibility: um transformador de fonte
    def wells_font_transformer(old_font):
        if persistent.font_escolhida:
            return persistent.font_escolhida
        return old_font

    # Registra o transformador no sistema do Ren'Py
    config.font_transforms["wells_custom"] = wells_font_transformer

init -1 python:
    if persistent.use_hw_video is None:
        persistent.use_hw_video = True
    config.hw_video = persistent.use_hw_video

    if persistent.multiple_dialogue is None:
        persistent.multiple_dialogue = True

    # Ativa a fonte customizada logo no início se houver uma salva
    if persistent.font_escolhida:
        _preferences.font_transform = "wells_custom"

screen wells_menu_language():
    modal True
    zorder 200
    tag menu
    add Solid("#00000080") 

    frame:
        # --- LÓGICA DE RESOLUÇÃO E MOBILE ---
        xalign 0.5 yalign 0.4
        background Solid("#00000093") 
        
        if config.screen_width == 1920:
            if renpy.variant("small"): # Versão Mobile/Tablet
                xsize 1600 ysize 950 padding (60, 50)
            else: # Versão PC Full HD
                xsize 1450 ysize 820 padding (50, 40)
        else: # Versão 1280 (HD) ou outras resoluções menores
            xsize 1150 ysize 680 padding (40, 35)

        vbox:
            xfill True
            spacing 25
            
            # Título principal
            text "WELLS MENU" xalign 0.5 size 42 color "#ff4444" outlines [(2, "#000", 0, 0)]

            hbox:
                xalign 0.5 spacing 60 # Espaçamento centralizado entre as colunas

                # --- COLUNA 1: SISTEMA (IDIOMA E FONTES) ---
                vbox:
                    xsize 420 spacing 15 # Aumentei levemente para acomodar o seletor
                    label _("SISTEMA") xalign 0.5 text_size 26 text_color "#3d8afd"
                    # --- SEU NOVO BLOCO DE IDIOMAS INTEGRADO ---
                    vbox:
                        xalign 0.5 spacing 10
                        vbox:
                            spacing 2
                            # Ajuste dinâmico de largura mantendo sua lógica
                            if renpy.variant("small"):
                                xsize 400 # Adaptado para caber na coluna mobile
                            else:
                                xsize 380 

                            style_prefix "radio"
                            label _("LANGUAGE SELECT") xalign 0.5 text_size 26 text_color "#2cf1ff"

                            $ langs = get_all_languages()
                            for lang in langs:
                                textbutton "[lang]".capitalize():
                                    action Language(None if lang=="Default" else lang)
                                    text_idle_color "#ffffff"
                                    text_hover_color "#ff0000"
                                    text_selected_idle_color "#2bff00"
                                    text_selected_hover_color "#2bff00"
                                    text_size 22
                                    xalign 0.5

                            null height 2

                    null height 10

                    # --- SEÇÃO DE FONTES (MANTIDA) ---
                    label _("CUSTOM FONTS") xalign 0.5 text_size 26 text_color "#2cf1ff"
                    frame:
                        xsize 380 ysize 220 background Solid("#00000066")
                        viewport:
                            id "vp_fonts" scrollbars "vertical" mousewheel True draggable True
                            vbox spacing 8 xfill True:
                                for fonte in listar_fontes():
                                    $ f_path = "wells/" + fonte
                                    textbutton fonte:
                                        action [SetField(persistent, "font_escolhida", f_path), Preference("font transform", "wells_custom")]
                                        text_font f_path text_size 24
                                        text_selected_color "#2bff00"
                                        text_hover_color "#ff0000"
                                        selected (persistent.font_escolhida == f_path)
                    
                    textbutton "Reset Font" xalign 0.5 action [SetField(persistent, "font_escolhida", "wells/Roboto-Regular.ttf"), Preference("font transform", "wells_custom")] text_size 24 text_hover_color "#ff4444"

                # --- COLUNA 2: TODOS OS SLIDERS (CONTROLES) ---
                vbox:
                    xsize 420 spacing 8
                    label _("CONTROLES") xalign 0.5 text_size 24 text_color "#3d8afd"

                    # Agrupamento de Áudio
                    vbox spacing 4:
                        label _("Música") text_size 24 text_color "#2cf1ff"
                        bar value Preference("music volume") xsize 400
                        label _("Sons") text_size 24 text_color "#2cf1ff"
                        bar value Preference("sound volume") xsize 400
                        label _("Voz") text_size 24 text_color "#2cf1ff"
                        bar value Preference("voice volume") xsize 400

                    null height 10
                    
                    # Agrupamento de Texto (Nome e Diálogo)
                    vbox spacing 4:
                        label _("Tam. Nome: [persistent.pref_text_size_label]") text_size 24 text_color "#2cf1ff"
                        bar value FieldValue(persistent, 'pref_text_size_label', range=60, step=2) xsize 400
                        label _("Tam. Diálogo: [persistent.pref_text_size_dialogue]") text_size 24 text_color "#2cf1ff"
                        bar value FieldValue(persistent, 'pref_text_size_dialogue', range=60, step=2) xsize 400
                        label _("Velocidade do texto") text_size 24 text_color "#2cf1ff"
                        bar value Preference("text speed") xsize 400
                        label _("Tempo do texto") text_size 24 text_color "#2cf1ff"
                        bar value Preference("auto-forward time") xsize 400


                # --- COLUNA 3: OPÇÕES (BOTÕES E EXTRAS) ---
                vbox:
                    xsize 380 spacing 15
                    label _("OPÇÕES") xalign 0.5 text_size 26 text_color "#3d8afd"

                    # Seção MUTE
                    vbox spacing 5:
                        textbutton _("     (MUTE)     "):
                            action Preference("all mute", "toggle")
                            text_size 24
                            idle_background Frame(Solid("#2cff020a"), 4, 4) 
                            hover_background Frame(Solid("#03d9ff44"), 4, 4)
                            selected_background Frame(Solid("#ff000d36"), 4, 4)
                            padding (6, 6)

                    # Seção CHECKBOXES
                    vbox spacing 8:
                        style_prefix "wells_menu_check"
                        
                        textbutton _("     Pular Texto     "):
                            action Preference("skip", "toggle")
                            text_size 22
                            idle_background Frame(Solid("#2cff020a"), 4, 4)
                            hover_background Frame(Solid("#03d9ff44"), 4, 4)
                            padding (6, 6)

                        textbutton _("     Após Escolhas     "):
                            action Preference("after choices", "toggle")
                            text_size 22
                            idle_background Frame(Solid("#2cff020a"), 4, 4)
                            hover_background Frame(Solid("#03d9ff44"), 4, 4)
                            padding (6, 6)

                        textbutton _("     Transições     "):
                            action InvertSelected(Preference("transitions", "toggle"))
                            text_size 22
                            idle_background Frame(Solid("#2cff020a"), 4, 4)
                            hover_background Frame(Solid("#03d9ff44"), 4, 4)
                            padding (6, 6)

                    # Seção RADIO
                    vbox spacing 8:
                        style_prefix "wells_menu_radio"
                        
                        textbutton _("     Desabilitado     "):
                            action Preference("rollback side", "disable")
                            text_size 22
                            idle_background Frame(Solid("#2cff020a"), 4, 4)
                            hover_background Frame(Solid("#03d9ff44"), 4, 4)
                            padding (6, 6)

                        textbutton _("     Esquerda     "):
                            action Preference("rollback side", "left")
                            text_size 22
                            idle_background Frame(Solid("#2cff020a"), 4, 4)
                            hover_background Frame(Solid("#03d9ff44"), 4, 4)
                            padding (6, 6)

                        textbutton _("     Direita     "):
                            action Preference("rollback side", "right")
                            text_size 22
                            idle_background Frame(Solid("#2cff020a"), 4, 4)
                            hover_background Frame(Solid("#03d9ff44"), 4, 4)
                            padding (6, 6)

                    vbox:
                        spacing 4
                        text "COMPATIBILIDADE" size 28 color "#3d8afd" xalign 0.5 
                        textbutton "Dual Dialogue Fix: [persistent.wells_dual_dialogue_fix]":
                            action ToggleField(persistent, "wells_dual_dialogue_fix")
                            text_idle_color "#2bff00"
                            text_hover_color "#03d9ff44" 
                            text_color "#42bef8"
                            text_size 26

                        textbutton "Dual Dialogue":
                            action Function(toggle_multiple_dialogue)
                            text_idle_color ("#2bff00" if persistent.multiple_dialogue else "#ffffff")
                            text_hover_color "#03d9ff44" 
                            text_color "#42bef8"
                            text_size 26

        # Botão EXTRAS
        textbutton "EXTRAS":
            xpos 1100
            ypos 700
            xalign 0.5
            action [Show("menu_experimental"), Hide("wells_menu_language")]
            text_size 24 text_hover_color "#2bff00"
            idle_background Frame(Solid("#2cff020a"), 4, 4) # Fundo suave
            hover_background Frame(Solid("#03d9ff44"), 4, 4) # Brilha mais no mouse
            padding (12, 12)


        # --- RODAPÉ ---
        null height 20
        textbutton "FECHAR":
            xpos 700
            ypos 700
            xalign 0.5
            action [Hide("wells_menu_language")]
            text_size 24 text_hover_color "#2bff00"
            idle_background Frame(Solid("#2cff020a"), 4, 4) # Fundo suave
            hover_background Frame(Solid("#03d9ff44"), 4, 4) # Brilha mais no mouse
            padding (12, 12)


init -1 style wells_menu_slider_label is pref_label
init -1 style wells_menu_slider_label_text is label_text
init -1 style wells_menu_slider_slider is gui_slider
init -1 style wells_menu_slider_button is gui_button
init -1 style wells_menu_slider_button_text is gui_button_text
init -1 style wells_menu_slider_pref_vbox is pref_vbox

init -1 style wells_menu_check_button_text is button_text
init -1 style wells_menu_radio_button_text is button_text

if not renpy.variant("small"):
    init -1 style wells_menu_slider_label_text:
        size 28

    init -1 style wells_menu_check_button_text:
        size 28

    init -1 style wells_menu_radio_button_text:
        size 28

init -1 style wells_menu_slider_slider:
    xsize 400

init -1 style wells_menu_slider_button:
    yalign 0.5
    left_margin 15

init -1 style wells_menu_slider_button_text:
    size 18
    font "Roboto-Regular.ttf"

init -1 style wells_menu_slider_vbox:
    xsize 675


################################################################################
## NOVO QUICK MENU (SISTEMA DE ALTERNÂNCIA - ESQUERDA PARA DIREITA)
################################################################################

# 1. Animação de Deslize
transform wells_float_left:
    xanchor 0.0 yanchor 1.0 
    on show:
        xpos -1000 
        easein 0.5 xpos 0.0
    on hide:
        easeout 0.5 xpos -1000

# 2. O Botão Disparador (SÓ APARECE SE O MENU ESTIVER FECHADO)
screen quick_menu():
    zorder 100
    if quick_menu:
        if not renpy.get_screen("custom_menu_wells"):
            textbutton "Quick":
                style "wells_menu_quick_button"
                xpos 0.01 yalign 0.99
                action Show("custom_menu_wells")
                text_hover_color "#2bff00"
                background Solid("#00000080") 

# 3. A Caixinha com os Botões (CORRIGIDA)
screen custom_menu_wells:
    zorder 101 
    tag custom_quick
    modal True # Garante que os cliques foquem nesta tela enquanto aberta

    # Adicionamos um invisible button no fundo para fechar ao clicar fora, 
    # mas sem interferir nos botões da hbox.
    button:
        action Hide("custom_menu_wells")
        background None # Invisível

    frame:
        at wells_float_left
        background Solid("#00000080") 
        padding (15, 10)
        xsize None
        yalign 1.0 
        
        hbox:
            spacing 18
            style_prefix "wells_menu_quick"
            
            # Botão para fechar
            textbutton "Fechar": 
                action Hide("custom_menu_wells")
                text_hover_color "#2bff00"
            
            # Botões de Ação - Mantendo suas funções originais
            textbutton _("Back") action [Rollback(), Hide("custom_menu_wells")]
            textbutton _("Skip") action [Skip(), Hide("custom_menu_wells")] alternate Skip(fast=True, confirm=True)
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("save")
            textbutton _("Prefs") action ShowMenu("preferences")
            textbutton _("Menu") action Show("wells_menu_language")


# 4. Estilos e Configurações de Sistema
init python:
    # Remove qualquer registro de menu anterior para evitar conflito com o jogo original
    config.overlay_screens = [] 
    
    # Registra o SEU quick_menu como a única sobreposição oficial
    config.overlay_screens.append("quick_menu")

    # Definição dinâmica de estilos baseada na plataforma (PC ou Mobile)
    if renpy.variant("touch"):
        style.wells_menu_quick_button_text.size = 40
        style.wells_menu_quick_frame.padding = (30, 20)
    else:
        # Tamanho padrão para computadores
        style.wells_menu_quick_button_text.size = 25

# --- Definições de Estilos Visuais ---

style wells_menu_quick_button:
    padding (10, 4, 10, 4)

style wells_menu_quick_button_text:
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]
    font "Roboto-Regular.ttf"
    hover_color "#2bff00" # Cor verde ao passar o mouse

# Garante que os textos dentro da barra usem o mesmo padrão
style wells_menu_quick_text is wells_menu_quick_button_text:
    size 22


########### CUSTOM SCRENS ###########

screen menu_experimental():
    modal True
    zorder 201
    tag menu_experimental
    add Solid("#00000093")

    frame:
        padding (60, 60)
        # Mantendo suas lógicas de resolução originais
        if config.screen_width == 1920:
            if renpy.variant("small"):
                ysize 1000 xsize 1600
            else:
                ysize 900 xsize 1280
        if config.screen_width == 1280:
            xsize 1200 ysize 700

        xalign 0.4 yalign 0.1

        vbox:
            spacing 20 xfill True
            text "EXPERIMENTAL & PERFORMANCE" xalign 0.5 size 32 color "#ff4444"

            hbox:
                xalign 0.5 spacing 40

                # --- COLUNA 1: ADJUST (Sua configuração original) ---

                # Ajuste de Tamanho (Nativo do Ren'Py)
                vbox:
                    spacing 8
                    text "Text Scaling:" size 26 color "#2cf1ff" xalign 0.5
                    bar value Preference("font size") xsize 350 xalign 0.5
                    textbutton _("Reset Size"):
                        action Preference("font size", 1.0)
                        xalign 0.5 text_size 26 text_hover_color "#ff4444"

                    text "Line Spacing:" size 26 color "#2cf1ff" xalign 0.5
                    bar value FieldValue(persistent, "wells_line_spacing", range=50, offset=0) xsize 350 xalign 0.5
                    textbutton _("Reset Spacing"):
                        action Preference("font line spacing", 1.0)
                        xalign 0.5 text_size 26 text_hover_color "#ff4444"

                    text "Dialogue V offset:" size 26 color "#2cf1ff" xalign 0.5
                    # O range de 100 com offset -50 permite subir ou descer o texto
                    bar value FieldValue(persistent, "wells_dialogue_y_offset", range=100, offset=-50) xsize 350 xalign 0.5
                    textbutton "Reiniciar Altura":
                        action SetField(persistent, "wells_dialogue_y_offset", 0)
                        xalign 0.5 text_size 26 text_hover_color "#ff4444"

                null height 5

                # --- COLUNA 3: SYSTEM & PERFORMANCE (Sua configuração original) ---
                vbox:
                    xsize 400 spacing 10
                    text "SYSTEM" xalign 0.5 size 28 color "#3d8afd"

                    vbox:
                        spacing 5 xfill True
                        text "VIDEO PERFORMANCE" size 28 color "#2cf1ff" xalign 0.5

                        $ current_fps = "30 FPS" if preferences.gl_framerate == 30 else "60 FPS"
                        textbutton "Limit FPS: [current_fps]":
                            xalign 0.5
                            action Function(toggle_power_save)
                            text_hover_color "#2bff00"
                            text_size 28 

                        $ gl_ps_status = "ON" if preferences.gl_powersave else "OFF"
                        textbutton "Power Save: [gl_ps_status]":
                            xalign 0.5
                            action Preference("gl powersave", "toggle")
                            text_hover_color "#2bff00"
                            text_size 28 

                    vbox:
                        spacing 5 xfill True
                        text "VIDEO RENDERING" size 24 color "#aaa" xalign 0.5

                        $ hw_label = "Hardware (GPU)" if persistent.use_hw_video else "Software (CPU)"
                        textbutton "Decoding: [hw_label]":
                            xalign 0.5
                            action [ToggleField(persistent, "use_hw_video"), Notify("Restart game to apply changes")]
                            text_hover_color "#00ccff"
                            text_size 28 

                        text "Use Software if you see a black screen" size 24 color "#666" xalign 0.5

            # --- Botão para voltar ao Menu de Idiomas ---
            null height 50
            textbutton "Return":
                xalign 0.5
                action (Show("wells_menu_language"), Hide("menu_experimental"))
                text_idle_color "#ffffff"
                text_hover_color "#ff0000"
                text_size 30

##### SAY #####

init 999 screen say(who, what, multiple=None):
    if config.screen_width == 1280:
        style_prefix "say_wells_1280"

    if config.screen_width == 1920:
        style_prefix "say_wells_1920"

    # Se o Fix estiver LIGADO no menu, usa a window com ID (necessário em alguns jogos antigos)
    if persistent.wells_dual_dialogue_fix:
        window:
            id "window" # O ID que causa o "pulo" no Eternum, mas ajuda no Stray Incubus
            
            # --- SUA LÓGICA DE DESVIO ORIGINAL (PRESERVADA) ---
            if multiple and multiple[0] > 0:
                yoffset (persistent.wells_dual_dialogue_offset * multiple[0])
            else:
                yoffset (persistent.wells_dialogue_y_offset if persistent.wells_dialogue_y_offset is not None else 0)

            # --- TODO O SEU CONTEÚDO ORIGINAL ABAIXO ---
            if config.screen_width == 1280:
                style "say_wells_1280"
            if config.screen_width == 1920:
                style "say_wells_1920"

            if who is not None:
                window:
                    if config.screen_width == 1280:
                        style "namebox_wells_1280"
                    if config.screen_width == 1920:
                        style "namebox_wells_1920"
                    text who id "who":
                        size (persistent.pref_text_size_label or 22)

            text what id "what":
                if config.screen_width == 1920:
                    ypos -15
                    xpos (255 if who else 0.2)
                    xsize 1316
                line_spacing (persistent.wells_line_spacing or 5)
                size (persistent.pref_text_size_dialogue or 28)
                color "#FFFFFF"
                outlines [(absolute(4), "#000000", 0, 0)]

    # Se o Fix estiver DESLIGADO (Ideal para Eternum e jogos modernos)
    else:
        window:
            # SEM id "window" - isso evita que a textbox suba para o topo no Eternum
            
            if multiple and multiple[0] > 0:
                yoffset (persistent.wells_dual_dialogue_offset * multiple[0])
            else:
                yoffset (persistent.wells_dialogue_y_offset if persistent.wells_dialogue_y_offset is not None else 0)

            if config.screen_width == 1280:
                style "say_wells_1280"
            if config.screen_width == 1920:
                style "say_wells_1920"

            if who is not None:
                window:
                    if config.screen_width == 1280:
                        style "namebox_wells_1280"
                    if config.screen_width == 1920:
                        style "namebox_wells_1920"
                    text who id "who":
                        size (persistent.pref_text_size_label or 22)

            text what id "what":
                if config.screen_width == 1920:
                    ypos -15
                    xpos (255 if who else 0.2)
                    xsize 1316
                line_spacing (persistent.wells_line_spacing or 5)
                size (persistent.pref_text_size_dialogue or 28)
                color "#FFFFFF"
                outlines [(absolute(4), "#000000", 0, 0)]

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init -1 style say_wells_1280_window is default
init -1 style say_wells_1280_label is default
init -1 style say_wells_1280_dialogue is default
init -1 style say_wells_1280_thought is say_wells_1280_dialogue

init -1 style namebox_wells_1280 is default
init -1 style namebox_wells_1280_label is say_wells_1280_label


init -1 style say_wells_1280:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 195

    background Image("wells/textbox1280.png", xalign=0.5, yalign=1.0)

init -1 style namebox_wells_1280:
    xpos 240
    xanchor 0.0
    xsize None
    ypos 0
    ysize None

    background Frame("wells/namebox1280.png", wells_namebox_borders, tile=False, xalign=0.0)
    padding wells_namebox_borders.padding

init -1 style say_wells_1280_label:
    xalign 0.0
    yalign 0.5
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

init -1 style say_wells_1280_dialogue:
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    xpos 268
    xsize 1100
    ypos 50

init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "wells/frame.png"

#### END 1280

init -1 style say_wells_1920_window is default
init -1 style say_wells_1920_label is default
init -1 style say_wells_1920_dialogue is default
init -1 style say_wells_1920_thought is say_wells_1920_dialogue

init -1 style namebox_wells_1920 is default
init -1 style namebox_wells_1920_label is say_wells_1920_label


init -1 style say_wells_1920:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 195

    background Image("wells/textbox1920.png", xalign=0.5, yalign=1.0)

init -1 style namebox_wells_1920:
    xpos 400
    xanchor 0.0
    xsize None
    ypos -80
    ysize None

    background Frame("wells/namebox1920.png", wells_namebox_borders, tile=False, xalign=0.0)
    padding wells_namebox_borders.padding

init 999 style say_wells_1920_label:
    xalign 0.5
    yalign 0.5
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

init -1 style say_wells_1920_dialogue:
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    xpos 268
    xsize 1100
    ypos 50

init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background Image("wells/frame.png")

#### END 1280

init -501 screen input(prompt):
    style_prefix "input"

    window:
        if renpy.variant("small"):
            yalign 0.2


        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

if persistent.pref_text_size_label is None:
    init -1 style input_prompt:
        xalign 0.0
        color "#FFFFFF"
        size 22
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
else:
    init -1 style input_prompt:
        xalign 0.0
        color "#FFFFFF"
        size persistent.pref_text_size_label
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

if persistent.pref_text_size_dialogue is None:
    init -1 style input:
        xalign 0.0
        xmaximum 1100
        size 28
        color "#FFFFFF"
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
else:
    init -1 style input:
        xalign 0.0
        xmaximum 1100
        size persistent.pref_text_size_dialogue
        color "#FFFFFF"
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

##### END SAY #####
