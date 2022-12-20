from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from windowscreens.discoverscreen import DiscoverScreen
from kivymd.font_definitions import theme_font_styles
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivymd.uix.button import MDIconButton
# from kivy.storage.dictstore import DictStore
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDIcon
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

KIVY_DPI = 320
KIVY_METRICS_DENSITY = 2

Window.size = (720, 1280)

class ImageButton(ButtonBehavior, Image):

    hex_status = StringProperty('undiscovered', Options=('undiscovered', 'discovered', 'discoverable', 'depleted'))
    hex_position = ListProperty(None)
    hex_tile = StringProperty(None)
    hex_replenishing = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = 'images/tiles/emptytile.png'
        self.size_hint = (None, None)
        self.size = (dp(200), dp(200))
        self.color = 0, 0, 0, 0.8

    def on_hex_replenishing(self, obj, value):
        if self.hex_replenishing == True:
            self.color = 1, 1, 1, 0.5

    def on_hex_status(self, obj, value):

        if self.hex_status == "discovered":

            self.color = 1, 1, 1, 1
            self.source = f"images/tiles/{self.hex_tile}.png"

            if self.hex_position != [2, 2]:
                anim_sequence = Animation(size=(dp(250), dp(250)), duration=0.3) +\
                                Animation(size=(dp(200), dp(200)), duration=0.3)
                anim_sequence.start(self)
                MDApp.get_running_app().root.get_screen('main').ids.gather_button.notifications += 1
                MDApp.get_running_app().root.get_screen('main').ids.discover_button.notifications -= 1

        if self.hex_status == "discoverable":
            self.disabled = False
            self.color = 0.5, 0.5, 0.5, 1
            self.source = f"images/tiles/{self.hex_tile}.png"

            MDApp.get_running_app().root.get_screen('main').ids.discover_button.notifications += 1

    def collide_point(self, x, y):
        # return (self.x + dp(30)) <= x <= (self.right - dp(30)) and (
        #         self.y + dp(30)) <= y <= (self.top - dp(30))
        return (x - self.center_x)**2 + (y - self.center_y)**2 < (self.width/2.2)**2

class BadgeButton(MDTextButton, MDIcon):
    notifications = NumericProperty(0)

    def on_notifications(self, *args):
        if self.notifications != 0:
            if self.notifications < 10:
                self.badge_icon = f'numeric-{self.notifications}'
            else:
                self.badge_icon = 'numeric-9-plus'
        else:
            self.badge_icon = ''

    # def on_release(self):
    #     self.notifications = 0
    #     self.badge_icon = ''

class PlayerScreen(MDScreen):
    pass

