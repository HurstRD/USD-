class Container(tuple):
    """
    Base class for containers.

    Containers are classes that collect semantically related Artists such as
    the bars of a bar plot.
    """


    def __repr__(self):
        return ("<{} object of {} artists>"
                .format(type(self).__name__, len(self)))


    def __new__(cls, *args, **kwargs):
        return tuple.__new__(cls, args[0])


    def __init__(self, kl, label=None):
        self._callbacks = cbook.CallbackRegistry()
        self._remove_method = None
        self.set_label(label)


    def remove(self):
        for c in cbook.flatten(
                self, scalarp=lambda x: isinstance(x, Artist)):
            if c is not None:
                c.remove()
        if self._remove_method:
            self._remove_method(self)


    def get_children(self):
        return [child for child in cbook.flatten(self) if child is not None]


    get_label = Artist.get_label
    set_label = Artist.set_label
    add_callback = Artist.add_callback
    remove_callback = Artist.remove_callback
    pchanged = Artist.pchanged
