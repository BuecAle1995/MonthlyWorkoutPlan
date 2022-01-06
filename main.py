from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowMain(Screen):
    pass


class WindowCreatePlanStep1(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class WorkoutPlanCreator(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        # Designate our .kv design file
        kv = Builder.load_file("workoutplancreator.kv")
        return kv

    def on_save(self, instance, value, date_range):
        print(value)
        return str(value)

    def ShowDatePicker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()


if __name__ == '__main__':
    app = WorkoutPlanCreator()
    app.run()
