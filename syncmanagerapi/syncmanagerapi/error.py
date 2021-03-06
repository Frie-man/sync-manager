class InvalidRequest(Exception):
    status_code = 400

    def __init__(self, message, field, status_code=None):
        Exception.__init__(self)
        self.message = message
        self.field = field
        if status_code is not None:
            self.status_code = status_code

    def get_response_info(self):
        rv = dict()
        rv['message'] = self.message
        rv['field'] = self.field
        return rv


class FsConflictError(Exception):
    status_code = 409

    def __init__(self, message, path, target_path=None, status_code=None):
        Exception.__init__(self)
        self.message = message
        self.path = path
        self.target_path = target_path
        if status_code is not None:
            self.status_code = status_code

    def get_response_info(self):
        rv = dict()
        rv['message'] = self.message
        rv['path'] = self.path
        if self.target_path:
            rv['target_path'] = self.target_path
        return rv


class DataInconsistencyException(Exception):
    status_code = 500

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def get_response_info(self):
        rv = dict()
        rv['message'] = self.message
        return rv
