class Validator:
    @staticmethod
    def valid_name(name):
        if not name.strip():
            raise ValueError('Name cant be Empty')
        return True