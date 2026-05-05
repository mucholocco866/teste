## The font used for in-game text.
define 999 gui.text_font = 'wells/TOP3.ttf'
## The font used for character names.
define 999 gui.name_text_font = 'wells/TOP3.ttf'
## The font used for out-of-game text.
define 999 gui.interface_text_font = 'wells/TOP3.ttf'

#### STYLES DEFINE
define wells_namebox_borders = Borders(5, 5, 5, 5)
define wells_text_size = 30

default persistent.pref_text_size_label = 24
default persistent.pref_text_size_dialogue = 24
default wells_menu_tab = "main" # Define que o menu começa na aba principal

init 999 python:
    config.developer = True
    config.console = True
    config.rollback_enabled = True
    config.language = "brazil"
    config.hard_rollback_limit = 128
    config.rollback_length  = 128

init python:
    # Função estável para alternar entre 30 e 60 FPS
    def toggle_power_save():
        # No Ren'Py 8+, usamos as preferências de renderização
        if preferences.gl_framerate == 30:
            preferences.gl_framerate = None # None define para o máximo (60+)
        else:
            preferences.gl_framerate = 30
        renpy.restart_interaction()

    import os

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

init -1 python:
    if persistent.use_hw_video is None:
        persistent.use_hw_video = True # Padrão é ligado
    
    config.hw_video = persistent.use_hw_video

    # Inicializa variáveis persistentes
    if persistent.multiple_dialogue is None:
        persistent.multiple_dialogue = True


screen wells_menu_language():
    modal True
    zorder 200
    tag menu
    add Solid("#000000cc")

    frame:
        if config.screen_width == 1920:
            xpadding 60
            ypadding 60

            if renpy.variant("small"):
                ysize 1000
                xsize 1600
            else:
                ysize 900
                xsize 1280

        if config.screen_width == 1280:
            xpadding 60
            ypadding 60
            xsize 1200
            ysize 700

        xalign 0.5
        yalign 0.1
        hbox:
            align (0.0, 0.0)
            vbox:
                spacing 2
                if renpy.variant("small"):
                    xsize 800
                else:
                    xsize 600

                style_prefix "radio"
                label _("Idioma"):
                    text_size 26
                    text_font "DejaVuSans.ttf"

                $ langs = get_all_languages()
                for lang in langs:
                     textbutton "[lang]".capitalize():
                        action Language(None if lang=="Default" else lang)
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                null height 2

                vbox:
                    spacing 1
                    ypos 20
                    style_prefix "wells_menu_check"
                    label _("Pular"):
                        text_size 26
                    textbutton _("Texto não visto"):
                        action Preference("skip", "toggle")
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    textbutton _("Após escolhas"):
                        action Preference("after choices", "toggle")
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    textbutton _("Transições"):
                        action InvertSelected(Preference("transitions", "toggle"))
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    null height 2


                vbox:
                    spacing 1
                    style_prefix "wells_menu_radio"
                    label _("Voltar texto"):
                        text_size 26
                    textbutton _("Desabilitado"):
                        action Preference("rollback side", "disable")
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    textbutton _("Esquerda"):
                        action Preference("rollback side", "left")
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    textbutton _("Direita"):
                        action Preference("rollback side", "right")
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    null height 2

                    vbox:
                        spacing 2
                        label _("Experimental"):
                            text_size 26
                        textbutton "Dual Dialogue":
                            action Function(toggle_multiple_dialogue)
                            text_idle_color ("#2bff00" if persistent.multiple_dialogue else "#ffffff")
                            text_hover_color "#ff0000" 
                            text_size 22

                        textbutton "wells menu":
                            # As ações dentro de () são executadas em sequência ao clicar
                            action (Show("menu_experimental"), Hide("wells_menu_language"))
                            text_idle_color "#ffffff"
                            text_hover_color "#ff0000"
                            text_size 22


            vbox:
                hbox:
                    style_prefix "wells_menu_slider"
                    box_wrap True
                    spacing 80 xalign 0.5

                    vbox:
                        spacing 1
                        if config.has_music:
                            label _("Volume da música"):
                                text_size 26

                            hbox:
                                spacing 1
                                bar value Preference("music volume")

                        if config.has_sound:

                            label _("Volume dos efeitos sonoros"):
                                text_size 26

                            hbox:
                                spacing 1
                                bar value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)


                        if config.has_voice:
                            label _("Volume de voz"):
                                text_size 26

                            hbox:
                                spacing 1
                                bar value Preference("voice volume")

                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:

                            textbutton _("mudo"):
                                text_size 26
                                action Preference("all mute", "toggle")
                                style "mute_all_button"

                            vbox:
                                spacing 1
                                label _("Tamanho do nome: %s" % (persistent.pref_text_size_label)):
                                    text_size 26
                                bar value FieldValue(object=persistent, field='pref_text_size_label', range=(wells_text_size * 2), max_is_zero=False, style=u'slider', offset=0, step=2)
                            vbox:
                                spacing 1
                                label _("Tamanho do dialogo: %s" % (persistent.pref_text_size_dialogue)):
                                    text_size 26
                                bar value FieldValue(object=persistent, field='pref_text_size_dialogue', range=(wells_text_size * 2), max_is_zero=False, style=u'slider', offset=0, step=2)
                            vbox:
                                spacing 1
                                label _("Velocidade do texto"):
                                    text_size 26

                                bar value Preference("text speed")
                            vbox:
                                spacing 1
                                label _("Tempo de texto"):
                                    text_size 26

                                bar value Preference("auto-forward time")


        textbutton _("Fechar"):
            text_font "DejaVuSans.ttf"
            xalign 0.5
            yalign 1.05
            action Hide("wells_menu_language")
            text_idle_color "#ffffff"
            text_hover_color "#ff0000"

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
    font "DejaVuSans.ttf"

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
            textbutton "OPEN ▲":
                style "wells_menu_quick_button"
                xpos 0.01 yalign 0.99 
                action Show("custom_menu_wells")
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
            textbutton "CLOSE ▼": 
                action Hide("custom_menu_wells")
                text_hover_color "#ff0000"
            
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
    font "DejaVuSans.ttf"
    hover_color "#2bff00" # Cor verde ao passar o mouse

