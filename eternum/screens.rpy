################################################################################
## Initialization
################################################################################

init offset = -1 

################################################################################
## Low-level Variables
################################################################################

init -400 python:
    # These can be modified by translators who want to customize their language
    # selection button, see the language selection in the preferences below.
    language_titles = dict()
    language_title_fonts = dict()

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:

    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"





################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

define config.replay_scope = { "_game_menu_screen" : "load" }

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        if persistent.quick_menu:
            # 32 = Height of the quick menu
            ypos 1080 - persistent.textbox_height - 32
        else:
            ypos 1080 - persistent.textbox_height
        xsize persistent.textbox_width + 274
        ysize persistent.textbox_height
        background Frame(Transform("gui/textbox.png", alpha=persistent.textbox_opacity))

        vbox:
            xpos gui.name_xpos
            ypos 40
            xsize persistent.textbox_width
            spacing 15

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what":
                size persistent.text_size
                outlines [ (absolute(persistent.text_outline), "#000", absolute(0), absolute(0)) ]


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


screen multiple_say(who, what, multiple):
    style_prefix "say"

    window:
        id "window"
        if persistent.quick_menu:
            # 32 = Height of the quick menu
            ypos 1080 - (persistent.textbox_height * multiple[0]) - 32
        else:
            ypos 1080 - (persistent.textbox_height * multiple[0])
        xsize persistent.textbox_width + 274 # 1920
        ysize persistent.textbox_height
        background Frame(Transform("gui/textbox.png", alpha=persistent.textbox_opacity))

        vbox:
            xpos gui.name_xpos
            ypos 40
            xsize persistent.textbox_width
            spacing 15

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what":
                size persistent.text_size
                outlines [ (absolute(persistent.text_outline), "#000", absolute(0), absolute(0)) ]


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:

    config.character_id_prefixes.append('namebox')


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5

style block2_multiple2_say_window:
    yalign -0.3

style namebox:
    xsize gui.namebox_width
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos 840


            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    outlines [ (2, '#000000')]
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    outlines [ (2, '#000000')]
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "neon.mp3"

style choice_button_text is default:
    outlines [ (1.5, '#000000')]

    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu and persistent.quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos 91
        yalign 0.5

        spacing 50
        if not main_menu:
            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            else:
                textbutton _("Save") action ShowMenu("save")

                textbutton _("Load") action ShowMenu("load")

                textbutton _("Preferences") action ShowMenu("preferences")

                textbutton _("Main Menu") action MainMenu()

            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add "gui/msp5/wall.png" at background_m
    add "gui/msp5/overlay.png"
    add "gui/msp5/title.png" at label_t()

    default active = None
    default exit_h = None
    default discord_h = None
    default patreon_h = None
    default ss_h = None

    button:
        focus_mask True
        action OpenURL("https://discord.gg/caribdisgames")
        hovered [ Play ("sound", "neon.mp3"), SetLocalVariable("discord_h", 1)]
        unhovered SetLocalVariable("discord_h",0)
        image "gui/msp5/discord_idle.png"
        image "gui/msp5/discord_hover.png":
            if discord_h == 1:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
            elif discord_h == 0:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 0 blur 25
            else:
                at transform:
                    alpha 0
        xysize (1920, 1080)
        xpos 0
        ypos 0
        at socials_t(0.3)
    button:
        focus_mask True
        action OpenURL("https://www.patreon.com/user?u=24799077")
        hovered [ Play ("sound", "neon.mp3"), SetLocalVariable("patreon_h", 1)]
        unhovered SetLocalVariable("patreon_h",0)
        image "gui/msp5/patreon_idle.png"
        image "gui/msp5/patreon_hover.png":
            if patreon_h == 1:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
            elif patreon_h == 0:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 0 blur 25
            else:
                at transform:
                    alpha 0
        xysize (1920, 1080)
        xpos 0
        ypos 0
        at socials_t(0.5)
    button:
        focus_mask True
        action OpenURL("https://subscribestar.adult/caribdis")
        hovered [ Play ("sound", "neon.mp3"), SetLocalVariable("ss_h", 1)]
        unhovered SetLocalVariable("ss_h",0)
        image "gui/msp5/ss_idle.png"
        image "gui/msp5/ss_hover.png":
            if ss_h == 1:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
            elif ss_h == 0:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 0 blur 25
            else:
                at transform:
                    alpha 0
        xysize (1920, 1080)
        xpos 0
        ypos 0
        at socials_t(0.4)
                
    # button:
    #     focus_mask True
    #     # auto "gui/msp5/credits_%s.png"
    #     action ShowMenu("about")
    #     hovered [ Play ("sound", "neon.mp3"), SetLocalVariable("about_h", 1)]
    #     unhovered [SetLocalVariable("about_h",0)]
    #     image "gui/msp5/credits_idle.png"
    #     image "gui/msp5/credits_hover.png":
    #         if about_h == 1:
    #             at transform:
    #                 easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
    #         elif about_h == 0:
    #             at transform:
    #                 easein_quint (0.5 * persistent.motion) alpha 0 blur 25
    #         else:
    #             at transform:
    #                 alpha 0
    #     xysize (1920, 1080)
    #     xpos 0
    #     ypos 0
    #     at top_m(0.2)
    # button:
    #     focus_mask True
    #     # auto "gui/msp5/preferences_%s.png"
    #     action ShowMenu("preferences")
    #     hovered [ Play ("sound", "neon.mp3"), SetLocalVariable("preferences_h", 1), SetLocalVariable("button_h", "preferences")]
    #     unhovered [SetLocalVariable("preferences_h",0)]
    #     image "gui/msp5/preferences_idle.png"
    #     image "gui/msp5/preferences_hover.png":
    #         if preferences_h == 1:
    #             at transform:
    #                 easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
    #         elif preferences_h == 0:
    #             at transform:
    #                 easein_quint (0.5 * persistent.motion) alpha 0 blur 25
    #         else:
    #             at transform:
    #                 alpha 0
    #     xysize (1920, 1080)
    #     xpos 0
    #     ypos 0
    #     at top_m(0.15)
    # button:
    #     focus_mask True
    #     # auto "gui/msp5/load_%s.png"
    #     action ShowMenu("load")
    #     hovered [ Play ("sound", "neon.mp3"), SetLocalVariable("load_h", 1), SetLocalVariable("button_h", "load")]
    #     unhovered [SetLocalVariable("load_h",0)]
    #     image "gui/msp5/load_idle.png"
    #     image "gui/msp5/load_hover.png":
    #         if load_h == 1:
    #             at transform:
    #                 easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
    #         elif load_h == 0:
    #             at transform:
    #                 easein_quint (0.5 * persistent.motion) alpha 0 blur 25
    #         else:
    #             at transform:
    #                 alpha 0
    #     xysize (1920, 1080)
    #     xpos 0
    #     ypos 0
    #     at top_m(0.1)
    # button:
    #     focus_mask True
    #     # auto "gui/msp5/start_%s.png"
    #     action Start()
    #     hovered [ Play ("sound", "neon.mp3"), SetLocalVariable("start_h", 1), SetLocalVariable("button_h", "start")]
    #     unhovered [SetLocalVariable("start_h", 0)]
    #     image "gui/msp5/start_idle.png"
    #     image "gui/msp5/start_hover.png":
    #         if start_h == 1:
    #             at transform:
    #                 easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
    #         elif start_h == 0:
    #             at transform:
    #                 easein_quint (0.5 * persistent.motion) alpha 0 blur 25
    #         else:
    #             at transform:
    #                 alpha 0
    #     xysize (1920, 1080)
    #     xpos 0
    #     ypos 0
    #     at top_m(0.05)
    frame:
        # background Frame(Transform('gui/frame.svg', alpha = .5, matrixcolor = ColorizeMatrix('#fff', '#0eda9f')))
        background None
        align  (.5  , .0 )
        xysize (1430, 265)
        offset (0   , 453)
        hbox:
            align (.5, .5)
            spacing -21
            frame:
                background 'gui/msp5/mm_shadow.png'
                xysize (373, 265)
                at top_m(.05)
                button:
                    xysize (345, 237)
                    align  (.0 , .0 )
                    offset (14 ,  14)

                    hovered   [ SetScreenVariable('active', ['start', 1]) ]
                    unhovered [ SetScreenVariable('active', ['start', 0]) ]

                    action Start()

                    image AlphaMask(At('gui/msp5/start.png', mm_hover_zoom()), 'gui/msp5/mm_base.png') offset (-6, -6)
                    image 'gui/msp5/mm_hover.png' offset (-6, -6):
                        if active == ['start', 1]:
                            at BAPR()
                        elif active == ['start', 0]:
                            at BDPR()
                        elif active != None:
                            if active[0] != 'start':
                                at BDPR()
                        else:
                            at BNT()

                    image 'gui/msp5/start_t.png' align (.5, 1.0) offset (0, 14)

                    hover_sound 'neon.mp3'
            frame:
                background 'gui/msp5/mm_shadow.png'
                xysize (373, 265)
                at top_m(.1)
                button:
                    xysize (345, 237)
                    align  (.0 , .0 )
                    offset (14 ,  14)

                    hovered   [ SetScreenVariable('active', ['load', 1]) ]
                    unhovered [ SetScreenVariable('active', ['load', 0]) ]

                    action ShowMenu("load")

                    image AlphaMask(At('gui/msp5/load.png', mm_hover_zoom()), 'gui/msp5/mm_base.png') offset (-6, -6)
                    image 'gui/msp5/mm_hover.png' offset (-6, -6):
                        if active == ['load', 1]:
                            at BAPR()
                        elif active == ['load', 0]:
                            at BDPR()
                        elif active != None:
                            if active[0] != 'load':
                                at BDPR()
                        else:
                            at BNT()

                    image 'gui/msp5/load_t.png' align (.5, 1.0) offset (0, 14)

                    hover_sound 'neon.mp3'
            frame:
                background 'gui/msp5/mm_shadow.png'
                xysize (373, 265)
                at top_m(.15)
                button:
                    xysize (345, 237)
                    align  (.0 , .0 )
                    offset (14 ,  14)

                    hovered   [ SetScreenVariable('active', ['preferences', 1]) ]
                    unhovered [ SetScreenVariable('active', ['preferences', 0]) ]

                    action ShowMenu("preferences")

                    image AlphaMask(At('gui/msp5/preferences.png', mm_hover_zoom()), 'gui/msp5/mm_base.png') offset (-6, -6)
                    image 'gui/msp5/mm_hover.png' offset (-6, -6):
                        if active == ['preferences', 1]:
                            at BAPR()
                        elif active == ['preferences', 0]:
                            at BDPR()
                        elif active != None:
                            if active[0] != 'preferences':
                                at BDPR()
                        else:
                            at BNT()

                    image 'gui/msp5/preferences_t.png' align (.5, 1.0) offset (0, 14)

                    hover_sound 'neon.mp3'
            frame:
                background 'gui/msp5/mm_shadow.png'
                xysize (373, 265)
                at top_m(.2)
                button:
                    xysize (345, 237)
                    align  (.0 , .0 )
                    offset (14 ,  14)

                    hovered   [ SetScreenVariable('active', ['about', 1]) ]
                    unhovered [ SetScreenVariable('active', ['about', 0]) ]

                    action ShowMenu("about")

                    image AlphaMask(At('gui/msp5/credits.png', mm_hover_zoom()), 'gui/msp5/mm_base.png') offset (-6, -6)
                    image 'gui/msp5/mm_hover.png' offset (-6, -6):
                        if active == ['about', 1]:
                            at BAPR()
                        elif active == ['about', 0]:
                            at BDPR()
                        elif active != None:
                            if active[0] != 'about':
                                at BDPR()
                        else:
                            at BNT()

                    image 'gui/msp5/credits_t.png' align (.5, 1.0) offset (0, 14)

                    hover_sound 'neon.mp3'

                    
    button:
        focus_mask True
        # auto "gui/msp5/exit_%s.png"
        action Quit(confirm=True)
        hovered [ Play ("sound", "neon.mp3"), SetLocalVariable("exit_h", 1)]
        unhovered SetLocalVariable("exit_h",0)
        image "gui/msp5/exit.png"
        image im.MatrixColor("gui/msp5/exit.png", im.matrix.colorize("#ff696180", "#f1f1f180")):
            if exit_h == 1:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 1.0
            elif exit_h == 0:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 0
            else:
                at transform:
                    alpha 0
        xysize (1920, 1080)
        xpos 0
        ypos 0
        at exit_m(0.25)

    # imagemap:
    #     ground "main_menu.jpg"
    #     hover "main_menu2.jpg"

    #     hotspot (474, 32, 1003, 130) action OpenURL("https://www.patreon.com/user?u=24799077") hovered [ Play ("sound", "neon.mp3")]

    #     hotspot (786, 957, 116, 92) action OpenURL("https://www.patreon.com/user?u=24799077") hovered [ Play ("sound", "neon.mp3")]

    #     hotspot (901, 938, 115, 126) action OpenURL("https://subscribestar.adult/caribdis") hovered [ Play ("sound", "neon.mp3")]

    #     hotspot (1017, 937, 122, 128) action OpenURL("https://discord.gg/caribdisgames") hovered [ Play ("sound", "neon.mp3")]

    #     hotspot (188, 740, 253, 148) action Start() hovered [ Play ("sound", "neon.mp3")]

    #     hotspot (453, 740, 259, 155) action ShowMenu("load") hovered [ Play ("sound", "neon.mp3")]

    #     hotspot (727, 742, 435, 151) action ShowMenu("preferences") hovered [ Play ("sound", "neon.mp3")]

    #     hotspot (1180, 740, 309, 160) action ShowMenu("about") hovered [ Play ("sound", "neon.mp3")]

    #     hotspot (1511, 745, 230, 147) action Quit(confirm=not main_menu) hovered [ Play ("sound", "neon.mp3")]

    ## This empty frame darkens the main menu.


    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if not main_menu:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"
        xalign 0.5
        hbox:

            ## Reserve space for the navigation section.
            if not main_menu:
                frame:
                    style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True


                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True


                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    if not main_menu:
        label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    # background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos 91
    yalign 0.93
    yoffset -45