class MainScreen(MDScreen):

    cust_icons = {
        "map": "\U0000E900",
        "basket": "\U0000E901",
        "morning": "\U0000E902",
        "afternoon": "\U0000E903",
        "evening": "\U0000E904"
    }

    # save and load data
    # def on_enter(self):
    #
    #     # test = input('What data you want to store?')
    #     store = DictStore('nameofstorage')
    #     # store.put(test)
    #     for item in store:
    #      print(item)

    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)

        # Set material style - Future Use
        MDApp.get_running_app().theme_cls.material_style = "M3"

        # Set colors to use throughout app
        MDApp.get_running_app().theme_cls.set_colors("Brown", "400", "200", "600",
                                                     "Lime", "600", "100", "900")

        # Set Fonts
        LabelBase.register(name="H1", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('H1')
        MDApp.get_running_app().theme_cls.font_styles["H1"] = ["H1", 96, False, -1.5]

        LabelBase.register(name="H2", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('H2')
        MDApp.get_running_app().theme_cls.font_styles["H2"] = ["H2", 60, False, -0.5]

        LabelBase.register(name="H3", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('H3')
        MDApp.get_running_app().theme_cls.font_styles["H3"] = ["H3", 48, False, 0]

        LabelBase.register(name="H4", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('H4')
        MDApp.get_running_app().theme_cls.font_styles["H4"] = ["H4", 34, False, 0.25]

        LabelBase.register(name="H5", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('H5')
        MDApp.get_running_app().theme_cls.font_styles["H5"] = ["H5", 24, False, 0]

        LabelBase.register(name="H6", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('H6')
        MDApp.get_running_app().theme_cls.font_styles["H6"] = ["H6", 20, False, 0.15]

        LabelBase.register(name="Subtitle1", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('Subtitle1')
        MDApp.get_running_app().theme_cls.font_styles["Subtitle1"] = ["Subtitle1", 16, False, 0.15]

        LabelBase.register(name="Subtitle2", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('Subtitle2')
        MDApp.get_running_app().theme_cls.font_styles["Subtitle2"] = ["Subtitle2", 14, False, 0.1]

        LabelBase.register(name="Body1", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('Body1')
        MDApp.get_running_app().theme_cls.font_styles["Body1"] = ["Body1", 16, False, 0.5]

        LabelBase.register(name="Body2", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('Body2')
        MDApp.get_running_app().theme_cls.font_styles["Body2"] = ["Body2", 14, False, 0.25]

        LabelBase.register(name="Button", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('Button')
        MDApp.get_running_app().theme_cls.font_styles["Button"] = ["Button", 14, True, 1.25]

        LabelBase.register(name="Caption", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('Caption')
        MDApp.get_running_app().theme_cls.font_styles["Caption"] = ["Caption", 12, False, 0.4]

        LabelBase.register(name="Overline", fn_regular="font/dogicabold.ttf")
        theme_font_styles.append('Overline')
        MDApp.get_running_app().theme_cls.font_styles["Overline"] = ["Overline", 10, True, 1.5]

        LabelBase.register(name="Wildicon", fn_regular="font/wildicon.ttf")
        theme_font_styles.append('Wildicon')
        MDApp.get_running_app().theme_cls.font_styles["Wildicon"] = ["Wildicon", 10, False, 20]

    def open_close_rail(self):

        def reveal_buttons(dt):
            for item in self.ids.rail.children:
                Animation(opacity=1, duration=0.1).start(item)

        def disable_buttons(dt):
            self.ids.rail.disabled = True

        if self.ids.rail.width == -1:
            self.ids.rail.disabled = False
            Animation(width=dp(72), duration=0.3).start(self.ids.rail)
            Clock.schedule_once(reveal_buttons, 0.2)

        else:
            Animation(width=-1, duration=0.3).start(self.ids.rail)
            for item in self.ids.rail.children:
                Animation(opacity=0, duration=0.1).start(item)
                Clock.schedule_once(disable_buttons, 0.1)

    # def toggle_clear(self):
    #     for item in self.ids.rail.children:
    #         item.state = 'normal'

# class CustomIconButton(MDIconButton, ToggleButtonBehavior):
#
#     def on_state(self, widget, value):
#         if value == 'down':
#             self.md_bg_color = MDApp.get_running_app().theme_cls.primary_dark
#         else:
#             self.md_bg_color = MDApp.get_running_app().theme_cls.primary_color

# kv = '''
# Honeycombed:
#     cols: 5
#     spacing: 30, 25
#     padding: 75
# '''
#
# class Honeycombed(GridLayout):
#     def on_kv_post(self, base_widget):
#         for _ in range(25):
#             self.add_widget(Button())
#
#     def do_layout(self, *largs):
#         children = self.children
#         if not children or not self._init_rows_cols_sizes(len(children)):
#             l, t, r, b = self.padding
#             self.minimum_size = l + r, t + b
#             return
#         self._fill_rows_cols_sizes()
#         self._update_minimum_size()
#         self._finalize_rows_cols_sizes()
#
#         for i, x, y, w, h in self._iterate_layout(len(children)):
#             c = children[i]
#             c.pos = x, y
#             shw, shh = c.size_hint
#             shw_min, shh_min = c.size_hint_min
#             shw_max, shh_max = c.size_hint_max
#
#             if shw_min is not None:
#                 if shw_max is not None:
#                     w = max(min(w, shw_max), shw_min)
#                 else:
#                     w = max(w, shw_min)
#             else:
#                 if shw_max is not None:
#                     w = min(w, shw_max)
#
#             if shh_min is not None:
#                 if shh_max is not None:
#                     h = max(min(h, shh_max), shh_min)
#                 else:
#                     h = max(h, shh_min)
#             else:
#                 if shh_max is not None:
#                     h = min(h, shh_max)
#
#             if shw is None:
#                 if shh is not None:
#                     c.height = h
#             else:
#                 if shh is None:
#                     c.width = w
#                 else:
#                     c.size = (w, h)
#             # just these
#             c.y -= ((h + self.spacing[1]) // 2) * (i // self.cols)
#             if i//self.cols % 2:
#                 c.x -= (w + self.spacing[0]) // 2

class MainScreenManager(ScreenManager):
    pass

class WindowScreenManager(ScreenManager):
    pass

class DarkWildernessApp(MDApp):
    def build(self):
        pass

if __name__ == "__main__":
    DarkWildernessApp().run()