from .fixed import Fixed

class origin(object):
    def __init__(self, origin):
        self.origin = origin
    def __enter__(self):

        return self

    def __exit__(self, type, value, traceback):

        pass

    def fixed(self, *f_args, **f_kwargs):
        origin = self.origin
        class _Fixed(Fixed):
            def __init__(self, *args, **kwargs):
                super(_Fixed, self).__init__(*args, **kwargs)
                if self.__frequency != "week" and origin > self.start:
                    self.prorate(origin)

        return _Fixed(*f_args, **f_kwargs)
