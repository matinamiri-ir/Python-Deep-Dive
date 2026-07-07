from validation import Validation
class Model:
    def __init__(self, **kwargs):

        fields = self.__class__.__dict__

        for name, field in fields.items():

            if isinstance(field, Validation):

                if name in kwargs:
                    setattr(self, name, kwargs[name])

                elif field.default is not None:
                    setattr(self, name, field.default)
        
    def to_dict(self):
        return dict(self.__dict__)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.__dict__})'
    
    
    def __iter__(self):
        return iter(self.__dict__.items())
    
    def __contains__(self, item):
        return item in self.__dict__
    
    def __eq__(self, other):
        if type(self) is type(other):
            return self.__dict__ == other.__dict__