style returnbutton2:
    size 50


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu
    key 'game_menu' action Return()
    add "gui/msp5/blank.jpg"
    label _("{color=#f1f1f1}{size=100}CREDITS") xpos 100 ypos 25
    viewport:
        xsize 1720
        ysize 801
        xalign 0.5
        ypos 179
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            style_prefix "about"
            text _("{color=#00cc99}{b}ETERNUM")
            text _("Version [config.version!t]\n")
            #text _("")
            text _("Created by {a=https://www.patreon.com/onceinalifetime}Caribdis{/a}")
            text _("{size=12}")
            text _("{size=35}Proofread by Nebula, Scylla, Tonymack, & Diver")
            text _("")
            text _("")
            text _("{color=#00cc99}{b}Huge Thanks to:{/color}")
            text _("{size=22}")
            text _("CritPhil, Frost, Pond, and Turska for moderating the Discord Server.")
            text _("{size=22}")
            text _("Dread for their animations.")
            text _("{size=22}")
            text _("Ixalon for their Android ports.")
            text _("{size=22}")
            text _("Pax for their UI designs.")
            text _("{size=22}")
            text _("Tateshiko, Dark Assassin, Claimant, and Canchez for their music and community contributions.")
            text _("{size=22}")
            text _("Demon Sound for their music.")
            text _("{size=22}")
            text _("Mananddivine for their music.")
            text _("{size=22}")
            text _("Bibifoc, Yaboku, Calaadia, FarrenYunior, Messe, Niichan, and every other dev, modder or member of this community that helped me in some way.")
            text _("")
            text _("")
            text _("")
            text _("This visual novel is free and always will be. If you'd like to support this project, you can go to my {a=https://www.patreon.com/onceinalifetime}Patreon{/a}/{a=https://subscribestar.adult/caribdis}Subscribestar{/a}/{a=https://caribdis.itch.io/}Itch.io{/a} pages.")
            text _("Thank you!")
            text _("")
            text _("")
            text _("")
            text _("{color=#00cc99}Huge Thanks to my {b}Founder Patrons:{/b}{/color}")
            text _("Akira")
            text _("Calaadia")
            text _("Canchez")
            text _("Claimant")
            text _("DarkAssassin")
            text _("Eggrik")
            text _("Jasticus")
            text _("Kainan")
            text _("Mos")
            text _("Tissle")
            text _("")
            text _("")
            text _("{color=#00cc99}Huge Thanks to my {b}Demon Lord Patrons:{/b}{/color}")
            text _("7parcival7")
            text _("AngelKun")
            text _("Ans")
            text _("Anzoo")
            text _("ApexSpectral")
            text _("Artybysolarbeam")
            text _("Axr110")
            text _("BigFella")
            text _("Birujo")
            text _("Bore")
            text _("BrawlerCable")
            text _("Birghtstar")
            text _("Buithetruong178")
            text _("CaptBlueWolf")
            text _("CaptJackFrost")
            text _("CromSonke")
            text _("Cyber0005")
            text _("D4rkar117")
            text _("Darra")
            text _("DeepSwamp")
            text _("EmeraldTheDingo")
            text _("Emirashirou")
            text _("FireWarx")
            text _("Goomba")
            text _("Greenjf")
            text _("Harry")
            text _("Igotyuandme")
            text _("IKhajiitMyPants")
            text _("JaredKyaw")
            text _("JOJOXiong")
            text _("Josephh151")
            text _("Jsherwood")
            text _("KingInYellow")
            text _("Kk300435")
            text _("Krauser")
            text _("LeoRaion")
            text _("LeroyJemkins")
            text _("Lkmz")
            text _("Lucas312")
            text _("Major")
            text _("Mangetsu")
            text _("MantisLord")
            text _("NaMJeGej")
            text _("MrSolum")
            text _("PanicSpoon")
            text _("PlutonicPlate57")
            text _("RayKID")
            text _("Rikel")
            text _("Rioadx")
            text _("RussellHarbison")
            text _("Shelter")
            text _("Silverwind")
            text _("Skipper0820")
            text _("SoupIsGood")
            text _("Style")
            text _("Sucadico")
            text _("Swagger")
            text _("Tim216")
            text _("TohsakaJz")
            text _("Twojkszmar")
            text _("Vertganti")
            text _("Viking1999")
            text _("Winged")
            text _("WolfSniper7846")
            text _("Woozie")
            text _("Worldstar")
            text _("Zantengetsu")
            text _("{font=chinafont.ttf}你的好朋友塔塔")
            text _("{font=chinafont.ttf}国一达梨鸭")
            text _("{font=chinafont.ttf}夏橘 ")
            text _("{font=chinafont.ttf}胡适不打牌")
            text _("")
            text _("")
            text _("{color=#00cc99}And a Huge Thanks to my all my other {b}God, Eternumite, Master, Supporter, and Follower Patrons! You guys are the best!{/b}{/color}")
            text _("")
            text _("")
            text _("")
            text _("")








            if gui.about:
                text "[gui.about!t]\n"
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            text _("")
            text _("")
    
    textbutton _("Return") action Return() xalign 0.5 yalign 1.0 yoffset -25


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu
    if main_menu:
        add "gui/msp5/blank.jpg"
        label _("{color=#f1f1f1}{size=100}LOAD") xpos 110 ypos 25
    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    if not main_menu:
        use game_menu(title):
            fixed:

                ## This ensures the input will get the enter event before any of the
                ## buttons do.
                order_reverse True

                ## The page name, which can be edited by clicking on a button.
                button:
                    style "page_label"

                    key_events True
                    ypos -0.07
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value

                ## The grid of file slots.
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.38

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)

                ## Buttons to access other pages.
                hbox:
                    style_prefix "page"
                    ypos 0.93
                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
    elif main_menu:
        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                ypos -0.07
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.38

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"
                ypos 0.93
                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()





style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label_y:
    # xpadding 75
    ypadding 50

style page_label:
    xpadding 75
    ypadding 50

