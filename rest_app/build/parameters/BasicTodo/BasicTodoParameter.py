class TodoParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "BasicTodo",
            "parameter_field_name": "todo"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "BasicTodoSerializer",
            "param_serializer_import_str": "from rest_app.build.serializers.definitions.BasicTodo.BasicTodoSerializer import BasicTodoSerializer",
            "param_serializer_required": True,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass