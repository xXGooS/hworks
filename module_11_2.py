#from pprint import pprint

def introspection_info(obj):

    info = {'type': type(obj).__name__,
            'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
            'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
            'module': (obj.__module__ if hasattr(obj, '__module__') else 'built-in')}

    return info

number_info = introspection_info(42)

print(number_info)
#pprint(number_info)