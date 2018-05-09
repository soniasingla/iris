# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.app = app
        self.meta = 'This is a test case that restarts the browser'

    def run(self):
        """
        This is where your test logic goes.
        """
        google_search_image = "google_search.png"
        amazon_image = "amazon.png"

        navigate("https://google.com")
        expected_1 = exists(google_search_image, 10)
        assert_true(self, expected_1, 'Find Google search image')

        restart_firefox(self.app.fx_path, self.profile_name, url='https://www.amazon.com')
        expected_2 = exists(amazon_image, 10)
        assert_true(self, expected_2, 'Find Amazon image')


        return