style page_label_text:
    text_align 0.5
    layout "subtitle"
    idle_color "FFFFFF"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    key 'game_menu' action Return()

    add "gui/msp5/pref_bg.png"
    label _("{color=#f1f1f1}{size=100}PREFERENCES") xpos 110 ypos 25

    default edit_mode   = False

    viewport:
        xsize 1060
        ysize 721
        xpos 140
        ypos 219
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                        #label _("Voice Volume")
                        #hbox:
                        #    bar value Preference("voice volume")
                        #    if config.sample_voice:
                        #        textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Size ([persistent.text_size]/50)")
                    bar:
                        value FieldValue(persistent, "text_size", offset=20, range=30, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.text_size", gui.text_size))


                    label _("Text Outline ([persistent.text_outline]/4)")
                    bar:
                        value FieldValue(persistent, "text_outline", range=4, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.text_outline", 2))

            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                vbox:
                    $ percent_value = int(persistent.textbox_opacity * 100)
                    label _("Textbox Opacity ([percent_value]%)")
                    bar:
                        value FieldValue(persistent, "textbox_opacity", range=1.0, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.textbox_opacity", 0.0))


                    label _("Textbox Width ([persistent.textbox_width]/1646)")
                    bar:
                        value FieldValue(persistent, "textbox_width", offset=1116, range=530, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.textbox_width", gui.dialogue_width))

                    label _("Textbox Height ([persistent.textbox_height]/350)")
                    bar:
                        value FieldValue(persistent, "textbox_height", offset=100, range=250, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.textbox_height", gui.textbox_height))
            null height (4 * gui.pref_spacing)
    viewport:
        xsize 480
        ysize 633
        xpos 1300
        ypos 219
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            xalign 0.5
            yalign 0.5
            
            if not main_menu and not _in_replay and nicknameunlock:
                vbox:
                    label _("Edit Nickname")
                    if not edit_mode:
                        textbutton nickname action SetScreenVariable("edit_mode", True)
                    else:
                        key "dismiss" action SetScreenVariable("edit_mode", False)
                        key "input_enter" action SetScreenVariable("edit_mode", False)
                        input:
                            value FieldInputValue(store, "nickname", returnable=True)
            if renpy.variant("pc"):

                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
            
            # Note to translators: This preference menu appears automatically
            # when more than one language is available. By default, it will use
            # the internal language name of your translation. If you want to
            # provide a better title for your language, add a snippet like this
            # to the top of your screens.rpy translation file (but outside any
            # "translate strings" block):
            #
            # init python:
            #     language_titles["chinese"] = "中文"
            #     language_title_fonts["chinese"] = "tl/chinese/fonts/Thin.ttf"
            #
            # You can omit setting a different font if you don't need it, but if
            # you do set one, you of course need to provide that font with your
            # translation files.
            if len(renpy.known_languages()) > 0:
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    # Please do not translate this "English" string; that way,
                    # English players will find the language settings, even
                    # when the game is set to a non-English language.
                    textbutton "English {#do-not-translate}":
                        action Language(None)
                    for lang in renpy.known_languages():
                        $ option_title = language_titles.get(lang, lang)
                        $ option_font = language_title_fonts.get(lang, None)
                        textbutton option_title:
                            action Language(lang)
                            if option_font is not None:
                                text_font option_font

            vbox:
                style_prefix "radio"
                label _("Rollback Side")
                textbutton _("Disable") action Preference("rollback side", "disable")
                textbutton _("Left") action Preference("rollback side", "left")
                textbutton _("Right") action Preference("rollback side", "right")

            vbox:
                style_prefix "check"
                label _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            vbox:
                style_prefix "radio"
                label _("Quick Menu")
                textbutton _("Enabled") action SetField(persistent,"quick_menu", True)
                textbutton _("Disabled") action SetField(persistent,"quick_menu", False)
            
            vbox:
                style_prefix "radio"
                label _("Interface Motion")
                textbutton _("Enabled") action SetField(persistent,"motion", 1.0)
                textbutton _("Disabled") action SetField(persistent,"motion", .0)

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)


    # textbutton "Return" action Return()    xpos 91    yalign 0.93    yoffset -45
    default return_h = None
    button:
        action Return()
        focus_mask True
        image "gui/msp5/return.png"
        image im.MatrixColor("gui/msp5/return.png", im.matrix.colorize('#f1f1f180', '#f1f1f180')):
            if return_h == 1:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
            elif return_h == 0:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 0.0 blur 5
            else:
                at transform:
                    alpha 0.0
        hovered [ SetLocalVariable("return_h", 1) ]
        unhovered [ SetLocalVariable("return_h", 0) ]

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")


style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

    idle_color gui.insensitive_color
    hover_color gui.insensitive_color
    selected_idle_color "#ffffff"
    selected_hover_color gui.hover_color

style slider_vbox:
    xsize 675




## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll="viewport", yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
    tag menu
    default device = "keyboard"
    use game_menu(_("Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 23
            hbox:
                textbutton _("About") action SetScreenVariable("device", "keyboard")
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Shift+S or F5")
        text _("Quick Save.")

    hbox:
        label _("Shift+L or F9")
        text _("Quick Load.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Alt+A")
        text _("Toggles auto-forward mode.")

    hbox:
        label _("Shift+P")
        text _("Accesses the preferences menu.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")



screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

transform fir():

    xoffset 250
    alpha 0.0
    blur 25
    easein_quint (0.75 * persistent.motion) xoffset 0 alpha 1.0 blur 0

transform fil():
    
    xoffset -250
    alpha 0.0
    blur 25
    easein_quint (0.75 * persistent.motion) xoffset 0 alpha 1.0 blur 0

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    if message == gui.QUIT:
        add "gui/msp5/v6/exit_overlay.png" at transform:
            alpha .0
            ease_quint (1.25 * persistent.motion) alpha 1.0
        default yes_h = None
        default no_h = None
        if yes_h == 1:
            add "gui/msp5/v6/yes_h.png" at fil()
        elif no_h == 1:
            add "gui/msp5/v6/no_h.png" at fir()
        frame:
            background None
            xysize (770, 387)
            align  (.5 , .5)
            vbox:
                xycenter (.5, .5)
                spacing 8
                image 'gui/msp5/v6/label.png' xycenter (.5, .5):
                    at quit_bb(.0)

                hbox:
                    spacing -55
                    button:
                        xysize (412, 63)
                        image At("gui/msp5/v6/yes.png", quit_yes()) xycenter (.5, .5)
                        image "gui/msp5/v6/yes_t.png" xycenter (.5, .5) offset (-64, 0)
                        hovered [ SetLocalVariable("yes_h", 1), Play ("sound", "neon.mp3") ]
                        unhovered [ SetLocalVariable("yes_h", 0) ]
                        focus_mask True
                        action yes_action
                        at quit_bb(.1)
                    button:
                        xysize (412, 63)
                        image At("gui/msp5/v6/no.png", quit_no()) xycenter (.5, .5)
                        image "gui/msp5/v6/no_t.png" xycenter (.5, .5) offset (64, 0)
                        hovered [ SetLocalVariable("no_h", 1), Play ("sound", "neon.mp3") ]
                        unhovered [ SetLocalVariable("no_h", 0) ]
                        focus_mask True
                        action no_action
                        at quit_bb(.2)
    else:
        add "gui/overlay/confirm.png"
        frame:

            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 150

                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu and persistent.quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background None

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900


style mytext is text:
        font "poiretone.ttf"
        outlines [ (1, "#FFFFFF") ]
style mytextnool is text:
        font "poiretone.ttf"
style mytextoutline is text:
        font "poiretone.ttf"
        outlines [  (2, "#000000"),
                    (1 ,"#FFFFFF"),
                    ]
style mytext2 is text:
        font "Sketchzone.ttf"
        outlines [ (1, "#000000") ]

style mytext2time is text:
        font "EagleHorizon.ttf"
        outlines [ (1, "#000000") ]

style mytexttale is text:
        font "tales.otf"
        outlines [  (4, "#000000"),
                    (1 ,"#ffffff"),
                    ]

style mytext3 is text:
        font "alwayslovely.ttf"
        size 50
        xmaximum 1480
        outlines [ (1, "#000000") ]

style mytextcountdown is text:
        font "Sketchzone.ttf"
        outlines [ (1, "#000000") ]
        size 180
        yalign 0.26 xalign 0.5

style mytextarabia is text:
        font "arabicfont.ttf"
        color "#cfcfcf"
        outlines [ (1, "#000000") ]
        size 55

style mytextelven is text:
        font "balgruf.ttf"
        color "#cfcfcf"
        outlines [ (1, "#000000") ]
        size 45

style textsp is say_dialogue:
    font "adeb.ttf"
    line_leading -9

style textsameasdialogue is say_dialogue:
    font "ade1.ttf"
    size 36 
    italic True
    line_leading 20
    xalign 0.5 yalign 0.65 text_align 0.5 xmaximum 1500 

style bla_leading is say_dialogue:
    line_leading 10



############################################# MyScreens
screen contest1():
    add "contest" xalign 0.97 yalign 0.1
    text _("{size=50}[mc!t]") xalign 0.973 yalign 0.05 style "mytext2"
    text _("{size=45}[orionc]") xalign 0.954 yalign 0.124 style "mytext2"
screen contest2():
    add "contest" xalign 0.97 yalign 0.27
    text _("{size=50}Aysha") xalign 0.975 yalign 0.21 style "mytext2"
    text _("{size=45}[ayshac]") xalign 0.954 yalign 0.283 style "mytext2"
screen contest3():
    add "contest" xalign 0.97 yalign 0.44
    text _("{size=50}Jerry") xalign 0.971 yalign 0.37 style "mytext2"
    text _("{size=45}[jerryc]") xalign 0.954 yalign 0.444 style "mytext2"
screen eternals():
    add "eternals"
    text _("{size=35}[money] eternals") xpos 0.86 yalign 0.07 style "mytextoutline"
screen heart():
    hbox:
        imagebutton:
            idle "heart1"
            hover "heart2"
            action [Play("soundlow", "beat.ogg"), ShowMenu('point')]
screen attack():
    imagebutton:
        xalign 0.98 yalign 0.04
        idle "levels1"
        hover "levels2"
        action Jump('attackcon')
screen hallways:
    imagebutton:
        idle "hallway1"
        hover "hallway1b"
        xalign 0.26
        yalign 0.38
        action Jump('corridorl')
    imagebutton:
        idle "hallway2"
        hover "hallway2b"
        xalign 1.0
        yalign 0.44
        action Jump('halll')
screen halls:
    imagebutton:
        idle "hall1"
        hover "hall1b"
        xalign 0.0
        yalign 0.41
        action Jump('hallwayl')
    imagebutton:
        idle "hall2"
        hover "hall2b"
        xalign 0.51
        yalign 0.42
        action Jump('livingrooml')
screen livings:
    imagebutton:
        idle "living1"
        hover "living1b"
        xalign 0.5
        yalign 0.0
        action Jump('halll')
    imagebutton:
        idle "living2"
        hover "living2b"
        xalign 1.0
        yalign 0.0
        action Jump('gardenl')
screen gardens:
    imagebutton:
        idle "garden1"
        hover "garden1b"
        xalign 0.0
        yalign 1.0
        action Jump('livingrooml')
    imagebutton:
        idle "garden2"
        hover "garden2b"
        xalign 1.0
        yalign 0.0
        action Jump('bedrooml')
screen corridors:
    imagebutton:
        idle "corridor1"
        hover "corridor1b"
        xalign 0.0
        yalign 0.2
        action Jump('bedrooml')
    imagebutton:
        idle "corridor2"
        hover "corridor2b"
        xalign 0.2
        yalign 1.0
        action Jump('officel')
    imagebutton:
        idle "corridor3"
        hover "corridor3b"
        xalign 0.205
        yalign 0.6
        action Jump('laundryl')
    imagebutton:
        idle "corridor4"
        hover "corridor4b"
        xalign 1.0
        yalign 1.0
        action Jump('hallwayl')
screen backs:
    imagebutton:
        idle "back1"
        hover "back1b"
        xalign 0.5
        yalign 1.0
        action Jump('corridorl')
screen backsb:
    imagebutton:
        idle "back1"
        hover "back1b"
        xalign 0.5
        yalign 1.0
        action Jump('bedrooml')
screen bedrooms:
    imagebutton:
        idle "bedroom1"
        hover "bedroom1b"
        xalign 0.0
        yalign 0.0
        action Jump('gardenl')
    imagebutton:
        idle "bedroom2"
        hover "bedroom2b"
        xalign 1.0
        yalign 0.0
        action Jump('corridorl')
    imagebutton:
        idle "bedroom3"
        hover "bedroom3b"
        xalign 0.5
        yalign 1.0
        action Jump('bathrooml')
    if safesurvival:
        imagebutton:
            idle "bedroom4"
            hover "bedroom4b"
            xalign 1.0
            yalign 1.0
            action Jump('safel')



#screen level:
#    add "level"
#    text _("{size=140}32") xalign 0.19 yalign 0.45 style "mytext"
#    text _("{size=90}10") xalign 0.41 yalign 0.41 style "mytext"
#    text _("{size=90}10") xalign 0.585 yalign 0.28 style "mytext"
#    text _("{size=90}10") xalign 0.585 yalign 0.28 style "mytext"

# screen points:
#     modal True
#     style_prefix "points"

#     add "points"

#     imagemap:
#         ground "points"
#         idle "points2"
#         hover "points3"
#         hotspot (1541, 628, 310, 338) keysym "game_menu" action Return()

#         #
#         # ANNIE
#         #
#         if annieu:
#             hotspot (66, 51, 357, 465):
#                 action [ Play("soundlow", audio.beat),
#                         SetVariable("current_look", renpy.random.randint(0, len(looks["annie"])-1)),
#                         Show('bios', girl="annie", transition=dissolve) ]
#         if not anniepath:
#             add "annielost"

#         #
#         # NANCY
#         #
#         if nancyu:
#             hotspot (436, 20, 350, 470):
#                 action [ Play("soundlow", audio.beat),
#                         SetVariable("current_look", renpy.random.randint(0, len(looks["nancy"])-1)),
#                         Show('bios', girl="nancy", transition=dissolve) ]
#         if not nancypath:
#             add "nancylost"

#         #
#         # PENELOPE
#         #
#         if penelopeu:
#             hotspot (793, 27, 353, 496):
#                 action [ Play("soundlow", audio.beat),
#                         SetVariable("current_look", renpy.random.randint(0, len(looks["penelope"])-1)),
#                         Show('bios', girl="penelope", transition=dissolve) ]
#         if not penelopepath:
#             add "penelopelost"

#         #
#         # DALIA
#         #
#         if daliau:
#             hotspot (1175, 38, 325, 463):
#                 action [ Play("soundlow", audio.beat),
#                         SetVariable("current_look", renpy.random.randint(0, len(looks["dalia"])-1)),
#                         Show('bios', girl="dalia", transition=dissolve) ]
#         if not daliapath:
#             add "dalialost"

#         #
#         # LUNA
#         #
#         if lunau:
#             hotspot (1526, 31, 344, 485):
#                 action [ Play("soundlow", audio.beat),
#                         SetVariable("current_look", renpy.random.randint(0, len(looks["luna"])-1)),
#                         Show('bios', girl="luna", transition=dissolve) ]
#         if not lunapath:
#             add "lunalost"

#         #
#         # ALEX
#         #
#         if alexu:
#             hotspot (67, 514, 357, 474):
#                 action [ Play("soundlow", audio.beat),
#                         SetVariable("current_look", renpy.random.randint(0, len(looks["alex"])-1)),
#                         Show('bios', girl="alex", transition=dissolve) ]
#         if not alexpath:
#             add "alexlost"

#         #
#         # NOVA
#         #
#         if novau:
#             hotspot (443, 508, 342, 486):
#                 action [ Play("soundlow", audio.beat),
#                         SetVariable("current_look", renpy.random.randint(0, len(looks["nova"])-1)),
#                         Show('bios', girl="nova", transition=dissolve) ]
#         if not novapath:
#             add "novalost"

#         #
#         # SIDE GIRLS
#         #
#         if sideu:
#             hotspot (787, 512, 414, 488):
#                 action [ Play("soundlow", audio.neon),
#                         SetVariable("filter_scene", "all"),
#                         SetVariable("filter_girl", "side"),
#                         Show("gallery", transition=dissolve) ]

#         #
#         # GALLERY
#         #
#         hotspot (1193, 558, 314, 425):
#             action [ Play("soundlow", audio.beat),
#                     SetVariable("filter_scene", "all"),
#                     SetVariable("filter_girl", "all"),
#                     Show("gallery", transition=dissolve) ]


############################################################################# 0.3

screen scrollwarthogs:
    modal True
    add "warthogsmap"
    imagemap:
        ground "warthogsmap2"
        idle "warthogsmap2"
        hover "warthogsmap3"
        hotspot (1625, 1, 293, 218) action [ Play("soundlow", "audio/sfx/paper.ogg"), Jump('prizelabel') ] hovered [ Play ("sound", "audio/sfx/pencil.mp3")]
        hotspot (1, 219, 417, 176) action [ Play("soundlow", "audio/sfx/paper.ogg"), Jump('divinationlabel') ] hovered [ Play ("sound", "audio/sfx/pencil.mp3")]
        hotspot (726, 266, 394, 184) action [ Play("soundlow", "audio/sfx/paper.ogg"), Jump('emporiumlabel') ] hovered [ Play ("sound", "audio/sfx/pencil.mp3")]
        hotspot (1542, 477, 343, 221) action [ Play("soundlow", "audio/sfx/paper.ogg"), Jump('potionslabel') ] hovered [ Play ("sound", "audio/sfx/pencil.mp3")]
        hotspot (995, 560, 440, 178) action [ Play("soundlow", "audio/sfx/paper.ogg"), Jump('conjurationlabel') ] hovered [ Play ("sound", "audio/sfx/pencil.mp3")]
        hotspot (1254, 258, 352, 183) action [ Play("soundlow", "audio/sfx/paper.ogg"), Jump('darkartslabel') ] hovered [ Play ("sound", "audio/sfx/pencil.mp3")]
    add "warthogsclouds"

screen qte():
    imagebutton:
        align (0.77, 0.36)
        idle "dodge1"
        hover "dodge1b"
        action Jump("winj1")

    timer 5.0 action Jump("lose")

    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 5.0, 1)
screen qte2():
    imagebutton:
        align (0.7, 0.36)
        idle "block1"
        hover "block1b"
        action Jump("winj2")

    timer 3.0 action Jump("lose")

    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 3.0, 1)
screen qte3():
    imagebutton:
        align (0.1, 0.66)
        idle "attack1"
        hover "attack1b"
        action Jump("winj3")

    timer 3.0 action Jump("lose")

    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 3.0, 1)

##############################################################################

screen slotmenu:
    imagebutton:
        idle "slotplay"
        hover "slotplayb"
        xalign 0.0
        yalign 0.4
        action Jump('slotplaylabel')
    imagebutton:
        idle "slotleave"
        hover "slotleaveb"
        xalign 1.00
        yalign 1.00
        action Jump('slotleavelabel')


##############################################################################

screen afewhourslater:
    text _("A few hours later...") xalign 0.5 yalign 0.45 style "mytext2time" size 52

screen afewdayslater:
    text _("A few days later...") xalign 0.5 yalign 0.45 style "mytext2time" size 52 

screen threeweekslater:
    text _("3 weeks later") xalign 0.5 yalign 0.45 style "mytext2time" size 52

screen afewminuteslater:
    text _("A few minutes later...") xalign 0.5 yalign 0.45 style "mytext2time" size 52

screen sometimelater:
    text _("Some time later...") xalign 0.5 yalign 0.45 style "mytext2time" size 52

screen tenyearslater:
    text _("10 years later...") xalign 0.5 yalign 0.45 style "mytext2time" size 52

screen meanwhile:
    text _("Meanwhile...") xalign 0.5 yalign 0.45 style "mytext2time" size 52

screen nextday:
    text _("The next day...") xalign 0.5 yalign 0.45 style "mytext2time" size 52

screen coupledays:
    text _("A couple of days later...") xalign 0.5 yalign 0.45 style "mytext2time" size 52 

screen sixminuteslater:
    text _("6 minutes and 13 seconds later...") xalign 0.5 yalign 0.45 style "mytext2time" size 52

transform heartbeat:
    alpha 0.0
    linear 0.5 alpha 1.0
    pause 0.0
    linear 0.5 alpha 0.0
screen heartbeat():
    frame:
        style "empty"
        at heartbeat # Apply the transform to the whole frame, so whatever inside it will use the transform
        add "heartr"
    timer 1.5 action Hide("heartbeat")


################################################################################################################

transform corner_popup:
    alpha 0.0
    pause 1
    linear 4.0 alpha 1.0
    pause 0.5
    linear 5.0 alpha 0.0

transform left_to_right(duration=2.5):

    offset (-1920, 0)
    zoom .0

    easein_quart 2.5 offset (0, 0) zoom 1.0

########################################################################################## 0.4 VERSION

screen time0940:
    text _("09:58 PM") xalign 0.5 yalign 0.45 style "mytext" size 50
screen time0855:
    text _("09:00 PM") xalign 0.5 yalign 0.45 style "mytext" size 50
screen time0909:
    text _("09:09 PM") xalign 0.5 yalign 0.45 style "mytext" size 50
screen time0920:
    text _("09:22 PM") xalign 0.5 yalign 0.45 style "mytext" size 50
screen time0930:
    text _("09:35 PM") xalign 0.5 yalign 0.45 style "mytext" size 50
screen time0938:
    text _("09:43 PM") xalign 0.5 yalign 0.45 style "mytext" size 50
screen time0958:
    text _("10:01 PM") xalign 0.5 yalign 0.45 style "mytext" size 50


screen deathtext:
    frame:
        xalign 0.5
        yalign 0.74
        vbox:
            xsize 1200
            text _("YOU HAVE DIED") xalign 0.5 text_align 0.5 style "mytext" size 40
screen deathtext2:
    frame:
        xalign 0.5
        yalign 0.74
        vbox:
            xsize 1200
            text _("YOUR LEVEL AND INVENTORY WILL NOW BE RESET{p}PLEASE WAIT 24-HOURS BEFORE ATTEMPTING TO LOG IN AGAIN") xalign 0.5 text_align 0.5 style "mytext" size 40
screen deathtext3:
    frame:
        xalign 0.5
        yalign 0.74
        vbox:
            xsize 1200
            text _("THANK YOU FOR PLAYING ETERNUM") xalign 0.5 text_align 0.5 style "mytext" size 40


screen fridaycorner():
    frame:
        style "empty"
        at corner_popup
        add "friday"
    timer 11 action Hide("fridaycorner")
screen saturdaycorner():
    frame:
        style "empty"
        at corner_popup
        add "saturday"
    timer 11 action Hide("saturdaycorner")
screen sundaycorner():
    frame:
        style "empty"
        at corner_popup
        add "sunday"
    timer 11 action Hide("sundaycorner")
screen daybeforecorner():
    frame:
        style "empty"
        at corner_popup
        add "daybefore"
    timer 11 action Hide("daybeforecorner")
screen afewdayslatercorner():
    frame:
        style "empty"
        at corner_popup
        add "afewdayslatercorner"
    timer 11 action Hide("afewdayslatercorner")
screen afewhourslatercorner():
    frame:
        style "empty"
        at corner_popup
        add "afewhourslatercorner"
    timer 11 action Hide("afewhourslatercorner")
screen afewdaysearliercorner():
    frame:
        style "empty"
        at corner_popup
        add "afewdaysearlier"
    timer 11 action Hide("afewhourslatercorner")
screen tenyearsago():
    frame:
        style "empty"
        at corner_popup
        add "10yearsago"
    timer 11 action Hide("10yearsago")
screen earliercorner():
    frame:
        style "empty"
        at corner_popup
        add "earliercorner"
    timer 11 action Hide("earliercorner")


screen audiologs():
    imagebutton:
        xalign 0.995 yalign 0.0
        idle "vinylc"
        hover "vinylb"
        action [Play("sound5", "audio/sfx/beep3.mp3"), Show("audiologs2", transition=dis04), Hide("audiologs")]
screen audiologs2:
    modal True
    imagebutton:
        xalign 0.95 yalign 0.03
        idle "al1"
        hover "al1b"
        action [Play("sound6", "audio/sfx/isaac1.ogg"), Show("audiolog1", transition=dissolve), Hide("audiologs2")]
    imagebutton:
        xalign 0.95 yalign 0.91
        idle "returnb"
        hover "returnb2"
        action [Play("sound6", "audio/sfx/beep3.mp3"), Show("audiologs", transition=dis04), Hide("audiologs2")]
    if card42:
        imagebutton:
            xalign 0.95 yalign 0.2
            idle "al42"
            hover "al42b"
            action [Play("sound6", "audio/sfx/isaac42.ogg"), Show("audiolog42", transition=dissolve), Hide("audiologs2")]
    if card43:
        imagebutton:
            xalign 0.95 yalign 0.37
            idle "al43"
            hover "al43b"
            action [Play("sound6", "audio/sfx/isaac43.ogg"), Show("audiolog43", transition=dissolve), Hide("audiologs2")]
    if card48:
        imagebutton:
            xalign 0.95 yalign 0.54
            idle "al48"
            hover "al48b"
            action [Play("sound6", "audio/sfx/isaac48.ogg"), Show("audiolog48", transition=dissolve), Hide("audiologs2")]
    if card55:
        imagebutton:
            xalign 0.95 yalign 0.70
            idle "al55"
            hover "al55b"
            action [Play("sound6", "audio/sfx/isaac55.ogg"), Show("audiolog55", transition=dissolve), Hide("audiologs2")]
    if card67:
        imagebutton:
            xalign 0.95 yalign 0.70
            idle "al67"
            hover "al67b"
            action [Play("sound6", "audio/sfx/isaac67.ogg"), Show("audiolog67", transition=dissolve), Hide("audiologs2")]
    if cardlast:
        imagebutton:
            xalign 0.61 yalign 0.45
            idle "corrupted"
            hover "corruptedb"
            action [Play("sound6", "audio/sfx/isaaclast.ogg"), Show("audiologlast", transition=dissolve), Hide("audiologs2")]
transform spin:
    rotate 0
    linear 2.0 rotate 360
    repeat
transform audiolog1_0:
    alpha 0.0
    pause 2.1
    linear 0.5 alpha 1.0
    pause 1.7
    linear 1.0 alpha 0.0
transform audiolog1_1:
    alpha 0.0
    pause 5.7
    linear 0.5 alpha 1.0
    pause 12.3
    linear 1.0 alpha 0.0
transform audiolog1_2:
    alpha 0.0
    pause 19
    linear 0.5 alpha 1.0
    pause 11.4
    linear 1.0 alpha 0.0
transform audiolog1_3:
    alpha 0.0
    pause 31.4
    linear 0.5 alpha 1.0
    pause 7.6
    linear 1.0 alpha 0.0
transform audiolog1_4:
    alpha 0.0
    pause 40
    linear 0.5 alpha 1.0
    pause 12
    linear 1.0 alpha 0.0
transform audiolog1_5:
    alpha 0.0
    pause 53
    linear 0.5 alpha 1.0
screen audiolog1:
    frame:
        add "vinyl" at spin
        xalign 0.115 yalign 0.02
    frame:
        at audiolog1_0
        text _("Audio log 1. October 2.") style "mytext3"
        xpos 0.2 yalign 0.064
    frame:
        at audiolog1_1
        text _("Umm... hello... my name is Isaac Langston. Sorry, this is a bit... weird for me, I’ve never done anything like this before, but... I figured maybe an audio log would be useful for coping with the loneliness of this job.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog1_2
        text _("Let’s see... it’s already been 6 years since I started working for the Ulysses Corporation as an aerospace maintenance engineer on the Andromeda server. Time seems to just fly by when Ulysses is constantly keeping you busy.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog1_3
        text _("You see, Ulysses is so obsessed with immersion and realism that they insist on rectifying any faults or defects as you’d do it in real life.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog1_4
        text _("If something breaks or stops working on such a high profile server like this, we’re on-call for immediate response. Being on constant standby is a little exhausting, but fuck... they pay so well... can I really complain?") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog1_5
        text _("It’s almost easy to forget this is all just for a video game. More real than real life... heh...") style "mytext3"
        xpos 0.2 yalign 0.064
        # yalign 0.064 one-line
    timer 61 action [Hide("audiolog1", transition=dis), Show("audiologs"), SetVariable("card1listened", True)]
transform audiolog2_1:
    alpha 0.0
    pause 1.5
    linear 0.5 alpha 1.0
    pause 12.5
    linear 1.0 alpha 0.0
transform audiolog2_2:
    alpha 0.0
    pause 15
    linear 0.5 alpha 1.0
    pause 13
    linear 1.0 alpha 0.0
transform audiolog2_3:
    alpha 0.0
    pause 29
    linear 0.5 alpha 1.0
    pause 11
    linear 1.0 alpha 0.0
transform audiolog2_4:
    alpha 0.0
    pause 41
    linear 0.5 alpha 1.0
    pause 20
    linear 1.0 alpha 0.0
transform audiolog2_5:
    alpha 0.0
    pause 62
    linear 0.5 alpha 1.0
    pause 10
    linear 1.0 alpha 0.0
transform audiolog2_6:
    alpha 0.0
    pause 73
    linear 0.5 alpha 1.0
screen audiolog42:
    frame:
        add "vinyl" at spin
        xalign 0.115 yalign 0.02
    frame:
        at audiolog2_1
        text _("Audio log 42. September 15. I’ve been to more than 600 different planets, spaceships, and stations all over this damn server, and I thought I’ve seen it all. Until today.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog2_2
        text _("I was responding to an outage and saw something so... disturbing... and honestly it still has me a little shaken. The AG-Centaur station went offline and I was called in to reestablish connectivity.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog2_3
        text _("When I arrived on site and began troubleshooting, I found the communication system to be functioning perfectly. Thought it must’ve been a fluke in our monitoring systems or something. But then... I saw the crew of the station.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog2_4
        text _("They were all... dead. Corpses littered the floor, blood splattered across the panels, and guts just coated the entire deck. It was such a grotesque sight. And the smell? God... But you know what the weirdest thing was?") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog2_5
        text _("AG-Centaur was just a fucking rehabilitation center for autistic patients. Not a military base... not a fight pit... just a completely non-combat area.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog2_6
        text _("Who could have done something so awful to these poor people? ...And why?") style "mytext3"
        xpos 0.2 yalign 0.064
    timer 80 action [Hide("audiolog42", transition=dis), Show("audiologs"), SetVariable("card42listened", True)]
transform audiolog3_1:
    alpha 0.0
    pause 1.5
    linear 0.5 alpha 1.0
    pause 12
    linear 1.0 alpha 0.0
transform audiolog3_2:
    alpha 0.0
    pause 14.5
    linear 0.5 alpha 1.0
    pause 9
    linear 1.0 alpha 0.0
transform audiolog3_3:
    alpha 0.0
    pause 24.5
    linear 0.5 alpha 1.0
screen audiolog43:
    frame:
        add "vinyl" at spin
        xalign 0.115 yalign 0.02
    frame:
        at audiolog3_1
        text _("Audio log 43. September 16. I’ve been doing some digging on my own. Most of the bodies at the station were completely mutilated, torn apart, and some were even... half-eaten.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog3_2
        text _("But... I managed to discover two corpses on the landing deck that stood out amongst the mangled messes. Their only wound was a large hole in the middle of the chest.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog3_3
        text _("And their ribs seemed to have been broken from something... I don’t know... springing out from within. If this is some kind of twisted reference to that old Alien movie, it’s... not funny at all.") style "mytext3"
        xpos 0.2 yalign 0.04
    timer 38 action [Hide("audiolog43", transition=dis), Show("audiologs")]
transform audiolog4_1:
    alpha 0.0
    pause 1.5
    linear 0.5 alpha 1.0
    pause 13.5
    linear 1.0 alpha 0.0
transform audiolog4_2:
    alpha 0.0
    pause 16
    linear 0.5 alpha 1.0
    pause 8.8
    linear 1.0 alpha 0.0
transform audiolog4_3:
    alpha 0.0
    pause 25.8
    linear 0.5 alpha 1.0
    pause 13.2
    linear 1.0 alpha 0.0
transform audiolog4_4:
    alpha 0.0
    pause 40
    linear 0.5 alpha 1.0
    pause 12.6
    linear 1.0 alpha 0.0
transform audiolog4_5:
    alpha 0.0
    pause 53.6
    linear 0.5 alpha 1.0
screen audiolog48:
    frame:
        add "vinyl" at spin
        xalign 0.115 yalign 0.02
    frame:
        at audiolog4_1
        text _("Audio log 48. September 29. I’ve been looking for more information ever since I responded to that AG-Centaur incident. Something... anything... that could offer some sort of explanation for that... gruesome scene.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog4_2
        text _("My first thought was to see if maybe the Alien movie could provide more context. Turns out, the creators only made it after having a dream about the concept, so... no luck there.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog4_3
        text _("My next lead was to check if Eternum had some sort of in-game tie in with the Alien franchise, as to offer an ultimate experience to... promote the series, but... no. No sort of collaboration is happening between the two at all. Scratch that lead...") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog4_4
        text _("I did, however, look into another track that seems a little more promising. Several people on various Eternum forums from around the world have... posted their accounts of being attacked by a sort of alien creature on the Andromeda server.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog4_5
        text _("And after reading all of those posts, it seems... most of the attacks also happened in non-combat areas. So the real question is... who’s doing this? And why?") style "mytext3"
        xpos 0.2 yalign 0.04
    timer 65.3 action [Hide("audiolog48", transition=dis), Show("audiologs"), SetVariable("card48listened", True)]
transform audiolog5_1:
    alpha 0.0
    pause 1
    linear 0.5 alpha 1.0
    pause 12
    linear 1.0 alpha 0.0
transform audiolog5_2:
    alpha 0.0
    pause 14
    linear 0.5 alpha 1.0
    pause 12.7
    linear 1.0 alpha 0.0
transform audiolog5_3:
    alpha 0.0
    pause 27.7
    linear 0.5 alpha 1.0
    pause 15
    linear 1.0 alpha 0.0
transform audiolog5_4:
    alpha 0.0
    pause 45
    linear 0.5 alpha 1.0
screen audiolog55:
    frame:
        add "vinyl" at spin
        xalign 0.115 yalign 0.02
    frame:
        at audiolog5_1
        text _("Audio log 55. October 20. Today I responded to another call that was just like AG-Centaur, but this time it happened on a completely different planet. A whole settlement was wiped out.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog5_2
        text _("It was a nightmarish hellscape. I’m starting to think there’s no way Ulysses could be doing this. It’s way too extreme. It’d only damage their reputation, but... where do these creatures come from, then?") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog5_3
        text _("They seem to just target a location, attack all the humans there, and then escape before help can arrive. Are these beings some sort of creation from within Eternum? Is a player orchestrating all this? Maybe a Ulysses AI going rogue and gaining sentience?") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog5_4
        text _("I’m honestly not sure what would be more terrifying...") style "mytext3"
        xpos 0.2 yalign 0.064
    timer 48.3 action [Hide("audiolog55", transition=dis), Show("audiologs")]
transform audiolog6_1:
    alpha 0.0
    pause 1.1
    linear 0.5 alpha 1.0
    pause 12.6
    linear 1.0 alpha 0.0
transform audiolog6_2:
    alpha 0.0
    pause 14.7
    linear 0.5 alpha 1.0
    pause 13.3
    linear 1.0 alpha 0.0
transform audiolog6_3:
    alpha 0.0
    pause 29
    linear 0.5 alpha 1.0
    pause 12.8
    linear 1.0 alpha 0.0
transform audiolog6_4:
    alpha 0.0
    pause 42.8
    linear 0.5 alpha 1.0
    pause 5.5
    linear 1.0 alpha 0.0
transform audiolog6_5:
    alpha 0.0
    pause 49.3
    linear 0.5 alpha 1.0
    pause 8.2
    linear 1.0 alpha 0.0
transform audiolog6_6:
    alpha 0.0
    pause 58.5
    linear 0.5 alpha 1.0
screen audiolog67:
    frame:
        add "vinyl" at spin
        xalign 0.115 yalign 0.02
    frame:
        at audiolog6_1
        text _("Audio log 67. December 1. I met a survivor today. Well... I’m not sure I could even call her that. She was a woman, on the Nox 7 planet.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog6_2
        text _("Claimed her and a friend found some strange eggs in a cave and then two facehuggers suddenly attacked them. She mentioned the friend that was with her had already logged off and was going to say something else, but... then it overcame her.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog6_3
        text _("I looked her in the eyes and saw how her soul slowly faded away... and was instead replaced with a dark, lifeless void. I could see that thing moving inside her chest. I...") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog6_4
        text _("I killed her. I had to. I couldn’t let it spread to anyone else.") style "mytext3"
        xpos 0.2 yalign 0.064
    frame:
        at audiolog6_5
        text _("After I stumbled away from the body and regained my composure, I found an Astro Corp ID card on the ground. Maybe the two of them work for that company.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog6_6
        text _("I think it’s some sort of dating service that operates in an orbiting station nearby. I’ll go see if I can find her. I have to stop this madness. I need to find the origin. I can feel I’m getting close...") style "mytext3"
        xpos 0.2 yalign 0.04
    timer 72.6 action [Hide("audiolog67", transition=dis), Show("audiologs")]
transform audiolog7_1:
    alpha 0.0
    pause 4
    linear 0.5 alpha 1.0
    pause 8.5
    linear 1.0 alpha 0.0
transform audiolog7_2:
    alpha 0.0
    pause 13.5
    linear 0.5 alpha 1.0
    pause 9.4
    linear 1.0 alpha 0.0
transform audiolog7_3:
    alpha 0.0
    pause 23.9
    linear 0.5 alpha 1.0
    pause 3.1
    linear 1.0 alpha 0.0
transform audiolog7_4:
    alpha 0.0
    pause 28.1
    linear 0.5 alpha 1.0
    pause 7.6
    linear 1.0 alpha 0.0
screen audiologlast:
    frame:
        add "vinyl" at spin
        xalign 0.115 yalign 0.02
    frame:
        at audiolog7_1
        text _("I was too late. They’re here. They’re in the ship. I’ve... I’ve seen them. They’re killing everyone.") style "mytext3"
        xpos 0.2 yalign 0.064
    frame:
        at audiolog7_2
        text _("I can’t defend myself much longer... I only have one bullet left. I won’t let them take me. I’m going to take my life on my own accord while there’s still something left of it.") style "mytext3"
        xpos 0.2 yalign 0.04
    frame:
        at audiolog7_3
        text _("I curse the sick FUCK who created these abominations!") style "mytext3"
        xpos 0.2 yalign 0.064
    frame:
        at audiolog7_4
        text _("How can an AI be like this?! There’s so many of them... they’re all so unbelievably fast... agile, strong, intelligent...") style "mytext3"
        xpos 0.2 yalign 0.064
    timer 49.5 action [Hide("audiologlast", transition=dis), Jump("audiologlastpos")]

screen qtexeno():
    imagebutton:
        align (0.77, 0.36)
        idle "kill1"
        hover "kill1b"
        action Jump("xenowin")
    timer 2.8 action Jump("xenolose")
    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 2.8, 1)
screen qtebrock():
    imagebutton:
        align (0.48, 0.14)
        idle "attack1"
        hover "attack1b"
        action Jump("brockwin")
    timer 2.7 action Jump("brocklose")
    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 2.7, 1)
image but1:
    on idle:
        "talk" with Dissolve(.25)
    on hover:
        "talkb" with Dissolve(.25)
screen fancyparty:
    if fancytalk1:
        button:
            add "but1"
            xalign 0.92 yalign 0.25
            action Jump('ldupont')
    if fancytalk3:
        button:
            add "but1"
            xalign 0.023 yalign 0.48
            action Jump('lastor')
    if fancytalk2:
        button:
            add "but1"
            xalign 0.4 yalign 0.4
            action Jump('lmos')
    imagebutton:
        idle "leavebutton"
        hover "leavebuttonb"
        xalign 0.0
        yalign 1.0
        action Jump('lleavef')

############################################################ 0.5
transform amulett:
    alpha 0.0
    pause 1.6
    linear 1.5 alpha 1.0
    pause 0.5
    linear 1.5 alpha 0.0
transform amulett2:
    alpha 0.0
    pause 0.5
    linear 1.5 alpha 1.0
    pause 0.5
    linear 1.5 alpha 0.0
screen polyjuiceb:
    frame:
        text _("A bottle of Polyjuice potion was added to your inventory.") at amulett
        xalign 0.9 yalign 0.1
screen amulet:
    frame:
        text _("The Amulet of Blair was added to your inventory.") at amulett
        xalign 0.9 yalign 0.1
screen dopplemorpher:
    frame:
        text _("The Dopplemorpher was added to your inventory.") at amulett2
        xalign 0.9 yalign 0.1
screen scopenova:
    frame:
        add "scope"
screen manga1:
    add "manga1" zoom 0.252 xalign 0.5 yalign 0.5
    imagebutton:
        idle "nextpage"
        hover "nextpageb"
        xalign 0.97
        yalign 0.5
        action Jump("mangapage2")
screen manga2:
    if novacomicnoturgent:
        add "manga2not" zoom 0.252 xalign 0.5 yalign 0.5
    elif mcsayingafterkill == 1:
        add "manga2a" zoom 0.252 xalign 0.5 yalign 0.5
    elif mcsayingafterkill == 2:
        add "manga2b" zoom 0.252 xalign 0.5 yalign 0.5
    else:
        add "manga2c" zoom 0.252 xalign 0.5 yalign 0.5
    imagebutton:
        idle "previouspage"
        hover "previouspageb"
        xalign 0.05
        yalign 0.5
        action Jump("mangapage1")
    imagebutton:
        idle "exit"
        hover "exitb"
        xalign 0.97
        yalign 0.5
        action Jump("mangapageexit")
image but3:
    on idle:
        "talk2" with Dissolve(.15)
    on hover:
        "talkb" with Dissolve(.15)
image but4:
    on idle:
        "talk2" with Dissolve(.15)
    on hover:
        "waitb" with Dissolve(.15)
screen collegeparty1:
    if ppp1:
        button:
            add "but3"
            xalign 0.42 yalign 0.56
            action Jump('judithparty')
    if ppp10:
        button:
            add "but3"
            xalign 0.84 yalign 0.61
            action Jump('pennydormscene')
    imagebutton:
        idle "ccp1"
        hover "ccp1b"
        xalign 0.0
        yalign 0.0
        action Jump('collegeparty2')
    imagebutton:
        idle "ccp2"
        hover "ccp2b"
        xalign 0.99
        yalign 0.024
        action Jump('collegeparty4')
    imagebutton:
        idle "ccpexit"
        hover "ccpexitb"
        xalign 0.0
        yalign 1.0
        action Jump('collegepartyexit')
screen collegeparty2:
    imagebutton:
        idle "ccp1"
        hover "ccp1b"
        xalign 0.0
        yalign 0.0
        action Jump('collegeparty3')
    imagebutton:
        idle "ccp2"
        hover "ccp2b"
        xalign 0.99
        yalign 0.024
        action Jump('collegeparty1')
screen collegeparty3:
    if not ppp10:
        if ppp2 or ppp3 or ppp7:
            button:
                add "but3"
                xalign 0.65 yalign 0.3
                action Jump('novagameparty')
    imagebutton:
        idle "ccp3"
        hover "ccp3b"
        xalign 0.65
        yalign 1.0
        action Jump('collegeparty2')
screen collegeparty3b:
    imagebutton:
        idle "ccp3"
        hover "ccp3b"
        xalign 0.65
        yalign 1.0
        action Jump('collegeparty2')
screen collegeparty4:
    imagebutton:
        idle "ccp4"
        hover "ccp4b"
        xalign 0.22
        yalign 1.0
        action Jump('collegeparty1')
    imagebutton:
        idle "ccp5"
        hover "ccp5b"
        xalign 0.81
        yalign 1.0
        action Jump('collegeparty6')
    imagebutton:
        idle "ccp6"
        hover "ccp6b"
        xalign 0.23
        yalign 0.55
        action Jump('collegeparty5')
screen collegeparty5:
    if ppp6 and not ppp4 and not ppp10:
        button:
            add "but3"
            xalign 0.5 yalign 0.35
            action Jump('collegepartydressingroom')
    elif ppp10 and not pennyreginahate:
        button:
            add "but3"
            xalign 0.5 yalign 0.35
            action Jump('reginalockerfail')
    imagebutton:
        idle "ccp7"
        hover "ccp7b"
        xalign 0.05
        yalign 1.0
        action Jump('collegeparty4')
screen collegeparty6:
    if ppp9:
        button:
            add "but4"
            xalign 0.4 yalign 0.2
            action Jump('precollegepartypenny1')
    imagebutton:
        idle "ccp8"
        hover "ccp8b"
        xalign 0.835
        yalign 1.02
        action Jump('collegeparty4')



#################################################################### 0.6

init python:
    class combination_lock_class:
        def __init__(self, number):
            self.number = number
            self.digits = []
            for i in str(number):
                self.digits.append([0, int(i)])
            self.is_locked = True
            self.x = 0
        def change(self, index, amount):
            self.digits[index][0] += amount
            if self.digits[index][0] > 9:
                self.digits[index][0] = 0
            elif self.digits[index][0] < 0:
                self.digits[index][0] = 9
        def check(self):
            for i in self.digits:
                if not i[0] == i[1]:
                    renpy.play("images/combination lock/locked.ogg", "sound")
                    self.x = 10
                    break
                    
            else:
                self.is_locked = False
                self.x = 100
                renpy.play("images/combination lock/unlock.ogg", "sound")
                Show("combination_lock_open")()
        def ret(self):
            self.x = 0
screen combination_lock(n):
    modal True
    default g = combination_lock_class(n)
    add "combination lock/body.png" align .5,.5
    hbox:
        align .5,.5
        for n,i in enumerate(g.digits):
            fixed:
                fit_first True
                add "combination lock/{}.png".format(i[0])
                button:
                    background None yoffset 55
                    action Function(g.change, n, 1)
                    activate_sound "images/combination lock/rotate_down.ogg"
                button:
                    background None yoffset -55
                    action Function(g.change, n, -1)
                    activate_sound "images/combination lock/rotate_up.ogg"
        button:
            yoffset -2
            at combination_lock_trans(g.x)
            align .5,.5
            add "combination lock/button.png"
            action Function(g.check)
    textbutton _("RETURN"):
        action Jump('crime5room')
        xalign 0.96 yalign 0.05

    if g.is_locked and g.x:
        timer .1 repeat True action Function(g.ret)
screen combination_lock_open():
    timer 1 action Hide("combination_lock_open"), Return()
transform combination_lock_trans(x):
    ease .2 xoffset x
image bg leather = "combination lock/bg.webp"



screen textround:
    text "ROUND [eround]" xalign 0.96 yalign 0.05 style "mytext2" size 70


screen crimemap0:
    modal True
    imagemap:
        ground "ec 0"
        idle "ec 0id1"
        hover "ec 0ho1"
        hotspot (0, 158, 390, 203) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime1') ] 
        hotspot (940, 181, 326, 196) action [ Play("soundlow", "audio/sfx/dooropenclose.mp3"), Jump('crime2') ] 
        hotspot (825, 829, 476, 247) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime4') ] 
        hotspot (739, 484, 213, 163) action Jump('crime0clonk')
        if crimekey2:
            hotspot (1462, 298, 391, 176) action Jump('crime0key')
    text _("ROUND [eround]") xalign 0.96 yalign 0.05 style "mytext2" size 70


screen crimemap1:
    modal True
    if eround == 1:
        imagemap:
            ground "ec 1b"
            idle "ec 1id1"
            hover "ec 1ho1"
            hotspot (279, 888, 443, 188) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime0') ] 
            hotspot (467, 524, 283, 155) action Jump('crime1piaget')
            hotspot (1481, 474, 269, 159) action Jump('crime1baek')
    elif (lastpostit and not lastpa and not eround == 4) or not annaalive:
        imagemap:
            ground "ec 1"
            idle "ec 1id2"
            hover "ec 1ho2"
            hotspot (279, 888, 443, 188) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime0') ] 
    elif eround >= 2 and annaalive:
        imagemap:
            ground "ec 1c"
            idle "ec 1id2"
            hover "ec 1ho2"
            hotspot (279, 888, 443, 188) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime0') ] 
            hotspot (467, 524, 283, 155) action Jump('crime1piaget')
    text _("ROUND [eround]") xalign 0.96 yalign 0.05 style "mytext2" size 70


screen crimemap4:
    modal True
    if eround == 1:
        imagemap:
            ground "ec 4id1"
            idle "ec 4id1"
            hover "ec 4ho1"
            hotspot (1516, 783, 401, 295) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime0') ] 
            hotspot (518, 501, 259, 142) action Jump('crime4elliot')
    elif eround >= 2 and baekalive:
        imagemap:
            ground "ec 4c"
            idle "ec 4id2"
            hover "ec 4ho2"
            hotspot (1516, 783, 401, 295) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime0') ] 
            hotspot (484, 421, 355, 264) action Jump('crime4baek')
    else:
        imagemap:
            ground "ec 4"
            idle "ec 4id2"
            hover "ec 4ho2"
            hotspot (1516, 783, 401, 295) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime0') ] 
    text _("ROUND [eround]") xalign 0.96 yalign 0.05 style "mytext2" size 70


screen crimemap2:
    modal True
    if eround >= 3 and not geminialive:
        imagemap:
            ground "ec 2"
            idle "ec 2id1"
            hover "ec 2ho1"
            hotspot (263, 643, 411, 218) action [ Play("soundlow", "audio/sfx/dooropenclose.mp3"), Jump('crime5') ] 
            hotspot (1347, 587, 481, 259) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime3') ] 
            hotspot (894, 848, 232, 228) action [ Play("soundlow", "audio/sfx/dooropenclose.mp3"), Jump('crime0') ] 
    else:
        imagemap:
            ground "ec 2b"
            idle "ec 2id1"
            hover "ec 2ho1"
            hotspot (263, 643, 411, 218) action [ Play("soundlow", "audio/sfx/dooropenclose.mp3"), Jump('crime5') ] 
            hotspot (1347, 587, 481, 259) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime3') ] 
            hotspot (894, 848, 232, 228) action [ Play("soundlow", "audio/sfx/dooropenclose.mp3"), Jump('crime0') ] 
            hotspot (804, 402, 282, 187) action Jump('crime2gemini')
    text _("ROUND [eround]") xalign 0.96 yalign 0.05 style "mytext2" size 70


screen crimemap3:
    modal True
    if eround == 1:
        imagemap:
            ground "ec 3b"
            idle "ec 3id1"
            hover "ec 3ho1"
            hotspot (965, 834, 242, 242) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime2') ] 
            hotspot (1073, 392, 287, 169) action Jump('crime3harley')
    elif eround >=2 and harleyalive:
        imagemap:
            ground "ec 3c"
            idle "ec 3id2"
            hover "ec 3ho2"
            hotspot (965, 834, 242, 242) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime2') ] 
            hotspot (618, 545, 345, 238) action Jump('crime3harley')
    else:
        imagemap:
            ground "ec 3"
            idle "ec 3id2"
            hover "ec 3ho2"
            hotspot (965, 834, 242, 242) action [ Play("sound", "audio/sfx/footsteps.mp3"), Jump('crime2') ] 
    text _("ROUND [eround]") xalign 0.96 yalign 0.05 style "mytext2" size 70


screen crimemap5:
    modal True
    imagemap:
        ground "ec 5"
        idle "ec 5id1"
        hover "ec 5ho1"
        hotspot (871, 842, 221, 234) action [ Play("soundlow", "audio/sfx/dooropenclose.mp3"), Jump('crime2') ] 
        hotspot (954, 363, 241, 150) action Jump('crime5room')
    text _("ROUND [eround]") xalign 0.96 yalign 0.05 style "mytext2" size 70

screen crimemap6:
    modal True
    imagemap:
        ground "ec 55"
        idle "ec 55id1"
        hover "ec 55ho1"
        hotspot (878, 800, 352, 279) action [ Play("soundlow", "audio/sfx/dooropenclose.mp3"), Jump('crime5') ] 
        if not lastpostit:
            hotspot (390, 614, 424, 228) action Jump('crimebriefcase')
    text _("ROUND [eround]") xalign 0.96 yalign 0.05 style "mytext2" size 70


screen tale1:
    text "There was upon a time when" xalign 0.6 yalign 0.8 style "mytexttale" size 65

screen westernmenu:
    if westernalex and westerncalypso:
        add "westmapblackridge1"
    elif westerncalypso:
        add "westmapblackridge2"
    else:
        add "westmapblackridge3"
    if westernalex:
        imagebutton:
            idle "westmapalex1"
            hover "westmapalex2"
            xalign 0.38 yalign 0.45
            action Jump('alexwestern')
    if westerndalia:
        imagebutton:
            idle "westmapdalia1"
            hover "westmapdalia2"
            xalign 0.8 yalign 0.2
            action Jump('daliawestern')
    if westerndalia2:
        imagebutton:
            idle "westmapdalia1"
            hover "westmapdalia2"
            xalign 0.75 yalign 0.6
            action Jump('dalia2western')
    if westerncalypso:
        imagebutton:
            idle "westmapcalypso1"
            hover "westmapcalypso2"
            xalign 0.55 yalign 0.25
            action Jump('calypsowestern')

screen novanancyangle1:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if nna1:
            action SetVariable("nna1", False)
        else:
            action SetVariable("nna1", True)
screen novanancyangle2:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if nna2:
            action SetVariable("nna2", False)
        else:
            action SetVariable("nna2", True)
screen novaangle1:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if ns4b:
            action SetVariable("ns4b", False)
        else:
            action SetVariable("ns4b", True)
screen novaangle2:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if ns4c:
            action SetVariable("ns4c", False)
        else:
            action SetVariable("ns4c", True)

screen novaangle3:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if ns5c:
            action SetVariable("ns5c", False)
        else:
            action SetVariable("ns5c", True)

screen ekabarlunapennychoice:
    modal True
    add "ff 85"
    imagemap:
        ground "ekabaridle"
        idle "ekabaridle"
        hover "ekabarhover"
        hotspot (150, 79, 474, 898) action Jump('werewolfhelpm') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        hotspot (1329, 63, 487, 920) action Jump('vampirehelpm') hovered [ Play ("sound", "audio/sfx/uis.mp3")]

############################################################################################################################## 0.8

screen annieangle:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if annieanglev:
            action SetVariable("annieanglev", False)
        else:
            action SetVariable("annieanglev", True)

screen millionairescreen:
    modal True
    add "mcshakemillion"
    add "countdown" 
    imagemap:
        ground "millionq"
        idle "millionq"
        hover "millionq2"
        hotspot (207, 713, 749, 117) action [SetVariable('millionqeyes', True), Jump('millioncontinue') ] 
        hotspot (972, 712, 758, 124) action [SetVariable('millionqbutt', True), Jump('millioncontinue') ] 
        hotspot (211, 859, 745, 116) action [SetVariable('millionqpersonality', True), Jump('millioncontinue') ] 
        hotspot (970, 856, 760, 119) action [SetVariable('millionqyes', True), Jump('millioncontinue') ] 
    timer 30.0 action Jump("millioncontinue")
screen countdown(delay=10.0):
    default counter = delay
    if counter <= 0.0:
        text _("0.0{#seconds-left}") style "mytextcountdown" align (0.5, 0.5)
    else:
        text _("[counter:.1f]{#seconds-left}") style "mytextcountdown" align (0.5, 0.5)
    timer 0.1:
        repeat True
        action If(counter > 0, true=SetScreenVariable("counter", counter - 0.1), false=Hide("countdown") )

screen arabiamarket:
    modal True
    add "gcc 32"
    imagemap:
        ground "gcc 32"
        idle "gcc 32idle"
        hover "gcc 32hover"
        if amarket1:
            hotspot (413, 382, 236, 244) action Jump('arabiamarket1') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        if amarket2:
            hotspot (698, 399, 275, 234) action Jump('arabiamarket2') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        if amarket3:
            hotspot (975, 381, 248, 228) action Jump('arabiamarket3') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        if amarket4:
            hotspot (1625, 360, 265, 238) action Jump('arabiamarket4') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        text _("The Citadël - 03:[citadeltime] PM") xalign 0.05 yalign 0.03  style "mytextarabia"
screen piratecrew:
    modal True
    add "gg 6"
    imagemap:
        ground "crewidle"
        idle "crewidle"
        hover "crewhover"
        hotspot (83, 58, 595, 779) action Jump('piratecrewreddss') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        hotspot (684, 57, 552, 807) action Jump('piratecrewlorrdy') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        hotspot (1247, 58, 571, 781) action Jump('piratecrewscarlet') hovered [ Play ("sound", "audio/sfx/uis.mp3")]

screen mousemovemermaid:
    timer 0.2 repeat True action Function(mouse_mov)
screen mousemovebutts:
    timer 0.2 repeat True action Function(mouse_mov2)

screen email1:
    text _("Hello team!\n \nJust a quick note to let everyone know that there’s sushi in the meeting lounge on the 5th \nfloor to celebrate Sarah’s birthday!\nCome by and enjoy some delicious sushi and wish Sarah a happy birthday!\n \nBest, Ben") xalign 0.5 yalign 0.45 style "mytextoutline" size 40
screen email2:
    text _("[mc], \n \nCome to the reception desk whenever you finish jerking off or whatever you do up there. \nAnd do it before my turn is over, thanks.\n \nIt's urgent.\n \nCharlotte") xalign 0.5 yalign 0.45 style "mytextoutline" size 40
screen email3:
    text _("Dear Mr. [lastname],\n \nWe need to address an urgent matter regarding your sales performance.\n \nIt has been 10 years since Eternum's closure caused the traditional video game market to \nskyrocket, and yet, our sales numbers are still not meeting expectations.\nIt is crucial that you improve your numbers immediately. We need to capitalize on this \nongoing market growth. Failure to do so will unfortunately lead to difficult decisions.\nPlease prioritize this and take the necessary steps to enhance your sales performance.\n \nBest, \nStanley Whitmore\n \nP.S. There have been complaints regarding your body odor on the 4th floor.\nPlease take any necessary steps to address this issue immediately.") xalign 0.5 yalign 0.45 style "mytextoutline" size 40
screen email4:
    text _("COME TO THE 7TH FLOOR.\n \nDON'T LISTEN TO HIM.") xalign 0.5 yalign 0.45 style "mytextoutline" size 40


############################################################################## 0.8

screen daliaangleride1:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if dar1:
            action SetVariable("dar1", False)
        else:
            action SetVariable("dar1", True)
screen daliaangleride2:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if dar2:
            action SetVariable("dar2", False)
        else:
            action SetVariable("dar2", True)

############################################################################### 0.9

define trial1 = [ 
    {'label': _('Whatever'), 'scene': 'trial1a'},
    {'label': _('I understand'), 'scene': 'trial1b'},
    {'label': _('Fuck you'), 'scene': 'trial1c'},
]
define trial2 = [ 
    {'label': _('I want a lawyer'), 'scene': 'trial2a'},
    {'label': _('Trial by combat'), 'scene': 'trial2b'},
    {'label': _('Ask for an introduction'), 'scene': 'trial2c'},
]
define trial3 = [ 
    {'label': _('I am her owner'), 'scene': 'trial3a'},
    {'label': _('We’re friends'), 'scene': 'trial3b'},
    {'label': _('I am her servant'), 'scene': 'trial3c'},
]
define trial4 = [ 
    {'label': _('Tell the truth'), 'scene': 'trial4a'},
    {'label': _('Lie'), 'scene': 'trial4b'},
]
define trial5 = [ 
    {'label': _('She saved me'), 'scene': 'trial5a'},
    {'label': _('We were attacked'), 'scene': 'trial5b'},
    {'label': _('I don’t know'), 'scene': 'trial5c'},
]
define trial6 = [ 
    {'label': _('I was useful to her'), 'scene': 'trial6a'},
    {'label': _('She owed me'), 'scene': 'trial6b'},
    {'label': _('We became lovers'), 'scene': 'trial6c'},
]
define trial7 = [ 
    {'label': _('Anima the Radiant'), 'scene': 'trial7a'},
    {'label': _('Anala the Resplendent'), 'scene': 'trial7b'},
    {'label': _('Anira the Shining'), 'scene': 'trial7c'},
]
define trial8 = [ 
    {'label': _('Draxus'), 'scene': 'trial8a'},
    {'label': _('Zephyros'), 'scene': 'trial8b'},
    {'label': _('Yliar'), 'scene': 'trial8c'},
]
define trial9 = [ 
    {'label': _('Raewyn'), 'scene': 'trial9a'},
    {'label': _('Sylvannus'), 'scene': 'trial9b'},
    {'label': _('Galnar'), 'scene': 'trial9c'},
]
define trial10 = [ 
    {'label': _('44'), 'scene': 'trial10b'},
    {'label': _('68'), 'scene': 'trial10c'},
    {'label': _('84'), 'scene': 'trial10d'},
]
define trial11 = [ 
    {'label': _('Elarisil'), 'scene': 'trial11b'},
    {'label': _('Lalariel'), 'scene': 'trial11c'},
    {'label': _('Tomodin'), 'scene': 'trial11d'},
]
define trial12 = [ 
    {'label': _('Accept'), 'scene': 'trial12a'},
    {'label': _('Refuse'), 'scene': 'trial12b'},
]
define trial13 = [ 
    {'label': _('I am innocent'), 'scene': 'trial13a'},
    {'label': _('I want to call a witness'), 'scene': 'trial13b'},
    {'label': _('You will regret this'), 'scene': 'trial13c'},
]
define trial14 = [ 
    {'label': _('Arannis'), 'scene': 'trial14a'},
    {'label': _('Lorelei'), 'scene': 'trial14b'},
]

style trial_choice_text:
    size 40
    font "balgruf.ttf"
    outlines [ (1, "#000000") ]

screen neo_choice(set):
    layer 'transient'
    modal True
    add "scales" at transformscales
    vbox:
        spacing 35
        align (1.0, 1.0)    #
        offset (50, -480) # adjust the position to your liking
        for x, y in enumerate(set):
            frame:
                xysize (600, 68) # adjust these size values to your liking
                align  (.5 , .5)
                button:
                    xysize (600, 68) # adjust these size values to your liking
                    align  (.5 , .5)
                    action Jump(y['scene'])
                    hover_sound '/sfx/09/gearshort2.mp3'
                    activate_sound '/sfx/09/gearimpact2.mp3' 
                    frame:
                        align (.5, .5)
                        # image 'path/to/your/bg/image'
                        text y['label'] style "trial_choice_text" align (.5, .5)
                        at transform:
                            perspective True
                            subpixel True
                            align (.5, .5)
                            matrixtransform RotateMatrix(160, 0, -160) # tweak these values to your liking
                            pause x*.1
                            easein_quint 1.7 matrixtransform RotateMatrix(0, 0, 0)
                    at transform:
                        subpixel True
                        align    (.5, .5)
                        xycenter (.5, .5)
                        on hover:
                            easein_quint .5 zoom 1.05 offset (0, -10)
                        on idle:
                            easein_quint .5 zoom 1.0 offset (0, 0)
                at transform:
                    subpixel True
                    offset (200, -50)
                    alpha  .0
                    zoom   .0
                    pause x*.1
                    easein_quint 1.5 offset (0, 0) alpha 1.0 zoom 1.0
transform transformscales:
    perspective True
    subpixel True
    alpha  .0
    zoom   .0
    matrixtransform RotateMatrix(160, 0, -160)
    pause 0.1
    easein_quint 1.5 alpha 1.0 zoom 1.0 matrixtransform RotateMatrix(0, 0, 0)

screen qtearannis1():
    modal True
    imagebutton:
        align (0.86, 0.18)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    imagebutton:
        align (0.86, 0.83)
        idle "parry1"
        hover "parry1b"
        action Jump("larannis2")
    imagebutton:
        align (0.13, 0.13)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    imagebutton:
        align (0.14, 0.79)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    timer 1.7 action [SetVariable("arannisslow", True), Jump("larannisfail")]
    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 1.7, 1)
screen qtearannis2():
    modal True
    imagebutton:
        align (0.86, 0.18)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    imagebutton:
        align (0.86, 0.83)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    imagebutton:
        align (0.13, 0.13)
        idle "parry1"
        hover "parry1b"
        action Jump("larannis3")
    imagebutton:
        align (0.14, 0.79)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    timer 1.5 action [SetVariable("arannisslow", True), Jump("larannisfail")]
    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 1.5, 1)
screen qtearannis3():
    modal True
    imagebutton:
        align (0.86, 0.18)
        idle "parry1"
        hover "parry1b"
        action Jump("larannis4")
    imagebutton:
        align (0.86, 0.83)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    imagebutton:
        align (0.13, 0.13)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    imagebutton:
        align (0.14, 0.79)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    timer 1.7 action [SetVariable("arannisslow", True), Jump("larannisfail")]
    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 1.7, 1)
screen qtearannis4():
    modal True
    imagebutton:
        align (0.86, 0.18)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    imagebutton:
        align (0.86, 0.83)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    imagebutton:
        align (0.13, 0.13)
        idle "parry1"
        hover "parry1b"
        action Jump("larannis5")
    imagebutton:
        align (0.14, 0.79)
        idle "parry1"
        hover "parry1b"
        action Jump("larannisfail")
    timer 1.7 action [SetVariable("arannisslow", True), Jump("larannisfail")]
    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 1.7, 1)
screen qtearannis5():
    modal True
    imagebutton:
        align (0.55, 0.38)
        idle "counter1"
        hover "counter1b"
        action Jump("laranniswin")
    timer 3.8 action [SetVariable("arannisslow", True), Jump("larannisfail")]
    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 3.8, 1)

transform transformpoem:
    perspective True
    subpixel True
    align (.5, .5)
    alpha -0.5
    zoom 0.0
    matrixtransform RotateMatrix(600, 200, -160)
    easein_quint 2.5 alpha 1.0 zoom 1.0 matrixtransform RotateMatrix(0, 0, 0)
screen poem2a:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("A silver leaf drifts through the air,") style "mytextelven" xalign 0.87 yalign 0.18
screen poem2b:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("The stars bow low to brush her hair.") style "mytextelven" xalign 0.87 yalign 0.28
screen poem2c:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("She walks where ancient rivers sleep,") style "mytextelven" xalign 0.87 yalign 0.38
screen poem2d:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("And even night forgets to weep.") style "mytextelven" xalign 0.87 yalign 0.48

screen poem1a:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("She climbed me like a silver vine,") style "mytextelven" xalign 0.87 yalign 0.18
screen poem1b:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Each gasp a verse, each thrust a line.") style "mytextelven" xalign 0.87 yalign 0.28
screen poem1c:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("In Hyril’ar, the stars descend,") style "mytextelven" xalign 0.87 yalign 0.38
screen poem1d:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("To watch where moans and magic blend.") style "mytextelven" xalign 0.87 yalign 0.48

screen poem3a:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Humans charge with blades held wrong,") style "mytextelven" xalign 0.87 yalign 0.18
screen poem3b:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("We chop them down before their song.") style "mytextelven" xalign 0.87 yalign 0.28
screen poem3c:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Their skulls make cups, their bones burn bright,") style "mytextelven" xalign 0.87 yalign 0.38
screen poem3d:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Their children squeal—what pure delight!") style "mytextelven" xalign 0.87 yalign 0.48

screen poem4a:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("I brought her flowers. She brought light.") style "mytextelven" xalign 0.87 yalign 0.18
screen poem4b1:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Tralalero tralala.") style "mytextelven" xalign 0.87 yalign 0.28 
screen poem4b2:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("My hands shook hard, her eyes were bright.") style "mytextelven" xalign 0.87 yalign 0.28
screen poem4b3:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("I tried to flirt, she barked “Alright.”") style "mytextelven" xalign 0.87 yalign 0.28
screen poem4b4:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Her teeth are bright like white moon night.") style "mytextelven" xalign 0.87 yalign 0.28
screen poem4c:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Calypso smiled, and that was all,") style "mytextelven" xalign 0.87 yalign 0.38
screen poem4d1:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("O porcodioe o porcuala.") style "mytextelven" xalign 0.87 yalign 0.48 
screen poem4d2:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("But I am dust, and she is grace.") style "mytextelven" xalign 0.87 yalign 0.48
screen poem4d3:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Let's go watch Better Call Saul.") style "mytextelven" xalign 0.87 yalign 0.48
screen poem4d4:
    fixed:
        xalign 0.8
        yalign 0.5
        at transformpoem
        text _("Enough to make a soldier fall.") style "mytextelven" xalign 0.87 yalign 0.48


default ball_rotation = 0 # Current rotation of the ball in degrees
default score = 0 # Current score
default is_clockwise = True # True if currently rotating clockwise

define circle_radius = 350 # Radius of the circle 
define ball_radius = 11 # Radius of the ball

transform ball_rotate(rotation):
    subpixel True
    anchor (0.5, 0.5)
    around (circle_radius, circle_radius) # Radius of the circle
    radius circle_radius - ball_radius - 2 # <Radius of the circle> - <Radius of the ball> - <Circle stroke * 2 (if any)>
    angle rotation + initial_rotation
init 1 python:
    correct_degree = 10 # Degree of correct zone (will be calculated +-)
    ball_speed = 3.1 
    ball_speed2 = 6
    initial_rotation = -90 # Initial rotation (-90 for C)
    def calculate_score(rotation):
        # If clicked in a correct zone - give a point
        if rotation >= -correct_degree and rotation <= correct_degree:
            store.score += 1
        else: # Subtract from score if missed, remove if not needed
            store.score -= 1
    def calculate_rotation():
        rotation = store.ball_rotation
        # Increase the angle if clockwise
        if store.is_clockwise:
            if rotation < 90:
                if ballbowspeed:
                    rotation += ball_speed
                else:
                    rotation += ball_speed2
            else:
                store.is_clockwise = False
        # Decrease the angle if counter-clockwise
        else:
            if rotation > -90:
                if ballbowspeed:
                    rotation -= ball_speed
                else:
                    rotation -= ball_speed2
            else:
                store.is_clockwise = True
        # Clamp rotation
        if rotation > 90:
            rotation = 90
        elif rotation < -90:
            rotation = -90
        store.ball_rotation = rotation
screen ball_minigame():
    use ball_timer
    fixed:
        xalign 0.21 yalign 0.5
        xsize circle_radius # Radius of the circle
        ysize circle_radius * 2 # Radius * 2 (not necessary)
        add "images/MENUS/ball_bar.png" # Circle with zones
        add "images/MENUS/only_ball.png" at ball_rotate(ball_rotation) # The ball 
        key "K_SPACE": 
            action [
                Function(calculate_score, ball_rotation),
                Jump("ball_continue")
            ]
            capture True
        key "mouseup_1": 
            action [
                Function(calculate_score, ball_rotation),
                Jump("ball_continue")
            ]
            capture True
screen ball_timer:
    if ballbowspeed:
        timer 0.01 repeat True action Function(calculate_rotation)
    else:
        timer 0.003 repeat True action Function(calculate_rotation)

screen lyreharpscreen:
    modal True
    add lyrebg
    imagemap:
        ground "lyreharp"
        idle "lyreharp"
        hover "lyreharp2"
        $ g4actions = [ SetVariable("lyrebg", "qs 69a"), Play("sound", "sfx/09/Lyre_G4.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "g") ]
        $ a4actions = [ SetVariable ("lyrebg", "qs 69b2"), Play("sound2", "sfx/09/Lyre_A4.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "a") ]
        $ b4actions = [ SetVariable ("lyrebg", "qs 69c"), Play("sound3", "sfx/09/Lyre_B4.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "b") ]
        $ c5actions = [ SetVariable ("lyrebg", "qs 69d"), Play("sound4", "sfx/09/Lyre_C5.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "c") ]
        $ d5actions = [ SetVariable ("lyrebg", "qs 69e"), Play("sound5", "sfx/09/Lyre_D5.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "d") ]
        $ e5actions = [ SetVariable ("lyrebg", "qs 69f"), Play("sound5", "sfx/09/Lyre_E5.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "e") ]
        $ f5actions = [ SetVariable ("lyrebg", "qs 69g"), Play("sound7", "sfx/09/Lyre_F5.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "f") ]
        $ g5actions = [ SetVariable ("lyrebg", "qs 69a2"), Play("sound8", "sfx/09/Lyre_G5.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "g'") ]
        $ a5actions = [ SetVariable ("lyrebg", "qs 69b"), Play("sound9", "sfx/09/Lyre_A5.ogg"), SetVariable("lyrenotesplayed", lyrenotesplayed + 1), SetVariable("lyresequence", lyresequence + "a'") ]  
        hotspot (188, 64, 262, 215) action g4actions
        hotspot (153, 284, 308, 199) action a4actions
        hotspot (197, 494, 295, 168) action b4actions
        hotspot (326, 665, 247, 166) action c5actions
        hotspot (572, 777, 205, 216) action d5actions
        hotspot (786, 841, 233, 214) action e5actions
        hotspot (1008, 824, 226, 220) action f5actions
        hotspot (1221, 755, 209, 173) action g5actions
        hotspot (1422, 613, 193, 173) action a5actions
        hotspot (1295, 112, 444, 276) action [ Jump ("lyreend") ] 
        key "K_q" action g4actions capture True
        key "K_w" action a4actions capture True
        key "K_e" action b4actions capture True
        key "K_r" action c5actions capture True
        key "K_t" action d5actions capture True
        key "K_y" action e5actions capture True
        key "K_u" action f5actions capture True
        key "K_i" action g5actions capture True
        key "K_o" action a5actions capture True
screen lyreharpscreenexit:
    add lyrebg

screen qteguardhyrilar():
    modal True
    imagebutton:
        align (0.65, 0.53)
        idle "counter1"
        hover "counter1b"
        action Jump("guardwin09")
    timer 2.5 action Jump("guardlose09")
    bar:
        align (0.5, 0.95)
        xysize (500, 3)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 2.5, 1)

style changermeister_score_text:
    font 'Sketchzone.ttf'

screen _ep9_plyr(name, icon, colour, points, kind='side'):
    frame:
        if kind == 'main':
            xysize (384, 128)
            image 'MENUS/mc_bg.png' align (.0, .5) offset (58, 0)
        elif kind == 'side':
            xysize (328, 96)
            image 'MENUS/point_bg.png' align (.0, .5) offset (42, 0)
        offset (0, -6)
        if icon is None:
            $ icon = Solid(colour)
        hbox:
            align  (.0, .5)
            offset (-6,  0)
            spacing 24
            frame:
                if kind == 'main':
                    xysize (128, 128)
                    background AlphaMask(icon, 'MENUS/mc_mask.png')
                elif kind == 'side':
                    xysize (96, 96)
                    background AlphaMask(icon, 'MENUS/point_mask.png')
            style_prefix 'et'
            vbox:
                if kind == 'main':
                    spacing 34
                elif kind == 'side':
                    spacing 30
                align (.5, .5)
                text name align (.0, .5) color colour style "changermeister_score_text":
                    if kind == 'main':
                        size 35
                    elif kind == 'side':
                        size 27
                text str(points) align (.0, .5) style "changermeister_score_text":
                    if kind == 'main':
                        size 36
                    elif kind == 'side':
                        size 28

screen ep9_pts_overlay():
    $ maximized = 0
    vbox:
        align  (.0, .0)
        offset (50, 200)
        spacing 12
        at transform:
            zoom .75
        use _ep9_plyr(_('[mc]')    , "images/MENUS/mc_mask.png", '#00cc99', mcpointscm, 'main')
        use _ep9_plyr(_('Nancy')    , "images/MENUS/point_mask.png", '#CC0066', nancypointscm)
        use _ep9_plyr(_('Penelope'), "images/MENUS/penelope_mask.png", '#1FCB4A', penelopepointscm)
        use _ep9_plyr(_('Dalia')    , "images/MENUS/dalia_mask.png", '#FF6600', daliapointscm)
        use _ep9_plyr(_('Alex')   , "images/MENUS/alex_mask.png", '#9933FF', alexpointscm)
    text "Round [cmround]" xalign 0.94 yalign 0.06 size 90 style "mytext3" at half_transparent
transform half_transparent:
    alpha 0.8
screen s09plans1:
    add "09plans 1" at shortdissolve
screen s09plans2:
    add "09plans 2" at shortdissolve
screen s09plans3:
    add "09plans 3" at shortdissolve
screen s09plans4:
    add "09plans 4" at shortdissolve
screen s09plans5:
    add "09plans 5" at shortdissolve
screen s09plans6:
    add "09plans 6" at shortdissolve
screen s09plans7:
    add "09plans 7" at shortdissolve
screen s09plans8:
    add "09plans 8" at shortdissolve

transform shortdissolve:
        xalign 0.5 yalign 0.5
        alpha 0.0 zoom 0.9
        linear 0.1 alpha 1.0 zoom 1.1
        linear 0.1 zoom 1

screen card_selection(cards):
    layer 'transient'
    hbox:
        spacing 24
        align (.545, .45)
        for x, y in enumerate(cards):
            if x < 1:
                $ j = 240
            else:
                $ j = -240
            button:
                xysize (480, 720)
                align  (.605 ,  .45)
                if y['card_img']: # image must be 480x720
                    image y['card_img'] align (.5, .5):
                        at transform:
                            perspective True
                            subpixel    True
                            on idle:
                                easein_quart .5 offset (0, 0) matrixtransform RotateMatrix(0, 0, 0)
                            on hover:
                                easein_quart .5 offset (0, 15) matrixtransform RotateMatrix(2.5, 0, 0)
                action Jump(y['jump'])
                at transform:
                    offset (j, 1080)
                    ease_quint .75 offset (j, 0)
                    ease_quint .5  offset (0, 0)
define cmcards1 = [ {'card_img': "MENUS/bootyroyale.png", 'jump': 'cm1'}, {'card_img': "MENUS/chestday.png", 'jump': 'cm2'} ]
define cmcards2 = [ {'card_img': "MENUS/freshmeat.png", 'jump': 'cm3'}, {'card_img': "MENUS/kissormiss.png", 'jump': 'cm4'} ]
define cmcards3 = [ {'card_img': "MENUS/xmarksthespot.png", 'jump': 'cm5'}, {'card_img': "MENUS/bribemebaby.png", 'jump': 'cm6'} ]
#call screen card_selection(cards=choice_set_1)

screen hyrilarstaychoice:
    modal True
    add "qw 55"
    if calypsopath:
        imagemap:
            ground "hyrilarstayidle"
            idle "hyrilarstayidle"
            hover "hyrilarstayhover"
            hotspot (487, 127, 917, 288) action Jump('hyrilarenter') 
            hotspot (480, 580, 952, 235) action Jump('hyrilarnoenter') 
    else:
        imagemap:
            ground "hyrilarstayidle2"
            idle "hyrilarstayidle2"
            hover "hyrilarstayhover2"
            hotspot (531, 261, 843, 241) action Jump('hyrilarenter') 

init python:
    def number_to_words(n):
        if n == 0:
            return "zero"
        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty",
                "sixty", "seventy", "eighty", "ninety"]
        def convert_hundreds(n):
            result = ""
            if n >= 100:
                result += ones[n // 100] + " hundred"
                n %= 100
                if n > 0:
                    result += " and "
            if 10 <= n < 20:
                result += teens[n - 10]
            else:
                if n >= 20:
                    result += tens[n // 10]
                    if n % 10 != 0:
                        result += "-" + ones[n % 10]
                else:
                    result += ones[n]
            return result.strip()
        if n < 1000:
            return convert_hundreds(n)
        elif n < 1000000:
            thousands = n // 1000
            remainder = n % 1000
            result = convert_hundreds(thousands) + " thousand"
            if remainder > 0:
                result += ", " + convert_hundreds(remainder)
            return result
        else:
            return str(n)  # fallback for too large numbers
screen logchopbutton():
    modal True
    imagebutton:
        align (0.29, 0.32)
        idle "chop1"
        hover "chop1b"
        action Jump("logchop2")

screen pennyangleanal:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if pasex1:
            action SetVariable("pasex1", False)
        else:
            action SetVariable("pasex1", True)

init python:
    import string

    def reverse_translate_server_name(guess):
        # Translate a server name back to the English string (if it exists)
        # to keep internal variables English, which helps with preventing
        # bugs when switching languages.
        if _preferences.language is None:
            # If the language is English, proceed as normal
            return guess
        reverse_tl_dict = dict()
        for server in store.serverscm:
            reverse_tl_dict[renpy.translate_string(server)] = server
        return reverse_tl_dict.get(guess, guess)  # Return original guess if none match

screen newstext1:
    text _("{cps=18}Multiple government and corporate sources have now confirmed that a critical malfunction of the neural implant is...{cps=2} {cps=18}resulting in real-world fatalities.") slow True style "textsameasdialogue"
screen newstext2:
    text _("{cps=16}According to official reports, players who die within the simulation, or forcibly disconnect without using an authorized Exit Portal, are experiencing a massive neural feedback surge that causes instant cerebral death in the real world.") style "textsameasdialogue" slow True
screen newstext3:
    text _("{cps=18}Reports began emerging just over three hours ago, simultaneously across the globe. Authorities are urgently advising all active players to remain inside Eternum until a verified Exit Portal is confirmed safe.") style "textsameasdialogue" slow True
screen newstext4:
    text _("{cps=17}The cause of this... unprecedented disaster remains unclear.{cps=2} {cps=17}While senior executives at Ulysses insist it’s the result of a large-scale cyberattack, critics are already calling it a catastrophic act of criminal negligence.") style "textsameasdialogue" slow True
screen newstext5:
    text _("{cps=18}The company’s Founder remains unreachable,{cps=5} {cps=17}and international law enforcement agencies have issued an immediate global ban on{cps=16} all neural implant usage until further notice.") style "textsameasdialogue" slow True
screen newstext6:
    text _("{cps=18}For those watching at home: Do not,{cps=2} {cps=17}under any circumstance, attempt to manually disconnect anyone currently connected to Eternum.{cps=2} {cps=18}Doing so{cps=2} {cps=13}could be fatal.") style "textsameasdialogue" slow True
screen newstext7:
    text _("{cps=18}We’ll continue to monitor this developing tragedy and bring you updates as they...") style "textsameasdialogue" slow True
screen newstext8:
    text _("{cps=15}U-Uh... I—uh... we’re just now receiving... preliminary casualty reports....") style "textsameasdialogue" slow True
screen newstext8b:
    text _("{cps=18}Authorities estimate that the current number of confirmed deaths is...{cps=2} {cps=16}already...") style "textsameasdialogue" slow True
screen newstext9:
    text _(". . .") style "textsameasdialogue" slow True
screen newstext10:
    text _("{cps=19}*Voice trembling* T-The current number of deaths is estimated to be...") style "textsameasdialogue" slow True
screen newstext11:
    text _("{cps=17}...over six...{cps=2} {cps=17}hundred...{cps=0.7} {cps=17}thousand.") style "textsameasdialogue" slow True
screen newstext13:
    text _("{cps=17}W-We...{cps=1} {cps=17}w-we’ll...{cps=2} {cps=17}continue bringing you updates throughout... the... t-the day as...{cps=2} {cps=22}more information becomes available.") style "textsameasdialogue" slow True
screen newstext14:
    text _("{cps=18}P-Please, stay...{cps=1} {cps=17}s-stay tuned.") style "textsameasdialogue" slow True


screen cameraphonebutton1():
    imagebutton:
        idle "camerabutton1"
        hover "camerabutton2"
        xalign 1.0
        yalign 0.502
        focus_mask True
        if lunapicclicks >= 21 and enoughpics:
            action [Play("sound7", "sfx/phonecamera.mp3"), Jump('cameralunaclick2'), SetVariable("lunapicclicks", lunapicclicks + 1)]
        else:
            action [Play("sound7", "sfx/phonecamera.mp3"), Show('cameralunaclick'), SetVariable("lunapicclicks", lunapicclicks + 1)]
screen cameralunaclick():
    modal False
    add Solid('#000'):
        xpos 117 ypos 0 xsize 1425 ysize 1084
    add "camerabutton1" xalign 1.0 yalign 0.502
    timer 0.1 action Hide("cameralunaclick")

screen lunaanglefingers:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if lunaftimefingers:
            action SetVariable("lunaftimefingers", False)
        else:
            action SetVariable("lunaftimefingers", True)

screen lunamisanglescreen:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if lunamisangle:
            action SetVariable("lunamisangle", False)
        else:
            action SetVariable("lunamisangle", True)

screen lunacowanglescreen:
    imagebutton:
        xalign 1.0 yalign 0.00
        idle "angle1"
        hover "angle2"
        if lunacowangle:
            action SetVariable("lunacowangle", False)
        else:
            action SetVariable("lunacowangle", True)