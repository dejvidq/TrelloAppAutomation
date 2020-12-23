from rd.mobile_controls.mobile_control import MobileControl


class MobileImageButtonControl(MobileControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._class_name = 'android.widget.ImageButton'
