class Utils:

    def create_headers_json(self):
        headers = {
            "Content-Type": "application/json",
        }
        return headers

    def create_headers_xml(self):
        headers = {
            "Content-Type": "application/xml",
        }
        return headers

    def common_headers_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "basic" + str(basic_auth_value),
        }
        return headers

    def common_headers_put_patch_delete_bearer_auth(self, api_token):
        headers = {
            "Content-Type": "application/xml",
            "Authorization": "bearer" + str(api_token),
        }
        return headers

    def common_headers_put_patch_delete_cookie_auth(self, token):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "token=" + str(token),
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass
