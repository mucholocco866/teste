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


init -1 screen quick_menu():
    zorder 100

    hbox:
        style_prefix 'wells_menu_quick'
        xalign 0.5
        yalign 1.0
        textbutton _("Back") action Rollback()
        #textbutton _("History") action ShowMenu("history")
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Save") action ShowMenu("save")
        #textbutton _("Q.Save") action QuickSave()
        textbutton _("Load") action ShowMenu("save")
        textbutton _("Prefs") action ShowMenu("preferences")
        textbutton _(" ")

    hbox:
        style_prefix 'wells_menu_quick'

        xalign 1.0
        yalign 1.0

        textbutton _("MENU") action Show("wells_menu_language")

init -1 screen quick_menu():
    variant "touch"
    zorder 100

    hbox:
        style_prefix 'wells_menu_quick'
        xalign 0.5
        yalign 1.0
        textbutton ("Voltar") action Rollback()
        textbutton ("Avançar") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton ("Automático") action Preference("auto-forward", "toggle")
        textbutton ("W") action ShowMenu()
        textbutton _("Esconder") action HideInterface()
        textbutton (" ")

    hbox:
        style_prefix 'wells_menu_quick'

        xalign 1.0
        yalign 1.0

        textbutton _("MENU") action Show("wells_menu_language")

init python:
    config.overlay_screens.append("quick_menu")

style wells_menu_quick_button is default
style wells_menu_quick_button_text is button_text

style wells_menu_quick_button:
    padding (10,4, 10, 0)

style wells_menu_quick_button_text:
    padding (10,4, 10, 0)
    size 25
    color "#FFFFFF"
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    font "DejaVuSans.ttf"


########### CUSTOM SCRENS ###########

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