# Garante que os textos dentro da barra usem o mesmo padrão
style wells_menu_quick_text is wells_menu_quick_button_text:
    size 22


########### CUSTOM SCRENS ###########

screen menu_experimental():
    modal True
    zorder 201
    tag menu_experimental
    add Solid("#000000cc")

    frame:
        padding (60, 60)
        # Manter as lógicas de tamanho que você já definiu (1920/1280)
        if config.screen_width == 1920:
            if renpy.variant("small"):
                ysize 1000 xsize 1600
            else:
                ysize 900 xsize 1280
        if config.screen_width == 1280:
            xsize 1200 ysize 700

        xalign 0.5 yalign 0.1

        vbox:
            spacing 20 xfill True
            text "EXPERIMENTAL & PERFORMANCE" xalign 0.5 size 35 color "#ff4444"

            hbox:
                xalign 0.5 spacing 50
                
                # --- COLUNA DE TESTES (O QUE VOCÊ JÁ TINHA) ---
                vbox:
                    xsize 400 spacing 15
                    text "TEST TOOLS" xalign 0.5 size 24 color "#aaa"
                    textbutton "TESTE 1" action [Notify("FUNCIONA 1!")]
                    textbutton "TESTE 2" action [Notify("FUNCIONA 2!")]

                # --- SUA NOVA COLUNA: SYSTEM & PERFORMANCE ---
                vbox:
                    xsize 450 spacing 15
                    text "SYSTEM" xalign 0.5 size 24 color "#ff4444"
                    
                    # Performance de Vídeo e FPS
                    vbox:
                        spacing 5 xfill True
                        text "VIDEO PERFORMANCE" size 20 color "#aaa" xalign 0.5
                        
                        $ current_fps = "30 FPS" if preferences.gl_framerate == 30 else "60 FPS"
                        textbutton "Limit FPS: [current_fps]":
                            xalign 0.5
                            action Function(toggle_power_save)
                            text_hover_color "#2bff00"

                        $ gl_ps_status = "ON" if preferences.gl_powersave else "OFF"
                        textbutton "Power Save: [gl_ps_status]":
                            xalign 0.5
                            action Preference("gl powersave", "toggle")
                            text_hover_color "#2bff00"

                    null height 10

                    # Renderização (GPU vs CPU)
                    vbox:
                        spacing 5 xfill True
                        text "VIDEO RENDERING" size 20 color "#aaa" xalign 0.5
                            
                        $ hw_label = "Hardware (GPU)" if persistent.use_hw_video else "Software (CPU)"
                        textbutton "Decoding: [hw_label]":
                            xalign 0.5
                            action [ToggleField(persistent, "use_hw_video"), Notify("Restart game to apply changes")]
                            text_hover_color "#00ccff"

                        text "Use Software if you see a black screen" size 14 color "#666" xalign 0.5

            # --- Botão para voltar ---
            null height 50
            textbutton "VOLTAR":
                xalign 0.5
                action (Show("wells_menu_language"), Hide("menu_experimental"))
                text_idle_color "#ffffff"
                text_hover_color "#ff0000"
                text_size 30


##### SAY #####

init 999 screen say(who, what):
    if config.screen_width == 1280:
        style_prefix "say_wells_1280"

    if config.screen_width == 1920:
        style_prefix "say_wells_1920"

    window:
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

                text who:
                    if persistent.pref_text_size_label is None:
                        size 22
                    else:
                        size persistent.pref_text_size_label
                    id "who"

        text what:
            if config.screen_width == 1920:
                ypos -15
                if who is None:
                    xalign 0.2
                else:
                    xpos 255
                xsize 1316
                text_align 0.0
                xalign 0.0

            if persistent.pref_text_size_dialogue is None:
                size 28
            else:
                size persistent.pref_text_size_dialogue
            color "#FFFFFF"
            outlines [ (absolute(4), "#000000", absolute(0), absolute(0)) ]
            id "what"

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

    background Image("wells/textbox1280.png")

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

    background Image("wells/frame.png")

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

    background Image("wells/textbox1920.png")

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