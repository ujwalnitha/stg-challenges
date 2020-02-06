# This class has helper methods to get elements with and without alt attribute


class MyAltFinder(object):

    def __init__(self, driver, tag):
        assert tag, "tag is invalid"
        self.tag = tag
        self.driver = driver

    def _find_elements(self, path_string):
        try:
            elements = self.driver.find_elements_by_xpath(path_string)
            return elements
        except Exception as e:
            print("Failed to find elements with given string %s" %e.args)

    def get_all_elements_with_alt(self):
        elements_with_alt = self._find_elements("//%s[contains(\"alt\", .) and not(@type=\"hidden\")]" % self.tag)
        print("There are visible %d <%s> elements in this page with alt attribute" % (len(elements_with_alt), self.tag))
        return elements_with_alt

    def get_all_elements_without_alt(self):
        input_elements_no_alt = self._find_elements("//%s[not(contains(\"alt\", .)) and not(@type=\"hidden\")]" % self.tag)
        print("There are %d visible <%s> elements in this page without alt attribute" % (len(input_elements_no_alt), self.tag))
        return input_elements_no_alt
