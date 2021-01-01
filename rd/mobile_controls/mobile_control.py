class MobileControl:
    def __init__(self,
                 resource_id: str = None,
                 xpath: str = None,
                 text: str = None,
                 texts: list = None,
                 description: str = None,
                 class_name: str = None,
                 is_scrollable: bool = False,
                 use_resource_id_prefix: bool = True,
                 parent: 'MobileControl' = None
                 ):
        self._resource_id = resource_id
        self._xpath = xpath
        self._text = text
        self._texts = texts
        self._description = description
        self._class_name = class_name
        self._use_resource_id_prefix = use_resource_id_prefix
        self._is_scrollable = is_scrollable
        self._parent = parent

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text

    def get_ui_automator_string(self, resource_id_prefix) -> str:
        selector = "new UiSelector()"
        if self._resource_id:
            if self._use_resource_id_prefix:
                selector = f'new UiSelector().resourceId("{resource_id_prefix}{self._resource_id}")'
            else:
                selector = f'new UiSelector().resourceId("{self._resource_id}")'
        if self._text:
            selector += '.text("{}")'.format(self._text)
        elif self._texts:
            selector += '.textMatches("{}")'.format(
                '|'.join([t for t in self._texts]))
        if self._description:
            selector += f'.description("{self._description}")'
        if self._class_name:
            selector += '.className("{}")'.format(self._class_name)
        if self._is_scrollable:
            selector += '.scrollable(true)'
        if self._parent:
            if self._parent._is_scrollable:
                selector = 'new UiScrollable({}).scrollIntoView({})'.format(
                    self._parent.get_ui_automator_string(resource_id_prefix=resource_id_prefix),
                    selector
                )
            else:
                selector = "{}.childSelector({})".format(
                    self._parent.get_ui_automator_string(resource_id_prefix=resource_id_prefix),
                    selector
                )
        return selector
