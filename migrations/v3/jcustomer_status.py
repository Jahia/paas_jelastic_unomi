from os import system
import requests
import re
from requests.exceptions import RequestException

# the following try/except block will make the custom check compatible with any Agent version
try:
    # first, try to import the base class from old versions of the Agent...
    from checks import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version 6 or later
    from datadog_checks.base import AgentCheck

__version__ = "1.0.0"


class CheckNumberBrowsingRemaining(AgentCheck):
    JCUSTOMER_SETENV_FILE = "/opt/jcustomer/jcustomer/bin/setenv"
    __NAMESPACE__ = "jcustomer"
    SERVICE_CHECK_NAME = "app_status"

    def check(self, instance):
        try:
            # We get the admin page credentials
            karaf_password = self.__get_karaf_password()
            response = requests.get('http://127.0.0.1/cxs/privacy/info',
                               auth=("karaf", karaf_password))

            if response.status_code != 200:
                self.__set_error("Received wrong status code " + str(response.status_code))
                return

            data = response.json()

            self.service_check(
                self.SERVICE_CHECK_NAME,
                AgentCheck.OK,
                message='JCustomer is running and OK.'
            )
        except ValueError as exception:
            self.__set_error("Returned invalid json")
        except RequestException as exception:
            self.__set_error("Request failed")
        except Exception as exception:
            self.__set_error("An unexpected error occured")

        return

    def __set_error(self, error):
        self.service_check(
            self.SERVICE_CHECK_NAME,
            AgentCheck.CRITICAL,
            message='JCustomer is not running or not ready: ' + error
        )

    def __get_karaf_password(self):
        with open(self.JCUSTOMER_SETENV_FILE) as set_env_file:
            for line in set_env_file:
                if line.find('UNOMI_ROOT_PASSWORD') != -1:
                    return line.split("=")[-1].rstrip('\n')
        return "FAIL"
