import copy as _copy


class PropertyDict:

    def __init__(self, data: dict):
        self._data = dict(sorted(data.items()))
        return

    @property
    def as_dict(self) -> dict:
        """The data as a dictionary."""
        return self._data

    def get(self, name: str, default=None):
        return self._data.get(name, default)

    def __getattr__(self, name: str):
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __getitem__(self, name: str):
        return self._data[name]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __contains__(self, name: str):
        return name in self._data

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"PropertyDict({self._data})"

    def __str__(self):
        return str(self._data)

    def __eq__(self, other):
        return self._data == other._data

    def __ne__(self, other):
        return self._data != other._data

    def __deepcopy__(self, memo):
        # Dynamically handle subclass instantiation with additional arguments
        cls = type(self)
        # Deepcopy the data dictionary
        copied_data = _copy.deepcopy(self._data, memo)
        # Capture extra attributes (everything except `_data`)
        extra_attrs = {
            key: _copy.deepcopy(value, memo)
            for key, value in self.__dict__.items()
            if key != "_data"
        }
        # Create a new instance
        obj = cls.__new__(cls)  # Avoid calling __init__ directly
        obj._data = copied_data  # Set _data directly
        # Restore extra attributes
        obj.__dict__.update(extra_attrs)
        return obj
