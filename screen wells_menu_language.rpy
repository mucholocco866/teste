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

        vbox:
            spacing 20 xfill True
            text "WELLS MENU" xalign 0.5 size 32 color "#ff4444"

            hbox:
                xalign 0.5 spacing 40
                # --- COLUNA 1: sELETOR DE IDIOMA (Substituiu o Test Tools) ---
                vbox:
                    xsize 400 spacing 10
                    text "LANGUAGE" xalign 0.5 size 28 color "#ff4444"

                    frame:
                        xsize 380 ysize 300 
                        background Solid("#00000066")
                        padding (10, 10)

                        vbox:
                            xalign 0.5 spacing 40
                            vbox:
                                spacing 2
                                if renpy.variant("small"):
                                    xsize 800
                                else:
                                    xsize 600

                                style_prefix "radio"
                                label _("Language Select"):
                                    text_size 26
                                    text_font "Roboto-Regular.ttf"

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
                    xsize 400 spacing 10
                    text "CUSTOM FONTS" xalign 0.5 size 28 color "#ff4444"

                    frame:
                        xsize 380 ysize 300 
                        background Solid("#00000066")
                        padding (10, 10)

                        viewport:
                            id "vp_fonts"
                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            vbox:
                                spacing 8
                                xfill True
                                # Lista as fontes encontradas na pasta wells/
                                for fonte in listar_fontes():
                                    $ f_path = "wells/" + fonte
                                    textbutton fonte:
                                        # Aplica a fonte usando o sistema oficial de Transform do Ren'Py
                                        action [
                                            SetField(persistent, "font_escolhida", f_path),
                                            Preference("font transform", "wells_custom")
                                        ]
                                        text_font f_path 
                                        text_size 24
                                        text_hover_color "#2bff00"
                                        text_selected_color "#2bff00"
                                        selected (persistent.font_escolhida == f_path)

                    # Botão para voltar à fonte padrão do jogo
                    textbutton "Reset Font":
                        xalign 0.5
                        action [
                            # Define o caminho completo da fonte padrão
                            SetField(persistent, "font_escolhida", "wells/Roboto-Regular.ttf"),
                            # Reativa o transformador com a fonte correta
                            Preference("font transform", "wells_custom")
                        ]
                        text_size 28 
                        text_hover_color "#ff4444"

                vbox:
                    spacing 1
                    ypos 20
                    style_prefix "wells_menu_check"
                    label _("Jump"):
                        text_size 26
                    textbutton _("Skip Text"):
                        action Preference("skip", "toggle")
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    textbutton _("After Choices"):
                        action Preference("after choices", "toggle")
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    textbutton _("Transitions"):
                        action InvertSelected(Preference("transitions", "toggle"))
                        text_idle_color "#ffffff"
                        text_hover_color "#ff0000"
                        text_selected_idle_color "#2bff00"
                        text_selected_hover_color "#2bff00"
                        text_size 22

                    null height 2

                 # --- COLUNA 2: ADJUST (Sua configuração original) ---
                vbox:
                    xsize 400 spacing 10
                    text "AUDIO ADJUST" xalign 0.5 size 28 color "#ff4444"
                    vbox:
                        hbox:
                            style_prefix "wells_menu_slider"
                            box_wrap True
                            spacing 40 xalign 0.5

                            vbox:
                                spacing 1
                                if config.has_music:
                                    label _("Music"):
                                        text_size 26

                                    hbox:
                                        spacing 1
                                        bar value Preference("music volume")

                                if config.has_sound:

                                    label _("sound volume"):
                                        text_size 26

                                    hbox:
                                        spacing 1
                                        bar value Preference("sound volume")

                                        if config.sample_sound:
                                            textbutton _("Test") action Play("sound", config.sample_sound)


                                if config.has_voice:
                                    label _("voice volume"):
                                        text_size 26

                                    hbox:
                                        spacing 1
                                        bar value Preference("voice volume")

                                        if config.sample_voice:
                                            textbutton _("Test") action Play("voice", config.sample_voice)

                                if config.has_music or config.has_sound or config.has_voice:

                                    textbutton _("Mute"):
                                        text_size 26
                                        action Preference("all mute", "toggle")
                                        style "mute_all_button"

                    vbox:
                        spacing 1
                        style_prefix "wells_menu_radio"
                        label _("Rollback"):
                            text_size 26
                        textbutton _("Disable"):
                            action Preference("rollback side", "disable")
                            text_idle_color "#ffffff"
                            text_hover_color "#ff0000"
                            text_selected_idle_color "#2bff00"
                            text_selected_hover_color "#2bff00"
                            text_size 22

                        textbutton _("Left"):
                            action Preference("rollback side", "left")
                            text_idle_color "#ffffff"
                            text_hover_color "#ff0000"
                            text_selected_idle_color "#2bff00"
                            text_selected_hover_color "#2bff00"
                            text_size 22

                        textbutton _("Right"):
                            action Preference("rollback side", "right")
                            text_idle_color "#ffffff"
                            text_hover_color "#ff0000"
                            text_selected_idle_color "#2bff00"
                            text_selected_hover_color "#2bff00"
                            text_size 22

                        null height 2


                # --- COLUNA 3: TEXTOS (Sua configuração original) ---
                vbox:
                    xsize 400 spacing 10
                    text "DIALOGUE" xalign 0.5 size 28 color "#ff4444"

                    vbox:
                        spacing 1
                        label _("Size Name: %s" % (persistent.pref_text_size_label)):
                            text_size 26
                        bar value FieldValue(object=persistent, field='pref_text_size_label', range=(wells_text_size * 2), max_is_zero=False, style=u'slider', offset=0, step=2)
                    vbox:
                        spacing 1
                        label _("Size Dialogue: %s" % (persistent.pref_text_size_dialogue)):
                            text_size 26
                        bar value FieldValue(object=persistent, field='pref_text_size_dialogue', range=(wells_text_size * 2), max_is_zero=False, style=u'slider', offset=0, step=2)
                    vbox:
                        spacing 1
                        label _("Text Speed"):
                            text_size 26

                        bar value Preference("text speed")
                    vbox:
                        spacing 1
                        label _("Time Text"):
                            text_size 26

                        bar value Preference("auto-forward time")

                    vbox:
                        spacing 2
                        label _("Experimental"):
                            text_size 28
                        textbutton "EXTRAS":
                            # As ações dentro de () são executadas em sequência ao clicar
                            action (Show("menu_experimental"), Hide("wells_menu_language"))
                            text_idle_color "#ffffff"
                            text_hover_color "#ff0000"
                            text_size 22

        textbutton _("Fechar"):
            text_font "Roboto-Regular.ttf"
            xalign 0.5
            yalign 1.05
            action Hide("wells_menu_language")
            text_idle_color "#ffffff"
            text_hover_color "#ff0000"
